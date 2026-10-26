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

<!-- table:start repos -->
| 排名 | 项目 | 一句话 | ⭐ | 7 日 Δ | 30 日 Δ | 语言 | 赛道 |
| --: | :-- | :-- | --: | --: | --: | :-- | :-- |
| 1 | [**alibaba/page-agent**](https://github.com/alibaba/page-agent) | JavaScript in-page GUI agent. Control web interfaces with natural language. | ⭐ 29,563 | ≈+520 | — | TypeScript | `agentic-vision` |
| 2 | [**bytedance/UI-TARS-desktop**](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models a… | ⭐ 39,392 | ≈+427 | — | TypeScript | `agentic-vision` |
| 3 | [**trycua/cua**](https://github.com/trycua/cua) | Scale computer-use 2.0 with open-source drivers, cross-OS sandboxes… | ⭐ 30,980 | ≈+343 | — | Rust | `agentic-vision` |
| 4 | [**Tongyi-MAI/OpenGCUA**](https://github.com/Tongyi-MAI/OpenGCUA) 🆕 | An open-source stack for generalist computer-use agents… | ⭐ 497 | ≈+316 | — | HTML | `agentic-vision` |
| 5 | [**ctoldigital/axuse**](https://github.com/ctoldigital/axuse) 🆕 | Accessibility-first browser & computer use for AI agents — one MCP server for… | ⭐ 495 | ≈+289 | — | JavaScript | `agentic-vision` |
| 6 | [**ComputerUseAgent/AutoCua**](https://github.com/ComputerUseAgent/AutoCua) 🆕 | One Computer Use agent for everything (macOS, Windows, Linux, Browser… | ⭐ 655 | ≈+255 | — | Python | `agentic-vision` |
| 7 | [**microsoft/OmniParser**](https://github.com/microsoft/OmniParser) | A simple screen parsing tool towards pure vision based GUI agent | ⭐ 25,551 | ≈+234 | — | Jupyter Notebook | `agentic-vision` |
| 8 | [**OpenBMB/MiniCPM-V**](https://github.com/OpenBMB/MiniCPM-V) | See, hear, and interact on your local devices. | ⭐ 26,976 | ≈+189 | — | Python | `multimodal-reasoning` |
| 9 | [**QwenLM/Qwen3-VL**](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL is the multimodal large language model series developed by Qwen team… | ⭐ 20,119 | ≈+179 | — | Jupyter Notebook | `multimodal-reasoning` |
| 10 | [**uclanlp/OpenVLHarness**](https://github.com/uclanlp/OpenVLHarness) 🆕 | Official Code for OpenVLHarness: Real-World Visual Agentic Tool‑Use with Multi… | ⭐ 258 | ≈+164 | — | Python | `agentic-vision` |
| 11 | [**AMAP-ML/LongHorizon-Harness**](https://github.com/AMAP-ML/LongHorizon-Harness) 🆕 | The long-horizon computer-use harness. Run AI agents across desktop apps and t… | ⭐ 1,779 | ≈+150 | — | Python | `agentic-vision` |
| 12 | [**bytedance/UI-TARS**](https://github.com/bytedance/UI-TARS) | Pioneering Automated GUI Interaction with Native Agents | ⭐ 11,633 | ≈+126 | — | Python | `agentic-vision` |
| 13 | [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | A framework for efficient model inference with omni-modality models | ⭐ 7,354 | ≈+126 | — | Python | `multimodal-reasoning` |
| 14 | [**microsoft/fara**](https://github.com/microsoft/fara) | Fara1.5 – A family of frontier computer use agent models | ⭐ 6,223 | ≈+120 | — | Python | `agentic-vision` |
| 15 | [**simular-ai/Agent-S**](https://github.com/simular-ai/Agent-S) | Agent S: the state-of-the-art open source computer use agents | ⭐ 12,742 | ≈+119 | — | Python | `agentic-vision` |
| 16 | [**MCG-NJU/VideoJev**](https://github.com/MCG-NJU/VideoJev) 🆕 | VideoJev: System One Model for Video Understanding and Interaction | ⭐ 251 | ≈+98 | — | Python | `video-reasoning` |
| 17 | [**chekusu/yomado**](https://github.com/chekusu/yomado) 🆕 | Native macOS virtual displays for visual agents… | ⭐ 196 | ≈+86 | — | Objective-C | `agentic-vision` |
| 18 | [**OpenGVLab/InternVL**](https://github.com/OpenGVLab/InternVL) | [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative to GPT-… | ⭐ 10,171 | ≈+67 | — | Python | `multimodal-reasoning` |
| 19 | [**Core-Mate/OpenGUI**](https://github.com/Core-Mate/OpenGUI) | OpenGUI is an Android GUI agent framework for phone-use AI that can see… | ⭐ 1,802 | ≈+66 | — | HTML | `agentic-vision` |
| 20 | [**X-PLUG/MobileAgent**](https://github.com/X-PLUG/MobileAgent) | Mobile-Agent: The Powerful GUI Agent Family | ⭐ 9,329 | ≈+65 | — | Python | `agentic-vision` |
| 21 | [**MoonshotAI/Kimi-K2.5**](https://github.com/MoonshotAI/Kimi-K2.5) | Open Visual Agentic Intelligence | ⭐ 2,316 | ≈+60 | — | — | `agentic-vision` |
| 22 | [**bytedance/Lance**](https://github.com/bytedance/Lance) | A 3B-active-parameter native unified multimodal model for image and video unde… | ⭐ 1,361 | ≈+58 | — | Python | `video-reasoning` |
| 23 | [**deepseek-ai/DeepSeek-VL2**](https://github.com/deepseek-ai/DeepSeek-VL2) | DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimoda… | ⭐ 5,384 | ≈+55 | — | Python | `multimodal-reasoning` |
| 24 | [**Tongyi-MAI/MAI-UI**](https://github.com/Tongyi-MAI/MAI-UI) | Qwen-UI-Agent: Towards Next-Generation Real-World Centric Foundation GUI Agent | ⭐ 2,421 | ≈+54 | — | Jupyter Notebook | `agentic-vision` |
| 25 | [**lahfir/agent-desktop**](https://github.com/lahfir/agent-desktop) | Agent Desktop gives any agent reliable computer use on the desktop… | ⭐ 1,823 | ≈+51 | — | Rust | `agentic-vision` |
| 26 | [**TurixAI/TuriX-CUA**](https://github.com/TurixAI/TuriX-CUA) | This is the official website for TuriX Computer-use-Agent | ⭐ 3,173 | ≈+50 | — | Python | `agentic-vision` |
| 27 | [**stepfun-ai/gelab-zero**](https://github.com/stepfun-ai/gelab-zero) | STEP-GUI: The top GUI agent solution in the galaxy… | ⭐ 2,291 | ≈+48 | — | Python | `agentic-vision` |
| 28 | [**ZJU-REAL/ClawGUI**](https://github.com/ZJU-REAL/ClawGUI) | Build, Evaluate, and Deploy GUI Agents — online RL training… | ⭐ 1,364 | ≈+47 | — | Python | `agentic-vision` |
| 29 | [**PolyU-VCLab/OmniCompass**](https://github.com/PolyU-VCLab/OmniCompass) 🆕 | OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understan… | ⭐ 118 | ≈+41 | — | Python | `multimodal-reasoning` |
| 30 | [**nv-tlabs/PixelUMM**](https://github.com/nv-tlabs/PixelUMM) 🆕 | Encoder-Free Unified Image and Video Understanding and Generation | ⭐ 297 | ≈+40 | — | Python | `video-reasoning` |
| 31 | [**BBBBchan/DeltaStreamer**](https://github.com/BBBBchan/DeltaStreamer) 🆕 | DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding | ⭐ 88 | ≈+36 | — | Python | `video-reasoning` |
| 32 | [**Purewhiter/mobilegym**](https://github.com/Purewhiter/mobilegym) | [EMNLP 2026] MobileGym: A Verifiable and Highly Parallel Simulation Platform f… | ⭐ 838 | ≈+36 | — | Python | `agentic-vision` |
| 33 | [**zai-org/GLM-V**](https://github.com/zai-org/GLM-V) | GLM-4.6V/4.5V/4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scala… | ⭐ 2,403 | ≈+35 | — | Python | `multimodal-reasoning` |
| 34 | [**TaoLiveAIGC/TLive-Omni**](https://github.com/TaoLiveAIGC/TLive-Omni) 🆕 | TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming | ⭐ 339 | ≈+32 | — | Python | `multimodal-reasoning` |
| 35 | [**IPADS-SAI/MobiAgent**](https://github.com/IPADS-SAI/MobiAgent) | The Intelligent GUI Agent for Mobile Phones | ⭐ 1,927 | ≈+32 | — | Python | `agentic-vision` |
| 36 | [**agent-sh/computer-use-linux**](https://github.com/agent-sh/computer-use-linux) | Native Linux desktop control for AI agents (MCP, Pi… | ⭐ 740 | ≈+31 | — | Rust | `agentic-vision` |
| 37 | [**HKUDS/VideoAgent**](https://github.com/HKUDS/VideoAgent) | [EMNLP2026] "VideoAgent: All-in-One Agentic Framework for Video Understanding… | ⭐ 1,973 | ≈+30 | — | Python | `video-reasoning` |
| 38 | [**NVlabs/VILA**](https://github.com/NVlabs/VILA) | VILA is a family of state-of-the-art vision language models (VLMs) for diverse… | ⭐ 3,867 | ≈+28 | — | Python | `multimodal-reasoning` |
| 39 | [**OpenMOSS/MOSS-VL**](https://github.com/OpenMOSS/MOSS-VL) | An open-weight 11B model series for long-form and real-time video understandin… | ⭐ 792 | ≈+28 | — | C++ | `video-reasoning` |
| 40 | [**yuruotong1/autoMate**](https://github.com/yuruotong1/autoMate) | Like Manus, Computer Use Agent(CUA) and Omniparser… | ⭐ 3,967 | ≈+28 | — | Python | `agentic-vision` |
| 41 | [**mrpulor-gh/nuphus-mcp**](https://github.com/mrpulor-gh/nuphus-mcp) 🆕 | Desktop automation MCP server — computer use for any AI agent: control screen… | ⭐ 329 | ≈+27 | — | Rust | `agentic-vision` |
| 42 | [**apromisedland/VLCoT**](https://github.com/apromisedland/VLCoT) 🆕 | VLCoT research implementation: stage-verifiable latent reasoning… | ⭐ 105 | ≈+26 | — | Python | `latent-visual-reasoning` |
| 43 | [**redai-studio/Relax**](https://github.com/redai-studio/Relax) | An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at… | ⭐ 655 | ≈+23 | — | Python | `multimodal-reasoning` |
| 44 | [**e2b-dev/open-computer-use**](https://github.com/e2b-dev/open-computer-use) | AI computer use powered by open source LLMs and E2B Desktop Sandbox | ⭐ 2,390 | ≈+23 | — | Python | `agentic-vision` |
| 45 | [**zhaochen0110/Awesome_Think_With_Images**](https://github.com/zhaochen0110/Awesome_Think_With_Images) | Resources and paper list for "Thinking with Images for LVLMs"… | ⭐ 1,516 | ≈+21 | — | — | `latent-visual-reasoning` |
| 46 | [**xlang-ai/OSWorld**](https://github.com/xlang-ai/OSWorld) | [NeurIPS 2024] OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in… | ⭐ 3,236 | ≈+21 | — | Python | `agentic-vision` |
| 47 | [**showlab/ShowUI**](https://github.com/showlab/ShowUI) | [CVPR 2025] Open-source, End-to-end, Vision-Language-Action model for GUI Agen… | ⭐ 1,925 | ≈+19 | — | Python | `agentic-vision` |
| 48 | [**OpenGVLab/Ask-Anything**](https://github.com/OpenGVLab/Ask-Anything) | [CVPR2024 Highlight][VideoChatGPT] ChatGPT with video understanding! And many… | ⭐ 3,363 | ≈+18 | — | Python | `video-reasoning` |
| 49 | [**Hacker-Valley-Media/Interceptor**](https://github.com/Hacker-Valley-Media/Interceptor) | Browser automation and computer use for AI agents… | ⭐ 572 | ≈+18 | — | TypeScript | `agentic-vision` |
| 50 | [**inclusionAI/UI-Venus**](https://github.com/inclusionAI/UI-Venus) | UI-Venus is a general-purpose foundation GUI agent for mobile apps… | ⭐ 1,061 | ≈+17 | — | HTML | `agentic-vision` |
| 51 | [**Omni-Scientist/OmniScientist**](https://github.com/Omni-Scientist/OmniScientist) 🆕 | An Omni-Modal, Omni-Discipline AI Scientist | ⭐ 172 | ≈+17 | — | TypeScript | `multimodal-reasoning` |
| 52 | [**teee000/LiLa-WAM**](https://github.com/teee000/LiLa-WAM) 🆕 | LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipula… | ⭐ 155 | ≈+13 | — | Python | `latent-visual-reasoning` |
| 53 | [**fyzhang1/ExpActivator**](https://github.com/fyzhang1/ExpActivator) 🆕 | Official code for "Relevance Does Not Imply Applicability: Experience Activati… | ⭐ 87 | ≈+13 | — | Python | `agentic-vision` |
| 54 | [**MME-Benchmarks/Video-MME-v2**](https://github.com/MME-Benchmarks/Video-MME-v2) | Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Und… | ⭐ 365 | ≈+12 | — | Python | `video-reasoning` |
| 55 | [**xlang-ai/OpenCUA**](https://github.com/xlang-ai/OpenCUA) | [NeurIPS 2025 Spotlight] OpenCUA: Open Foundations for Computer-Use Agents | ⭐ 868 | ≈+12 | — | Python | `agentic-vision` |
| 56 | [**ZiiJianLiu/Omni-Woodpecker**](https://github.com/ZiiJianLiu/Omni-Woodpecker) 🆕 | Official implementation of "Omni-Woodpecker: Hallucination Correction via Evid… | ⭐ 97 | ≈+12 | — | Python | `multimodal-reasoning` |
| 57 | [**facebookresearch/pytorchvideo**](https://github.com/facebookresearch/pytorchvideo) | A deep learning library for video understanding research. | ⭐ 3,571 | ≈+12 | — | Python | `video-reasoning` |
| 58 | [**NVlabs/OmniVinci**](https://github.com/NVlabs/OmniVinci) | OmniVinci is an omni-modal LLM for joint understanding of vision, audio… | ⭐ 685 | ≈+12 | — | Python | `multimodal-reasoning` |
| 59 | [**TeleAI-UAGI/telemem**](https://github.com/TeleAI-UAGI/telemem) | TeleMem is a high-performance drop-in replacement for Mem0… | ⭐ 494 | ≈+11 | — | Python | `video-reasoning` |
| 60 | [**Tencent/UI-Mate**](https://github.com/Tencent/UI-Mate) 🆕 | Advancing Foundation GUI Agents with In-Context Demonstrations | ⭐ 111 | ≈+11 | — | JavaScript | `agentic-vision` |
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
