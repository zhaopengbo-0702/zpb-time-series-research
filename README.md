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

## 独立原版来源

以下六个仓库提供独立原版入口；它们也已作为模型条目列入上方统一目录。

| 模型 | 主要思路 | 原版源码 | 核心模型 | 训练入口 | 论文 / 上游 |
| --- | --- | --- | --- | --- | --- |
| EMAformer | 用通道、相位及联合嵌入增强变量之间的建模 | [EMAformer](baselines/EMAformer/) | [model/EMAformer.py](baselines/EMAformer/model/EMAformer.py) | [run.py](baselines/EMAformer/run.py) | [论文](https://arxiv.org/abs/2511.08396) · [上游](https://github.com/PlanckChang/EMAformer) |
| Pyraformer | 金字塔式多尺度结构与稀疏注意力 | [Pyraformer](baselines/Pyraformer/) | [Pyraformer_LR.py](baselines/Pyraformer/pyraformer/Pyraformer_LR.py) · [Pyraformer_SS.py](baselines/Pyraformer/pyraformer/Pyraformer_SS.py) | [长预测](baselines/Pyraformer/long_range_main.py) · [单步预测](baselines/Pyraformer/single_step_main.py) | [论文](https://openreview.net/forum?id=0EXmFzUn5I) · [上游](https://github.com/ant-research/Pyraformer) |
| Informer2020 | ProbSparse 注意力、编码器蒸馏及生成式解码 | [Informer2020](baselines/Informer2020/) | [models/model.py](baselines/Informer2020/models/model.py) | [main_informer.py](baselines/Informer2020/main_informer.py) | [论文](https://arxiv.org/abs/2012.07436) · [上游](https://github.com/zhouhaoyi/Informer2020) |
| Autoformer | 趋势与季节分解，加上基于时延的 Auto-Correlation | [Autoformer](baselines/Autoformer/) | [models/Autoformer.py](baselines/Autoformer/models/Autoformer.py) | [run.py](baselines/Autoformer/run.py) | [论文](https://arxiv.org/abs/2106.13008) · [上游](https://github.com/thuml/Autoformer) |
| ETSformer | 指数平滑与频率注意力，分解水平、增长与季节项 | [ETSformer](baselines/ETSformer/) | [models/etsformer/model.py](baselines/ETSformer/models/etsformer/model.py) | [run.py](baselines/ETSformer/run.py) | [论文](https://arxiv.org/abs/2202.01381) · [上游](https://github.com/azkanaon/etsformer) |
| Time-LLM | 将时间序列重编程为语言模型可处理的表示，配合上下文提示 | [Time-LLM](baselines/Time-LLM/) | [models/TimeLLM.py](baselines/Time-LLM/models/TimeLLM.py) | [run_main.py](baselines/Time-LLM/run_main.py) | [论文](https://arxiv.org/abs/2310.01728) · [上游](https://github.com/KimMeen/Time-LLM) |

按技术主题查找时：嵌入设计先看 EMAformer，多尺度结构先看 Pyraformer，稀疏注意力先看 Informer，分解与周期聚合先看 Autoformer，指数平滑与频率建模先看 ETSformer，语言模型重编程先看 Time-LLM。

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
