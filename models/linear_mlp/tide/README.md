# TiDE

用残差 MLP 编码历史和协变量，再通过稠密解码与时间投影得到预测。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

用前馈网络把历史与可用的未来信息压缩成一段表示，再逐时刻解码未来。它尝试用残差 MLP 完成常见编码器和解码器的工作。

## 核心思路

历史目标与协变量经过特征投影、残差编码和解码，时间解码器将表示与各未来时刻的特征组合；线性残差路径为预测提供直接的历史参考。

## 适用问题

适合多步预测以及未来日历、计划等协变量已知的场景。可以用来研究未来特征的价值，或比较 MLP 编解码与注意力编解码的差异。

## 局限与边界

未来协变量必须在实际预测时可获得，事后才知道的变量不能输入。固定预测窗和特征投影带来配置约束，残差结构本身也不保证能外推未见过的变化。

## 阅读建议

先区分历史目标、历史协变量和未来已知协变量，沿编码器、解码器、时间解码器和残差连接画出数据流，核对每条信息何时可用。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2304.08424.pdf)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/TiDE.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/TiDE.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/tide.py) | `TiDE` | [查看](../../../_sources/source-10/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/tide/_tide.py) | `TiDEModel` | [查看](../../../_sources/source-11/) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/tide/_tide_dsipts/_tide_forecaster_v2.py) | `TIDEForecaster` | [查看](../../../_sources/source-11/) |
| 实现6 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/tide/_tide_dsipts/_tide_v2.py) | `TIDE` | [查看](../../../_sources/source-11/) |
| 实现7 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/tide/_tide_pkg.py) | `TiDEModel_pkg` | [查看](../../../_sources/source-11/) |
| 实现8 | [核心文件](../../../_sources/source-12/darts/models/forecasting/tide_model.py) | `TiDEModel` | [查看](../../../_sources/source-12/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现7：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现8：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
