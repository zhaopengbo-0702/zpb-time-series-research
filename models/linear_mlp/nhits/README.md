# NHITS

以多分辨率采样和分层插值组合短期细节与长期预测。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

预测很远的未来时，不要求每个模块都逐点描绘细节。不同模块先看不同分辨率的历史，输出疏密不同的未来锚点，再插值拼出整段预测。

## 核心思路

输入经多尺度池化，前馈残差块学习不同频率的贡献；分层插值将较少的预测系数展开为完整预测窗，并累加各块结果。

## 适用问题

适合长预测窗与多尺度变化任务，适合研究粗尺度趋势和细尺度波动的分工。也可对池化核、插值形式和块级分辨率做消融。

## 局限与边界

粗分辨率可能平滑掉重要突变或高频信息，插值无法凭空恢复训练中缺失的细节。不同采样频率下，尺度与池化参数需要重新设置。

## 阅读建议

先画出每一层看到的历史分辨率及输出锚点数，再理解如何插值到预测长度。对照 NBEATS 时核对块数、宽度和实际参数量。

## 阅读材料

[模型论文](https://arxiv.org/abs/2201.12886)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-10/neuralforecast/models/nhits.py) | `NHITS` | [查看](../../../_sources/source-10/README.md) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nhits/_nhits.py) | `NHiTS` | [查看](../../../_sources/source-11/README.md) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nhits/_nhits_forecaster_v2.py) | `NHiTSForecaster` | [查看](../../../_sources/source-11/README.md) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nhits/_nhits_pkg.py) | `NHiTS_pkg` | [查看](../../../_sources/source-11/README.md) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nhits/_nhits_v2.py) | `NHiTS_v2` | [查看](../../../_sources/source-11/README.md) |
| 实现6 | [核心文件](../../../_sources/source-12/darts/models/forecasting/nhits.py) | `NHiTSModel` | [查看](../../../_sources/source-12/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
