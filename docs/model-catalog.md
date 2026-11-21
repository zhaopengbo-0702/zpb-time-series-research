# 统一模型目录

当前共 **43 个模型家族**，含 6 个独立原版入口和 Time-Series-Library 的全部 41 个模型文件。同名模型合并为同一行，分别链接独立原版与库内实现。

目录根据 [sources.lock.json](../sources.lock.json) 与 [分类元数据](../tools/model_categories.json) 生成。分类用于查找源码；每个模型的任务支持仍由其 `forward()`、依赖和具体实验脚本决定。

按当前源码的主要建模机制为每个模型家族指定一个主分类。交叉方法只出现一次，次要机制写在简介中；同一模型的独立原版与库内实现共用一个家族条目，源码入口分别保留。分类用于查找，不是性能排名，也不表示模型只使用一种技术。

## 按方法类别查找

- [线性与MLP](#category-linear_mlp)（4）
- [循环与卷积](#category-recurrent_convolution)（4）
- [Transformer与注意力](#category-transformer_attention)（13）
- [分解平滑频域](#category-decomposition_frequency)（6）
- [状态空间动力学](#category-state_space_dynamics)（5）
- [图结构](#category-graph)（2）
- [LLM重编程](#category-llm_reprogramming)（1）
- [预训练时序模型](#category-pretrained_foundation)（7）
- [专用异常检测](#category-anomaly_specialized)（1）

<a id="category-linear_mlp"></a>

## 线性与MLP

主要通过线性映射或前馈网络混合时间和变量，适合寻找简单对照与轻量结构。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| DLinear | 先分解趋势与剩余变化，再分别做线性预测，是结构简单的对照模型。 | — | [DLinear.py](../libraries/Time-Series-Library/models/DLinear.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| LightTS | 通过连续与间隔采样提取序列片段，用 MLP 混合局部和跨片段信息。 | — | [LightTS.py](../libraries/Time-Series-Library/models/LightTS.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TiDE | 用残差 MLP 编码历史和协变量，再通过稠密解码与时间投影得到预测。 | — | [TiDE.py](../libraries/Time-Series-Library/models/TiDE.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TSMixer | 交替沿时间轴和变量轴使用 MLP 混合信息，再映射到预测窗口。 | — | [TSMixer.py](../libraries/Time-Series-Library/models/TSMixer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-recurrent_convolution"></a>

## 循环与卷积

以循环状态或局部、多尺度卷积为主要计算结构，也包括先发现周期再做卷积的方法。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| MICN | 用多尺度下采样、等距和上采样卷积提取局部与全局变化，并结合序列分解。 | — | [MICN.py](../libraries/Time-Series-Library/models/MICN.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| SCINet | 递归拆分奇偶时间点，用交互卷积交换信息后重新合并序列。 | — | [SCINet.py](../libraries/Time-Series-Library/models/SCINet.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| SegRNN | 将序列分段后交给 GRU 编码，再按预测片段输出未来值。 | — | [SegRNN.py](../libraries/Time-Series-Library/models/SegRNN.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TimesNet | 用 FFT 寻找周期，将序列按周期重排为二维，再用 Inception 卷积提取变化。 | — | [TimesNet.py](../libraries/Time-Series-Library/models/TimesNet.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-transformer_attention"></a>

## Transformer与注意力

主要围绕 token 表示、注意力连接、稀疏化或输入序列特性改造 Transformer。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| Crossformer | 把每个变量的序列切成片段，用分层和两阶段注意力处理时间与变量关系。 | — | [Crossformer.py](../libraries/Time-Series-Library/models/Crossformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| EMAformer | 在变量 token 上叠加通道、相位和联合嵌入，再用 Transformer 预测。 | [EMAformer](../baselines/EMAformer/) · [核心文件](../baselines/EMAformer/model/EMAformer.py) | — | [原版入口](../baselines/EMAformer/run.py) |
| Informer / Informer2020 | 用 ProbSparse 选择重要 query，并通过编码器蒸馏压缩长序列。 | [Informer2020](../baselines/Informer2020/) · [核心文件](../baselines/Informer2020/models/model.py) | [Informer.py](../libraries/Time-Series-Library/models/Informer.py) | [原版入口](../baselines/Informer2020/main_informer.py) · [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| iTransformer | 把每个变量的历史作为一个 token，让注意力直接学习变量之间的关系。 | — | [iTransformer.py](../libraries/Time-Series-Library/models/iTransformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| MultiPatchFormer | 用多种 patch 尺度表示序列，再结合注意力组织不同尺度与通道信息。 | — | [MultiPatchFormer.py](../libraries/Time-Series-Library/models/MultiPatchFormer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Nonstationary_Transformer / Non-stationary Transformer | 在归一化输入之外学习去平稳注意力因子，补回序列的非平稳信息。 | — | [Nonstationary_Transformer.py](../libraries/Time-Series-Library/models/Nonstationary_Transformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| PatchTST | 把连续时间点切为 patch，并以通道独立的 Transformer 建模长历史。 | — | [PatchTST.py](../libraries/Time-Series-Library/models/PatchTST.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| PAttn | 用 patch 嵌入和单层注意力进行预测，提供无需调用语言模型的对照入口。 | — | [PAttn.py](../libraries/Time-Series-Library/models/PAttn.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Pyraformer | 构建多尺度金字塔，在层内与层间设置稀疏连接以传递长期信息。 | [Pyraformer](../baselines/Pyraformer/) · [核心文件](../baselines/Pyraformer/pyraformer/Pyraformer_LR.py) | [Pyraformer.py](../libraries/Time-Series-Library/models/Pyraformer.py) | [原版入口](../baselines/Pyraformer/long_range_main.py) · [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Reformer | 使用 Reformer 的局部敏感哈希注意力处理长序列。 | — | [Reformer.py](../libraries/Time-Series-Library/models/Reformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TemporalFusionTransformer / TFT | 通过变量选择、门控循环层和注意力融合历史与时间协变量。 | — | [TemporalFusionTransformer.py](../libraries/Time-Series-Library/models/TemporalFusionTransformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TimeXer | 结合目标序列的 patch 与外生变量表示，用注意力融合两类信息。 | — | [TimeXer.py](../libraries/Time-Series-Library/models/TimeXer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Transformer | 使用标准编码器和解码器注意力结构，作为其他改造模型的对照。 | — | [Transformer.py](../libraries/Time-Series-Library/models/Transformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-decomposition_frequency"></a>

## 分解平滑频域

突出趋势季节分解、指数平滑、频谱或小波处理，可能同时包含注意力或 MLP。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| Autoformer | 逐层拆分趋势与季节变化，再用自相关选择时延并聚合序列。 | [Autoformer](../baselines/Autoformer/) · [核心文件](../baselines/Autoformer/models/Autoformer.py) | [Autoformer.py](../libraries/Time-Series-Library/models/Autoformer.py) | [原版入口](../baselines/Autoformer/run.py) · [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| ETSformer | 将水平、增长和季节项分开建模，结合可学习指数平滑、傅里叶外推与增长阻尼。 | [ETSformer](../baselines/ETSformer/) · [核心文件](../baselines/ETSformer/models/etsformer/model.py) | [ETSformer.py](../libraries/Time-Series-Library/models/ETSformer.py) | [原版入口](../baselines/ETSformer/run.py) · [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| FEDformer | 在趋势季节分解的基础上，用傅里叶或小波模块处理长期依赖。 | — | [FEDformer.py](../libraries/Time-Series-Library/models/FEDformer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| FreTS | 把序列变到频域，用复数 MLP 混合时间和通道信息，再还原预测。 | — | [FreTS.py](../libraries/Time-Series-Library/models/FreTS.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TimeMixer | 将序列分为多个尺度和趋势季节成分，通过 MLP 混合并汇总多尺度预测。 | — | [TimeMixer.py](../libraries/Time-Series-Library/models/TimeMixer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| WPMixer | 先用离散小波拆分序列，再对不同分量做 patch 混合与预测重建。 | — | [WPMixer.py](../libraries/Time-Series-Library/models/WPMixer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-state_space_dynamics"></a>

## 状态空间动力学

以状态递推、动力学算子或连续历史的状态压缩为主要机制。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| FiLM | 用 Legendre/HiPPO 状态投影压缩历史，再以频域处理提取预测信息。 | — | [FiLM.py](../libraries/Time-Series-Library/models/FiLM.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Koopa | 分离不同变化成分，用可学习和动态估计的 Koopman 算子推进隐状态。 | — | [Koopa.py](../libraries/Time-Series-Library/models/Koopa.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Mamba | 用 Mamba 的选择性状态空间模块递推处理序列，减少对全量注意力的依赖。 | — | [Mamba.py](../libraries/Time-Series-Library/models/Mamba.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| MambaSimple | 在库内保留较简化的 Mamba 与扫描计算实现，便于阅读状态递推机制。 | — | [MambaSimple.py](../libraries/Time-Series-Library/models/MambaSimple.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| MambaSingleLayer / MambaSL | 用单层 Mamba 做序列分类，当前构造和前向路径限定分类任务。 | — | [MambaSingleLayer.py](../libraries/Time-Series-Library/models/MambaSingleLayer.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-graph"></a>

## 图结构

重点学习时间片段、通道或多尺度之间的图关系，并通过图传播组织信息。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| MSGNet | 先发现不同周期尺度，再通过图卷积和注意力学习多变量之间的关系。 | — | [MSGNet.py](../libraries/Time-Series-Library/models/MSGNet.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TimeFilter | 将时序 patch 组织成图，用邻接构造和路由过滤关系后预测。 | — | [TimeFilter.py](../libraries/Time-Series-Library/models/TimeFilter.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-llm_reprogramming"></a>

## LLM重编程

把时序输入适配到预训练语言模型，以提示和可训练接口进行预测。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| Time-LLM / TimeLLM | 把时序 patch 对齐到文本原型，并用提示词与冻结语言模型生成预测表示。 | [Time-LLM](../baselines/Time-LLM/) · [核心文件](../baselines/Time-LLM/models/TimeLLM.py) | — | [原版入口](../baselines/Time-LLM/run_main.py) |

<a id="category-pretrained_foundation"></a>

## 预训练时序模型

库内提供外部预训练时序模型的调用接口，通常用于零样本预测；权重与各自依赖另行获取。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| Chronos | 调用预训练 Chronos，把数值序列交给其预测管线，库内入口用于零样本预测。 | — | [Chronos.py](../libraries/Time-Series-Library/models/Chronos.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Chronos2 / Chronos-2 | 调用 Chronos-2 预训练预测管线，与第一代 Chronos 分开保留接口。 | — | [Chronos2.py](../libraries/Time-Series-Library/models/Chronos2.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Moirai | 调用 uni2ts 的预训练 Moirai 模型，库内接口用于零样本预测。 | — | [Moirai.py](../libraries/Time-Series-Library/models/Moirai.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| Sundial | 调用外部预训练 Sundial 时序模型，保留其零样本预测适配接口。 | — | [Sundial.py](../libraries/Time-Series-Library/models/Sundial.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TimeMoE / Time-MoE | 调用预训练 TimeMoE 混合专家时序模型，库内入口用于零样本预测。 | — | [TimeMoE.py](../libraries/Time-Series-Library/models/TimeMoE.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TimesFM | 调用预训练 TimesFM 预测接口，外部权重与运行依赖单独加载。 | — | [TimesFM.py](../libraries/Time-Series-Library/models/TimesFM.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |
| TiRex | 调用 tirex-ts 的预训练模型，为库内零样本预测提供接口。 | — | [TiRex.py](../libraries/Time-Series-Library/models/TiRex.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

<a id="category-anomaly_specialized"></a>

## 专用异常检测

当前源码重点实现异常检测，不按通用预测模型归类。

| 模型 | 特点与源码定位 | 独立原版 | 库内实现 | 任务与脚本入口 |
| --- | --- | --- | --- | --- |
| KANAD | 结合周期余弦特征和卷积重建序列，当前库内模型只实现异常检测。 | — | [KANAD.py](../libraries/Time-Series-Library/models/KANAD.py) | [库内任务脚本](../libraries/Time-Series-Library/scripts/) |

## 按任务查实验入口

库的统一入口为 [run.py](../libraries/Time-Series-Library/run.py)。实际脚本目录如下；目录存在不代表全部模型支持该任务。

- [长期预测](../libraries/Time-Series-Library/scripts/long_term_forecast/)
- [短期预测](../libraries/Time-Series-Library/scripts/short_term_forecast/)
- [缺失补全](../libraries/Time-Series-Library/scripts/imputation/)
- [异常检测](../libraries/Time-Series-Library/scripts/anomaly_detection/)
- [分类](../libraries/Time-Series-Library/scripts/classification/)
- [外生变量预测](../libraries/Time-Series-Library/scripts/exogenous_forecast/)

零样本预测示例：[LTSM.sh](../libraries/Time-Series-Library/scripts/long_term_forecast/ETT_script/LTSM.sh)。这是脚本名；具体模型与参数以脚本当前内容为准，预训练权重由模型接口另外加载。

## 独立原版与库内实现怎么选

读论文原实现、对照原作者实验时，从“独立原版”进入；使用库内统一实验接口时，从“库内实现”进入。两个入口都保留原始文件，目录没有移动或拆成新的伪原版仓库。

完整来源提交、文件数和最近同步状态见 [上游状态](upstream-status.md)；阅读关键文件的顺序见 [源码导航](model-guide.md)。
