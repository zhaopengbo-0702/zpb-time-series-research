# 六个独立模型与完整时间序列库的源码导航

本页记录最初六个项目与 TSLib 的源码阅读路线，全部新增模型与多来源实现见[统一模型目录](model-catalog.md)，六套模型库的使用入口见[模型库指南](library-guide.md)。锁定提交与文件范围见[来源记录](upstream-sources.md)。

本页按“看论文 → 找模型 → 看训练 → 改数据 → 做实验”的顺序定位源码。六个独立模型项目位于 `baselines/`；完整 Time-Series-Library 位于 `libraries/`，作为包含多种模型与多种任务的工具库单独收录。所有路径指向本仓库收录的上游版本；这里完成的是源码整理与路径核查，尚未执行训练或复现实验。

## 先选阅读入口

| 项目 | 主要关注点 | 先读的模型文件或目录 | 训练/实验入口 |
| --- | --- | --- | --- |
| [EMAformer](#emaformer) | 变量 token、通道/相位/联合嵌入 | [model/EMAformer.py](../baselines/EMAformer/model/EMAformer.py) | [run.py](../baselines/EMAformer/run.py) |
| [Pyraformer](#pyraformer) | 多尺度金字塔结构与稀疏连接 | [pyraformer/Pyraformer_LR.py](../baselines/Pyraformer/pyraformer/Pyraformer_LR.py) | [long_range_main.py](../baselines/Pyraformer/long_range_main.py) |
| [Informer2020](#informer2020) | ProbSparse 注意力、编码器蒸馏 | [models/model.py](../baselines/Informer2020/models/model.py) | [main_informer.py](../baselines/Informer2020/main_informer.py) |
| [Autoformer](#autoformer) | 趋势/季节项分解、自相关与时延聚合 | [models/Autoformer.py](../baselines/Autoformer/models/Autoformer.py) | [run.py](../baselines/Autoformer/run.py) |
| [ETSformer](#etsformer) | 指数平滑、傅里叶季节项与增长阻尼 | [models/etsformer/model.py](../baselines/ETSformer/models/etsformer/model.py) | [run.py](../baselines/ETSformer/run.py) |
| [Time-LLM](#time-llm) | 冻结语言模型、时序 patch 重编程、提示词 | [models/TimeLLM.py](../baselines/Time-LLM/models/TimeLLM.py) | [run_main.py](../baselines/Time-LLM/run_main.py) |
| [Time-Series-Library](#time-series-library)（完整库） | 多模型、多任务和零样本预测实验 | [models](../libraries/Time-Series-Library/models)、[exp](../libraries/Time-Series-Library/exp) | [run.py](../libraries/Time-Series-Library/run.py) |

独立模型各节的路径均相对于对应的 `baselines/<模型名>/`；库内路径相对于 `libraries/Time-Series-Library/`。运行原脚本时，先进入对应项目目录，避免相对数据路径和模块导入错位。各项目保留独立的数据处理、依赖和实验流程。

## EMAformer

- 上游：[PlanckChang/EMAformer](https://github.com/PlanckChang/EMAformer)
- 论文：[EMAformer: Enhancing Transformer through Embedding Armor for Time Series Forecasting](https://arxiv.org/abs/2511.08396)
- 上游说明：[README](../baselines/EMAformer/README.md)

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 核心模型 | [model/EMAformer.py](../baselines/EMAformer/model/EMAformer.py) | `Model`、`forecast()`；通道嵌入、相位嵌入、通道与相位联合嵌入的生成及相加方式；`projector` 预测头 |
| 输入嵌入 | [layers/Embed.py](../baselines/EMAformer/layers/Embed.py) | `DataEmbedding_inverted`，从时间序列到变量 token 的转换 |
| 注意力 | [layers/SelfAttention_Family.py](../baselines/EMAformer/layers/SelfAttention_Family.py) | `FullAttention`、`AttentionLayer` 及其他注意力实现 |
| 编码器 | [layers/Transformer_EncDec.py](../baselines/EMAformer/layers/Transformer_EncDec.py) | `Encoder`、`EncoderLayer` |
| 参数与训练开关 | [run.py](../baselines/EMAformer/run.py) | `seq_len`、`pred_len`、`cycle`、`enc_in`、`is_training` 等参数 |
| 模型注册与设备 | [experiments/exp_basic.py](../baselines/EMAformer/experiments/exp_basic.py) | `model_dict`，新增模型的注册位置 |
| 训练、验证与测试 | [experiments/exp_long_term_forecasting.py](../baselines/EMAformer/experiments/exp_long_term_forecasting.py) | 数据调用、损失、优化器、训练循环与评估 |
| 数据集定义 | [data_provider/data_loader.py](../baselines/EMAformer/data_provider/data_loader.py) | 读入、切分、标准化、时间特征和周期索引 |
| 数据集注册 | [data_provider/data_factory.py](../baselines/EMAformer/data_provider/data_factory.py) | 数据集名称与 loader 的对应关系 |
| 评价指标 | [utils/metrics.py](../baselines/EMAformer/utils/metrics.py) | MAE、MSE 等指标的实现 |
| 常规实验脚本 | [scripts/multivariate_forecasting](../baselines/EMAformer/scripts/multivariate_forecasting) | 按数据集查找参数；如 [ETTh1 脚本](../baselines/EMAformer/scripts/multivariate_forecasting/ETT/EMAformer_ETTh1.sh) |
| 长输入窗口实验 | [scripts/increasing_lookback](../baselines/EMAformer/scripts/increasing_lookback) | 不同历史窗口设置 |
| 嵌入对其他骨干的实验 | [scripts/boost_performance](../baselines/EMAformer/scripts/boost_performance) | EMAformer 与其他骨干配置 |

**准备改进时：** 先从 `model/EMAformer.py` 的三个辅助嵌入与预测头入手，分别做消融；要改变相位定义或周期索引，再沿着 `data_loader.py → exp_long_term_forecasting.py → Model.forward()` 检查输入。新增模型时同步修改 `exp_basic.py` 的注册表。每项尝试在独立研究副本或分支中开展，保留原版作为对照。

**路径提醒：** ETT 脚本实际使用 `./dataset/ETT-small/`。上游目录是单数 `model/`，与 Informer、Autoformer 的 `models/` 不同。EMAformer 自带的 `model/Informer.py` 是该项目内部的基线实现，单独收录的 `Informer2020/` 才是原始 Informer 仓库。

## Pyraformer

- 上游：[ant-research/Pyraformer](https://github.com/ant-research/Pyraformer)
- 论文：[Pyraformer: Low-Complexity Pyramidal Attention for Long-Range Time Series Modeling and Forecasting](https://openreview.net/forum?id=0EXmFzUn5I)
- 上游说明：[README](../baselines/Pyraformer/README.md)

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 长区间预测模型 | [pyraformer/Pyraformer_LR.py](../baselines/Pyraformer/pyraformer/Pyraformer_LR.py) | `Encoder`、`Model`；金字塔构造、跨尺度取值与解码方式 |
| 单步预测模型 | [pyraformer/Pyraformer_SS.py](../baselines/Pyraformer/pyraformer/Pyraformer_SS.py) | 单步任务编码器及预测分布参数的头部 |
| 多尺度与连接结构 | [pyraformer/Layers.py](../baselines/Pyraformer/pyraformer/Layers.py) | `get_mask`、`refer_points`、`Bottleneck_Construct` 及卷积/池化构造；`EncoderLayer` |
| 注意力与前馈层 | [pyraformer/SubLayers.py](../baselines/Pyraformer/pyraformer/SubLayers.py)、[pyraformer/Modules.py](../baselines/Pyraformer/pyraformer/Modules.py) | 多头注意力、缩放点积注意力及前馈模块 |
| 输入嵌入 | [pyraformer/embed.py](../baselines/Pyraformer/pyraformer/embed.py) | `DataEmbedding`、`CustomEmbedding`、`SingleStepEmbedding` |
| 长区间训练/测试 | [long_range_main.py](../baselines/Pyraformer/long_range_main.py) | 参数、数据准备、训练循环与 `-eval` 开关 |
| 单步训练/测试 | [single_step_main.py](../baselines/Pyraformer/single_step_main.py) | 单步任务的数据与训练评估流程 |
| 数据加载 | [data_loader.py](../baselines/Pyraformer/data_loader.py) | 各任务数据集、切分和处理逻辑 |
| 原始数据预处理 | [preprocess_elect.py](../baselines/Pyraformer/preprocess_elect.py)、[preprocess_wind.py](../baselines/Pyraformer/preprocess_wind.py)、[preprocess_flow.py](../baselines/Pyraformer/preprocess_flow.py) | Electricity、Wind、App Flow 的预处理 |
| 合成数据 | [simulate_sin.py](../baselines/Pyraformer/simulate_sin.py) | 生成上游实验使用的合成序列 |
| 长区间实验脚本 | [scripts/Pyraformer_LR.sh](../baselines/Pyraformer/scripts/Pyraformer_LR.sh) | ETT、Electricity、synthetic 的实验参数 |
| 单步实验脚本 | [scripts/Pyraformer_SS.sh](../baselines/Pyraformer/scripts/Pyraformer_SS.sh) | Electricity、Wind、App Flow 的单步参数 |
| 可选 TVM 实现 | [pyraformer/PAM_TVM.py](../baselines/Pyraformer/pyraformer/PAM_TVM.py)、[pyraformer/hierarchical_mm_tvm.py](../baselines/Pyraformer/pyraformer/hierarchical_mm_tvm.py) | 稀疏矩阵乘法与 TVM 内核路径 |

**准备改进时：** 金字塔的层级、窗口与邻接关系主要从 `Layers.py` 下手，输入表示从 `embed.py` 下手，长区间预测输出与解码策略从 `Pyraformer_LR.py` 下手。长区间与单步任务的模型、数据和评价流程分别独立，先明确改的是哪一个任务。

**路径与依赖提醒：** 原 README 写的 `scripts/Pyraformer_LR_FC.sh` 在收录版本中不存在，正确文件名是上表的 `scripts/Pyraformer_LR.sh`。`-use_tvm` 默认关闭；上游树中的 `pyraformer/tvm` 只有提交指针，且没有 `.gitmodules`，源码快照未包含其内容。仓库中的 `.so` 是 Linux/CUDA 动态库，不能直接当作 Windows 原生库使用。

## Informer2020

- 上游：[zhouhaoyi/Informer2020](https://github.com/zhouhaoyi/Informer2020)
- 论文：[Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting](https://arxiv.org/abs/2012.07436)
- 上游说明：[README](../baselines/Informer2020/README.md)

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 模型组装 | [models/model.py](../baselines/Informer2020/models/model.py) | `Informer`、`InformerStack`；编码器、解码器、嵌入和预测投影 |
| ProbSparse 注意力 | [models/attn.py](../baselines/Informer2020/models/attn.py) | `ProbAttention` 的 query 采样、筛选和上下文更新；`FullAttention`、`AttentionLayer` |
| 编码器与蒸馏 | [models/encoder.py](../baselines/Informer2020/models/encoder.py) | `ConvLayer`、`EncoderLayer`、`Encoder`、`EncoderStack` |
| 解码器 | [models/decoder.py](../baselines/Informer2020/models/decoder.py) | 自注意力、交叉注意力与前馈路径 |
| 输入与时间嵌入 | [models/embed.py](../baselines/Informer2020/models/embed.py) | `TokenEmbedding`、位置/时间嵌入与 `DataEmbedding` |
| 参数与实验调用 | [main_informer.py](../baselines/Informer2020/main_informer.py) | 数据配置、`attn`、`factor`、`distil`、`seq_len`、`label_len`、`pred_len` |
| 模型注册、数据、训练和评估 | [exp/exp_informer.py](../baselines/Informer2020/exp/exp_informer.py) | `_build_model()`、`_get_data()`、训练循环、`test()`、`predict()` |
| 设备选择 | [exp/exp_basic.py](../baselines/Informer2020/exp/exp_basic.py) | CPU/GPU 与模型初始化 |
| 数据集 | [data/data_loader.py](../baselines/Informer2020/data/data_loader.py) | `Dataset_ETT_hour`、`Dataset_ETT_minute`、`Dataset_Custom`、`Dataset_Pred` |
| 时间特征与指标 | [utils/timefeatures.py](../baselines/Informer2020/utils/timefeatures.py)、[utils/metrics.py](../baselines/Informer2020/utils/metrics.py) | 日期编码与评价指标 |
| 实验脚本 | [scripts](../baselines/Informer2020/scripts) | [ETTh1](../baselines/Informer2020/scripts/ETTh1.sh)、[ETTh2](../baselines/Informer2020/scripts/ETTh2.sh)、[ETTm1](../baselines/Informer2020/scripts/ETTm1.sh)、[WTH](../baselines/Informer2020/scripts/WTH.sh) |

**准备改进时：** 修改稀疏 query 选择规则，先看 `attn.py`；修改编码器压缩/蒸馏，先看 `encoder.py` 的 `ConvLayer`；修改时间编码，先看 `embed.py`。加入新模型要在 `exp_informer.py` 的 `model_dict` 注册；加入新数据要同时检查 loader、`_get_data()` 与 `main_informer.py` 中的数据配置。

**参数提醒：** `--distil` 使用 `store_false`，因此命令中显式加入它会关闭蒸馏。默认 ETT 数据路径为 `./data/ETT/`。不同 PyTorch 版本的循环填充行为可能影响 `TokenEmbedding`，上游 README 的 FAQ 已说明此兼容性问题。

## Autoformer

- 上游：[thuml/Autoformer](https://github.com/thuml/Autoformer)
- 论文：[Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting](https://arxiv.org/abs/2106.13008)
- 上游说明：[README](../baselines/Autoformer/README.md)

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 模型组装与初始分解 | [models/Autoformer.py](../baselines/Autoformer/models/Autoformer.py) | `Model`；趋势/季节项初始分解、解码器输入和最终相加输出 |
| 自相关机制 | [layers/AutoCorrelation.py](../baselines/Autoformer/layers/AutoCorrelation.py) | FFT 自相关、周期/时延选择、`time_delay_agg_training()` 与 `time_delay_agg_inference()` |
| 分解与编码/解码层 | [layers/Autoformer_EncDec.py](../baselines/Autoformer/layers/Autoformer_EncDec.py) | `moving_avg`、`series_decomp`、`my_Layernorm`、分解式编码器与解码器 |
| 输入嵌入 | [layers/Embed.py](../baselines/Autoformer/layers/Embed.py) | 核心模型使用的 `DataEmbedding_wo_pos`，保留数值和时间特征嵌入 |
| 内部基线注意力 | [layers/SelfAttention_Family.py](../baselines/Autoformer/layers/SelfAttention_Family.py) | `FullAttention`、`ProbAttention` 等；Autoformer 核心自相关实现位于 `AutoCorrelation.py` |
| 参数与训练开关 | [run.py](../baselines/Autoformer/run.py) | `model`、`moving_avg`、`factor`、输入/预测长度与 `is_training` |
| 模型注册与实验流程 | [exp/exp_main.py](../baselines/Autoformer/exp/exp_main.py) | `model_dict`、数据调用、损失、优化器、训练、测试与预测 |
| 设备选择 | [exp/exp_basic.py](../baselines/Autoformer/exp/exp_basic.py) | CPU/GPU 与模型初始化 |
| 数据集与注册 | [data_provider/data_loader.py](../baselines/Autoformer/data_provider/data_loader.py)、[data_provider/data_factory.py](../baselines/Autoformer/data_provider/data_factory.py) | ETT/custom/pred 数据集、切分与标准化；`data_dict` 和 loader 配置 |
| 指标与时间特征 | [utils/metrics.py](../baselines/Autoformer/utils/metrics.py)、[utils/timefeatures.py](../baselines/Autoformer/utils/timefeatures.py) | MAE/MSE 等指标与时间编码 |
| 实验脚本 | [scripts](../baselines/Autoformer/scripts) | 按 `ETT_script`、`ECL_script`、`Exchange_script`、`Traffic_script`、`Weather_script`、`ILI_script` 查找；如 [ETTh1](../baselines/Autoformer/scripts/ETT_script/Autoformer_ETTh1.sh) |
| 交互示例 | [predict.ipynb](../baselines/Autoformer/predict.ipynb) | 上游提供的中文预测流程示例 |

**准备改进时：** 分解方法或趋势建模先看 `Autoformer_EncDec.py`，周期选择与时延聚合先看 `AutoCorrelation.py`，趋势和季节项的预测融合先看 `models/Autoformer.py`。训练与推理使用不同的时延聚合函数，修改该模块时两条路径都要检查。新增模型在 `exp_main.py` 注册；新数据在 loader 与 `data_factory.py` 接入。

**参数与路径提醒：** ETT 脚本使用 `./dataset/ETT-small/`，而 `run.py` 的默认根目录是 `./data/ETT/`，实际以传入参数为准。部分脚本固定了 `CUDA_VISIBLE_DEVICES`，运行前应检查本机设备。`requirements.txt` 未锁定版本，且未单独列出 `torch`；上游 README 指定 Python 3.6、PyTorch 1.9.0，不能把只安装该 requirements 文件视为环境已经验证。

## ETSformer

- 用户指定来源：[azkanaon/etsformer](https://github.com/azkanaon/etsformer)
- 论文：[ETSformer: Exponential Smoothing Transformers for Time-series Forecasting](https://arxiv.org/abs/2202.01381)
- 收录版本说明：[README](../baselines/ETSformer/README.md)

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 核心模型与输出分解 | [models/etsformer/model.py](../baselines/ETSformer/models/etsformer/model.py) | `ETSformer`，水平项、增长项、季节项的组合；`decomposed=True` 分解输出；训练时的 `Transform` 数据增强 |
| 指数平滑与 FFT 卷积 | [models/etsformer/exponential_smoothing.py](../baselines/ETSformer/models/etsformer/exponential_smoothing.py) | `ExponentialSmoothing`、可学习平滑系数、`get_exponential_weight()`、`conv1d_fft()` |
| 傅里叶与分解编码器 | [models/etsformer/encoder.py](../baselines/ETSformer/models/etsformer/encoder.py) | `FourierLayer` 的频率 Top-K 与外推；`GrowthLayer`、`LevelLayer`、`EncoderLayer` |
| 增长阻尼与解码 | [models/etsformer/decoder.py](../baselines/ETSformer/models/etsformer/decoder.py) | `DampingLayer`、可学习阻尼系数、增长和季节项的预测聚合 |
| 输入嵌入与前馈 | [models/etsformer/modules.py](../baselines/ETSformer/models/etsformer/modules.py) | 卷积式 `ETSEmbedding` 和 `Feedforward` |
| 参数与实验调用 | [run.py](../baselines/ETSformer/run.py) | `K`、`std`、编码器/解码器层数、分组学习率、输入/预测长度；训练后分别评价验证集和测试集 |
| 模型注册、训练与评估 | [exp/exp_main.py](../baselines/ETSformer/exp/exp_main.py) | `_build_model()`、`_select_optimizer()`、`train()`、`test()`；普通网络、平滑参数、阻尼参数的分组 |
| 自定义优化器 | [utils/Adam.py](../baselines/ETSformer/utils/Adam.py) | 项目自带的 Adam 实现 |
| 数据集与注册 | [data_provider/data_loader.py](../baselines/ETSformer/data_provider/data_loader.py)、[data_provider/data_factory.py](../baselines/ETSformer/data_provider/data_factory.py) | ETT/custom/pred 数据集、标准化与 batch 组成 |
| 指标与时间特征 | [utils/metrics.py](../baselines/ETSformer/utils/metrics.py)、[utils/timefeatures.py](../baselines/ETSformer/utils/timefeatures.py) | 评价指标和数据时间特征 |
| 常规实验脚本 | [scripts](../baselines/ETSformer/scripts) | [ETTm2](../baselines/ETSformer/scripts/ETTm2.sh)、[ETTm2 单变量](../baselines/ETSformer/scripts/ETTm2_univar.sh)、ECL、Traffic、Weather、Exchange、ILI |
| 网格搜索 | [scripts/grid_search.sh](../baselines/ETSformer/scripts/grid_search.sh) | 学习率、傅里叶基数量、输入窗口和预测窗口的组合搜索 |

**准备改进时：** 平滑核与记忆衰减先看 `exponential_smoothing.py`；季节频率选择或频谱外推先看 `encoder.py` 的 `FourierLayer`；长预测的增长衰减先看 `decoder.py` 的 `DampingLayer`。这些参数在优化器中单独分组，改名或添加参数后要同步检查 `exp_main.py` 的分组规则。新模型还需从 `models/__init__.py` 导出，并在 `exp_main.py` 注册。

**依赖与脚本提醒：** 收录版本要求 Python 3.8，依赖锁定 `torch==1.11.0`、`scipy==1.7.3`、`einops==0.4.1` 等；平滑模块直接依赖 SciPy 的 `next_fast_len` 与 PyTorch FFT，不能只复制模型文件而遗漏依赖。ETT 脚本要求 `./dataset/ETT-small/ETTm2.csv`。原 README 写的根目录 `./grid_search.sh` 不存在，实际执行入口为 `bash scripts/grid_search.sh`。模型要求 `e_layers == d_layers`，但命令行默认值分别为 2 和 1，手写命令时应显式设为相同值，原始实验脚本已这样设置。该 `run.py` 的参数解析与主循环位于顶层，Windows 原生多进程 DataLoader 需单独验证；首次尝试可设置 `--num_workers 0`，或使用上游脚本所面向的 Linux/WSL 环境。

## Time-LLM

- 上游：[KimMeen/Time-LLM](https://github.com/KimMeen/Time-LLM)
- 论文：[Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://arxiv.org/abs/2310.01728)
- 上游说明：[README](../baselines/Time-LLM/README.md)

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 核心模型、提示与重编程 | [models/TimeLLM.py](../baselines/Time-LLM/models/TimeLLM.py) | `Model`、`forecast()`、`ReprogrammingLayer`；输入统计提示、文本原型映射、冻结 LLM、预测头 |
| patch 嵌入 | [layers/Embed.py](../baselines/Time-LLM/layers/Embed.py) | `PatchEmbedding`，窗口长度与步长对应的 patch 数量 |
| 标准化与还原 | [layers/StandardNorm.py](../baselines/Time-LLM/layers/StandardNorm.py) | `Normalize` 的 `norm` / `denorm` 路径 |
| 常规预测训练 | [run_main.py](../baselines/Time-LLM/run_main.py) | 模型选择、数据、Accelerate/DeepSpeed、训练/验证/测试损失、学习率和早停 |
| M4 短期预测 | [run_m4.py](../baselines/Time-LLM/run_m4.py) | M4 任务的训练、损失与评估配置 |
| 跨数据集预训练/迁移入口 | [run_pretrain.py](../baselines/Time-LLM/run_pretrain.py) | `data_pretrain` / `data_path_pretrain` 与目标 `data` / `data_path` 的区别 |
| 常规数据加载与注册 | [data_provider/data_loader.py](../baselines/Time-LLM/data_provider/data_loader.py)、[data_provider/data_factory.py](../baselines/Time-LLM/data_provider/data_factory.py) | ETT、ECL、Traffic、Weather、M4；`percent` 训练比例与数据划分 |
| 迁移数据加载 | [data_provider_pretrain](../baselines/Time-LLM/data_provider_pretrain) | 预训练数据与目标数据的独立加载逻辑 |
| 数据集提示文本 | [dataset/prompt_bank](../baselines/Time-LLM/dataset/prompt_bank)、[utils/tools.py](../baselines/Time-LLM/utils/tools.py) | 各数据集文本；`load_content()` 的文件名选择规则 |
| M4 损失与汇总 | [utils/losses.py](../baselines/Time-LLM/utils/losses.py)、[utils/m4_summary.py](../baselines/Time-LLM/utils/m4_summary.py) | 短期预测指标与 M4 汇总流程 |
| 分布式配置 | [ds_config_zero2.json](../baselines/Time-LLM/ds_config_zero2.json) | DeepSpeed ZeRO stage 2、BF16 与自动 batch 配置 |
| 实验脚本 | [scripts](../baselines/Time-LLM/scripts) | [ETTh1](../baselines/Time-LLM/scripts/TimeLLM_ETTh1.sh)、[M4](../baselines/Time-LLM/scripts/TimeLLM_M4.sh)、[ETTh1 → ETTh2](../baselines/Time-LLM/scripts/TimeLLM_ETTh1_ETTh2.sh) 等 |

**准备改进时：** 提示词与输入统计从 `TimeLLM.py` 的 `forecast()` 入手，patch 与语言原型对齐从 `PatchEmbedding`、`mapping_layer`、`ReprogrammingLayer` 入手，预测头从 `FlattenHead` 入手。LLM 主干参数被设为 `requires_grad=False`；若研究解冻、LoRA 或替换主干，需同时检查参数组、训练显存和维度，而不能只修改模型名称。

**任务与资源提醒：** 该 `TimeLLM.Model` 实际实现长、短期预测，其他任务会触发 `NotImplementedError`，不能由命令行 help 中的多任务列表推断已支持分类或异常检测。代码支持 Llama/GPT-2/BERT，切换时需同步 `llm_model` 与 `llm_dim`；模型配置、权重和 tokenizer 通过 Hugging Face 加载，未随源码归档。默认 ETTh1 脚本是 8 进程、多 GPU、BF16、32 层 Llama 的配置；它是原始实验入口，不代表单卡机器已经具备运行条件。项目要求 Python 3.11，且锁定 torch 2.2.2、transformers 4.31.0、accelerate 0.28.0、deepspeed 0.14.0 等，与旧模型环境分开。

**源码行为提醒：** `run_main.py` 在创建模型后才设置 `args.content`，但启用 `--prompt_domain 1` 时模型构造就会读取它；开展该功能实验前，应在自己的副本中调整加载顺序。`run_main.py` 与 `run_pretrain.py` 末尾会调用 `del_files('./checkpoints')` 删除整个默认 checkpoint 目录，保存研究权重时需先检查并调整个人副本的清理行为。原始快照保持不变，便于对照这些改动。

## Time-Series-Library

- 上游：[thuml/Time-Series-Library](https://github.com/thuml/Time-Series-Library)
- 项目说明：[英文 README](../libraries/Time-Series-Library/README.md)、[中文 README](../libraries/Time-Series-Library/README_zh.md)
- 定位：这是一套完整库，不是第七个单模型。本次保留指定提交的完整文件树，包括模型、层、任务实验、数据加载、脚本、教程和部署文件；数据集与外部预训练权重仍需另行获取。

### 按任务查找

统一入口是 [run.py](../libraries/Time-Series-Library/run.py)，根据 `--task_name` 选择实验类。以下六条实验路径都包含在本次快照中：

| 任务 | `task_name` | 实验文件 | 原始脚本入口 |
| --- | --- | --- | --- |
| 长期预测 | `long_term_forecast` | [exp/exp_long_term_forecasting.py](../libraries/Time-Series-Library/exp/exp_long_term_forecasting.py) | [scripts/long_term_forecast](../libraries/Time-Series-Library/scripts/long_term_forecast) |
| 短期预测 | `short_term_forecast` | [exp/exp_short_term_forecasting.py](../libraries/Time-Series-Library/exp/exp_short_term_forecasting.py) | [scripts/short_term_forecast](../libraries/Time-Series-Library/scripts/short_term_forecast)，如 M4 |
| 缺失值插补 | `imputation` | [exp/exp_imputation.py](../libraries/Time-Series-Library/exp/exp_imputation.py) | [scripts/imputation](../libraries/Time-Series-Library/scripts/imputation) |
| 异常检测 | `anomaly_detection` | [exp/exp_anomaly_detection.py](../libraries/Time-Series-Library/exp/exp_anomaly_detection.py) | [scripts/anomaly_detection](../libraries/Time-Series-Library/scripts/anomaly_detection) |
| 分类 | `classification` | [exp/exp_classification.py](../libraries/Time-Series-Library/exp/exp_classification.py) | [scripts/classification](../libraries/Time-Series-Library/scripts/classification) |
| 零样本预测 | `zero_shot_forecast` | [exp/exp_zero_shot_forecasting.py](../libraries/Time-Series-Library/exp/exp_zero_shot_forecasting.py) | [scripts/long_term_forecast/ETT_script/LTSM.sh](../libraries/Time-Series-Library/scripts/long_term_forecast/ETT_script/LTSM.sh)，原脚本使用 `--is_training 0` |

另有完整的 [scripts/exogenous_forecast](../libraries/Time-Series-Library/scripts/exogenous_forecast) 目录组织外生变量预测实验，如 [ETTh1/TimeXer.sh](../libraries/Time-Series-Library/scripts/exogenous_forecast/ETTh1/TimeXer.sh)。该脚本通过 `long_term_forecast` 任务入口运行，而不是一个独立的 `exogenous_forecast` 实验类。

### 按源码职责查找

| 要找什么 | 文件入口 | 重点看什么 |
| --- | --- | --- |
| 模型集合 | [models](../libraries/Time-Series-Library/models) | 指定提交中有 41 个模型模块；各模型实际支持哪些任务，应看自身的 `forward()` 分支 |
| 模型发现与导入 | [exp/exp_basic.py](../libraries/Time-Series-Library/exp/exp_basic.py) | 扫描 `models/*.py`、`LazyModelDict` 按需导入模型；类名可为 `Model` 或与模块同名 |
| 通用数据与注册 | [data_provider/data_loader.py](../libraries/Time-Series-Library/data_provider/data_loader.py)、[data_provider/data_factory.py](../libraries/Time-Series-Library/data_provider/data_factory.py) | ETT/custom/M4、PSM/MSL/SMAP/SMD/SWAT、UEA；按任务构造 batch |
| 分类序列处理 | [data_provider/uea.py](../libraries/Time-Series-Library/data_provider/uea.py) | 变长序列整理、padding 与分类 batch 拼接 |
| M4 数据 | [data_provider/m4.py](../libraries/Time-Series-Library/data_provider/m4.py) | M4 数据读取和子集元信息 |
| 公共层 | [layers](../libraries/Time-Series-Library/layers) | 嵌入、注意力、自相关、分解、傅里叶/小波、Mamba、图结构等组件 |
| 通用评价与损失 | [utils/metrics.py](../libraries/Time-Series-Library/utils/metrics.py)、[utils/losses.py](../libraries/Time-Series-Library/utils/losses.py) | 任务使用的指标与损失；还需结合对应实验文件查看聚合方式 |
| 数据增强 | [utils/augmentation.py](../libraries/Time-Series-Library/utils/augmentation.py) | 扰动、缩放、时间变形等策略的实现与调用 |
| TimesNet 教程 | [tutorial/TimesNet_tutorial.ipynb](../libraries/Time-Series-Library/tutorial/TimesNet_tutorial.ipynb) | 原始教学 notebook 与配套图示 |
| 环境与部署 | [requirements.txt](../libraries/Time-Series-Library/requirements.txt)、[Dockerfile](../libraries/Time-Series-Library/Dockerfile)、[docker-compose.yml](../libraries/Time-Series-Library/docker-compose.yml) | 核心依赖与额外模型依赖、容器配置 |

### 按研究主题选择库内模型

| 主题 | 可先阅读的代码 |
| --- | --- |
| 简单线性对照 | [models/DLinear.py](../libraries/Time-Series-Library/models/DLinear.py) |
| 周期与二维变化 | [models/TimesNet.py](../libraries/Time-Series-Library/models/TimesNet.py)，关注 `FFT_for_Period` 与 `TimesBlock` |
| patch 与通道独立建模 | [models/PatchTST.py](../libraries/Time-Series-Library/models/PatchTST.py) |
| 变量 token | [models/iTransformer.py](../libraries/Time-Series-Library/models/iTransformer.py) |
| 多尺度混合 | [models/TimeMixer.py](../libraries/Time-Series-Library/models/TimeMixer.py) |
| 外生变量预测 | [models/TimeXer.py](../libraries/Time-Series-Library/models/TimeXer.py) |
| 状态空间 | [models/Mamba.py](../libraries/Time-Series-Library/models/Mamba.py)、[models/MambaSingleLayer.py](../libraries/Time-Series-Library/models/MambaSingleLayer.py) |
| 预训练时序模型与零样本 | [models/Chronos2.py](../libraries/Time-Series-Library/models/Chronos2.py)、[models/Moirai.py](../libraries/Time-Series-Library/models/Moirai.py)、[models/TimesFM.py](../libraries/Time-Series-Library/models/TimesFM.py)、[models/TiRex.py](../libraries/Time-Series-Library/models/TiRex.py) |
| 与独立原版项目对照 | 库内 [Autoformer](../libraries/Time-Series-Library/models/Autoformer.py)、[Informer](../libraries/Time-Series-Library/models/Informer.py)、[Pyraformer](../libraries/Time-Series-Library/models/Pyraformer.py)、[ETSformer](../libraries/Time-Series-Library/models/ETSformer.py) |

**准备扩展时：** 在自己的研究副本的 `models/` 增加模型模块，按 `Transformer.py` 等现有接口提供模型类、`forward()` 和所需任务分支；此固定版本会自动发现模块，无需套用旧版手工修改 `model_dict` 的做法。新数据先修改 loader 与 `data_factory.py`，新损失或训练流程修改相应 `exp/` 文件，并为每个任务准备脚本。要新增全新任务，再在 `run.py` 增加分派入口。

**版本与依赖提醒：** 独立模型项目和库内同名模型是不同上游版本与接口，不能默认为等价复现。库保留五类常规任务和零样本预测入口，不代表每个模型都实现全部任务。上游当前 README 使用 Python 3.11、推荐 torch 2.5.1；`requirements.txt` 包含不同预训练模型的依赖，Mamba 仍需匹配 Linux/CUDA 的额外包，Moirai 还需 `uni2ts`。没有通过完整文件收录推断所有模型已可运行，也未下载预训练权重。

## 研究改进如何定位

| 你的改进目标 | 优先查看 |
| --- | --- |
| 改输入表示、周期或时间特征 | EMAformer 的 `model/EMAformer.py`、`layers/Embed.py`；Pyraformer 的 `pyraformer/embed.py`；Informer 的 `models/embed.py`；Autoformer 的 `layers/Embed.py`；ETSformer 的 `models/etsformer/modules.py` |
| 改注意力选择或连接结构 | EMAformer 的 `layers/SelfAttention_Family.py`；Pyraformer 的 `pyraformer/Layers.py`；Informer 的 `models/attn.py`；Autoformer 的 `layers/AutoCorrelation.py`；ETSformer 的 `models/etsformer/exponential_smoothing.py`、`encoder.py` |
| 改趋势/季节项分解与融合 | Autoformer 的 `layers/Autoformer_EncDec.py`、`models/Autoformer.py` |
| 改平滑、增长与季节外推 | ETSformer 的 `models/etsformer/exponential_smoothing.py`、`encoder.py`、`decoder.py` |
| 改语言模型重编程或提示 | Time-LLM 的 `models/TimeLLM.py`、`layers/Embed.py`、`dataset/prompt_bank/` |
| 为同一方法测试多类任务 | Time-Series-Library 的 `models/`、对应的 `exp/exp_*.py` 和 `scripts/<任务>/`；先核实模型的任务分支 |
| 接入新数据集 | 各模型的数据 loader 和数据注册入口，再检查训练脚本中的路径、频率与通道数 |
| 改训练目标或优化器 | 各模型的实验/训练入口，而不只修改模型 `forward()` |
| 做可比较的基线实验 | 先统一数据切分、输入/预测长度、标准化、指标、随机种子及训练预算，再比较结果 |

固定上游源码可作为原版对照；自己的改动、假设与实验结果分别记录，注明所基于的模型与提交。新增方法应先做单项消融，再决定是否组合多个模型的模块。
