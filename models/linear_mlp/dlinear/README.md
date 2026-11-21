# DLinear

先分解趋势与剩余变化，再分别做线性预测，是结构简单的对照模型。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

先把曲线拆成平滑的长期走向和剩余波动，再分别用一条线性映射预测未来。它回答一个很实用的问题：复杂网络的效果，是否只是来自对趋势和周期的简单拟合？

## 核心思路

移动平均提取趋势，原序列减去趋势得到剩余项；两组线性层各自将历史窗口投影到预测窗口，再将结果相加。共享通道和各通道独立参数是不同配置，不能混为一谈。

## 适用问题

适合作为多步预测的基础对照，检查数据中可由固定时间权重解释的结构，也适合做分解模块、通道共享和窗口长度的消融。统一实验入口已接通其原始模型。

## 局限与边界

时间权重在训练后固定，不能像内容相关注意力那样为每个样本重建关系；共享通道线性映射也不等于显式学习变量间因果联系。突变和复杂非线性关系需要额外检验。

## 阅读建议

先画出原序列、移动平均与剩余项，再检查两组线性层的输入输出长度。比较不同实现时核对初始化、移动平均窗口、归一化和通道独立选项。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2205.13504.pdf)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/DLinear.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/DLinear.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/dlinear.py) | `DLinear` | [查看](../../../_sources/source-10/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/dlinear/_dlinear_forecaster_v2.py) | `DLinearForecaster` | [查看](../../../_sources/source-11/) |
| 实现5 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/dlinear/_dlinear_v2.py) | `DLinear` | [查看](../../../_sources/source-11/) |
| 实现6 | [核心文件](../../../_sources/source-12/darts/models/forecasting/dlinear.py) | `DLinearModel` | [查看](../../../_sources/source-12/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
