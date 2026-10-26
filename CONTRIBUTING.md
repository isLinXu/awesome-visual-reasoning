# 贡献指南

这个仓库有两种内容：**人写的判断** 和 **机器抓的数据**。两者的贡献方式不同。

---

## 1. 推荐一篇论文 / 一个项目

最省事的方式：直接开 Issue，标题写 `[paper] 论文名` 或 `[repo] owner/name`。

请附上：

- arXiv 链接（`https://arxiv.org/abs/XXXX.XXXXX`）或仓库链接
- **一句话说明它属于哪条赛道**，以及为什么值得收
- 如果是论文，说明它属于哪一类：`latent` / `agentic` / `video` / `multimodal` / `efficient`

维护者会把它加进对应的 `classics`（奠基/必读）或 `github_seed`（长期跟踪）。

> ⚠️ 请不要直接往 `docs/*.md` 的论文表里手工加行——那些表由脚本维护，
> 手工加的行没有对应的 `data/papers.json` 记录，下次跑脚本可能被截断掉。

## 2. 改进自动分类（收益最大）

分类逻辑全在 [`config/taxonomy.yml`](config/taxonomy.yml)。三类改法：

| 现象 | 改哪里 |
| :-- | :-- |
| 某类工作总收不进来 | 在对应赛道的 `arxiv_queries` 加查询式，或 `keywords.strong` 加词 |
| 收进来一堆离题的论文 | 加到 `negative`，或把过宽的词从 `strong` 降到 `medium` |
| 赛道之间抢论文 | 调 `keywords` 权重，让该赛道的关键词更"专有" |
| 某个仓库明显不属于本赛道 | 加到 `github_blocklist`，见下方说明 |

`github_blocklist` 是**人工精确剔除**用的，和自动召回分工明确：

- 只放你**确定**离题的仓库，比如"用 LLM 写代码的桌面工作台"被 `computer-use` 这个词带进来
- 拿不准的先开 Issue 讨论，不要直接加——误杀一个真项目比漏收一个噪声更糟
- 加的时候**必须写注释说明为什么**，否则半年后没人敢删

改完请本地验证，不要盲提 PR：

```bash
python scripts/fetch_arxiv.py --dry-run --days 30 --sources arxiv
```

dry-run 会打印"命中 N 篇、将新增 M 行"，确认没把噪声收进来再提交。

## 3. 加一条新赛道

1. 在 `config/taxonomy.yml` 的 `categories` 下加一块（照抄现有结构）
2. 新建 `docs/<id>.md`，**必须**包含这段标记块，否则脚本无处写入：

```markdown
<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
<!-- table:end classics -->

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
<!-- table:end papers -->
```

3. 在 `README.md` 的赛道表里加一行
4. 跑 `python scripts/render_charts.py`——它会生成该赛道的 sparkline 并**自动插入**到文档里
   （图里需要一种新颜色的话，在 `scripts/render_charts.py` 的 `TRACK_COLORS` 加一行）
5. 跑一遍 `python scripts/seed_classics.py && python scripts/fetch_arxiv.py --dry-run`

## 4. 提交前自检

```bash
python scripts/seed_classics.py          # 必读清单里的 arXiv ID 是否还有效
python scripts/fetch_arxiv.py --dry-run   # 分类是否收进了噪声
python scripts/update_metadata.py --dry-run
python scripts/render_charts.py           # 图表能否正常渲染（幂等，重复跑无 diff）
python scripts/check_md.py                # 表格 / 链接 / 图片引用 / 标记
```

## 5. 关于"必读"清单的标准

能进 `classics` 的论文，需要满足至少两条：

- 提出了一种**新范式**，而不只是把分数刷高
- 被后续工作**反复引用**为 baseline 或起点
- 定义了一个**被广泛采用的评测方式**
- 对某个开放问题给出了**可复用的分析**

不要提交"我也觉得不错"的增量工作——那个交给自动抓取就够了。

## 6. 代码风格

- 只用 `requests` + `PyYAML`，不引入新依赖
- 所有网络请求走 `common.http_get`（自带指数退避与 4xx 短路）
- 任何一步失败只降级不抛异常，定时任务不能因为单个数据源挂了就全红
- 写文件前先 `write_if_changed` / 幂等判断，避免产生无意义的 diff
