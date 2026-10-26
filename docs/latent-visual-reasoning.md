# 🧠 Latent Visual Reasoning · 潜在视觉推理

> 一句话：**不写出来，直接在隐空间里想。**
> 把中间推理从「生成自然语言 token」换成「生成/复用连续隐状态」，让模型在视觉证据上推理，而不是在语言先验上推理。

[← 返回总览](../README.md) · [智能体视觉 →](agentic-vision.md)

---

## 1. 为什么会有这条赛道

多模态模型的推理长期被两件事夹住：

| 问题 | 显式文本 CoT 的处境 |
| :-- | :-- |
| **推理成本** | 每个思考 token 都要过一遍 decode，长链推理的延迟和显存随长度线性涨 |
| **视觉流失真** | 图像被一次性压进若干 token，之后所有推理都在语言空间里进行，视觉证据只剩"摘要" |
| **不可微** | 文本是离散采样，中间步骤没法用梯度端到端优化 |

潜在视觉推理的赌注是：**如果中间状态不需要给人看，那它就不必是文字。** 用连续隐向量承载"我在看哪里、下一步查什么"，既省掉 decode，又保留了通往视觉特征的梯度通路。

## 2. 三种「隐」的位置

理解这条赛道，先分清 latent 被放在哪里——这决定了方法的能力上限：

```
            ┌──────────────── 隐 token 派 ────────────────┐
输入 ──▶ [视觉编码] ──▶ [<lat_1> <lat_2> … <lat_k>] ──▶ [解码] ──▶ 答案
                              ▲  在输入序列里插入可学习的连续槽位
                              │  优点：实现简单，兼容现有 AR 训练
                              └─ 风险：latent 容易退化成"无信息的占位符"

            ┌──────────────── 隐状态派 ───────────────────┐
输入 ──▶ [编码] ──▶ hidden state h_t ──▶ 直接回灌为下一步输入（不经过 lm_head）
                              ▲  优点：真正绕开离散瓶颈，推理步数与 token 数解耦
                              └─ 风险：无监督锚点，容易表示坍缩（所有 h 趋同）

            ┌──────────────── 隐视觉派 ───────────────────┐
输入 ──▶ [编码] ──▶ 在视觉特征空间生成中间"想象中的图/框/掩码" ──▶ 再推理
                              ▲  优点：中间态本身就是可检查的视觉证据
                              └─ 风险：需要额外的视觉生成/对齐目标，训练复杂
```

## 3. 方法谱系

| 谱系 | 核心机制 | 代表思路 | 主要代价 |
| :-- | :-- | :-- | :-- |
| **连续思维链** | 用隐状态替代文本 CoT 步骤 | 把最后隐状态当作下一步输入，逐步"想" | 需要课程式训练，否则学不到有效隐步骤 |
| **隐 token 监督** | 插入 latent 槽位 + 分阶段监督（规划/定位/取证） | 用框、证据区域、规划文本分别监督不同 latent | 监督信号设计成本高，标注依赖强 |
| **隐专家/混合** | 多个 latent 分工提取互补视觉证据 | 不同 latent 走不同投影，最后聚合 | 结构复杂，需防冗余 |
| **视觉中间态生成** | 先"想象"再推理（visualization-of-thought） | 生成中间图像/标注图，再基于它作答 | 生成误差会传播到最终答案 |
| **隐空间蒸馏** | 用文本 CoT 教师蒸馏出隐推理学生 | 学生只出隐状态，不出文字 | 上限受教师限制 |

## 4. 关键矛盾（读论文时对着这张表看）

| 矛盾 | 表现 | 常见解法 |
| :-- | :-- | :-- |
| 可解释性 ↔ 效率 | 隐状态说不出"我在想什么" | 分阶段探针、把 latent 解码回文本做审计 |
| 自由度 ↔ 可控性 | latent 想跑偏没人拦 | 类型化阶段监督、对比式反事实训练 |
| 表达力 ↔ 坍缩 | 多个 latent 学到同一件事 | 互补性正则、专家隔离、增加 latent 预算的边际收益检验 |
| 省 token ↔ 需更多步 | 隐步骤数变多，总 FLOPs 未必降 | 步数预算控制、早停 |

## 5. 阅读路径建议

1. 先看**连续思维链**，理解"隐状态回灌"为什么能work、什么时候失效；
2. 再看**隐 token 监督**，这是当前把隐推理做得"可控"的主流路线；
3. 然后看**隐视觉**，它把"想"和"看"绑在一起，是这条赛道与 agentic vision 的接口；
4. 最后看**评测**——隐推理最大的软肋是"分数涨了但说不清为什么"，务必关注消融是否证明了 latent 通路真的被用上（例如遮掉 latent 通路后掉多少分）。

## 6. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充；ID 失效会自动剔除，不留死链。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2024-12-09 | **Training Large Language Models to Reason in a Continuous Latent Space** | Shibo Hao, Sainbayar Sukhbaatar et al. | 连续隐空间推理的开创性工作：用隐状态替代文本 CoT，是本赛道一切工作的起点 | [📄 2412.06769](https://arxiv.org/abs/2412.06769) |
| 2025-09-29 | **Latent Visual Reasoning** | Bangzheng Li, Ximeng Sun et al. | 把隐推理正式搬到视觉域的代表作，确立了'隐视觉推理'这一提法 | [📄 2509.24251](https://arxiv.org/abs/2509.24251) |
| 2024-06-13 | **Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models** | Yushi Hu, Weijia Shi et al. | 把草图/标注当视觉思维链，隐视觉派最直观的范式 | [📄 2406.09403](https://arxiv.org/abs/2406.09403) |
| 2025-01-13 | **Imagine while Reasoning in Space: Multimodal Visualization-of-Thought** | Chengzu Li, Wenshan Wu et al. | 多模态可视化思维链：先在心里'画出'中间图再推理 | [📄 2501.07542](https://arxiv.org/abs/2501.07542) |
| 2025-06-30 | **Thinking with Images for Multimodal Reasoning: Foundations, Methods, and Future Frontiers** | Zhaochen Su, Peng Xia et al. | 综述：系统梳理'用图像思考'的谱系、方法与开放问题，入门首选 | [📄 2506.23918](https://arxiv.org/abs/2506.23918) |
<!-- table:end classics -->

## 7. 📄 自动跟踪的最新论文

> 每日由 GitHub Actions 从 arXiv 抓取、打分、去重后写入；按提交日期倒序，表内最多保留 300 条，更早的仍留在 `data/papers.json`。

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-10-22 | **See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space** | Jiawei Chen, Yinxi Wang et al. | What visual representation should a navigation policy act on? Navigation policies built on visi... | [📄 2610.31762](https://arxiv.org/abs/2610.31762) `cs.RO` |
| 2026-10-21 | **ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination** | Nithin Sivakumaran, Ali Payani et al. | Forming an accurate theory-of-mind (ToM) is key to successful multi-agent collaboration and req... | [📄 2610.29934](https://arxiv.org/abs/2610.29934) [💻](https://github.com/nsivaku/tom2vec) 🤗 |
| 2026-10-19 | **Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation** | Jiaming Liu, Xinghao Zhu et al. | Multimodal reasoning provides robotic foundation models with predictive context needed for reli... | [📄 2610.26854](https://arxiv.org/abs/2610.26854) `cs.RO` |
| 2026-10-15 | **Does Latent Chain-of-Thought Actually Reason? A Single, Unifying Taxonomy for Latent Reasoning** | Jingjie Qiu, Sheldon Yu et al. | Latent chain-of-thought replaces written reasoning steps with continuous hidden states... | [📄 2610.21182](https://arxiv.org/abs/2610.21182) `cs.AI` |
| 2026-10-14 | **ReferFlow: Beyond Final-Target Localization for Complex Referring Expressions** | Tianyi Gao, Han Fang et al. | Multimodal Large Language Models have made significant progress in referring expression compreh... | [📄 2610.20352](https://arxiv.org/abs/2610.20352) `cs.CV` |
| 2026-10-13 | **Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine** | Thomas Hannagan | The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes pr... | [📄 2610.19220](https://arxiv.org/abs/2610.19220) `cs.LG` |
| 2026-10-13 | **Breaking the Average: Overcoming Convergent Defaults in Robotic Manipulation via Diagnostic Chain-of-Thought and Structured Guidance** | Mohammed Daba, Waleed Abdulrahman Saleh AlAkwa | Recent Vision-Language-Action (VLA) models, such as $π_{0.5}$... | [📄 2610.17983](https://arxiv.org/abs/2610.17983) `cs.RO` |
| 2026-10-09 | **Thinking with Images without Coordinates** | Meng Cao, Haoze Zhao et al. | Recent advances in multi-modal large language models have shifted toward the "thinking with ima... | [📄 2610.14265](https://arxiv.org/abs/2610.14265) `cs.CV` |
| 2026-10-08 | **Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models** | Hongyu Shi, Sen Zhao et al. | Latent reasoning enables vision-language-action (VLA) models to transform multimodal observatio... | [📄 2610.12090](https://arxiv.org/abs/2610.12090) `cs.AI` |
| 2026-10-07 | **Think Before You Paint: Recursive Latent Reasoning for Diffusion Models** | Paweł Skierś, Małgorzata Grzanka et al. | Diffusion models generate realistic images but often fail on visual reasoning tasks... | [📄 2610.09876](https://arxiv.org/abs/2610.09876) `cs.AI` |
| 2026-10-07 | **Spatial Latent Reasoning for Embodied Reference Understanding** | Ling Li, Jianhui Zhong et al. | Pointing-gesture visual grounding requires connecting hand geometry with the visual identity an... | [📄 2610.09418](https://arxiv.org/abs/2610.09418) `cs.CV` |
| 2026-10-05 | **CALR: Continuous Anchored Latent Reasoning via Render-of-Thought Compression** | Zhaoyang Wei, Bowen Jiang et al. | Visual latent reasoning compresses rendered derivations into compact intermediate states... | [📄 2610.07175](https://arxiv.org/abs/2610.07175) `cs.CV` |
| 2026-10-04 | **Enhancing Long-Video VLM Embeddings with Query-Aware Streaming Latent Reasoning** | Haozhe Chi, Song Jin et al. | Long-video embedding requires capturing sparse query-relevant evidence under a limited visual-t... | [📄 2610.04864](https://arxiv.org/abs/2610.04864) `cs.CV` |
| 2026-10-01 | **MoLE: Mixture of Latent Experts for Complementary Visual Reasoning** | Yingcheng Liu, Tianyi Jiang et al. | Latent visual reasoning equips vision--language models with continuous intermediate states that... | [📄 2610.01917](https://arxiv.org/abs/2610.01917) `cs.CV` |
| 2026-09-30 | **Looped Diffusion Transformer** | Yong Xien Chng, Tianyi Chen et al. | Improving text-to-image models has traditionally relied on increasing model size or the number... | [📄 2609.40305](https://arxiv.org/abs/2609.40305) `cs.CV` |
| 2026-09-28 | **Rethinking Latent Visual Reasoning: Grounding Latent Reasoning in Visual Evidence** | Xi Xiao, Tianchen Zhao et al. | Latent visual reasoning (LVR) enables multimodal large language models (MLLMs) to perform inter... | [📄 2609.34563](https://arxiv.org/abs/2609.34563) `cs.CV` |
| 2026-09-28 | **GenoMorph: Pathway-Grounded Genomic Disease Reasoning via Adaptive Latent Computation** | Tanmoy Kanti Halder, Akash Ghosh et al. | Large language models (LLMs) have demonstrated strong capabilities in biological reasoning... | [📄 2609.34079](https://arxiv.org/abs/2609.34079) `cs.AI` |
| 2026-09-27 | **VaME: Exploring Variational Latent Reasoning for Multimodal Embeddings** | Peixi Wu, Mingzhou Jiang et al. | Universal multimodal retrieval requires compact embeddings that preserve task-relevant semantic... | [📄 2609.33402](https://arxiv.org/abs/2609.33402) `cs.CV` |
| 2026-09-27 | **Next Thoughts Are Distributions: Generative Autoregressive Reasoning in the Latent Space** | Yang Li, Yi Wang et al. | Reasoning problems often admit multiple valid ways to proceed... | [📄 2609.33271](https://arxiv.org/abs/2609.33271) `cs.AI` |
| 2026-09-25 | **Skip the Talk, Re-Focus on Vision: Latent Reasoning for Reasoning Segmentation in Multimodal Large Language Models** | Tianhang Guo, Yulin He et al. | Reasoning segmentation aims to interpret implicit textual queries and enable fine-grained visua... | [📄 2609.30783](https://arxiv.org/abs/2609.30783) `cs.CV` |
| 2026-09-24 | **Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent Space** | Jaron Yeh, Yen-Wei Chang et al. | Industrial anomaly detection (IAD) is evolving beyond conventional detection and localization t... | [📄 2609.29457](https://arxiv.org/abs/2609.29457) `cs.CV` |
| 2026-09-17 | **Schema-Anchored Latent Reasoning for Semantic Parsing-Based Knowledge Base Question Answering** | Guangze Gao, Zixuan Li et al. | Semantic parsing (SP)-based knowledge base question answering aims to answer natural language q... | [📄 2609.20398](https://arxiv.org/abs/2609.20398) `cs.CL` |
| 2026-09-17 | **Learn Your Own Thoughts: Abstract Token Curriculum** | Khashayar Gatmiry, Avrajit Ghosh et al. | Large Language Models (LLMs) have achieved remarkable reasoning capabilities by utilizing chain... | [📄 2609.19717](https://arxiv.org/abs/2609.19717) `cs.LG` |
| 2026-09-09 | **Structural Process Supervision for Latent Chain-of-Thought Reasoning** | Yiqi Li, Xu Chen et al. | Latent reasoning approaches enhance token-level efficiency and robustness by replacing verbose... | [📄 2609.09928](https://arxiv.org/abs/2609.09928) `cs.AI` |
| 2026-09-04 | **Fractal basins trap latent reasoning** | Jeffrey Lai, Anthony Bao et al. | Reasoning allows artificial intelligence models to revisit and correct their mistakes... | [📄 2609.04963](https://arxiv.org/abs/2609.04963) `cs.LG` |
| 2026-09-04 | **Latent-Aligned Reasoning for Multimodal Recommendation** | Jiarui Jin, Anyang Ji | Multimodal Vision-Language Models (VLMs) have demonstrated remarkable capabilities in cross-mod... | [📄 2609.04645](https://arxiv.org/abs/2609.04645) `cs.IR` |
| 2026-09-03 | **Assessing Adversarial Robustness of Latent Reasoning Models** | Shaolong Chen, Ang Li et al. | Large language models increasingly rely on long chain-of-thought (CoT) trajectories for complex... | [📄 2609.22228](https://arxiv.org/abs/2609.22228) `cs.CL` |
| 2026-09-01 | **Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs** | Zhaoliang Chen, Jie Fu | Chain-of-thought reasoning unfolds in discrete token space: each step is committed as text... | [📄 2609.01117](https://arxiv.org/abs/2609.01117) `cs.AI` |
| 2026-08-04 | **Perception Before Reasoning: Dynamic Latent Reasoning for Video Understanding and Question Answering** | Haotian Xia, Zilin Xiao et al. | Video question answering requires models to ground language queries in visual evidence and... | [📄 2608.04124](https://arxiv.org/abs/2608.04124) `cs.CV` |
| 2026-08-04 | **Balancing Efficiency and Efficacy: Training-Free Attention-Guided Switching Between Explicit and Latent Thoughts for MLLMs** | Haoqian Kang, Liupeng Li et al. | Reasoning in Multimodal Large Language Models (MLLMs) requires both fine-grained visual percept... | [📄 2608.03450](https://arxiv.org/abs/2608.03450) `cs.MM` |
| 2026-08-04 | **LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation** | Fan Yang, Yuting Su et al. | World-action modeling has emerged as a promising paradigm for robotic control... | [📄 2608.03701](https://arxiv.org/abs/2608.03701) `cs.RO` |
| 2026-08-03 | **Douyin Multimodal Embedding Model Technical Report** | Haonan Chen, Chu Li et al. | Multimodal representation learning is a cornerstone of modern AI... | [📄 2608.02148](https://arxiv.org/abs/2608.02148) `cs.IR` |
| 2026-07-23 | **The Weight of Silence: A Causal Case for Weights Over the Scratchpad in Latent Chess Reasoning** | Ishan S. Kshirsagar | Latent, or silent, reasoning lets language models carry out intermediate computation in continu... | [📄 2607.20952](https://arxiv.org/abs/2607.20952) `cs.LG` |
| 2026-07-15 | **GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding** | Hao Li, Han Fang et al. | Although multimodal large language models (MLLMs) have achieved remarkable progress... | [📄 2607.13454](https://arxiv.org/abs/2607.13454) `cs.CV` |
| 2026-07-09 | **LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action** | Qi Lyu, Baicheng Liu et al. | Vision-language-action (VLA) models aim to map multimodal inputs to robot actions... | [📄 2607.08182](https://arxiv.org/abs/2607.08182) `cs.CV` |
| 2026-07-05 | **CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving** | Zhaohong Liu, Hao Ye et al. | End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving... | [📄 2607.04179](https://arxiv.org/abs/2607.04179) `cs.CV` |
| 2026-07-03 | **ProLaViT: Learning Progressive Latent Visual Thoughts in Structured Latent Space** | Peiming Li, Yifan Wang et al. | Multimodal Large Language Models (MLLMs) have achieved remarkable progress but still struggle w... | [📄 2607.02907](https://arxiv.org/abs/2607.02907) `cs.CV` |
| 2026-07-01 | **Think in Latent, Explain in Language: Self-Explainable Latent Reasoning** | Dayuan Zhao, Shengcao Cao et al. | Latent reasoning has emerged as a powerful alternative to text-based Chain-of-Thought (CoT)... | [📄 2608.13570](https://arxiv.org/abs/2608.13570) `cs.CL` |
| 2026-07-01 | **Retrieved Images as Visual Thought: Training-Free Multimodal In-Context Learning for the Open-vs-Closed Gap** | Bingchen Huang, Zhiling Wang et al. | Recent work on Thinking with Images makes vision a dynamic part of reasoning... | [📄 2607.00606](https://arxiv.org/abs/2607.00606) `cs.CV` |
| 2026-07-01 | **Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning** | Shijie Li, Yilin Gao et al. | Multimodal Large Language Models (MLLMs) are often constrained by a language-space bottleneck... | [📄 2607.00461](https://arxiv.org/abs/2607.00461) `cs.CV` |
| 2026-06-30 | **CoLT: Teaching Multi-Modal Models to Think with Chain of Latent Thoughts** | Lianyu Hu, Shengqian Qin et al. | Chain-of-thought (CoT) reasoning has enabled multi-modal large language models (MLLMs) to tackl... | [📄 2606.31986](https://arxiv.org/abs/2606.31986) `cs.CV` |
| 2026-06-30 | **MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents** | Hao Sun, Yu Song et al. | VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-sca... | [📄 2606.31167](https://arxiv.org/abs/2606.31167) `cs.RO` |
| 2026-06-29 | **Why Struggle with Continuous Latents? Interpretable Discrete Latent Reasoning via Rendered Compression** | Shuochen Chang, Qingyang Liu et al. | Large language models achieve high reasoning performance via explicit chain-of-thought and rein... | [📄 2606.29712](https://arxiv.org/abs/2606.29712) `cs.CL` |
| 2026-06-25 | **From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP** | Zhixing Li, Yinan Yu | Current VLM evaluations often conflate language priors with genuine spatial reasoning... | [📄 2606.26535](https://arxiv.org/abs/2606.26535) `cs.CV` |
| 2026-06-18 | **What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis** | Xinghao Chen, Chak Tou Leong et al. | Latent Chain-of-Thought (CoT) internalizes reasoning within continuous hidden states... | [📄 2606.20075](https://arxiv.org/abs/2606.20075) `cs.LG` |
| 2026-06-17 | **Taming I2V models for Image HOI Editing: A Cognitive Benchmark and Agentic Self-Correcting Framework** | Jiayi Gao, Qingchao Chen et al. | Current image editing methods excel at static attributes but fail at complex Human-Object Inter... | [📄 2606.19073](https://arxiv.org/abs/2606.19073) `cs.CV` |
| 2026-06-15 | **Latent Thought Flow: Efficient Latent Reasoning in Large Language Models** | Xiandong Zou, Jing Huang et al. | Large Language Models (LLMs) increasingly rely on intermediate reasoning... | [📄 2606.16222](https://arxiv.org/abs/2606.16222) `cs.AI` |
| 2026-06-13 | **Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models** | Dianqiao Lei, Lianlei Shan | Existing Vision-Language-Action (VLA) models predominantly rely on explicit Chain-of-Thought (C... | [📄 2606.15099](https://arxiv.org/abs/2606.15099) `cs.CV` |
| 2026-06-13 | **From Frames to Temporal Graphs: In-Context Egocentric Action Recognition with Vision-Language Models** | Bessie Dominguez-Dager, Francisco Gomez-Donoso et al. | Action reasoning in egocentric video requires capturing fine-grained transitions of hand-object... | [📄 2606.15417](https://arxiv.org/abs/2606.15417) `cs.CV` |
| 2026-06-11 | **LaME: Learning to Think in Latent Space for Multimodal Embedding via Information Bottleneck** | Peixi Wu, Biao Yang et al. | Reasoning-driven universal multimodal embedding has advanced rapidly by introducing Chain-of-Th... | [📄 2606.13061](https://arxiv.org/abs/2606.13061) `cs.CV` |
| 2026-06-04 | **Closing the Loop on Latent Reasoning via Test-Time Reconstruction** | Xiaopeng Yuan, Haibo Jin et al. | Recent work moves intermediate reasoning from natural-language traces into latent or cache-leve... | [📄 2606.06252](https://arxiv.org/abs/2606.06252) `cs.AI` |
| 2026-06-04 | **MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action** | Boyang Zhang, Lianlei Shan | Vision-Language-Action (VLA) policies remain brittle in long-horizon control... | [📄 2606.06245](https://arxiv.org/abs/2606.06245) `cs.RO` |
| 2026-06-04 | **Cosine Misleads: Auxiliary Losses Reshape Vision Language Models, Not Their Latents** | XiuYu Zhang, Junfeng Fang et al. | Latent visual reasoning (LVR) inserts supervised latent tokens between perception and answer ge... | [📄 2606.05753](https://arxiv.org/abs/2606.05753) `cs.CV` |
| 2026-06-04 | **Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems** | Yingzhuo Liu | Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for... | [📄 2606.05711](https://arxiv.org/abs/2606.05711) `cs.CL` |
| 2026-05-31 | **Unlocking the Black Box of Latent Reasoning: An Interpretability-Guided Approach to Intervention** | Shuochen Chang, Tong Bai et al. | Latent reasoning enables Large Language Models (LLMs) to perform multi-step inference within co... | [📄 2606.01243](https://arxiv.org/abs/2606.01243) `cs.CL` |
| 2026-05-30 | **DeepLatent: Think with Images via Parallel Latent Visual Reasoning** | Dongchen Lu, Zhimo Li et al. | The emerging paradigm of "thinking with images" embeds visual states into intermediate reasonin... | [📄 2606.00562](https://arxiv.org/abs/2606.00562) `cs.CV` |
| 2026-05-29 | **Continuous Reasoning for Vision-Language-Action** | Yueh-Hua Wu, Tatsuya Matsushima et al. | Natural language is a powerful reasoning medium for language and vision-language models... | [📄 2606.00229](https://arxiv.org/abs/2606.00229) `cs.RO` |
<!-- table:end papers -->

## 8. 常用评测

`MMVP`（细粒度视觉感知）· `BLINK`（视觉感知短板）· `V*`（高分辨率搜索）· `MathVista`（视觉数学）· `ChartQA`（图表）· `MMMU`（学科推理）

> 隐推理论文常见的问题：只报平均分。真正有说服力的证据是 **同 token 预算下的对比** 与 **latent 通路消融**。

## 9. 开放问题

- 隐步骤数该由谁决定？固定 K、学习式停止、还是按难度自适应？
- 隐状态能不能跨样本复用（把"推理模板"存成可检索的 latent）？
- 隐推理与工具调用如何共存——什么时候"想"，什么时候"去看"？
- 如何评测隐推理的**忠实性**，而不只是准确率？

---

[← 返回总览](../README.md) · [智能体视觉 →](agentic-vision.md)
