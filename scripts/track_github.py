#!/usr/bin/env python3
"""跟踪 GitHub 上与多模态推理相关的仓库：搜索 → 快照 star → 计算增速 → 出榜。

两个数据来源：
  1. 配置里的 github_seed —— 长期盯盘的旗舰仓库（逐个 /repos 校验，失效自动跳过）
  2. 配置里的 github_queries —— 按赛道关键词搜索，发现新项目

star 历史存在 data/repos.json，每天追加一条快照，因此 7 天 / 30 天增速是
真实累积出来的；仓库第一次被看到时增速记为 0，第二天起才有意义。

用法：
  python scripts/track_github.py
  python scripts/track_github.py --top 40 --dry-run
  GITHUB_TOKEN=xxx python scripts/track_github.py   # 有 token 才能跑到 5000/h
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

from common import (
    DATA,
    DOCS,
    GITHUB_API,
    http_get,
    replace_table_body,
    load_config,
    log,
    md_escape,
    read_json,
    shorten,
    today_utc,
    warn,
    write_json,
)

REPO_STORE = DATA / "repos.json"
PROJECTS_DOC = DOCS / "projects.md"


def gh_headers() -> Dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    hdrs = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        hdrs["Authorization"] = f"Bearer {token}"
    return hdrs


def normalize(item: Dict[str, Any], category: str) -> Dict[str, Any]:
    return {
        "full_name": item["full_name"],
        "url": item.get("html_url") or f"https://github.com/{item['full_name']}",
        "description": item.get("description") or "",
        "stars": int(item.get("stargazers_count") or 0),
        "forks": int(item.get("forks_count") or 0),
        "language": item.get("language") or "",
        "topics": item.get("topics") or [],
        "pushed_at": (item.get("pushed_at") or "")[:10],
        "created_at": (item.get("created_at") or "")[:10],
        "archived": bool(item.get("archived")),
        "categories": [category] if category else [],
    }


def search_repos(query: str, min_stars: int, per_page: int, pushed_after: str) -> Optional[List[Dict[str, Any]]]:
    q = f"{query} stars:>={min_stars} pushed:>{pushed_after}"
    resp = http_get(
        f"{GITHUB_API}/search/repositories",
        params={"q": q, "sort": "stars", "order": "desc", "per_page": per_page},
        headers=gh_headers(),
        retries=2,
        base_wait=5,
    )
    if resp is None:
        return None
    try:
        return resp.json().get("items", [])
    except ValueError:
        return None


def fetch_repo(full_name: str) -> Optional[Dict[str, Any]]:
    resp = http_get(f"{GITHUB_API}/repos/{full_name}", headers=gh_headers(), retries=2, base_wait=2)
    if resp is None:
        return None
    try:
        return resp.json()
    except ValueError:
        return None


def stars_before(history: List[Dict[str, Any]], days: int) -> Optional[int]:
    """取「至少 days 天前」最近一次快照的 star 数。"""
    if not history:
        return None
    cutoff = today_utc() - timedelta(days=days)
    best: Optional[Dict[str, Any]] = None
    for snap in history:
        try:
            from datetime import datetime, timezone

            d = datetime.strptime(snap["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except (KeyError, ValueError):
            continue
        if d <= cutoff:
            if best is None or snap["date"] > best["date"]:
                best = snap
    return int(best["stars"]) if best else None


def render_row(rank: int, repo: Dict[str, Any]) -> str:
    name = repo["full_name"]
    url = repo["url"]
    desc = md_escape(shorten(repo.get("description") or "（无描述）", 78))
    stars = repo.get("stars", 0)
    d7, d30 = repo.get("delta_7d"), repo.get("delta_30d")

    def fmt(delta: Optional[int]) -> str:
        if delta is None:
            return "—"
        if delta == 0:
            return "0"
        return f"+{delta:,}" if delta > 0 else f"{delta:,}"

    lang = repo.get("language") or "—"
    tags = " ".join(f"`{t}`" for t in repo.get("categories", [])[:2])
    badge = " 🆕" if repo.get("is_new") else ""
    row = (
        f"| {rank} | [**{name}**]({url}){badge} | {desc} | ⭐ {stars:,} | {fmt(d7)} | {fmt(d30)} | {lang} | {tags} |"
    )
    return row


def is_relevant(item: Dict[str, Any], category: Dict[str, Any]) -> bool:
    """搜索结果的相关性闸门。

    GitHub 搜索是"分词匹配"，`video llm` 会命中"用 LLM 生成短视频"这类无关仓库
    （star 还特别高）。这里要求名称/描述/topics 里真的出现该赛道的强或中档关键词。
    种子仓库不走这道闸门——它们是人挑的。
    """
    keywords = category.get("keywords") or {}
    terms = list(keywords.get("strong", [])) + list(keywords.get("medium", []))
    text = " ".join(
        [
            item.get("full_name", ""),
            item.get("description") or "",
            " ".join(item.get("topics") or []),
        ]
    ).lower()
    return any(t.lower() in text for t in terms)


def main() -> int:
    parser = argparse.ArgumentParser(description="跟踪 GitHub 多模态推理仓库")
    parser.add_argument("--top", type=int, default=60, help="写入文档的仓库数量")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-search", action="store_true", help="只刷新种子仓库")
    parser.add_argument("--offline", action="store_true", help="不发请求，只用 data/repos.json 重渲染榜单")
    args = parser.parse_args()

    config = load_config()
    meta = config["meta"]
    min_stars = int(meta.get("github_min_stars", 80))
    per_query = int(meta.get("github_max_per_query", 30))
    keep_days = int(meta.get("github_history_keep", 90))
    today_str = today_utc().strftime("%Y-%m-%d")
    pushed_after = (today_utc() - timedelta(days=180)).strftime("%Y-%m-%d")

    store = read_json(REPO_STORE, {"updated": "", "repos": {}})
    known: Dict[str, Dict[str, Any]] = store.get("repos", {})

    found: Dict[str, Dict[str, Any]] = {}

    def merge(item: Dict[str, Any], category: str, check_relevance: bool = False) -> bool:
        if check_relevance:
            cat = next((c for c in config["categories"] if c["id"] == category), None)
            if cat is not None and not is_relevant(item, cat):
                return False
        norm = normalize(item, category)
        if norm["archived"]:
            return False
        existing = found.get(norm["full_name"])
        if existing:
            for c in norm["categories"]:
                if c not in existing["categories"]:
                    existing["categories"].append(c)
            existing["stars"] = max(existing["stars"], norm["stars"])
        else:
            found[norm["full_name"]] = norm
        return True

    # 1) 种子仓库（逐个精确校验）
    log("━━ 种子仓库校验 ━━" if not args.offline else "━━ 离线模式：跳过抓取，仅重渲染 ━━")
    for seed in ([] if args.offline else config.get("github_seed", [])):
        full_name = seed["full_name"]
        category = seed.get("category", "")
        data = fetch_repo(full_name)
        if data is None:
            warn(f"种子仓库不可用，跳过: {full_name}")
            continue
        merge(data, category)
        resolved = data.get("full_name", full_name)
        note = f" (已改名 ← {full_name})" if resolved.lower() != full_name.lower() else ""
        log(f"  ✓ {resolved} ⭐{data.get('stargazers_count', 0):,}{note}")

    # 2) 关键词搜索（未认证限流 10 次/分钟，故每次之间 sleep）
    dropped = 0
    if not args.offline and not args.skip_search:
        for cat in config["categories"]:
            for query in cat.get("github_queries", []):
                log(f"━━ 搜索 [{cat['id']}] {query} ━━")
                items = search_repos(query, min_stars, per_query, pushed_after)
                if items is None:
                    warn(f"搜索失败/限流，跳过: {query}")
                    continue
                kept = sum(1 for item in items if merge(item, cat["id"], check_relevance=True))
                dropped += len(items) - kept
                log(f"  {len(items)} 条结果，相关性过滤后保留 {kept} 条")
                time.sleep(7)  # 未认证搜索限流保护

    log("")
    log(f"本轮识别仓库 {len(found)} 个（历史库 {len(known)} 个，丢弃不相关 {dropped} 个）")

    # 3) 合并进历史库 + 打快照
    for full_name, repo in found.items():
        record = known.get(full_name, {})
        history = record.get("history", [])
        if not history or history[-1].get("date") != today_str:
            history.append({"date": today_str, "stars": repo["stars"]})
        history = history[-keep_days:]

        first_seen = record.get("first_seen") or today_str
        record.update(repo)
        record["first_seen"] = first_seen
        record["last_seen"] = today_str
        record["history"] = history
        record["categories"] = sorted(set(record.get("categories", [])))
        known[full_name] = record

    # 4) 计算增速并排序
    rows: List[Dict[str, Any]] = []
    for full_name, record in known.items():
        record["delta_7d"] = (
            record["stars"] - stars_before(record.get("history", []), 7)
            if stars_before(record.get("history", []), 7) is not None
            else None
        )
        record["delta_30d"] = (
            record["stars"] - stars_before(record.get("history", []), 30)
            if stars_before(record.get("history", []), 30) is not None
            else None
        )
        created = record.get("created_at") or ""
        record["is_new"] = bool(created and created >= (today_utc() - timedelta(days=120)).strftime("%Y-%m-%d"))
        rows.append(record)

    def sort_key(r: Dict[str, Any]):
        return (r.get("delta_7d") or -1, r.get("delta_30d") or -1, r.get("stars", 0))

    rows.sort(key=sort_key, reverse=True)
    top = rows[: args.top]

    # 榜单是全量快照：排名每次都会变，必须整表重写而不是增量追加
    table_rows = [render_row(i + 1, r) for i, r in enumerate(top)]
    written = replace_table_body(PROJECTS_DOC, "repos", table_rows, dry_run=args.dry_run)
    log(f"写入 {PROJECTS_DOC.name}: {written} 行（榜单按 7 日增速排序）")

    if not args.dry_run:
        store["updated"] = today_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
        store["repos"] = known
        write_json(REPO_STORE, store)

    movers = [r for r in rows if (r.get("delta_7d") or 0) > 0][:5]
    if movers:
        log("本周增速 Top5：")
        for r in movers:
            log(f"  +{r['delta_7d']:,}  {r['full_name']} (⭐{r['stars']:,})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
