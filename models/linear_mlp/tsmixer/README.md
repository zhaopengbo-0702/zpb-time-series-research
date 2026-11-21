# TSMixer

交替沿时间轴和变量轴使用 MLP 混合信息，再映射到预测窗口。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

轮流在时间方向和变量方向使用 MLP：先让一个变量的不同时刻交换信息，再让同一时刻的不同变量交换信息，反复几次后预测。

## 核心思路

残差块包含时间混合与通道混合，两种操作通过转置张量选择作用轴；最后把历史长度映射到预测长度。工作区已接通真实原始模型的统一训练与预测。

## 适用问题

适合多变量预测，以及检验“时间混合加变量混合”是否足以替代更复杂交互结构。可分别移除时间分支、变量分支或残差连接做消融。

## 局限与边界

混合层的尺寸依赖输入窗口和变量配置；参数学习到的关联不等于因果关系。变量强弱相关、噪声及样本量都会影响联合混合是否有收益。

## 阅读建议

从一个张量的转置前后形状入手，确认每个 MLP 究竟沿哪个轴工作。统一示例提供训练损失和逐变量预测，便于先验证数据链再改结构。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2303.06053.pdf)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/TSMixer.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/TSMixer.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/tsmixer.py) | `TSMixer` | [查看](../../../_sources/source-10/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/tsmixer/_tsmixer_forecaster_v2.py) | `TSMixerForecaster` | [查看](../../../_sources/source-11/) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/tsmixer/_tsmixer_v2.py) | `TSMixer` | [查看](../../../_sources/source-11/) |
| 实现6 | [核心文件](../../../_sources/source-12/darts/models/forecasting/tsmixer_model.py) | `TSMixerModel` | [查看](../../../_sources/source-12/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
