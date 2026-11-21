# zpb-time-series-research

个人时间序列研究工作区，将已收录的模型逐个展开，按技术路线统一分类。EMAformer、Pyraformer、Informer、Autoformer、ETSformer、Time-LLM 与 TSLib 的全部模型在同一目录中查找；同名模型同时提供独立原版和库内实现入口。

[![Upstream sync](https://github.com/zhaopengbo-0702/zpb-time-series-research/actions/workflows/sync-upstreams.yml/badge.svg)](https://github.com/zhaopengbo-0702/zpb-time-series-research/actions/workflows/sync-upstreams.yml)

每天北京时间约 **10:20** 自动检查七个上游，有更新时同步原始源码、来源锁定和同步历史。也可以在 [Actions](https://github.com/zhaopengbo-0702/zpb-time-series-research/actions/workflows/sync-upstreams.yml) 点击 **Run workflow** 立即执行。查看[当前版本](docs/upstream-status.md)与[同步说明](docs/upstream-sync.md)。

## 从这里开始

| 想做什么 | 去哪里 |
| --- | --- |
| 按名称查模型，区分原版与库内实现 | [全部模型与任务索引](docs/model-catalog.md) |
| 查模型、注意力、嵌入、数据加载代码 | [源码导航](docs/model-guide.md) |
| 查环境、数据位置和训练命令 | [运行指南](docs/running-baselines.md) |
| 查上游版本、导入范围和来源校验 | [来源记录](docs/upstream-sources.md) · [版本锁定清单](sources.lock.json) |
| 同步上游、查看执行结果 | [自动同步说明](docs/upstream-sync.md) · [同步历史](docs/upstream-sync-history.md) |
| 写自己的模型和改进思路 | [研究工作区](research/README.md) |
| 记录配置、消融实验与结果 | [实验管理](experiments/README.md) |
| 整理数据来源、划分和预处理 | [数据索引](data/README.md) |

## 全部模型，按技术路线分类

**从[统一模型目录](docs/model-catalog.md)开始**。六个独立项目与 TSLib 内全部模型合并整理，同名模型以一个条目提供两个实现入口。当前总数和各分类数量随上游同步自动生成。

<!-- MODEL_CATALOG_START -->

当前 **43 个模型家族**，按主要建模机制分类。每个模型名称都直接链接到源码。

| 分类 | 全部模型 |
| --- | --- |
| [线性与MLP](docs/model-catalog.md#category-linear_mlp) | [DLinear](libraries/Time-Series-Library/models/DLinear.py) · [LightTS](libraries/Time-Series-Library/models/LightTS.py) · [TiDE](libraries/Time-Series-Library/models/TiDE.py) · [TSMixer](libraries/Time-Series-Library/models/TSMixer.py) |
| [循环与卷积](docs/model-catalog.md#category-recurrent_convolution) | [MICN](libraries/Time-Series-Library/models/MICN.py) · [SCINet](libraries/Time-Series-Library/models/SCINet.py) · [SegRNN](libraries/Time-Series-Library/models/SegRNN.py) · [TimesNet](libraries/Time-Series-Library/models/TimesNet.py) |
| [Transformer与注意力](docs/model-catalog.md#category-transformer_attention) | [Crossformer](libraries/Time-Series-Library/models/Crossformer.py) · [EMAformer](baselines/EMAformer/model/EMAformer.py) · [Informer](baselines/Informer2020/models/model.py) · [iTransformer](libraries/Time-Series-Library/models/iTransformer.py) · [MultiPatchFormer](libraries/Time-Series-Library/models/MultiPatchFormer.py) · [Nonstationary_Transformer](libraries/Time-Series-Library/models/Nonstationary_Transformer.py) · [PatchTST](libraries/Time-Series-Library/models/PatchTST.py) · [PAttn](libraries/Time-Series-Library/models/PAttn.py) · [Pyraformer](baselines/Pyraformer/pyraformer/Pyraformer_LR.py) · [Reformer](libraries/Time-Series-Library/models/Reformer.py) · [TemporalFusionTransformer](libraries/Time-Series-Library/models/TemporalFusionTransformer.py) · [TimeXer](libraries/Time-Series-Library/models/TimeXer.py) · [Transformer](libraries/Time-Series-Library/models/Transformer.py) |
| [分解平滑频域](docs/model-catalog.md#category-decomposition_frequency) | [Autoformer](baselines/Autoformer/models/Autoformer.py) · [ETSformer](baselines/ETSformer/models/etsformer/model.py) · [FEDformer](libraries/Time-Series-Library/models/FEDformer.py) · [FreTS](libraries/Time-Series-Library/models/FreTS.py) · [TimeMixer](libraries/Time-Series-Library/models/TimeMixer.py) · [WPMixer](libraries/Time-Series-Library/models/WPMixer.py) |
| [状态空间动力学](docs/model-catalog.md#category-state_space_dynamics) | [FiLM](libraries/Time-Series-Library/models/FiLM.py) · [Koopa](libraries/Time-Series-Library/models/Koopa.py) · [Mamba](libraries/Time-Series-Library/models/Mamba.py) · [MambaSimple](libraries/Time-Series-Library/models/MambaSimple.py) · [MambaSingleLayer](libraries/Time-Series-Library/models/MambaSingleLayer.py) |
| [图结构](docs/model-catalog.md#category-graph) | [MSGNet](libraries/Time-Series-Library/models/MSGNet.py) · [TimeFilter](libraries/Time-Series-Library/models/TimeFilter.py) |
| [LLM重编程](docs/model-catalog.md#category-llm_reprogramming) | [Time-LLM](baselines/Time-LLM/models/TimeLLM.py) |
| [预训练时序模型](docs/model-catalog.md#category-pretrained_foundation) | [Chronos](libraries/Time-Series-Library/models/Chronos.py) · [Chronos2](libraries/Time-Series-Library/models/Chronos2.py) · [Moirai](libraries/Time-Series-Library/models/Moirai.py) · [Sundial](libraries/Time-Series-Library/models/Sundial.py) · [TimeMoE](libraries/Time-Series-Library/models/TimeMoE.py) · [TimesFM](libraries/Time-Series-Library/models/TimesFM.py) · [TiRex](libraries/Time-Series-Library/models/TiRex.py) |
| [专用异常检测](docs/model-catalog.md#category-anomaly_specialized) | [KANAD](libraries/Time-Series-Library/models/KANAD.py) |

<!-- MODEL_CATALOG_END -->

各分类的完整模型、特点与源码入口均在[统一模型目录](docs/model-catalog.md)逐项展开。自动同步发现的新模型也会加入目录，尚未审定的类别放入“待分类”。这里的“全部”指已收录上游中的全部模型文件。

## 全部模型明细

<!-- MODEL_DETAILS_START -->

共 **43 个模型**，按名称排序，每个模型一行。分类见上表；各行使用相同字段，有多个实现时同时列出。悬停在链接上可查看完整文件路径。

| 模型 | 主要思路 | 源码 | 核心模型 | 运行入口 | 论文&nbsp;/&nbsp;项目 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Autoformer | 逐层拆分趋势与季节变化，再用自相关选择时延并聚合序列。 | [原项目](baselines/Autoformer/ "baselines/Autoformer/")<br>[TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [原版模型](baselines/Autoformer/models/Autoformer.py "baselines/Autoformer/models/Autoformer.py")<br>[库内模型](libraries/Time-Series-Library/models/Autoformer.py "libraries/Time-Series-Library/models/Autoformer.py") | [原版入口](baselines/Autoformer/run.py "baselines/Autoformer/run.py")<br>[库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2106.13008 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Autoformer "https://github.com/thuml/Autoformer") |
| Chronos | 调用预训练 Chronos，把数值序列交给其预测管线，库内入口用于零样本预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Chronos.py "libraries/Time-Series-Library/models/Chronos.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2403.07815 "链接为上游 README 列出的 Chronos 系列论文；当前接口实际加载 chronos-bolt-base，不将该链接标成该权重的专属论文。")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Chronos2 | 调用 Chronos-2 预训练预测管线，与第一代 Chronos 分开保留接口。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Chronos2.py "libraries/Time-Series-Library/models/Chronos2.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2510.15821 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Crossformer | 把每个变量的序列切成片段，用分层和两阶段注意力处理时间与变量关系。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Crossformer.py "libraries/Time-Series-Library/models/Crossformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=vSVLM2j9eie "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| DLinear | 先分解趋势与剩余变化，再分别做线性预测，是结构简单的对照模型。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/DLinear.py "libraries/Time-Series-Library/models/DLinear.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2205.13504.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| EMAformer | 在变量 token 上叠加通道、相位和联合嵌入，再用 Transformer 预测。 | [原项目](baselines/EMAformer/ "baselines/EMAformer/") | [原版模型](baselines/EMAformer/model/EMAformer.py "baselines/EMAformer/model/EMAformer.py") | [原版入口](baselines/EMAformer/run.py "baselines/EMAformer/run.py") | [论文](https://arxiv.org/abs/2511.08396 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/PlanckChang/EMAformer "https://github.com/PlanckChang/EMAformer") |
| ETSformer | 将水平、增长和季节项分开建模，结合可学习指数平滑、傅里叶外推与增长阻尼。 | [原项目](baselines/ETSformer/ "baselines/ETSformer/")<br>[TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [原版模型](baselines/ETSformer/models/etsformer/model.py "baselines/ETSformer/models/etsformer/model.py")<br>[库内模型](libraries/Time-Series-Library/models/ETSformer.py "libraries/Time-Series-Library/models/ETSformer.py") | [原版入口](baselines/ETSformer/run.py "baselines/ETSformer/run.py")<br>[库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2202.01381 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/azkanaon/etsformer "https://github.com/azkanaon/etsformer") |
| FEDformer | 在趋势季节分解的基础上，用傅里叶或小波模块处理长期依赖。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/FEDformer.py "libraries/Time-Series-Library/models/FEDformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://proceedings.mlr.press/v162/zhou22g.html "模型论文")&nbsp;·&nbsp;[项目](https://github.com/MAZiqing/FEDformer "https://github.com/MAZiqing/FEDformer") |
| FiLM | 用 Legendre/HiPPO 状态投影压缩历史，再以频域处理提取预测信息。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/FiLM.py "libraries/Time-Series-Library/models/FiLM.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/forum?id=zTQdHSQUQWc "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| FreTS | 把序列变到频域，用复数 MLP 混合时间和通道信息，再还原预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/FreTS.py "libraries/Time-Series-Library/models/FreTS.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2311.06184.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Informer | 用 ProbSparse 选择重要 query，并通过编码器蒸馏压缩长序列。 | [原项目](baselines/Informer2020/ "baselines/Informer2020/")<br>[TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [原版模型](baselines/Informer2020/models/model.py "baselines/Informer2020/models/model.py")<br>[库内模型](libraries/Time-Series-Library/models/Informer.py "libraries/Time-Series-Library/models/Informer.py") | [原版入口](baselines/Informer2020/main_informer.py "baselines/Informer2020/main_informer.py")<br>[库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2012.07436 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/zhouhaoyi/Informer2020 "https://github.com/zhouhaoyi/Informer2020") |
| iTransformer | 把每个变量的历史作为一个 token，让注意力直接学习变量之间的关系。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/iTransformer.py "libraries/Time-Series-Library/models/iTransformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2310.06625 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| KANAD | 结合周期余弦特征和卷积重建序列，当前库内模型只实现异常检测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/KANAD.py "libraries/Time-Series-Library/models/KANAD.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2411.00278 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Koopa | 分离不同变化成分，用可学习和动态估计的 Koopman 算子推进隐状态。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Koopa.py "libraries/Time-Series-Library/models/Koopa.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2305.18803.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| LightTS | 通过连续与间隔采样提取序列片段，用 MLP 混合局部和跨片段信息。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/LightTS.py "libraries/Time-Series-Library/models/LightTS.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2207.01186 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Mamba | 用 Mamba 的选择性状态空间模块递推处理序列，减少对全量注意力的依赖。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Mamba.py "libraries/Time-Series-Library/models/Mamba.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2312.00752 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| MambaSimple | 在库内保留较简化的 Mamba 与扫描计算实现，便于阅读状态递推机制。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/MambaSimple.py "libraries/Time-Series-Library/models/MambaSimple.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2312.00752 "共用 Mamba 方法论文；当前文件是简化实现，参考 mamba-minimal，不宣称另有独立论文。")&nbsp;·&nbsp;[项目](https://github.com/johnma2006/mamba-minimal/ "https://github.com/johnma2006/mamba-minimal/") |
| MambaSingleLayer | 用单层 Mamba 做序列分类，当前构造和前向路径限定分类任务。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/MambaSingleLayer.py "libraries/Time-Series-Library/models/MambaSingleLayer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/forum?id=YDl4vqQqGP "当前模块对应 MambaSL 分类论文；文件名 MambaSingleLayer 与论文模型名 MambaSL 分别保留。")&nbsp;·&nbsp;[项目](https://github.com/yoom618/MambaSL "https://github.com/yoom618/MambaSL") |
| MICN | 用多尺度下采样、等距和上采样卷积提取局部与全局变化，并结合序列分解。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/MICN.py "libraries/Time-Series-Library/models/MICN.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=zt53IDUR1U "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Moirai | 调用 uni2ts 的预训练 Moirai 模型，库内接口用于零样本预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Moirai.py "libraries/Time-Series-Library/models/Moirai.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2402.02592 "链接为上游 README 列出的 Moirai 系列论文；当前接口实际加载 moirai-2.0-R-small，具体版本以源码和权重标识为准。")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| MSGNet | 先发现不同周期尺度，再通过图卷积和注意力学习多变量之间的关系。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/MSGNet.py "libraries/Time-Series-Library/models/MSGNet.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://dl.acm.org/doi/10.1609/aaai.v38i10.28991 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| MultiPatchFormer | 用多种 patch 尺度表示序列，再结合注意力组织不同尺度与通道信息。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/MultiPatchFormer.py "libraries/Time-Series-Library/models/MultiPatchFormer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://www.nature.com/articles/s41598-024-82417-4 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Nonstationary<br>Transformer | 在归一化输入之外学习去平稳注意力因子，补回序列的非平稳信息。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Nonstationary_Transformer.py "libraries/Time-Series-Library/models/Nonstationary_Transformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=ucNDIDRNjjv "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Nonstationary_Transformers "https://github.com/thuml/Nonstationary_Transformers") |
| PatchTST | 把连续时间点切为 patch，并以通道独立的 Transformer 建模长历史。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/PatchTST.py "libraries/Time-Series-Library/models/PatchTST.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=Jbdc0vTOcol "模型论文")&nbsp;·&nbsp;[项目](https://github.com/yuqinie98/PatchTST "https://github.com/yuqinie98/PatchTST") |
| PAttn | 用 patch 嵌入和单层注意力进行预测，提供无需调用语言模型的对照入口。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/PAttn.py "libraries/Time-Series-Library/models/PAttn.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2406.16964 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Pyraformer | 构建多尺度金字塔，在层内与层间设置稀疏连接以传递长期信息。 | [原项目](baselines/Pyraformer/ "baselines/Pyraformer/")<br>[TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [原版模型](baselines/Pyraformer/pyraformer/Pyraformer_LR.py "baselines/Pyraformer/pyraformer/Pyraformer_LR.py")<br>[单步模型](baselines/Pyraformer/pyraformer/Pyraformer_SS.py "baselines/Pyraformer/pyraformer/Pyraformer_SS.py")<br>[库内模型](libraries/Time-Series-Library/models/Pyraformer.py "libraries/Time-Series-Library/models/Pyraformer.py") | [原版入口](baselines/Pyraformer/long_range_main.py "baselines/Pyraformer/long_range_main.py")<br>[单步入口](baselines/Pyraformer/single_step_main.py "baselines/Pyraformer/single_step_main.py")<br>[库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/forum?id=0EXmFzUn5I "模型论文")&nbsp;·&nbsp;[项目](https://github.com/ant-research/Pyraformer "https://github.com/ant-research/Pyraformer") |
| Reformer | 使用 Reformer 的局部敏感哈希注意力处理长序列。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Reformer.py "libraries/Time-Series-Library/models/Reformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/forum?id=rkgNKkHtvB "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| SCINet | 递归拆分奇偶时间点，用交互卷积交换信息后重新合并序列。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/SCINet.py "libraries/Time-Series-Library/models/SCINet.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=AyajSjTAzmg "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| SegRNN | 将序列分段后交给 GRU 编码，再按预测片段输出未来值。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/SegRNN.py "libraries/Time-Series-Library/models/SegRNN.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2308.11200.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Sundial | 调用外部预训练 Sundial 时序模型，保留其零样本预测适配接口。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Sundial.py "libraries/Time-Series-Library/models/Sundial.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2502.00816 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Temporal Fusion<br>Transformer | 通过变量选择、门控循环层和注意力融合历史与时间协变量。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TemporalFusionTransformer.py "libraries/Time-Series-Library/models/TemporalFusionTransformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/1912.09363 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TiDE | 用残差 MLP 编码历史和协变量，再通过稠密解码与时间投影得到预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TiDE.py "libraries/Time-Series-Library/models/TiDE.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2304.08424.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Time-LLM | 把时序 patch 对齐到文本原型，并用提示词与冻结语言模型生成预测表示。 | [原项目](baselines/Time-LLM/ "baselines/Time-LLM/") | [原版模型](baselines/Time-LLM/models/TimeLLM.py "baselines/Time-LLM/models/TimeLLM.py") | [原版入口](baselines/Time-LLM/run_main.py "baselines/Time-LLM/run_main.py") | [论文](https://arxiv.org/abs/2310.01728 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/KimMeen/Time-LLM "https://github.com/KimMeen/Time-LLM") |
| TimeFilter | 将时序 patch 组织成图，用邻接构造和路由过滤关系后预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TimeFilter.py "libraries/Time-Series-Library/models/TimeFilter.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2501.13041 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TimeMixer | 将序列分为多个尺度和趋势季节成分，通过 MLP 混合并汇总多尺度预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TimeMixer.py "libraries/Time-Series-Library/models/TimeMixer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=7oLshfEIC2 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TimeMoE | 调用预训练 TimeMoE 混合专家时序模型，库内入口用于零样本预测。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TimeMoE.py "libraries/Time-Series-Library/models/TimeMoE.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2409.16040 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TimesFM | 调用预训练 TimesFM 预测接口，外部权重与运行依赖单独加载。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TimesFM.py "libraries/Time-Series-Library/models/TimesFM.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2310.10688 "链接为上游 README 列出的 TimesFM 系列论文；当前接口实际调用 TimesFM 2.5，具体版本以源码和权重标识为准。")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TimesNet | 用 FFT 寻找周期，将序列按周期重排为二维，再用 Inception 卷积提取变化。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TimesNet.py "libraries/Time-Series-Library/models/TimesNet.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://openreview.net/pdf?id=ju_Uqw384Oq "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TimeXer | 结合目标序列的 patch 与外生变量表示，用注意力融合两类信息。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TimeXer.py "libraries/Time-Series-Library/models/TimeXer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2402.19072 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TiRex | 调用 tirex-ts 的预训练模型，为库内零样本预测提供接口。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TiRex.py "libraries/Time-Series-Library/models/TiRex.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2505.23719 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| Transformer | 使用标准编码器和解码器注意力结构，作为其他改造模型的对照。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/Transformer.py "libraries/Time-Series-Library/models/Transformer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| TSMixer | 交替沿时间轴和变量轴使用 MLP 混合信息，再映射到预测窗口。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/TSMixer.py "libraries/Time-Series-Library/models/TSMixer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/pdf/2303.06053.pdf "模型论文")&nbsp;·&nbsp;[项目](https://github.com/thuml/Time-Series-Library "https://github.com/thuml/Time-Series-Library") |
| WPMixer | 先用离散小波拆分序列，再对不同分量做 patch 混合与预测重建。 | [TSLib](libraries/Time-Series-Library/ "libraries/Time-Series-Library/") | [库内模型](libraries/Time-Series-Library/models/WPMixer.py "libraries/Time-Series-Library/models/WPMixer.py") | [库内入口](libraries/Time-Series-Library/run.py "按任务选择参数；查看库内 scripts 目录") | [论文](https://arxiv.org/abs/2412.17176 "模型论文")&nbsp;·&nbsp;[项目](https://github.com/Secure-and-Intelligent-Systems-Lab/WPMixer "https://github.com/Secure-and-Intelligent-Systems-Lab/WPMixer") |

原项目与库内入口对应不同实现；运行参数和支持任务见各自源码。系列论文与当前预训练权重的差异已放入论文链接的悬停说明。

<!-- MODEL_DETAILS_END -->

## 完整库源码与任务流程

[Time-Series-Library](libraries/Time-Series-Library/) 放在 `libraries/`，保留锁定提交的**全部原始文件**，包括模型模块、实验类、数据加载、组件、任务脚本、教程、中英文 README 和 Docker 部署文件。当前文件数量见[版本状态](docs/upstream-status.md)，模型名称见[模型目录](docs/model-catalog.md)。

| 想查什么 | 入口 |
| --- | --- |
| 全部模型名称与原版对应关系 | [模型目录](docs/model-catalog.md) · [models/](libraries/Time-Series-Library/models/) |
| 统一命令入口与任务选择 | [run.py](libraries/Time-Series-Library/run.py) · [exp/](libraries/Time-Series-Library/exp/) |
| 长短期预测、插补、异常检测、分类、外生变量预测脚本 | [scripts/](libraries/Time-Series-Library/scripts/) |
| 大型时间序列模型零样本预测 | [exp_zero_shot_forecasting.py](libraries/Time-Series-Library/exp/exp_zero_shot_forecasting.py) |
| 数据读取与注册 | [data_provider/](libraries/Time-Series-Library/data_provider/) |
| 中文说明与入门教程 | [README_zh.md](libraries/Time-Series-Library/README_zh.md) · [tutorial/](libraries/Time-Series-Library/tutorial/) |
| 上游论文与项目 | [综述](https://arxiv.org/abs/2407.13278) · [上游](https://github.com/thuml/Time-Series-Library) |

TSLib 内的 Autoformer、Informer、Pyraformer、ETSformer 是该库集成后的实现，独立原版保留在 `baselines/`。它们在统一目录中并列提供两个入口。各实现使用不同环境与任务配置，比较前按[运行指南](docs/running-baselines.md)对齐实验设置。

## 目录结构

```text
zpb-time-series-research/
├── baselines/                 # 六个独立项目，保留原文件名与目录
│   ├── EMAformer/
│   ├── Pyraformer/
│   ├── Informer2020/
│   ├── Autoformer/
│   ├── ETSformer/
│   └── Time-LLM/
├── libraries/
│   └── Time-Series-Library/   # 完整时序库：模型、任务、脚本、教程与部署
├── docs/                      # 源码导航、运行指南、来源记录
├── research/
│   ├── models/                # 自己的模型和改动说明
│   └── notes/                 # 论文笔记、想法和代码阅读记录
├── experiments/
│   ├── templates/             # 可复制的实验记录模板
│   └── results/               # 小型指标汇总；大文件留在本地
├── data/                      # 数据来源与划分索引
├── tools/verify_sources.py    # 原始源码完整性校验
├── sources.lock.json          # 上游提交、文件哈希与模式
├── LICENSES.md                # 各上游的许可证与署名
└── CHANGELOG.md               # 本研究工作区的变更记录
```

## 获取与使用

```bash
git clone https://github.com/zhaopengbo-0702/zpb-time-series-research.git
cd zpb-time-series-research
python tools/verify_sources.py
```

阅读代码无需安装训练依赖。开始运行时，进入对应的 `baselines/<模型名>/` 目录，按[运行指南](docs/running-baselines.md)分别准备环境与数据；本仓库根目录不提供合并的 `requirements.txt`。

已建立 **7 个来源**的归档与逐文件来源校验，当前文件数和提交见[版本状态](docs/upstream-status.md)。完整范围是锁定提交中受 Git 跟踪的全部文件；训练数据和外部模型权重按各项目要求另行准备。模型训练和论文指标复现尚未执行。Pyraformer 的可选 TVM gitlink 状态见[来源记录](docs/upstream-sources.md)。

后续改进可先在 `research/` 下建立独立版本，通过实验记录保存基线提交、配置和结果。各上游论文的引用条目保留在对应原 README 中；许可证说明见 [LICENSES.md](LICENSES.md)。
