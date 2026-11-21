# 模型总目录

从这里按名称找源码。仓库包含六个独立模型快照，以及完整的 [Time-Series-Library](../libraries/Time-Series-Library/) 快照。独立模型与库内同名模型分别保留，各自的实现、依赖和实验设置可以不同。

## 六个独立模型

| 模型 | 原版目录 | 核心模型文件 | 训练入口 |
| --- | --- | --- | --- |
| EMAformer | [EMAformer](../baselines/EMAformer/) | [model/EMAformer.py](../baselines/EMAformer/model/EMAformer.py) | [run.py](../baselines/EMAformer/run.py) |
| Pyraformer | [Pyraformer](../baselines/Pyraformer/) | [Pyraformer_LR.py](../baselines/Pyraformer/pyraformer/Pyraformer_LR.py)、[Pyraformer_SS.py](../baselines/Pyraformer/pyraformer/Pyraformer_SS.py) | [long_range_main.py](../baselines/Pyraformer/long_range_main.py)、[single_step_main.py](../baselines/Pyraformer/single_step_main.py) |
| Informer2020 | [Informer2020](../baselines/Informer2020/) | [models/model.py](../baselines/Informer2020/models/model.py) | [main_informer.py](../baselines/Informer2020/main_informer.py) |
| Autoformer | [Autoformer](../baselines/Autoformer/) | [models/Autoformer.py](../baselines/Autoformer/models/Autoformer.py) | [run.py](../baselines/Autoformer/run.py) |
| ETSformer | [ETSformer](../baselines/ETSformer/) | [models/etsformer/model.py](../baselines/ETSformer/models/etsformer/model.py) | [run.py](../baselines/ETSformer/run.py) |
| Time-LLM | [Time-LLM](../baselines/Time-LLM/) | [models/TimeLLM.py](../baselines/Time-LLM/models/TimeLLM.py) | [run_main.py](../baselines/Time-LLM/run_main.py) |

详细阅读路线见 [源码导航](model-guide.md)。EMAformer 和 Time-LLM 没有在本次收录的库内 `models/` 中出现，独立源码仍完整放在上表位置。

## Time-Series-Library 的全部 41 个模型文件

以下按文件名排序，完整列出 [models/](../libraries/Time-Series-Library/models/) 下除 `__init__.py` 外的 41 个 Python 文件。“独立原版位置”仅指本研究仓库另行收录的对应源码，不代表所有模型都已另行克隆原仓库。四个重名模型可以直接对照库内适配版与独立版。

定位说明依据当前文件的结构与 `forward()` 分支，用于阅读导航。实际选任务时同时核对模型分支、输入形状、依赖和对应脚本；某个任务出现在库的入口中，并不表示每个模型都实现了该任务。

| 库内模型文件 | 独立原版位置 | 定位说明 |
| --- | --- | --- |
| [Autoformer.py](../libraries/Time-Series-Library/models/Autoformer.py) | [Autoformer 原版](../baselines/Autoformer/) | 序列分解、自相关；含预测、补全、异常检测与分类分支 |
| [Chronos.py](../libraries/Time-Series-Library/models/Chronos.py) | — | 预训练 Chronos 接口；`zero_shot_forecast` 分支，需要外部模型权重 |
| [Chronos2.py](../libraries/Time-Series-Library/models/Chronos2.py) | — | 预训练 Chronos-2 接口；`zero_shot_forecast` 分支 |
| [Crossformer.py](../libraries/Time-Series-Library/models/Crossformer.py) | — | 分段嵌入与跨维度注意力；含预测及其他任务分支 |
| [DLinear.py](../libraries/Time-Series-Library/models/DLinear.py) | — | 分解后线性映射；适合作为结构简单的对照入口 |
| [ETSformer.py](../libraries/Time-Series-Library/models/ETSformer.py) | [ETSformer 原版](../baselines/ETSformer/) | 指数平滑与频率分解；库内任务适配版 |
| [FEDformer.py](../libraries/Time-Series-Library/models/FEDformer.py) | — | 频域注意力与序列分解；含预测及其他任务分支 |
| [FiLM.py](../libraries/Time-Series-Library/models/FiLM.py) | — | Legendre 投影与频域处理；含预测及其他任务分支 |
| [FreTS.py](../libraries/Time-Series-Library/models/FreTS.py) | — | 频域 MLP；当前 `forward()` 返回长、短期预测结果 |
| [Informer.py](../libraries/Time-Series-Library/models/Informer.py) | [Informer2020 原版](../baselines/Informer2020/) | ProbSparse 注意力；库内接口与原版目录结构不同 |
| [iTransformer.py](../libraries/Time-Series-Library/models/iTransformer.py) | — | 变量 token 与倒置嵌入；含预测及其他任务分支 |
| [KANAD.py](../libraries/Time-Series-Library/models/KANAD.py) | — | 当前实现仅提供异常检测；其他列出的任务抛出 `NotImplementedError` |
| [Koopa.py](../libraries/Time-Series-Library/models/Koopa.py) | — | Koopman 预测模块；当前 `forward()` 分支为长期预测 |
| [LightTS.py](../libraries/Time-Series-Library/models/LightTS.py) | — | 轻量时序建模；含预测、补全、异常检测与分类分支 |
| [Mamba.py](../libraries/Time-Series-Library/models/Mamba.py) | — | Mamba 状态空间模块；当前入口为长、短期预测 |
| [MambaSimple.py](../libraries/Time-Series-Library/models/MambaSimple.py) | — | 简化 Mamba 实现与扫描计算；当前入口为长、短期预测 |
| [MambaSingleLayer.py](../libraries/Time-Series-Library/models/MambaSingleLayer.py) | — | 单层 Mamba 分类实现；构造与 `forward()` 限定 `classification` |
| [MICN.py](../libraries/Time-Series-Library/models/MICN.py) | — | 多尺度卷积与分解模块；含预测及其他任务分支 |
| [Moirai.py](../libraries/Time-Series-Library/models/Moirai.py) | — | 预训练 Moirai 接口；`zero_shot_forecast` 分支 |
| [MSGNet.py](../libraries/Time-Series-Library/models/MSGNet.py) | — | 多尺度图模块与周期提取；含预测及其他任务分支 |
| [MultiPatchFormer.py](../libraries/Time-Series-Library/models/MultiPatchFormer.py) | — | 多 patch 预测结构；当前实现返回预测，其他列出任务未实现 |
| [Nonstationary_Transformer.py](../libraries/Time-Series-Library/models/Nonstationary_Transformer.py) | — | 非平稳序列处理与注意力调节；含预测及其他任务分支 |
| [PAttn.py](../libraries/Time-Series-Library/models/PAttn.py) | — | Patch 嵌入与单层注意力；`forward()` 直接输出预测 |
| [PatchTST.py](../libraries/Time-Series-Library/models/PatchTST.py) | — | Patch token 建模；含预测、补全、异常检测与分类分支 |
| [Pyraformer.py](../libraries/Time-Series-Library/models/Pyraformer.py) | [Pyraformer 原版](../baselines/Pyraformer/) | 金字塔注意力；库内任务适配版 |
| [Reformer.py](../libraries/Time-Series-Library/models/Reformer.py) | — | Reformer 注意力；含预测及其他任务分支 |
| [SCINet.py](../libraries/Time-Series-Library/models/SCINet.py) | — | 递归交互卷积；当前 `forward()` 为长、短期预测 |
| [SegRNN.py](../libraries/Time-Series-Library/models/SegRNN.py) | — | 分段循环网络；含预测、补全、异常检测与分类分支 |
| [Sundial.py](../libraries/Time-Series-Library/models/Sundial.py) | — | 预训练 Sundial 接口；`zero_shot_forecast` 分支 |
| [TemporalFusionTransformer.py](../libraries/Time-Series-Library/models/TemporalFusionTransformer.py) | — | 时序融合结构；当前 `forward()` 为长、短期预测 |
| [TiDE.py](../libraries/Time-Series-Library/models/TiDE.py) | — | 稠密编码与解码；提供预测、补全分支，异常检测和分类未实现 |
| [TimeFilter.py](../libraries/Time-Series-Library/models/TimeFilter.py) | — | 时序图过滤模块；含预测、补全、异常检测与分类分支 |
| [TimeMixer.py](../libraries/Time-Series-Library/models/TimeMixer.py) | — | 多尺度混合；含预测、补全、异常检测与分类分支 |
| [TimeMoE.py](../libraries/Time-Series-Library/models/TimeMoE.py) | — | 预训练 TimeMoE 接口；`zero_shot_forecast` 分支 |
| [TimesFM.py](../libraries/Time-Series-Library/models/TimesFM.py) | — | 预训练 TimesFM 接口；`zero_shot_forecast` 分支 |
| [TimesNet.py](../libraries/Time-Series-Library/models/TimesNet.py) | — | 周期发现与二维时序变化建模；含预测及其他任务分支 |
| [TimeXer.py](../libraries/Time-Series-Library/models/TimeXer.py) | — | 结合外生变量的预测结构；当前 `forward()` 为长、短期预测 |
| [TiRex.py](../libraries/Time-Series-Library/models/TiRex.py) | — | 预训练 TiRex 接口；`zero_shot_forecast` 分支 |
| [Transformer.py](../libraries/Time-Series-Library/models/Transformer.py) | — | 标准 Transformer 对照入口；含预测及其他任务分支 |
| [TSMixer.py](../libraries/Time-Series-Library/models/TSMixer.py) | — | 时序混合模块；当前 `forward()` 为长、短期预测 |
| [WPMixer.py](../libraries/Time-Series-Library/models/WPMixer.py) | — | 小波与 patch 混合；当前实现预测，其他列出任务未实现 |

## 按任务查脚本和实验流程

[scripts/](../libraries/Time-Series-Library/scripts/) 当前有六个任务目录。`zero_shot_forecast` 是 [run.py](../libraries/Time-Series-Library/run.py) 中单独实现的任务分支，其示例位于长期预测目录内，没有独立的第七个脚本目录。

| 要找什么 | 脚本位置 | 实验类入口 |
| --- | --- | --- |
| 长期预测 | [long_term_forecast/](../libraries/Time-Series-Library/scripts/long_term_forecast/) | [exp_long_term_forecasting.py](../libraries/Time-Series-Library/exp/exp_long_term_forecasting.py) |
| 短期预测 | [short_term_forecast/](../libraries/Time-Series-Library/scripts/short_term_forecast/) | [exp_short_term_forecasting.py](../libraries/Time-Series-Library/exp/exp_short_term_forecasting.py) |
| 缺失值补全 | [imputation/](../libraries/Time-Series-Library/scripts/imputation/) | [exp_imputation.py](../libraries/Time-Series-Library/exp/exp_imputation.py) |
| 异常检测 | [anomaly_detection/](../libraries/Time-Series-Library/scripts/anomaly_detection/) | [exp_anomaly_detection.py](../libraries/Time-Series-Library/exp/exp_anomaly_detection.py) |
| 分类 | [classification/](../libraries/Time-Series-Library/scripts/classification/) | [exp_classification.py](../libraries/Time-Series-Library/exp/exp_classification.py) |
| 外生变量预测 | [exogenous_forecast/](../libraries/Time-Series-Library/scripts/exogenous_forecast/) | 按脚本的 `--task_name` 进入对应实验流程，不另设同名实验类 |
| 零样本预测 | [long_term_forecast/ETT_script/LTSM.sh](../libraries/Time-Series-Library/scripts/long_term_forecast/ETT_script/LTSM.sh) | [exp_zero_shot_forecasting.py](../libraries/Time-Series-Library/exp/exp_zero_shot_forecasting.py) |

`LTSM.sh` 是示例脚本名，并非 `models/LTSM.py` 模型。当前脚本设置 `model_name=Chronos2`、`--task_name zero_shot_forecast` 和 `--is_training 0`。预训练接口的权重由各模型文件中的加载代码获取，源码快照不包含这些外部权重。

统一命令行入口是 [run.py](../libraries/Time-Series-Library/run.py)，模型文件由 [exp/exp_basic.py](../libraries/Time-Series-Library/exp/exp_basic.py) 扫描并延迟加载。阅读数据管线可从 [data_provider/](../libraries/Time-Series-Library/data_provider/) 开始；来源提交与原始文件校验见 [sources.lock.json](../sources.lock.json)。
