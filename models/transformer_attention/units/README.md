# UniTS

以统一时序表示和结构适配多种序列任务。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

UniTS 的研究方向是用统一表示处理不同序列任务。本仓库当前收录的类明确是简化的 patch 预测适配实现，需要区分论文全框架与此实现范围。

## 核心思路

当前实现按通道独立切片并共享投影，在 patch 序列前加入可学习任务提示 token，通过 Transformer 编码，再聚合通道表示和预测头输出。

## 适用问题

适合阅读统一任务表示的设计，并对当前简化预测实现进行 patch 或任务提示消融。

## 局限与边界

源码标明为实验性简化版本，不能据此宣称完整复现论文的多任务能力。输入长度、patch 长度及隐藏维度与注意力头数存在约束。

## 阅读建议

先读类文档对简化范围的说明，再检查 patch_embedding、prompt token 和通道平均的位置，最后与论文结构逐项对照。

## 阅读材料

[模型论文](https://arxiv.org/abs/2403.00131)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/units/_units_forecaster_v2.py) | `UniTSForecaster` | [查看](../../../_sources/source-11/) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/units/_units_v2.py) | `UniTS` | [查看](../../../_sources/source-11/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
