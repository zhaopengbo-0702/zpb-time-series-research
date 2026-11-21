# PatchTST

把连续时间点切为 patch，并以通道独立的 Transformer 建模长历史。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

PatchTST 把多个连续时间点当作一个词块，减少模型要处理的 token 数。常见实现分别处理各通道，但让各通道共享同一套 Transformer 参数。

## 核心思路

历史窗口按长度和步长切成 patch，线性投影后进入编码器，预测头把 patch 表示映射到未来。通道独立策略使跨通道信息主要通过参数共享体现，而不是显式通道注意力。

## 适用问题

适合长历史预测、patch 长度研究，以及检验通道独立建模是否足够。也适合作为多变量复杂交互方法的对照。

## 局限与边界

局部切片可能弱化细粒度时序位置，通道独立可能遗漏变量间关系。这里保留的多个实现包含不同输出头和接口变体，训练参数不能直接混用。

## 阅读建议

先看切片与 padding，再确认是否通道独立、是否共享头部，最后对齐输出维度、归一化和预测损失。

## 阅读材料

[模型论文](https://openreview.net/pdf?id=Jbdc0vTOcol)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/PatchTST.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现2 | [核心文件](../../../_sources/source-08/models/PatchTST.py) | `Model` | [查看](../../../_sources/source-08/README.md) |
| 实现3 | [核心文件](../../../_sources/source-09/tsai/models/PatchTST.py) | `PatchTST` | [查看](../../../_sources/source-09/README.md) |
| 实现4 | [核心文件](../../../_sources/source-10/neuralforecast/models/patchtst.py) | `PatchTST` | [查看](../../../_sources/source-10/README.md) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_forecaster_v2.py) | `PatchTSTForecaster` | [查看](../../../_sources/source-11/README.md) |
| 实现6 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_pkg.py) | `PatchTST_pkg` | [查看](../../../_sources/source-11/README.md) |
| 实现7 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_v2.py) | `PatchTST_v2` | [查看](../../../_sources/source-11/README.md) |
| 实现8 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/patch_tst/patch_tst.py) | `PatchTST` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现7：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现8：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
