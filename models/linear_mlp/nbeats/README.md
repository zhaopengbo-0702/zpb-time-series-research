# NBEATS

堆叠残差前馈块，分别拟合历史与预测基函数并累加结果。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

让多个前馈模块接力工作：每个模块解释掉一部分历史，同时贡献一部分未来预测，后面的模块继续处理剩下没解释好的部分。

## 核心思路

块输出回看重建和前瞻预测，回看项从残差中减去，前瞻项逐块相加。基展开可以采用通用可学习形式，也可选趋势、季节等带结构的形式。

## 适用问题

适合单变量多步预测和残差分解研究，也适合观察逐块预测如何累加，以及结构化基与通用基的差异。是否支持协变量须看具体变体。

## 局限与边界

块的可加分量不天然等同真实物理成分；通用块的解释性尤其有限。网络堆叠深度和宽度会增加训练开销，外部信息通常需要专门扩展。

## 阅读建议

先理解一个块的 backcast 和 forecast，再看残差减法与预测加法。最后核对该实现使用通用块还是解释型块，以及训练预算与集成设置。

## 阅读材料

[模型论文](https://arxiv.org/abs/1905.10437)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-10/neuralforecast/models/nbeats.py) | `NBEATS` | [查看](../../../_sources/source-10/README.md) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nbeats/_nbeats.py) | `NBeats` | [查看](../../../_sources/source-11/README.md) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nbeats/_nbeats_pkg.py) | `NBeats_pkg` | [查看](../../../_sources/source-11/README.md) |
| 实现4 | [核心文件](../../../_sources/source-12/darts/models/forecasting/nbeats.py) | `NBEATSModel` | [查看](../../../_sources/source-12/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
