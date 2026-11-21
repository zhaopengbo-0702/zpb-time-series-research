# DeepAR

用自回归循环网络学习未来值的概率分布。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

DeepAR 不只给出一个未来数值，还让循环网络描述下一步可能落在哪些范围。预测时根据前一步的结果继续向前展开，从而形成多步预测分布。

## 核心思路

模型用循环状态编码历史目标与可用协变量，再输出指定概率分布的参数，以分布损失训练；多步预测通常通过自回归展开或采样传播不确定性，分布种类由实现配置决定。

## 适用问题

适合需要预测区间、概率评价或大量相关序列共享参数的场景，例如需求量与负荷预测；也可用于分析逐步递推的误差传播。

## 局限与边界

所选分布的支持域必须符合目标值类型，区间校准也需要实际检验。长预测步的误差会沿递推传播，未来协变量必须确实能在预测时获得。

## 阅读建议

先确认分布损失、参数转换和目标缩放，再看训练时使用真实前值还是预测值。最后追踪采样维度与区间汇总，区分网络原始参数、点预测和分位数。

## 阅读材料

[模型论文](https://www.sciencedirect.com/science/article/pii/S0169207019301888)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-10/neuralforecast/models/deepar.py) | `DeepAR` | [查看](../../../_sources/source-10/README.md) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/deepar/_deepar.py) | `DeepAR` | [查看](../../../_sources/source-11/README.md) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/deepar/_deepar_pkg.py) | `DeepAR_pkg` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
