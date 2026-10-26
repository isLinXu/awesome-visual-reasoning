# ⚡ Efficient Visual Reasoning · 视觉推理效率

> 一句话：**让模型"想得起"，也"想得便宜"。**
> 这是横切赛道：隐推理之所以被提出，很大动力就是省掉长文本 CoT 的 decode 开销。这里收录视觉 token 压缩、动态分辨率、thinking budget、早停与蒸馏。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/spark-efficient-visual-reasoning-dark.svg">
  <img src="../assets/spark-efficient-visual-reasoning-light.svg" alt="Efficient Visual Reasoning 近 12 周论文发布趋势" width="900">
</picture>

[← 多模态推理底座](multimodal-reasoning.md) · [返回总览](../README.md)

---

## 1. 成本花在哪里

一次多模态推理的 token 账本：

```
视觉 token（固定大头）  ████████████████████  高分辨率图轻松上千
思考 token（可变大头）  ██████████████████████████  长 CoT 可到数千
输出 token              ██  通常很短
```

两个大头正好对应两类工作：**压视觉输入** 与 **控思考长度**。

## 2. 压视觉输入

| 手段 | 做法 | 风险 |
| :-- | :-- | :-- |
| Token 剪枝/合并 | 按注意力或相似度丢掉冗余视觉 token | 丢的恰好是关键细节（小字、细线） |
| 动态分辨率 | 按图像内容/任务难度决定切图数量 | 策略学不好就两头不讨好 |
| 分层/多尺度编码 | 先粗看再局部精看 | 需要两阶段推理，延迟不一定降 |
| 视觉 tokenizer 压缩 | 更高压缩率的离散码本 | 保真度下降，重建与理解目标冲突 |

## 3. 控思考长度

- **Thinking budget**：显式限制思考 token 上限，或让模型自己预测需要多长。
- **早停 / 自适应深度**：用置信度或验证器判断"想够了"。
- **过度思考（overthinking）治理**：简单题上长 CoT 反而降分，需要难度感知的路由。
- **隐式推理**：直接把思考压进隐状态，是这条线的极端形态 → 见 [潜在视觉推理](latent-visual-reasoning.md)。

## 4. 正确的评价方式

> 单看准确率毫无意义。这个赛道唯一有说服力的图是 **准确率–成本 Pareto 前沿**：
> 横轴为平均输出 token 数或端到端延迟，纵轴为 benchmark 分数，比较谁在同等成本下更高。

至少要报：平均 token 数、P95 延迟、峰值显存、以及在**高分辨率/长视频**子集上的退化幅度。

## 5. 🏛 奠基与必读

> 由 `scripts/seed_classics.py` 按 arXiv ID 校验后自动填充。

<!-- table:start classics -->
| 日期 | 论文 | 作者 | 为什么必读 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2024-03-11 | **An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models** | Liang Chen, Haozhe Zhao et al. | 视觉 token 剪枝的开创性工作：图像 token 的注意力极稀疏，砍掉大部分几乎不掉点 | [📄 2403.06764](https://arxiv.org/abs/2403.06764) |
| 2024-03-22 | **LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models** | Yuzhang Shang, Mu Cai et al. | 自适应 token 归并，把'压多少'交给数据决定而非固定比例 | [📄 2403.15388](https://arxiv.org/abs/2403.15388) |
| 2025-02-16 | **Learning to Stop Overthinking at Test Time** | Hieu Tran Bao, Nguyen Cong Dat et al. | 测试时学会'停止思考'，多模态过度思考治理的代表 | [📄 2502.10954](https://arxiv.org/abs/2502.10954) |
<!-- table:end classics -->

## 6. 📄 自动跟踪的最新论文

<!-- table:start papers -->
| 日期 | 论文 | 作者 | 核心贡献 | 链接 |
| :-- | :-- | :-- | :-- | :-- |
| 2026-10-19 | **On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models** | Chenpan Li, Thies Brockmoeller et al. | Modern language models are increasingly asked to handle several tasks within a single prompt... | [📄 2610.27190](https://arxiv.org/abs/2610.27190) `cs.CL` [💻](https://github.com/chenpanli/fragility) |
| 2026-10-18 | **ReTrace: Visual Backtracking for Efficient Multimodal Large Language Models** | Guangzong Si, Dong Wang et al. | Multimodal Large Language Models (MLLMs) encode images into dense visual token sequences... | [📄 2610.25005](https://arxiv.org/abs/2610.25005) `cs.CV` |
| 2026-10-18 | **Visual Sufficiency Landscapes: Understanding Query-Conditioned Reliability in Visual Token Pruning** | Zhenghan Li, Kexin Sun et al. | Different visual token pruning strategies retain different subsets while maintaining similar ta... | [📄 2610.24968](https://arxiv.org/abs/2610.24968) `cs.CV` |
| 2026-10-17 | **Are We Evaluating VLM Token Pruning Right? Looking Beyond Accuracy and Token Count** | Geng Li, Guohao Chen et al. | Visual token pruning aims to reduce inference cost while preserving the capabilities of the ori... | [📄 2610.24740](https://arxiv.org/abs/2610.24740) `cs.AI` |
| 2026-10-16 | **Hierarchical and Query-Aware Visual Token Pruning for High-Resolution LVLMs** | Luther Wei, Ling Zou et al. | High-resolution Large Vision-Language Models (LVLMs) preserve critical... | [📄 2610.24102](https://arxiv.org/abs/2610.24102) `cs.CV` |
| 2026-10-15 | **FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models** | Jiuyi Xu, Chengyuan Qian et al. | Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot mani... | [📄 2610.22146](https://arxiv.org/abs/2610.22146) `cs.RO` |
| 2026-10-15 | **MedSTP: Preserving Subspace and Transition Evidence for Medical VQA Token Pruning** | Mengchen Fan, Qizhen Lan et al. | Medical vision-language models (VLMs) for visual question answering (VQA) often pass long visua... | [📄 2610.22751](https://arxiv.org/abs/2610.22751) `cs.CV` |
| 2026-10-15 | **PACE: Pareto-Adaptive Compression for Efficient Native MLLMs** | Lei Tian, Chunzheng Zhu et al. | Native multimodal large language models (native MLLMs) jointly encode visual and linguistic seq... | [📄 2610.24005](https://arxiv.org/abs/2610.24005) `cs.CV` |
| 2026-10-14 | **Complementary Future Token Pruning for World Action Models** | Baekseung Kim, Junhoo Lee et al. | World action models (WAMs) jointly predict future visual states and robot actions... | [📄 2610.19957](https://arxiv.org/abs/2610.19957) `cs.RO` |
| 2026-10-14 | **OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score** | Liang-Hsun Huang, Min-Yi Chen et al. | OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models... | [📄 2610.19848](https://arxiv.org/abs/2610.19848) `cs.CL` |
| 2026-10-13 | **How Much Can We Prune? Exploring the Performance Limits of Visual Token Pruning** | Janghoon Cho, Shubhankar Borse et al. | Visual token pruning is increasingly used to reduce the memory and inference costs of vision-la... | [📄 2610.23974](https://arxiv.org/abs/2610.23974) `cs.CV` |
| 2026-10-13 | **Visual Tokens on Demand: Visual Budgeting for Scalable and Efficient Multi-Image Reasoning in Multimodal LLMs** | Aimon Rahman, Joymallya Chakraborty et al. | Multimodal large language models have advanced rapidly... | [📄 2610.18858](https://arxiv.org/abs/2610.18858) `cs.CV` |
| 2026-10-13 | **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs** | Peiran Yin, Hao Wu et al. | Visual token pruning for multimodal large language models (MLLMs) appears highly effective... | [📄 2610.18399](https://arxiv.org/abs/2610.18399) `cs.CV` |
| 2026-10-13 | **TwinPrune: Density-Aware Two-Phase Token Pruning for Vision-Language Models** | Kai Liu, Anqi Li et al. | A unified spatial-density signal to score token importance for both inference phases: bipartite... | [📄 2610.17530](https://arxiv.org/abs/2610.17530) `cs.CV` |
| 2026-10-13 | **LoOPSD: On-Policy Self-Distillation with Looped Teachers** | Wei Fan, Qingyue Yang et al. | On-policy self-distillation improves a model using guidance from the model itself... | [📄 2610.18162](https://arxiv.org/abs/2610.18162) `cs.LG` |
| 2026-10-13 | **DVTR-KD: Distilling Vision-Language Models via Intermediate Visual Token Reconstruction** | Haolan Wei, Jiahui Wang et al. | Multimodal large language models (MLLMs) have achieved strong performance on diverse vision-lan... | [📄 2610.17853](https://arxiv.org/abs/2610.17853) `cs.CV` |
| 2026-10-12 | **When 1+1 Backfires: Rethinking Relevance-Diversity Balancing for Sample-Aware Visual Token Reduction** | Yihang Huang, Peisong Wen et al. | Visual token compression has emerged as a critical technique for reducing the inference cost of... | [📄 2610.16615](https://arxiv.org/abs/2610.16615) `cs.AI` |
| 2026-10-12 | **FoveaTree: Information-Density Trees for Query-Guided Visual Token Pruning in Video Large Language Models** | Zihan Meng, Weidong Chen et al. | Video large language models (Video LLMs) encode each frame into hundreds of visual tokens... | [📄 2610.16744](https://arxiv.org/abs/2610.16744) `cs.CV` |
| 2026-10-09 | **SheafPrune: Sheaf-Guided Graph Propagation for Visual Token Pruning** | Xiaoyang Ma, Chi Wang et al. | Multimodal large language models process the complete visual token sequence... | [📄 2610.13263](https://arxiv.org/abs/2610.13263) `cs.CV` |
| 2026-10-09 | **Video Codec-Guided Training-Free Token Compression for Video Large Language Models** | Xihua Sheng, Ruijie Liu et al. | Video large language models (VLLMs) rely on long visual token sequences to understand complex t... | [📄 2610.12959](https://arxiv.org/abs/2610.12959) `cs.CV` |
| 2026-10-07 | **Adaptive Visual Token Reduction for Accelerated Image Understanding** | Seyoung Jeong, Jong Pil Yun et al. | Large Vision-Language Models achieve strong VQA performance, but processing high-resolution... | [📄 2610.09252](https://arxiv.org/abs/2610.09252) `cs.CV` |
| 2026-10-07 | **Unbalanced Optimal Transport for Efficient Visual Document Retrieval** | Hoyeon Shin, Jeongyeon Kim et al. | Vision-Language Models(VLMs)have advanced Visual Document Retrieval (VDR) by enabling OCR-free... | [📄 2610.23929](https://arxiv.org/abs/2610.23929) `cs.CV` |
| 2026-10-06 | **DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models** | Shuo Yang, Changbai Li et al. | Recent training-free pruning approaches for Multimodal Large Language Models (MLLMs) effectivel... | [📄 2610.08341](https://arxiv.org/abs/2610.08341) `cs.CV` |
| 2026-10-06 | **VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models** | Owen Du, Yang Yue et al. | Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur h... | [📄 2610.08133](https://arxiv.org/abs/2610.08133) `cs.RO` |
| 2026-10-06 | **CARE: Certifying Acceleration for Vision-Language-Action Inference** | Rui Liu, Tong Zheng et al. | While vision-language-action (VLA) models have advanced rapidly... | [📄 2610.08917](https://arxiv.org/abs/2610.08917) `cs.CL` |
| 2026-10-04 | **When and What to Prune? Stage-Aware Visual Token Pruning for Efficient VLA** | Tianjun Shi, Haotian Xiong et al. | Visual token pruning is an effective way to accelerate vision-language models and is especially... | [📄 2610.05273](https://arxiv.org/abs/2610.05273) `cs.CV` |
| 2026-09-30 | **Sparse-WAM: Accelerating World Action Models via Action-Guided Sparse Imagination** | Xinling Xie, Haodong Wang et al. | World-action models (WAMs) leverage pretrained video models to improve generalization in robot... | [📄 2609.38984](https://arxiv.org/abs/2609.38984) `cs.RO` |
| 2026-09-30 | **When Masking Helps or Hurts Robustness in Compressed CLIP: A Pre-Deployment Diagnostic** | Muhammad Zawish, Steven Davy | This paper demonstrate that whether masking-based token pruning helps or hurts worst-group robu... | [📄 2609.39704](https://arxiv.org/abs/2609.39704) `cs.CV` |
| 2026-09-29 | **TReVS: Integrating Textual Relevance and Visual Saliency for Efficient Vision-Language Model Token Pruning** | Jing Wang, Zhiping Wu et al. | Vision-Language Models (VLMs) excel at visual understanding and reasoning but often incur subst... | [📄 2609.37581](https://arxiv.org/abs/2609.37581) `cs.CV` |
| 2026-09-29 | **Representation Dynamics Reveal Semantic Saliency and Similarity for Visual Token Pruning in MLLMs** | Weixuan Li, Zikun Zhou et al. | Multimodal large language models (MLLMs) incur high inference latency from long visual token se... | [📄 2609.36916](https://arxiv.org/abs/2609.36916) `cs.CV` |
| 2026-09-29 | **RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA** | Chengjie Jiang, Yunqi Zhou et al. | Ultra-high-resolution (UHR) remote sensing visual question answering (VQA) requires models to r... | [📄 2609.38072](https://arxiv.org/abs/2609.38072) `cs.CV` |
| 2026-09-29 | **Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference** | Jiayu Chen, Shuyong Gao et al. | Existing VLA pruning strategies primarily select individual visual tokens according to task-lev... | [📄 2609.36967](https://arxiv.org/abs/2609.36967) `cs.RO` |
| 2026-09-28 | **Beyond Selection: Token Parameterization for Extreme Visual Token Compression** | Rui Zhong, Yu Li et al. | Visual-token compression is effective for improving the efficiency of vision-language models... | [📄 2609.35232](https://arxiv.org/abs/2609.35232) `cs.CV` |
| 2026-09-28 | **P4Q: Co-designing Token Pruning and Quantization for Vision-Language Model Acceleration** | Haizhao Jing, Zhenhao Shang et al. | Vision language models have achieved strong performance across a wide range of multimodal appli... | [📄 2609.34867](https://arxiv.org/abs/2609.34867) `cs.CV` |
| 2026-09-28 | **When Text Matters: Design Principles for Visual Token Pruning in Vision-Language Model** | Minchan Kang, Kyeonghye Park et al. | Visual token pruning has been widely studied as a practical approach to reducing the computatio... | [📄 2609.34861](https://arxiv.org/abs/2609.34861) `cs.CV` |
| 2026-09-28 | **ACPruner: Visual Token Pruning as Biased Attention Coverage Maximization in LVLMs** | Xu Li, Yuxuan Liang et al. | Large Vision-Language Models (LVLMs) face significant computational inefficiencies caused by th... | [📄 2609.34558](https://arxiv.org/abs/2609.34558) `cs.CV` |
| 2026-09-28 | **Rethinking Visual Token Compression for Video Large Language Models: A Simple Yet Strong Baseline** | Xiao Zhang, Wang Zeng et al. | Video Large Language Models (Video LLMs) have achieved remarkable progress in video understandi... | [📄 2609.35394](https://arxiv.org/abs/2609.35394) `cs.CV` |
| 2026-09-28 | **SPIDER: Multi-Layer Semantic Token Pruning and Adaptive Sub-Layer Skipping in Multimodal Large Language Models** | Tianxiang Chen, Zhentao Tan et al. | Multimodal Large Language Models face significant efficiency challenges that stem from two dist... | [📄 2609.34977](https://arxiv.org/abs/2609.34977) `cs.CV` |
| 2026-09-28 | **DORA: Dynamic Online Reinforcement Agent for Token Pruning in Vision Transformers** | Kaixuan He, Song Chen et al. | Vision Transformers (ViTs) incur quadratic self-attention cost in the number of tokens... | [📄 2609.34325](https://arxiv.org/abs/2609.34325) `cs.CV` |
| 2026-09-28 | **SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models** | Ahmadreza Jeddi, Enming Zhang et al. | Reasoning vision-language models (VLMs) process images and videos as long sequences of visual t... | [📄 2609.34044](https://arxiv.org/abs/2609.34044) `cs.CV` |
| 2026-09-28 | **EdgeVLN: Runtime-Aware Deployment Ready Quantized Vision Language Navigation Model** | Rithvik Jonna, Man Namgung et al. | Vision-language navigation (VLN) models perform well but target compute-rich platforms... | [📄 2609.35570](https://arxiv.org/abs/2609.35570) `cs.RO` |
| 2026-09-28 | **Still There, No Longer Seen: Exposing Compression-Induced Risk in Large Vision-Language Models** | Qiankun Li, Yuechen Zhang et al. | Visual token compression reduces the inference cost of Large Vision-Language Models (LVLMs)... | [📄 2609.35002](https://arxiv.org/abs/2609.35002) `cs.CV` |
| 2026-09-28 | **Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models** | Jingdi lei, Junxian Li et al. | Long visual token sequences often account for a substantial fraction of the computational overh... | [📄 2609.34972](https://arxiv.org/abs/2609.34972) `cs.CV` |
| 2026-09-27 | **CoViST: Visual Token Compression via Composable States** | Qi Zhang, Xiandong Meng et al. | Visual token compression lowers the inference cost of vision--language models by representing i... | [📄 2609.33397](https://arxiv.org/abs/2609.33397) `cs.AI` |
| 2026-09-26 | **Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction** | Junxian Li, Ruixuan Yang et al. | Visual token reduction is an effective way to accelerate multimodal large language models (MLLM... | [📄 2609.32353](https://arxiv.org/abs/2609.32353) `cs.CV` |
| 2026-09-24 | **MedTokenBudget: Lesion-Preserving Token Routing for Dermoscopic Image Classification** | Zhexiang Li | Dermoscopy classifiers built on Vision Transformers process all image patches uniformly... | [📄 2609.30613](https://arxiv.org/abs/2609.30613) `cs.CV` |
| 2026-09-23 | **Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces** | Andrew Bond, Ege Erdem Özlü et al. | Methods operating on Vision Transformer (ViT) feature spaces typically rely on Euclidean distan... | [📄 2609.27988](https://arxiv.org/abs/2609.27988) `cs.CV` |
| 2026-09-22 | **From Token Importance to Conditional Removability: Rethinking Visual Token Pruning in Multimodal Large Language Models** | Shengli He, Yongchao Liang et al. | Training-free visual-token pruning often uses token importance, redundancy... | [📄 2609.26484](https://arxiv.org/abs/2609.26484) `cs.CV` |
| 2026-09-22 | **Shallow to Deep: Aligning Token Pruning with Stage-wise Roles in LVLMs** | Shuo Zhang, Jintao Tong et al. | Large Vision-Language Models (LVLMs) incur high computational costs from redundant visual token... | [📄 2609.25635](https://arxiv.org/abs/2609.25635) `cs.CV` |
| 2026-09-21 | **VPRune: Efficient Training-free Pre-LLM Visual Token Pruning** | Guangchuan Lv, Dianxing Shi et al. | Visual token pruning is a promising approach to reducing the inference cost of large vision-lan... | [📄 2609.24485](https://arxiv.org/abs/2609.24485) `cs.CV` |
| 2026-09-21 | **SLICEChat: Progressive In-Encoder Token Pruning for Whole-Slide Pathology Language Models** | Ali Kerem Bozkurt, Baris Cem Bakay et al. | Whole-slide pathology images (WSIs) contain gigapixel-scale visual content... | [📄 2609.24894](https://arxiv.org/abs/2609.24894) `cs.CV` |
| 2026-09-20 | **Layer-Aware Position Embeddings for Visual Token Pruning in Multimodal Large Language Models** | Yahong Wang, Zhangkai Ni et al. | Multimodal large language models (MLLMs) incur substantial computational overhead due to the re... | [📄 2609.23715](https://arxiv.org/abs/2609.23715) `cs.CV` |
| 2026-09-18 | **Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing** | Chongbo Zhao, Jiangming Wang et al. | Text-guided video editing modifies target content while preserving the appearance and temporal... | [📄 2609.21268](https://arxiv.org/abs/2609.21268) `cs.CV` |
| 2026-09-17 | **QCPruner: Query-Conditioned Population Coverage for Visual Token Pruning** | Shengli He, Yongchao Liang et al. | The high visual-token load in multimodal large language models (MLLMs) motivates training-free... | [📄 2609.19990](https://arxiv.org/abs/2609.19990) `cs.CV` |
| 2026-09-14 | **Don't Send What You Don't Need: Question-Guided Token Pruning as a Privacy Defense for Vision-Language Models** | Md Khalid Syfullah, Alvi Ataur Khalil | Visual Question Answering (VQA) with Vision-Language Models (VLMs) is increasingly used in priv... | [📄 2609.15671](https://arxiv.org/abs/2609.15671) `cs.CV` |
| 2026-09-12 | **StepPrune: Adaptive Sequential Visual Token Selection across Multimodal Large Language Models** | Hansen Zhang, Landi He et al. | Visual prefixes account for a major portion of the per-layer computation in multimodal large la... | [📄 2609.13804](https://arxiv.org/abs/2609.13804) `cs.CV` |
| 2026-09-09 | **Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs** | Haiji Liang, Pengfei Zhou et al. | Multimodal large language models (MLLMs) process hundreds or thousands of visual tokens per ima... | [📄 2609.10346](https://arxiv.org/abs/2609.10346) `cs.CV` |
| 2026-09-08 | **CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs** | Nhat-Tan Bui, Varshini Elangovan et al. | Representing a 3D scene as multi-view images allows 2D VLMs to reason in 3D by reusing priors f... | [📄 2609.08345](https://arxiv.org/abs/2609.08345) `cs.CV` |
| 2026-09-05 | **STAR-Pro: Stage-Wise Token Adaptive Reduction with Progressive Refinement for Efficient Large Vision-Language Models** | Yichen Guo, Tinghao Wang et al. | Large vision-language models (LVLMs) achieve strong multimodal understanding... | [📄 2609.05916](https://arxiv.org/abs/2609.05916) `cs.CV` |
| 2026-09-03 | **CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding** | Jing Jiang, Yiran Ling et al. | Streaming video understanding requires Vision Language Models (VLLMs) to process growing video... | [📄 2609.03675](https://arxiv.org/abs/2609.03675) `cs.CV` |
| 2026-09-02 | **Who Speaks for the Pruned? Visual Token Pruning as Coverage Optimization** | Qingchan Zhu, Weihang You et al. | Visual token pruning reduces the inference cost of vision-language models (VLMs)... | [📄 2609.03158](https://arxiv.org/abs/2609.03158) `cs.CV` |
| 2026-09-01 | **SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models** | Shiyu Li, Zi-Yuan Hu et al. | Despite their strong multimodal understanding ability... | [📄 2609.01004](https://arxiv.org/abs/2609.01004) `cs.CV` |
| 2026-09-01 | **S$^2$Prune: Spatially Structured Visual Token Pruning for Multimodal Large Language Models** | Yuanyuan Jia, Shunpu Tang et al. | Visual token pruning reduces the inference overhead of multimodal large language models (MLLMs)... | [📄 2609.01224](https://arxiv.org/abs/2609.01224) `cs.CV` |
| 2026-09-01 | **From Saliency to Discriminability: Rank-Preserving Visual Token Pruning for VLM Rerankers** | Siyi Liu, Hanjun Yang et al. | Large vision-language models used as listwise rerankers must jointly process visual tokens from... | [📄 2609.00667](https://arxiv.org/abs/2609.00667) `cs.IR` |
| 2026-08-31 | **Centering before Pruning: Lightweight Geometry Correction for Diversity-Based Visual Token Pruning in LVLMs** | Shunjie Wen, Jaeyeon Lee et al. | Large vision-language models (LVLMs) incur substantial inference costs due to their long and hi... | [📄 2608.30263](https://arxiv.org/abs/2608.30263) `cs.CV` |
| 2026-08-27 | **Multi-Image Visual Token Pruning in Large Visual Language Models** | Rongyang Zhang, Chengqiang Lu et al. | With the growing demand for processing multiple image sequences in real-world applications... | [📄 2608.26806](https://arxiv.org/abs/2608.26806) `cs.CV` |
| 2026-08-27 | **PACE: A Unified Condense-and-Extract Paradigm for Fast VLM Inference** | Junjie Liu, Shengyuan Ye et al. | Vision-Language Models (VLMs) demonstrate exceptional visual reasoning capabilities... | [📄 2608.27206](https://arxiv.org/abs/2608.27206) `cs.CV` |
| 2026-08-26 | **Not All Attention Heads Contribute to Critical Visual Token Selection: Head-Aware Pruning Matters More** | Chaofang Ma, Lin Jiang et al. | Vision-Language Models (VLMs) have exhibited impressive performance across diverse visual scena... | [📄 2608.25332](https://arxiv.org/abs/2608.25332) `cs.CV` |
| 2026-08-24 | **E2S-Pruner: Progressive Two-Stage Evidence Fusion for Visual Token Pruning in Vision-Language Models** | Taoyu Qian, Qi Wang et al. | Vision-language models typically encode an image into hundreds of visual tokens... | [📄 2608.23253](https://arxiv.org/abs/2608.23253) `cs.CV` |
| 2026-08-24 | **HAP: Head-Adaptive Visual Token Pruning via Cross-Modal Alignment** | Yuanhao Sun, Huawei Ji et al. | Recent Vision-Language Models encode high-resolution images into long visual token sequences... | [📄 2608.23921](https://arxiv.org/abs/2608.23921) `cs.CV` |
| 2026-08-23 | **RS$^3$-Prune: Read-Sparse, Store-Sparse Token Pruning for Video Object Segmentation** | Avilasha Mandal, Sarvesh Shashikumar | RS$^3$-Prune, a training-free token-pruning recipe that instantiates as a small set of inferenc... | [📄 2608.22526](https://arxiv.org/abs/2608.22526) `cs.CV` |
| 2026-08-21 | **Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models** | Zhuoyuan Li, Rui Zhao et al. | Token compression has become a key technique for reducing the inference cost of large foundatio... | [📄 2608.21247](https://arxiv.org/abs/2608.21247) `cs.CV` |
| 2026-08-19 | **Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies** | Wei Jiang, Wei Wang | Vision-Language-Action (VLA) models process long multimodal token sequences... | [📄 2608.18410](https://arxiv.org/abs/2608.18410) `cs.LG` |
| 2026-08-19 | **Clustering and Token Denoising for Faster and More Robust VLMs** | Baptiste Rossigneux, Inna Kucher et al. | Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by addi... | [📄 2608.19285](https://arxiv.org/abs/2608.19285) `cs.CV` |
| 2026-08-17 | **SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation** | Xunyao Lei, Renjun Wu et al. | At every re-observation point in a hierarchical Vision-Language-Action (VLA) system... | [📄 2608.16172](https://arxiv.org/abs/2608.16172) `cs.RO` |
| 2026-08-15 | **SA-GEM: Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning for Efficient Remote Sensing Large Vision-Language Models** | Kexin Ma, Jing Xiao et al. | RS-LVLMs have advanced multimodal understanding of Earth observation imagery... | [📄 2608.15075](https://arxiv.org/abs/2608.15075) `cs.CV` |
| 2026-08-13 | **CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport** | Peng Ling, Yingda Yin et al. | While 3D Vision-Language Models (3D VLMs) have demonstrated remarkable spatial reasoning capabi... | [📄 2608.13226](https://arxiv.org/abs/2608.13226) `cs.CV` |
| 2026-08-11 | **When Vision Becomes Text: Visual Token Pruning via Cross-Modal Residual Guidance in VLMs** | Congyang Ou, Ruike Song et al. | Abundant visual information strengthens vision-language model (VLM) perception... | [📄 2608.10489](https://arxiv.org/abs/2608.10489) `cs.CV` |
| 2026-08-11 | **Putting Registers to Work: Task Registers for Token Pruning in Vision Transformers** | Hongsen Cao, Mona Jaber et al. | Token-pruning policies are usually designed for a single recognition pipeline... | [📄 2608.10989](https://arxiv.org/abs/2608.10989) `cs.CV` |
| 2026-08-07 | **An AI4AI Framework for Visual Token Pruning** | Zhen Liu, Wenli Huang et al. | Visual-token pruning can substantially reduce the inference cost of multimodal large language m... | [📄 2608.07193](https://arxiv.org/abs/2608.07193) `cs.LG` |
| 2026-08-07 | **RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs** | Qiyanhui Lu, Han Wu et al. | Multimodal large language models (MLLMs) encode images as long visual token sequences... | [📄 2608.07088](https://arxiv.org/abs/2608.07088) `cs.CV` |
| 2026-07-30 | **Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large Language Models** | Jie Ma, Zhike Qiu et al. | While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs)... | [📄 2607.28341](https://arxiv.org/abs/2607.28341) `cs.CV` |
| 2026-07-28 | **Salient Knowledge Pathways: Sparse Cross-Modal Routing for Efficient Knowledge-Intensive Multimodal Question Answering** | Noor Islam S. Mohammad, Uluğ Bayazıt | Knowledge-intensive multimodal question answering (KI-MMQA) sits at the intersection of three e... | [📄 2607.25422](https://arxiv.org/abs/2607.25422) `cs.AI` |
| 2026-07-23 | **Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence** | Jay Gor, Karm Dave et al. | Efficient multimodal inference is increasingly constrained not only by model quality or FLOP co... | [📄 2607.20981](https://arxiv.org/abs/2607.20981) `cs.AI` |
| 2026-07-08 | **AnchorPrune: Relevance-Anchored Contextual Expansion for Visual Token Pruning** | Kyuan Oh, Bumsoo Kim | Large vision-language models incur substantial inference costs because high-resolution inputs i... | [📄 2607.07033](https://arxiv.org/abs/2607.07033) `cs.CV` |
| 2026-06-14 | **Stepwise Token Selection for Efficient Multimodal Large Language Models** | Landi He, Shawn Young et al. | In multimodal large language models (MLLMs), inference cost is largely dominated by the visual... | [📄 2606.16067](https://arxiv.org/abs/2606.16067) `cs.CV` |
| 2026-06-05 | **Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors** | Hanxun Yu, Xuan Qu et al. | Despite advances in 3D scene understanding, existing 3D Large Multimodal Models operate in offl... | [📄 2606.06891](https://arxiv.org/abs/2606.06891) `cs.CV` |
| 2026-06-01 | **Improving Visual Token Reduction via Rectifying Distortions for Efficient Multimodal LLM Inference** | Hyeonwoo Cho, Donghyeon Baek et al. | Recent advancements in Multimodal Large Language Models (MLLMs) have achieved remarkable succes... | [📄 2606.01711](https://arxiv.org/abs/2606.01711) `cs.CV` |
| 2026-05-29 | **VisionPulse: Dynamic Visual Sparsity for Efficient Multimodal Reasoning** | Hengbo Xu, Shengjie Jin et al. | With the rapid advancement of large multimodal models (LMMs)... | [📄 2605.31457](https://arxiv.org/abs/2605.31457) `cs.CV` |
<!-- table:end papers -->

## 7. 开放问题

- 视觉 token 的"信息密度"能否被显式度量，从而指导剪枝预算？
- 隐推理的 FLOPs 到底省没省？很多工作报告了 token 数减少，却没报实际墙钟延迟。
- 压缩与推理能力是否存在相变点（压过某个比例后断崖式下降）？

---

[← 多模态推理底座](multimodal-reasoning.md) · [返回总览](../README.md)
