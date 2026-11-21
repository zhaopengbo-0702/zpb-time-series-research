# PatchTSTFMModel

调用预训练 PatchTST foundation model，与从头训练版本区分。

**类别：** 预训练时序模型

[返回分类目录](../../../docs/model-catalog.md#category-pretrained_foundation)

## 这是什么

PatchTSTFMModel 是预训练 PatchTST-FM 的适配器，复用大型预训练权重预测，而不是普通 PatchTST 在当前数据上从零训练。

## 核心思路

patch 编码器配合分位数头生成概率预测，默认只输出中位数。接口可配置分位数并支持全量或部分微调，多变量输入逐分量独立处理。

## 适用问题

适合零样本预测、预训练与从零训练对照，以及数据量较小时的微调研究。

## 局限与边界

当前实现明确不支持协变量，多变量也不是联合交互建模。预训练分位数集合限制可选输出；不同权重标识的许可条款可能不同，必须核对实际权重。

## 阅读建议

先看 hub_model_name 与权重版本，再读 likelihood、微调开关及分量独立处理。比较普通 PatchTST 时同时交代预训练数据与权重来源。

## 阅读材料

[模型论文](https://arxiv.org/abs/2602.06909)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-12/darts/models/forecasting/patchtst_fm_model.py) | `PatchTSTFMModel` | [查看](../../../_sources/source-12/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
