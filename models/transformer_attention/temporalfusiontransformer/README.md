# TemporalFusionTransformer

通过变量选择、门控循环层和注意力融合历史与时间协变量。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TemporalFusionTransformer 将历史目标、已知未来特征和静态属性分别处理，再决定哪些信息应参与每个时间点的预测。它适合把多种类型的协变量接在一起。

## 核心思路

变量选择网络和门控残差块筛选特征，循环层处理局部时间信息，注意力层融合较长依赖。不同实现可提供分位数输出、静态上下文或不同程度的结构简化。

## 适用问题

适合同时拥有静态属性、历史观测和未来已知计划特征的多步预测，如需求与负荷预测。

## 局限与边界

必须区分未来可知特征和未来不可知观测，错误配置会造成泄漏。变量选择权重有解释用途，但不能直接视为因果效应；各实现的特征支持要单独核实。

## 阅读建议

先把输入按静态、历史、未来已知三组列出来，再读变量选择、循环处理、注意力和输出头的连接。

## 阅读材料

[模型论文](https://arxiv.org/abs/1912.09363)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/TemporalFusionTransformer.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/TemporalFusionTransformer.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/tft.py) | `TFT` | [查看](../../../_sources/source-10/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft.py) | `TemporalFusionTransformer` | [查看](../../../_sources/source-11/) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft_forecaster_v2.py) | `TFTForecaster` | [查看](../../../_sources/source-11/) |
| 实现6 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft_pkg.py) | `TemporalFusionTransformer_pkg` | [查看](../../../_sources/source-11/) |
| 实现7 | [核心文件](../../../_sources/source-12/darts/models/forecasting/tft_model.py) | `TFTModel` | [查看](../../../_sources/source-12/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现7：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
