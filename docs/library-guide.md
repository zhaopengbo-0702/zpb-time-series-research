# 完整时序库的源码与使用路线

[返回首页](../README.md) · [全部模型目录](model-catalog.md) · [独立基线运行指南](running-baselines.md) · [来源记录](upstream-sources.md)

`libraries/` 保存各库固定提交中的完整受 Git 跟踪文件，保留模型、数据接口、训练流程、教程及许可证。下表先按用途找库，再到各节定位实现。这里完成了源码与入口核查，尚未安装这些环境或执行训练。

| 库 | 适合先查的问题 | 统一接口与主要入口 |
| --- | --- | --- |
| [Time-Series-Library](../libraries/Time-Series-Library/) | 多模型、多任务的论文实验与零样本预测 | `run.py` → `exp/` → `models/`；详见[原有运行说明](running-baselines.md#4-time-series-library-多任务实验库) |
| [TimeSeriesLibrary-ZJ](../libraries/TimeSeriesLibrary-ZJ/) | 对照另一份 TSLib 实现，查 MambaSimple 与旧版训练流程 | `run.py` → `exp/exp_basic.py` 的模型映射 → `models/` |
| [tsai](../libraries/tsai/) | 时间序列分类、回归、预测，以及 fastai 训练与增强流程 | `TSClassifier` / `TSRegressor` / `TSForecaster` → fastai `Learner` |
| [NeuralForecast](../libraries/neuralforecast/) | 多序列预测、外生变量、概率损失、超参数搜索 | `NeuralForecast(models=..., freq=...)` → `.fit()` / `.predict()` |
| [PyTorch Forecasting](../libraries/pytorch-forecasting/) | 分组时序数据、已知/未知协变量、Lightning 训练与可解释预测 | `TimeSeriesDataSet` → 模型 `.from_dataset()` → Lightning `Trainer.fit()` |
| [Darts](../libraries/darts/) | 统一比较统计模型、机器学习与深度模型，做回测、集成与异常检测 | `TimeSeries` → 模型 `.fit()` / `.predict()` / `.historical_forecasts()` |

同名模型在不同库中可能使用不同的数据处理、默认参数、训练目标和预测接口。完整库是一种实现来源，独立论文仓库是另一种实现来源；开展比较时记录具体来源与提交。

## TimeSeriesLibrary-ZJ

上游：[ZJ-LuoGuangQing/TimeSeriesLibrary](https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary) · [原 README](../libraries/TimeSeriesLibrary-ZJ/README.md)

这份项目保留 TSLib 的五任务实验结构。查代码时按下面的顺序走：

| 要找的内容 | 路径 |
| --- | --- |
| 命令参数、任务分支、训练/测试启动 | [run.py](../libraries/TimeSeriesLibrary-ZJ/run.py) |
| 模型导入和注册 | [exp/exp_basic.py](../libraries/TimeSeriesLibrary-ZJ/exp/exp_basic.py) |
| 全部模型实现 | [models/](../libraries/TimeSeriesLibrary-ZJ/models/) |
| MambaSimple | [models/MambaSimple.py](../libraries/TimeSeriesLibrary-ZJ/models/MambaSimple.py) |
| 任务训练和评估 | [exp/](../libraries/TimeSeriesLibrary-ZJ/exp/) |
| 数据类型映射和加载器 | [data_factory.py](../libraries/TimeSeriesLibrary-ZJ/data_provider/data_factory.py) · [data_loader.py](../libraries/TimeSeriesLibrary-ZJ/data_provider/data_loader.py) |
| 可复用网络组件 | [layers/](../libraries/TimeSeriesLibrary-ZJ/layers/) |
| 各任务的参数脚本 | [scripts/](../libraries/TimeSeriesLibrary-ZJ/scripts/) |
| 入门教程 | [TimesNet_tutorial.ipynb](../libraries/TimeSeriesLibrary-ZJ/tutorial/TimesNet_tutorial.ipynb) |

此版本通过 `Exp_Basic.model_dict` 显式注册模型，新增模型要同时修改导入和映射；`thuml/Time-Series-Library` 当前收录版本则自动扫描模型目录，两个入口的注册方式不同。`MambaSimple` 为基于 PyTorch 的简化状态空间实现；另一个 `Mamba` 分支才会导入 `mamba_ssm`，不能把二者当成相同的依赖路径。

原 README 使用 Python 3.8；[requirements.txt](../libraries/TimeSeriesLibrary-ZJ/requirements.txt) 固定 torch 2.0.0、NumPy 1.23.5、pandas 1.5.3、SciPy 1.10.1 等。数据需按原 README 另行放在该库的 `dataset/`，在该库目录内运行脚本，例如长期预测入口为 `scripts/long_term_forecast/ETT_script/TimesNet_ETTh1.sh`。具体模型是否支持分类、补全或异常检测，仍需查看其 `forward()` 分支。

## tsai

上游：[timeseriesAI/tsai](https://github.com/timeseriesAI/tsai) · [原 README](../libraries/tsai/README.md) · [在线文档](https://timeseriesai.github.io/tsai/)

tsai 基于 PyTorch 与 fastai。读取一条训练链路时，可先看 `TSClassifier`、`TSRegressor`、`TSForecaster` 如何创建 DataLoaders 和模型，再看所选模型和数据变换。

| 要找的内容 | 路径 |
| --- | --- |
| 分类/回归/预测的高层训练器 | [tsai/tslearner.py](../libraries/tsai/tsai/tslearner.py) |
| Learner 扩展、训练相关工具 | [tsai/learner.py](../libraries/tsai/tsai/learner.py) · [tsai/callback/](../libraries/tsai/tsai/callback/) |
| 模型目录 | [tsai/models/](../libraries/tsai/tsai/models/) |
| InceptionTimePlus / PatchTST 示例实现 | [InceptionTimePlus.py](../libraries/tsai/tsai/models/InceptionTimePlus.py) · [PatchTST.py](../libraries/tsai/tsai/models/PatchTST.py) |
| 数据集与 DataLoaders | [tsai/data/core.py](../libraries/tsai/tsai/data/core.py) |
| 数据准备、划分、外部数据集入口 | [preparation.py](../libraries/tsai/tsai/data/preparation.py) · [validation.py](../libraries/tsai/tsai/data/validation.py) · [external.py](../libraries/tsai/tsai/data/external.py) |
| 预处理与增强 | [tsai/data/](../libraries/tsai/tsai/data/) |
| 开发用 Notebook 源码 | [nbs/](../libraries/tsai/nbs/) |
| 面向用户的教程 | [tutorial_nbs/](../libraries/tsai/tutorial_nbs/) |

推荐从[分类入门](../libraries/tsai/tutorial_nbs/01_Intro_to_Time_Series_Classification.ipynb)、[回归入门](../libraries/tsai/tutorial_nbs/04_Intro_to_Time_Series_Regression.ipynb)、[PatchTST 长期预测](../libraries/tsai/tutorial_nbs/15_PatchTST_a_new_transformer_for_LTSF.ipynb)中选一个任务开始。训练通常通过 `Learner.fit_one_cycle()` 等 fastai 接口进行，未提供一个与 TSLib 相同的全局 `run.py`。

本次快照的 [pyproject.toml](../libraries/tsai/pyproject.toml) 声明 Python ≥ 3.10、fastai ≥ 2.8.7、fastcore ≥ 1.13.2、torch ≥ 2.12 且 < 3、scikit-learn ≥ 1.7 且 < 1.8。以这些实际版本约束为准，独立准备环境；`extras` 中的 sktime、tsfresh、PyWavelets、nbformat 只用于部分功能。包内多个 `.py` 文件标有 Notebook 自动生成说明，做正式改进时应留意其对应 `nbs/` 源文件，避免后续导出覆盖自己的修改。

## NeuralForecast

上游：[Nixtla/neuralforecast](https://github.com/Nixtla/neuralforecast) · [原 README](../libraries/neuralforecast/README.md) · [在线文档](https://nixtlaverse.nixtla.io/neuralforecast/)

NeuralForecast 将多个神经预测模型接到统一的 `fit` / `predict` 接口。常规长表使用 `unique_id` 标识序列、`ds` 表示时间、`y` 表示目标；外生变量与静态变量按模型配置传入。

| 要找的内容 | 路径 |
| --- | --- |
| `NeuralForecast` 的训练、预测、交叉验证与保存加载 | [neuralforecast/core.py](../libraries/neuralforecast/neuralforecast/core.py) |
| 模型实现与导出 | [neuralforecast/models/](../libraries/neuralforecast/neuralforecast/models/) |
| NHITS / TimeLLM 示例 | [nhits.py](../libraries/neuralforecast/neuralforecast/models/nhits.py) · [timellm.py](../libraries/neuralforecast/neuralforecast/models/timellm.py) |
| 模型共用的训练与窗口处理 | [common/_base_model.py](../libraries/neuralforecast/neuralforecast/common/_base_model.py) |
| 时序数据集 | [neuralforecast/tsdataset.py](../libraries/neuralforecast/neuralforecast/tsdataset.py) |
| 损失与概率分布 | [losses/pytorch.py](../libraries/neuralforecast/neuralforecast/losses/pytorch.py) |
| 自动调参模型与配置 | [neuralforecast/auto.py](../libraries/neuralforecast/neuralforecast/auto.py) |
| 论文和基准实验 | [experiments/](../libraries/neuralforecast/experiments/) |
| 快速入门 / 新增模型 | [quickstart.ipynb](../libraries/neuralforecast/nbs/docs/getting-started/quickstart.ipynb) · [adding_models.ipynb](../libraries/neuralforecast/nbs/docs/tutorials/adding_models.ipynb) |
| 长序列 Transformer 教程 | [longhorizon_transformers.ipynb](../libraries/neuralforecast/nbs/docs/tutorials/longhorizon_transformers.ipynb) |

本次 [pyproject.toml](../libraries/neuralforecast/pyproject.toml) 声明 Python ≥ 3.11、torch ≥ 2.9.1、pytorch-lightning ≥ 2.6.6、pandas ≥ 2.3.3，并包含 Ray、Optuna 等依赖。训练资源由所选模型、序列数、输入窗、预测长和 Trainer 参数共同决定。

普通神经模型与 `TimeLLM` 的额外资源要求不同。后者需要语言模型相关依赖及权重；当前 README 还单独说明 `TimeLLM` 的保存/加载限制，应按该库当前实现使用，不能直接套用独立 Time-LLM 仓库的参数或保存方式。

## PyTorch Forecasting

上游：[sktime/pytorch-forecasting](https://github.com/sktime/pytorch-forecasting) · [原 README](../libraries/pytorch-forecasting/README.md) · [在线文档](https://pytorch-forecasting.readthedocs.io/)

PyTorch Forecasting 重点将分组数据、协变量、归一化、预测损失和 Lightning 训练连接起来。先理解数据集接口，再阅读模型，通常比直接读模型层更容易看清真实输入输出。

| 要找的内容 | 路径 |
| --- | --- |
| 对外包入口 | [pytorch_forecasting/__init__.py](../libraries/pytorch-forecasting/pytorch_forecasting/__init__.py) |
| 模型目录 | [pytorch_forecasting/models/](../libraries/pytorch-forecasting/pytorch_forecasting/models/) |
| Temporal Fusion Transformer | [models/temporal_fusion_transformer/_tft.py](../libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft.py) |
| 传统 BaseModel 训练、预测和 `from_dataset` 接口 | [models/base/_base_model.py](../libraries/pytorch-forecasting/pytorch_forecasting/models/base/_base_model.py) |
| 数据集接口与 v2 数据接口 | [data/timeseries/](../libraries/pytorch-forecasting/pytorch_forecasting/data/timeseries/) |
| 类别编码、归一化 | [data/encoders.py](../libraries/pytorch-forecasting/pytorch_forecasting/data/encoders.py) |
| 指标与分布损失 | [metrics/](../libraries/pytorch-forecasting/pytorch_forecasting/metrics/) |
| 调参、回调与适配器 | [tuning/](../libraries/pytorch-forecasting/pytorch_forecasting/tuning/) · [callbacks/](../libraries/pytorch-forecasting/pytorch_forecasting/callbacks/) · [adapters/](../libraries/pytorch-forecasting/pytorch_forecasting/adapters/) |
| 可运行示例 | [examples/](../libraries/pytorch-forecasting/examples/) |
| 数据到训练的教程 | [stallion.ipynb](../libraries/pytorch-forecasting/docs/source/tutorials/stallion.ipynb) |
| 新模型开发 / v2 / TSLib 接入 | [building.ipynb](../libraries/pytorch-forecasting/docs/source/tutorials/building.ipynb) · [ptf_V2_example.ipynb](../libraries/pytorch-forecasting/docs/source/tutorials/ptf_V2_example.ipynb) · [tslib_v2_example.ipynb](../libraries/pytorch-forecasting/docs/source/tutorials/tslib_v2_example.ipynb) |

通常用带整数 `time_idx`、目标列和分组标识的数据创建 `TimeSeriesDataSet`，声明静态变量、已知未来变量与未知未来变量，经 `.to_dataloader()` 后交给 Lightning `Trainer.fit()`。未来是否已知是数据语义，不能仅为使用某个模型而把未来目标误放进已知协变量。

本次 [pyproject.toml](../libraries/pytorch-forecasting/pyproject.toml) 声明 Python ≥ 3.10 且 < 3.15、torch ≥ 2.0 且 < 3（排除 2.0.1）、Lightning ≥ 2.0 且 < 2.7（另排除指定版本），并区分 `tuning`、`mqf2` 等可选依赖。快照同时包含已有接口与 v2 接口，教程、数据类、模型基类和训练方式应选用同一套接口。

## Darts

上游：[unit8co/darts](https://github.com/unit8co/darts) · [原 README](../libraries/darts/README.md) · [安装说明](../libraries/darts/INSTALL.md) · [在线文档](https://unit8co.github.io/darts/)

Darts 使用 `TimeSeries` 统一承载时间索引、多变量与概率样本，再为统计、回归、深度模型及预训练模型提供一致的预测接口。研究回测和协变量设置时，可从高层预测基类追到具体实现。

| 要找的内容 | 路径 |
| --- | --- |
| 时间序列数据结构 | [darts/timeseries.py](../libraries/darts/darts/timeseries.py) |
| 公开模型名与惰性导入表 | [darts/models/__init__.py](../libraries/darts/darts/models/__init__.py) |
| 预测模型 | [darts/models/forecasting/](../libraries/darts/darts/models/forecasting/) |
| `fit`、预测与历史回测的共同接口 | [forecasting_model.py](../libraries/darts/darts/models/forecasting/forecasting_model.py) |
| PyTorch 训练与 Lightning 模块 | [torch_forecasting_model.py](../libraries/darts/darts/models/forecasting/torch_forecasting_model.py) · [pl_forecasting_module.py](../libraries/darts/darts/models/forecasting/pl_forecasting_module.py) |
| 内置数据集入口与下载加载器 | [datasets/](../libraries/darts/darts/datasets/) · [dataset_loaders.py](../libraries/darts/darts/datasets/dataset_loaders.py) |
| Torch 窗口数据集 | [utils/data/torch_datasets/](../libraries/darts/darts/utils/data/torch_datasets/) |
| 变换、编码与指标 | [dataprocessing/](../libraries/darts/darts/dataprocessing/) · [metrics/](../libraries/darts/darts/metrics/) |
| 异常检测组件 | [darts/ad/](../libraries/darts/darts/ad/) |
| 入门与任务示例 | [examples/](../libraries/darts/examples/) |

推荐先看[快速入门](../libraries/darts/examples/00-quickstart.ipynb)，再根据任务选[多序列与协变量](../libraries/darts/examples/01-multi-time-series-and-covariates.ipynb)、[异常检测](../libraries/darts/examples/22-anomaly-detection-examples.ipynb)、[基础模型](../libraries/darts/examples/25-FoundationModel-examples.ipynb)或[NeuralForecast 接口](../libraries/darts/examples/26-NeuralForecast-examples.ipynb)。

本次 [pyproject.toml](../libraries/darts/pyproject.toml) 声明 Python ≥ 3.11。基础依赖与 `torch`、`notorch`、`all` extras 分开：例如深度模型依赖 `torch` extra，当前约束包含 torch ≥ 2.6.0 与 pytorch-lightning ≥ 2.6.6；LightGBM、CatBoost、Prophet 等有各自的额外包。预训练基础模型还需对应权重，源码目录中存在接口不代表权重已经下载。

模型目录还包含集成、保形校准、外部包适配器和滤波器，查数量时应区分这些用途。`EnsembleModel` 为抽象基类；`RandomForest` 与 `RegressionModel` 是兼容旧名称的别名。`NeuralForecastModel`、`StatsForecastModel` 等是统一调用外部模型的适配器，并非另外提出一种独立预测算法。

## 安排自己的阅读与实验

先按任务选择一种数据接口和训练框架，再选模型。分类与增强可先读 tsai；统一论文实验可先读两份 TSLib；多序列预测和调参可读 NeuralForecast；复杂协变量和分组数据可读 PyTorch Forecasting；统计与神经模型的统一回测可读 Darts。

每个库分别准备环境。复制教程时记录来源提交，并固定数据划分、归一化拟合范围、输入窗、预测长、输出变量、评价尺度和随机性设置。实验结果与改进说明放在 [experiments/](../experiments/) 和 [research/](../research/)，所需外部数据与权重按各库要求另行准备。
