# TimeXer

结合目标序列的 patch 与外生变量表示，用注意力融合两类信息。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TimeXer 区分真正要预测的目标序列和辅助外生变量。它让目标保留细的时间片段，同时用另一套表示吸收外部信息。

## 核心思路

目标序列进行 patch 嵌入，配合全局 token；外生变量形成变量表示，通过交叉注意力与目标编码交互。输出头利用融合后的目标表示完成预测。

## 适用问题

适合研究外生变量能否帮助预测，例如天气、价格或控制条件与目标序列的关系。

## 局限与边界

外生变量必须在预测时真实可用。不同实现对单目标、多目标和特征排列有约定，不能把输入所有列不加区分地交给模型。

## 阅读建议

先确认目标列与外生列的拆分规则，再追踪 patch token、全局 token 和交叉注意力，最后核对 M、MS 等特征设置。

## 阅读材料

[模型论文](https://arxiv.org/abs/2402.19072)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/TimeXer.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现2 | [核心文件](../../../_sources/source-08/models/TimeXer.py) | `Model` | [查看](../../../_sources/source-08/README.md) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/timexer.py) | `TimeXer` | [查看](../../../_sources/source-10/README.md) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/timexer/_timexer.py) | `TimeXer` | [查看](../../../_sources/source-11/README.md) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/timexer/_timexer_forecaster_v2.py) | `TimeXerForecaster` | [查看](../../../_sources/source-11/README.md) |
| 实现6 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/timexer/_timexer_pkg.py) | `TimeXer_pkg` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
