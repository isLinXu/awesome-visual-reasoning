# 🚀 项目雷达 · GitHub Tracker

> 每日快照 star 数，按 **7 日增速** 排序。增速比总量更能反映"现在大家在做什么"。
> 数据来自 `data/repos.json`（含每个仓库的 star 历史），由 `scripts/track_github.py` 维护。

[← 返回总览](../README.md) · [自动周报](digest.md)

---

## 榜单口径

| 项目 | 说明 |
| :-- | :-- |
| 入选 | 配置中的种子仓库 + 按赛道关键词搜索命中（`stars ≥ 阈值`、近半年有 push、非归档、不在黑名单） |
| 排序 | 7 日 star 增量 → 30 日增量 → 总 star；**快照不足 7 天时用日均增速折算兜底** |
| `≈+N` | **估算值**：按 `总 star ÷ 仓库存活天数 × 7` 折算，不是实测增量，仅供建库首日排序参考 |
| `—` | 该窗口无法计算，也没有估算依据（如缺少创建时间） |
| `🆕` | 仓库创建于近 120 天内 |

> 为什么不用总 star 排？因为总 star 是**存量**，会把多年前的老项目顶在上面；
> 增速是**流量**，才看得出赛道当前的注意力在哪。
>
> 为什么首日要用估算兜底？因为本仓库的快照是逐日累积的，刚建库时所有仓库都只有一天记录，
> 真实 7 日增量算不出来。若此时直接按总 star 排，榜单会退化成"老牌大项目榜"，
> 刚爆发的项目永远上不来——这恰好违背了做增速榜的初衷。所以用日均速度折算成 7 日估计值顶上，
> **满 7 天后自动切换为真实增量**，估算值随之消失。

## 当前榜单

先看增速，再看明细——条形长度是 7 日 star 增量，颜色是所属赛道：

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/ranking-dark.svg">
  <img src="../assets/ranking-light.svg" alt="项目 star 增速 Top 12">
</picture>

完整 60 条含语言、赛道、30 日增量的明细表：

<!-- table:start repos -->
| 排名 | 项目 | 一句话 | ⭐ | 7 日 Δ | 30 日 Δ | 语言 | 赛道 |
| --: | :-- | :-- | --: | --: | --: | :-- | :-- |
| 1 | [**vercel-labs/agent-desktop**](https://github.com/vercel-labs/agent-desktop) | Computer use CLI for AI agents | ⭐ 18,325 | +15,615 | — | Rust | `agentic-vision` |
| 2 | [**trycua/cua**](https://github.com/trycua/cua) | Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes… | ⭐ 31,911 | +527 | — | Rust | `agentic-vision` |
| 3 | [**reacher-z/Awesome-CUA**](https://github.com/reacher-z/Awesome-CUA) 🆕 | Open, source-backed catalog of computer-use agents: reviewed papers… | ⭐ 531 | ≈+169 | — | Python | `agentic-vision` |
| 4 | [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | A framework for efficient model inference with omni-modality models | ⭐ 7,597 | +160 | — | Python | `multimodal-reasoning` |
| 5 | [**ctoldigital/axuse**](https://github.com/ctoldigital/axuse) 🆕 | Accessibility-first browser & computer use for AI agents — one MCP server for… | ⭐ 803 | +130 | — | JavaScript | `agentic-vision` |
| 6 | [**ComputerUseAgent/AutoCua**](https://github.com/ComputerUseAgent/AutoCua) 🆕 | Automate with computer-use agent (ComputerUse / CUA) for macOS, Windows… | ⭐ 1,074 | +125 | — | Python | `agentic-vision` |
| 7 | [**bytedance/UI-TARS-desktop**](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models a… | ⭐ 39,565 | +91 | — | TypeScript | `agentic-vision` |
| 8 | [**uclanlp/OpenVLHarness**](https://github.com/uclanlp/OpenVLHarness) 🆕 | Official Code for OpenVLHarness: Real-World Visual Agentic Tool‑Use with Multi… | ⭐ 404 | +72 | — | Python | `agentic-vision` |
| 9 | [**nv-tlabs/PixelUMM**](https://github.com/nv-tlabs/PixelUMM) 🆕 | Encoder-Free Unified Image and Video Understanding and Generation | ⭐ 417 | +66 | — | Python | `video-reasoning` |
| 10 | [**AMAP-ML/LongHorizon-Harness**](https://github.com/AMAP-ML/LongHorizon-Harness) 🆕 | The long-horizon computer-use harness. Run AI agents across desktop apps and t… | ⭐ 1,855 | +65 | — | Python | `agentic-vision` |
| 11 | [**simular-ai/Agent-S**](https://github.com/simular-ai/Agent-S) | Agent S: the state-of-the-art open source computer use agents | ⭐ 12,896 | +64 | — | Python | `agentic-vision` |
| 12 | [**agent-sh/computer-use-linux**](https://github.com/agent-sh/computer-use-linux) | Native Linux desktop control for AI agents (MCP, Pi… | ⭐ 821 | +45 | — | Rust | `agentic-vision` |
| 13 | [**OpenBMB/MiniCPM-V**](https://github.com/OpenBMB/MiniCPM-V) | See, hear, and interact on your local devices. | ⭐ 27,083 | +43 | — | Python | `multimodal-reasoning` |
| 14 | [**alibaba/page-agent**](https://github.com/alibaba/page-agent) | JavaScript in-page GUI agent. Control web interfaces with natural language. | ⭐ 29,646 | +33 | — | TypeScript | `agentic-vision` |
| 15 | [**Tongyi-MAI/OpenGCUA**](https://github.com/Tongyi-MAI/OpenGCUA) 🆕 | An open-source stack for generalist computer-use agents… | ⭐ 593 | +32 | — | HTML | `agentic-vision` |
| 16 | [**bytedance/UI-TARS**](https://github.com/bytedance/UI-TARS) | Pioneering Automated GUI Interaction with Native Agents | ⭐ 11,683 | +31 | — | Python | `agentic-vision` |
| 17 | [**Hacker-Valley-Media/Interceptor**](https://github.com/Hacker-Valley-Media/Interceptor) | Browser automation and computer use for AI agents… | ⭐ 608 | +26 | — | TypeScript | `agentic-vision` |
| 18 | [**HKUDS/VideoAgent**](https://github.com/HKUDS/VideoAgent) | [EMNLP2026] "VideoAgent: All-in-One Agentic Framework for Video Understanding… | ⭐ 2,007 | +25 | — | Python | `video-reasoning` |
| 19 | [**QwenLM/Qwen3-VL**](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team… | ⭐ 20,175 | +24 | — | Jupyter Notebook | `multimodal-reasoning` |
| 20 | [**yuruotong1/autoMate**](https://github.com/yuruotong1/autoMate) | Like Manus, Computer Use Agent(CUA) and Omniparser… | ⭐ 4,007 | +23 | — | Python | `agentic-vision` |
| 21 | [**X-PLUG/MobileAgent**](https://github.com/X-PLUG/MobileAgent) | Mobile-Agent: The Powerful GUI Agent Family | ⭐ 9,368 | +22 | — | Python | `agentic-vision` |
| 22 | [**OpenMOSS/MOSS-VL**](https://github.com/OpenMOSS/MOSS-VL) | An open-weight 11B model series for long-form and real-time video understandin… | ⭐ 819 | +18 | — | C++ | `video-reasoning` |
| 23 | [**MCG-NJU/VideoJev**](https://github.com/MCG-NJU/VideoJev) 🆕 | VideoJev: System One Model for Video Understanding and Interaction | ⭐ 294 | +18 | — | Python | `video-reasoning` |
| 24 | [**microsoft/OmniParser**](https://github.com/microsoft/OmniParser) | A simple screen parsing tool towards pure vision based GUI agent | ⭐ 25,610 | +14 | — | Jupyter Notebook | `agentic-vision` |
| 25 | [**e2b-dev/open-computer-use**](https://github.com/e2b-dev/open-computer-use) | AI computer use powered by open source LLMs and E2B Desktop Sandbox | ⭐ 2,406 | +14 | — | Python | `agentic-vision` |
| 26 | [**microsoft/fara**](https://github.com/microsoft/fara) | Fara1.5 – A family of frontier computer use agent models | ⭐ 6,248 | +12 | — | Python | `agentic-vision` |
| 27 | [**xlang-ai/OSWorld**](https://github.com/xlang-ai/OSWorld) | [NeurIPS 2024] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in… | ⭐ 3,256 | +11 | — | Python | `agentic-vision` |
| 28 | [**OpenAdaptAI/OpenAdapt**](https://github.com/OpenAdaptAI/OpenAdapt) | For EHRs, payer portals, and any app your team clicks through… | ⭐ 1,865 | +11 | — | Python | `agentic-vision` |
| 29 | [**Purewhiter/mobilegym**](https://github.com/Purewhiter/mobilegym) | [EMNLP 2026] MobileGym: A Verifiable and Highly Parallel Simulation Platform f… | ⭐ 854 | +11 | — | Python | `agentic-vision` |
| 30 | [**xlang-ai/OSWorld-V2**](https://github.com/xlang-ai/OSWorld-V2) | OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks | ⭐ 411 | +10 | — | Python | `agentic-vision` |
| 31 | [**MadeAgents/mobile-use**](https://github.com/MadeAgents/mobile-use) | MobileUse: an open-source mobile GUI agent for Android phone automation… | ⭐ 259 | +10 | — | Python | `agentic-vision` |
| 32 | [**PolyU-VCLab/OmniCompass**](https://github.com/PolyU-VCLab/OmniCompass) 🆕 | OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understan… | ⭐ 151 | +9 | — | Python | `multimodal-reasoning` |
| 33 | [**redai-studio/Relax**](https://github.com/redai-studio/Relax) | An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at… | ⭐ 671 | +8 | — | Python | `multimodal-reasoning` |
| 34 | [**skalesapp/skales**](https://github.com/skalesapp/skales) | Personal AI agent harness for macOS, Windows, Linux, Android & iOS… | ⭐ 2,229 | +7 | — | — | `agentic-vision` |
| 35 | [**sotayang/Awesome-Streaming-Video-Understanding**](https://github.com/sotayang/Awesome-Streaming-Video-Understanding) | 🔥🔥🔥 [Awesome] Latest Papers, Codes & Datasets on Streaming / Online Video Unde… | ⭐ 490 | +7 | — | — | `video-reasoning` |
| 36 | [**microsoft/GUI-Actor**](https://github.com/microsoft/GUI-Actor) | [NeurIPS'25] GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents | ⭐ 424 | ≈+6 | — | Python | `agentic-vision` |
| 37 | [**deepseek-ai/DeepSeek-VL2**](https://github.com/deepseek-ai/DeepSeek-VL2) | DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimoda… | ⭐ 5,399 | +5 | — | Python | `multimodal-reasoning` |
| 38 | [**OSU-NLP-Group/GUI-Agents-Paper-List**](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | Awesome GUI Agent Paper List | ⭐ 926 | +5 | — | TypeScript | `agentic-vision` |
| 39 | [**chekusu/yomado**](https://github.com/chekusu/yomado) 🆕 | Native macOS virtual displays for visual agents… | ⭐ 214 | +5 | — | Objective-C | `agentic-vision` |
| 40 | [**stepfun-ai/gelab-zero**](https://github.com/stepfun-ai/gelab-zero) | STEP-GUI: The top GUI agent solution in the galaxy… | ⭐ 2,295 | +4 | — | Python | `agentic-vision` |
| 41 | [**ZJU-REAL/ClawGUI**](https://github.com/ZJU-REAL/ClawGUI) | Build, Evaluate, and Deploy GUI Agents — online RL training… | ⭐ 1,370 | +4 | — | Python | `agentic-vision` |
| 42 | [**teee000/LiLa-WAM**](https://github.com/teee000/LiLa-WAM) 🆕 | LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipula… | ⭐ 163 | +4 | — | Python | `latent-visual-reasoning` |
| 43 | [**Tencent/UI-Mate**](https://github.com/Tencent/UI-Mate) 🆕 | Advancing Foundation GUI Agents with In-Context Demonstrations | ⭐ 117 | +4 | — | JavaScript | `agentic-vision` |
| 44 | [**NVlabs/VILA**](https://github.com/NVlabs/VILA) | VILA is a family of state-of-the-art vision language models (VLMs) for diverse… | ⭐ 3,871 | +3 | — | Python | `multimodal-reasoning` |
| 45 | [**IPADS-SAI/MobiAgent**](https://github.com/IPADS-SAI/MobiAgent) | The Intelligent GUI Agent for Mobile Phones | ⭐ 1,935 | +3 | — | Python | `agentic-vision` |
| 46 | [**Core-Mate/OpenGUI**](https://github.com/Core-Mate/OpenGUI) | OpenGUI is an Android GUI agent framework for phone-use AI that can see… | ⭐ 1,807 | +3 | — | HTML | `agentic-vision` |
| 47 | [**zhaochen0110/Awesome_Think_With_Images**](https://github.com/zhaochen0110/Awesome_Think_With_Images) | Resources and paper list for "Thinking with Images for LVLMs"… | ⭐ 1,519 | +3 | — | — | `latent-visual-reasoning` |
| 48 | [**bytedance/Lance**](https://github.com/bytedance/Lance) | A 3B-active-parameter native unified multimodal model for image and video unde… | ⭐ 1,365 | +3 | — | Python | `video-reasoning` |
| 49 | [**inclusionAI/UI-Venus**](https://github.com/inclusionAI/UI-Venus) | UI-Venus is a general-purpose foundation GUI agent for mobile apps… | ⭐ 1,077 | +3 | — | HTML | `agentic-vision` |
| 50 | [**sotayang/LiveStar**](https://github.com/sotayang/LiveStar) | [NeurIPS'2025] Official repository for "LiveStar: Live Streaming Assistant for… | ⭐ 163 | +3 | — | Python | `video-reasoning` |
| 51 | [**HarryHsing/OmniAgent**](https://github.com/HarryHsing/OmniAgent) | OmniAgent (ICML 2026): the first native omni-modal agent for active video perc… | ⭐ 86 | +3 | — | Python | `multimodal-reasoning` |
| 52 | [**showlab/ShowUI**](https://github.com/showlab/ShowUI) | [CVPR 2025] Open-source, End-to-end, Vision-Language-Action model for GUI Agen… | ⭐ 1,929 | +2 | — | Python | `agentic-vision` |
| 53 | [**mbzuai-oryx/Video-ChatGPT**](https://github.com/mbzuai-oryx/Video-ChatGPT) | [ACL 2024 🔥] Video-ChatGPT is a video conversation model capable of generating… | ⭐ 1,516 | +2 | — | Python | `video-reasoning` |
| 54 | [**zai-org/CogAgent**](https://github.com/zai-org/CogAgent) | An open-sourced end-to-end VLM-based GUI Agent | ⭐ 1,198 | +2 | — | Python | `agentic-vision` |
| 55 | [**xlang-ai/OpenCUA**](https://github.com/xlang-ai/OpenCUA) | [NeurIPS 2025 Spotlight] OpenCUA: Open Foundations for Computer-Use Agents | ⭐ 874 | +2 | — | Python | `agentic-vision` |
| 56 | [**bytedance/vidi**](https://github.com/bytedance/vidi) | The official repo for "Vidi: Large Multimodal Models for Video Understanding a… | ⭐ 663 | +2 | — | Python | `video-reasoning` |
| 57 | [**google-deepmind/videoprism**](https://github.com/google-deepmind/videoprism) | Official repository for "VideoPrism: A Foundational Visual Encoder for Video U… | ⭐ 401 | +2 | — | Python | `video-reasoning` |
| 58 | [**TaoLiveAIGC/TLive-Omni**](https://github.com/TaoLiveAIGC/TLive-Omni) 🆕 | TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming | ⭐ 342 | +2 | — | Python | `multimodal-reasoning` |
| 59 | [**egolife-ai/Ego-R1**](https://github.com/egolife-ai/Ego-R1) | [TPAMI 2026] Ego-R1: Agentic Chain-of-Tool-Thought for Ultra-Long Egocentric V… | ⭐ 172 | +2 | — | Python | `video-reasoning` |
| 60 | [**huggingface/screensuite**](https://github.com/huggingface/screensuite) | ScreenSuite - The most comprehensive benchmarking suite for GUI Agents! | ⭐ 150 | +2 | — | Python | `agentic-vision` |
<!-- table:end repos -->

## 怎么读这张榜

- **`agentic-vision` 扎堆**：说明工程侧正在从"模型能力"转向"可执行的 agent 产品"，GUI/computer-use 是最卷的落地场景。
- **`multimodal-reasoning` 长期霸榜**：底座模型的每一次发布都会带来一波 star 迁移，看增量比看总量更有信息量。
- **`latent-visual-reasoning` 仓库偏少**：这是典型的研究早期特征——论文多、开源少、复现成本高。想找机会的话，这里是空档。
- **增速突然拉起的仓库**，通常对应一次模型发布或一篇高传播度论文，值得点进去看 commit 时间线。

## 想看更细的？

- 每个仓库的完整 star 历史：`data/repos.json` → `repos.<full_name>.history`
- 赛道分布与总量：`data/stats.json`
- 想加仓库：改 `config/taxonomy.yml` 的 `github_seed` 或 `github_queries`，或直接提 Issue。

---

[← 返回总览](../README.md) · [自动周报](digest.md)
