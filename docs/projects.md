# 🚀 项目雷达 · GitHub Tracker

> 每日快照 star 数，按 **7 日增速** 排序。增速比总量更能反映"现在大家在做什么"。
> 数据来自 `data/repos.json`（含每个仓库的 star 历史），由 `scripts/track_github.py` 维护。

[← 返回总览](../README.md) · [自动周报](digest.md)

---

## 榜单口径

| 项目 | 说明 |
| :-- | :-- |
| 入选 | 配置中的种子仓库 + 按赛道关键词搜索命中（`stars ≥ 阈值`、近半年有 push、非归档） |
| 排序 | 7 日 star 增量 → 30 日增量 → 总 star（历史不足时自动退化为总 star 排序） |
| `🆕` | 仓库创建于近 120 天内 |
| `—` | 快照历史不足，无法计算该窗口增量 |

> 为什么不用总 star 排？因为总 star 是**存量**，会把多年前的老项目顶在上面；
> 增速是**流量**，才看得出赛道当前的注意力在哪。

## 当前榜单

<!-- table:start repos -->
| 排名 | 项目 | 一句话 | ⭐ | 7 日 Δ | 30 日 Δ | 语言 | 赛道 |
| --: | :-- | :-- | --: | --: | --: | :-- | :-- |
| 1 | [**bytedance/UI-TARS-desktop**](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models a… | ⭐ 39,392 | — | — | TypeScript | `agentic-vision` |
| 2 | [**trycua/cua**](https://github.com/trycua/cua) | Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes… | ⭐ 30,980 | — | — | Rust | `agentic-vision` |
| 3 | [**alibaba/page-agent**](https://github.com/alibaba/page-agent) | JavaScript in-page GUI agent. Control web interfaces with natural language. | ⭐ 29,563 | — | — | TypeScript | `agentic-vision` |
| 4 | [**OpenBMB/MiniCPM-V**](https://github.com/OpenBMB/MiniCPM-V) | See, hear, and interact on your local devices. | ⭐ 26,976 | — | — | Python | `multimodal-reasoning` |
| 5 | [**microsoft/OmniParser**](https://github.com/microsoft/OmniParser) | A simple screen parsing tool towards pure vision based GUI agent | ⭐ 25,551 | — | — | Jupyter Notebook | `agentic-vision` |
| 6 | [**QwenLM/Qwen3-VL**](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team… | ⭐ 20,119 | — | — | Jupyter Notebook | `multimodal-reasoning` |
| 7 | [**NanmiCoder/cc-haha**](https://github.com/NanmiCoder/cc-haha) | 本地优先的跨平台 Claude Code / AI Agent 桌面工作台：多 Agent 协作、Git Worktree、代码 Diff、技能市场、多模型… | ⭐ 15,167 | — | — | TypeScript | `agentic-vision` |
| 8 | [**simular-ai/Agent-S**](https://github.com/simular-ai/Agent-S) | Agent S: the state-of-the-art open source computer use agents | ⭐ 12,742 | — | — | Python | `agentic-vision` |
| 9 | [**bytedance/UI-TARS**](https://github.com/bytedance/UI-TARS) | Pioneering Automated GUI Interaction with Native Agents | ⭐ 11,633 | — | — | Python | `agentic-vision` |
| 10 | [**OpenGVLab/InternVL**](https://github.com/OpenGVLab/InternVL) | [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-… | ⭐ 10,171 | — | — | Python | `multimodal-reasoning` |
| 11 | [**X-PLUG/MobileAgent**](https://github.com/X-PLUG/MobileAgent) | Mobile-Agent: The Powerful GUI Agent Family | ⭐ 9,329 | — | — | Python | `agentic-vision` |
| 12 | [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | A framework for efficient model inference with omni-modality models | ⭐ 7,354 | — | — | Python | `multimodal-reasoning` |
| 13 | [**microsoft/fara**](https://github.com/microsoft/fara) | Fara1.5 – A family of frontier computer use agent models | ⭐ 6,223 | — | — | Python | `agentic-vision` |
| 14 | [**the-open-agent/openagent**](https://github.com/the-open-agent/openagent) | ⚡️next-generation personal AI assistant powered by LLM, RAG and agent loops… | ⭐ 5,712 | — | — | Go | `agentic-vision` |
| 15 | [**deepseek-ai/DeepSeek-VL2**](https://github.com/deepseek-ai/DeepSeek-VL2) | DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimoda… | ⭐ 5,384 | — | — | Python | `multimodal-reasoning` |
| 16 | [**yuruotong1/autoMate**](https://github.com/yuruotong1/autoMate) | Like Manus, Computer Use Agent(CUA) and Omniparser… | ⭐ 3,967 | — | — | Python | `agentic-vision` |
| 17 | [**NVlabs/VILA**](https://github.com/NVlabs/VILA) | VILA is a family of state-of-the-art vision language models (VLMs) for diverse… | ⭐ 3,867 | — | — | Python | `multimodal-reasoning` |
| 18 | [**facebookresearch/pytorchvideo**](https://github.com/facebookresearch/pytorchvideo) | A deep learning library for video understanding research. | ⭐ 3,571 | — | — | Python | `video-reasoning` |
| 19 | [**OpenGVLab/Ask-Anything**](https://github.com/OpenGVLab/Ask-Anything) | [CVPR2024 Highlight][VideoChatGPT] ChatGPT with video understanding! And many… | ⭐ 3,363 | — | — | Python | `video-reasoning` |
| 20 | [**xlang-ai/OSWorld**](https://github.com/xlang-ai/OSWorld) | [NeurIPS 2024] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in… | ⭐ 3,236 | — | — | Python | `agentic-vision` |
| 21 | [**TurixAI/TuriX-CUA**](https://github.com/TurixAI/TuriX-CUA) | This is the official website for TuriX Computer-use-Agent | ⭐ 3,173 | — | — | Python | `agentic-vision` |
| 22 | [**Tongyi-MAI/MAI-UI**](https://github.com/Tongyi-MAI/MAI-UI) | Qwen-UI-Agent: Towards Next-Generation Real-World Centric Foundation GUI Agent | ⭐ 2,421 | — | — | Jupyter Notebook | `agentic-vision` |
| 23 | [**zai-org/GLM-V**](https://github.com/zai-org/GLM-V) | GLM-4.6V/4.5V/4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scala… | ⭐ 2,403 | — | — | Python | `multimodal-reasoning` |
| 24 | [**e2b-dev/open-computer-use**](https://github.com/e2b-dev/open-computer-use) | AI computer use powered by open source LLMs and E2B Desktop Sandbox | ⭐ 2,390 | — | — | Python | `agentic-vision` |
| 25 | [**MoonshotAI/Kimi-K2.5**](https://github.com/MoonshotAI/Kimi-K2.5) | Open Visual Agentic Intelligence | ⭐ 2,316 | — | — | — | `agentic-vision` |
| 26 | [**stepfun-ai/gelab-zero**](https://github.com/stepfun-ai/gelab-zero) | STEP-GUI: The top GUI agent solution in the galaxy… | ⭐ 2,291 | — | — | Python | `agentic-vision` |
| 27 | [**HKUDS/VideoAgent**](https://github.com/HKUDS/VideoAgent) | [EMNLP2026] "VideoAgent: All-in-One Agentic Framework for Video Understanding… | ⭐ 1,973 | — | — | Python | `video-reasoning` |
| 28 | [**IPADS-SAI/MobiAgent**](https://github.com/IPADS-SAI/MobiAgent) | The Intelligent GUI Agent for Mobile Phones | ⭐ 1,927 | — | — | Python | `agentic-vision` |
| 29 | [**showlab/ShowUI**](https://github.com/showlab/ShowUI) | [CVPR 2025] Open-source, End-to-end, Vision-Language-Action model for GUI Agen… | ⭐ 1,925 | — | — | Python | `agentic-vision` |
| 30 | [**OpenAdaptAI/OpenAdapt**](https://github.com/OpenAdaptAI/OpenAdapt) | For EHRs, payer portals, and any app your team clicks through… | ⭐ 1,826 | — | — | Python | `agentic-vision` |
| 31 | [**lahfir/agent-desktop**](https://github.com/lahfir/agent-desktop) | Agent Desktop gives any agent reliable computer use on the desktop… | ⭐ 1,823 | — | — | Rust | `agentic-vision` |
| 32 | [**Core-Mate/OpenGUI**](https://github.com/Core-Mate/OpenGUI) | OpenGUI is an Android GUI agent framework for phone-use AI that can see… | ⭐ 1,802 | — | — | HTML | `agentic-vision` |
| 33 | [**AMAP-ML/LongHorizon-Harness**](https://github.com/AMAP-ML/LongHorizon-Harness) 🆕 | The long-horizon computer-use harness. Run AI agents across desktop apps and t… | ⭐ 1,779 | — | — | Python | `agentic-vision` |
| 34 | [**zhaochen0110/Awesome_Think_With_Images**](https://github.com/zhaochen0110/Awesome_Think_With_Images) | Resources and paper list for "Thinking with Images for LVLMs"… | ⭐ 1,516 | — | — | — | `latent-visual-reasoning` |
| 35 | [**mbzuai-oryx/Video-ChatGPT**](https://github.com/mbzuai-oryx/Video-ChatGPT) | [ACL 2024 🔥] Video-ChatGPT is a video conversation model capable of generating… | ⭐ 1,513 | — | — | Python | `video-reasoning` |
| 36 | [**ZJU-REAL/ClawGUI**](https://github.com/ZJU-REAL/ClawGUI) | Build, Evaluate, and Deploy GUI Agents — online RL training… | ⭐ 1,364 | — | — | Python | `agentic-vision` |
| 37 | [**bytedance/Lance**](https://github.com/bytedance/Lance) | A 3B-active-parameter native unified multimodal model for image and video unde… | ⭐ 1,361 | — | — | Python | `video-reasoning` |
| 38 | [**zai-org/CogAgent**](https://github.com/zai-org/CogAgent) | An open-sourced end-to-end VLM-based GUI Agent | ⭐ 1,197 | — | — | Python | `agentic-vision` |
| 39 | [**inclusionAI/UI-Venus**](https://github.com/inclusionAI/UI-Venus) | UI-Venus is a general-purpose foundation GUI agent for mobile apps… | ⭐ 1,061 | — | — | HTML | `agentic-vision` |
| 40 | [**OSU-NLP-Group/GUI-Agents-Paper-List**](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | Awesome GUI Agent Paper List | ⭐ 917 | — | — | TypeScript | `agentic-vision` |
| 41 | [**feder-cr/invisible_playwright_mcp**](https://github.com/feder-cr/invisible_playwright_mcp) 🆕 | Playwright MCP server undetected by anti-bots and captchas: AI agent browses t… | ⭐ 882 | — | — | Python | `agentic-vision` |
| 42 | [**xlang-ai/OpenCUA**](https://github.com/xlang-ai/OpenCUA) | [NeurIPS 2025 Spotlight] OpenCUA: Open Foundations for Computer-Use Agents | ⭐ 868 | — | — | Python | `agentic-vision` |
| 43 | [**Purewhiter/mobilegym**](https://github.com/Purewhiter/mobilegym) | [EMNLP 2026] MobileGym: A Verifiable and Highly Parallel Simulation Platform f… | ⭐ 838 | — | — | Python | `agentic-vision` |
| 44 | [**OpenMOSS/MOSS-VL**](https://github.com/OpenMOSS/MOSS-VL) | An open-weight 11B model series for long-form and real-time video understandin… | ⭐ 792 | — | — | C++ | `video-reasoning` |
| 45 | [**agent-sh/computer-use-linux**](https://github.com/agent-sh/computer-use-linux) | Native Linux desktop control for AI agents (MCP, Pi… | ⭐ 740 | — | — | Rust | `agentic-vision` |
| 46 | [**NVlabs/OmniVinci**](https://github.com/NVlabs/OmniVinci) | OmniVinci is an omni-modal LLM for joint understanding of vision, audio… | ⭐ 685 | — | — | Python | `multimodal-reasoning` |
| 47 | [**bytedance/vidi**](https://github.com/bytedance/vidi) | The official repo for "Vidi: Large Multimodal Models for Video Understanding a… | ⭐ 661 | — | — | Python | `video-reasoning` |
| 48 | [**ComputerUseAgent/AutoCua**](https://github.com/ComputerUseAgent/AutoCua) 🆕 | One Computer Use agent for everything (macOS, Windows, Linux, Browser… | ⭐ 655 | — | — | Python | `agentic-vision` |
| 49 | [**redai-studio/Relax**](https://github.com/redai-studio/Relax) | An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at… | ⭐ 655 | — | — | Python | `multimodal-reasoning` |
| 50 | [**HITsz-TMG/Awesome-Large-Multimodal-Reasoning-Models**](https://github.com/HITsz-TMG/Awesome-Large-Multimodal-Reasoning-Models) | The development and future prospects of large multimodal reasoning models. | ⭐ 620 | — | — | — | `multimodal-reasoning` |
| 51 | [**gokayfem/ComfyUI_VLM_nodes**](https://github.com/gokayfem/ComfyUI_VLM_nodes) | ComfyUI nodes for vision-language models: Qwen3-VL, Moondream 3, Florence-2… | ⭐ 592 | — | — | Python | `multimodal-reasoning` |
| 52 | [**Hacker-Valley-Media/Interceptor**](https://github.com/Hacker-Valley-Media/Interceptor) | Browser automation and computer use for AI agents… | ⭐ 572 | — | — | TypeScript | `agentic-vision` |
| 53 | [**Tongyi-MAI/OpenGCUA**](https://github.com/Tongyi-MAI/OpenGCUA) 🆕 | An open-source stack for generalist computer-use agents… | ⭐ 497 | — | — | HTML | `agentic-vision` |
| 54 | [**ctoldigital/axuse**](https://github.com/ctoldigital/axuse) 🆕 | Accessibility-first browser & computer use for AI agents — one MCP server for… | ⭐ 495 | — | — | JavaScript | `agentic-vision` |
| 55 | [**TeleAI-UAGI/telemem**](https://github.com/TeleAI-UAGI/telemem) | TeleMem is a high-performance drop-in replacement for Mem0… | ⭐ 494 | — | — | Python | `video-reasoning` |
| 56 | [**sotayang/Awesome-Streaming-Video-Understanding**](https://github.com/sotayang/Awesome-Streaming-Video-Understanding) | 🔥🔥🔥 [Awesome] Latest Papers, Codes & Datasets on Streaming / Online Video Unde… | ⭐ 481 | — | — | — | `video-reasoning` |
| 57 | [**ZJU-REAL/Awesome-GUI-Agents**](https://github.com/ZJU-REAL/Awesome-GUI-Agents) | A curated collection of resources, tools… | ⭐ 464 | — | — | — | `agentic-vision` |
| 58 | [**testdriverai/testdriverai**](https://github.com/testdriverai/testdriverai) | Computer-Use SDK for E2E QA Testing | ⭐ 464 | — | — | JavaScript | `agentic-vision` |
| 59 | [**MugheesMehdi07/langvio**](https://github.com/MugheesMehdi07/langvio) | A powerful AI library that bridges Large Language Models (LLMs) with video pro… | ⭐ 425 | — | — | Python | `video-reasoning` |
| 60 | [**google-deepmind/videoprism**](https://github.com/google-deepmind/videoprism) | Official repository for "VideoPrism: A Foundational Visual Encoder for Video U… | ⭐ 400 | — | — | Python | `video-reasoning` |
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
