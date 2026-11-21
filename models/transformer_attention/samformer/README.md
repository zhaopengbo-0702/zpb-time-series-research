# Samformer

以浅层注意力组织变量关系，结合对应训练策略预测。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

Samformer 关注较浅的注意力结构能否做好预测，并把变量间关系作为建模重点。论文方法还涉及训练优化策略，结构和训练器应分开理解。

## 核心思路

当前实现将历史长度映射为 query、key 和 value，在通道维做注意力，配合可逆归一化与线性预测头。是否使用论文中的 SAM 优化需由训练配置确认。

## 适用问题

适合比较浅层通道注意力、线性预测和归一化设置，也适合研究优化器对预测结果的影响。

## 局限与边界

当前类要求单目标 out_channels=1，不能默认多目标通用。仅实例化模型不会自动保证采用论文训练策略，优化器与训练流程需要另查。

## 阅读建议

先核对 query 和 key 的轴，再看 RevIN 与线性头，最后检查训练器实际选择的优化器及是否存在 SAM 步骤。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/samformer/_samformer_forecaster_v2.py) | `SamformerForecaster` | [查看](../../../_sources/source-11/README.md) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/samformer/_samformer_v2.py) | `Samformer` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
