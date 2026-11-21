# SOFTS

将多变量聚合到共享核心，再融合回各变量，控制交互成本。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

多个变量先向一个共享核心汇报信息，再由核心把汇总结果分发回每个变量。这样用中心交换代替显式列出所有变量两两关系。

## 核心思路

序列先形成变量表示，STAD 模块执行聚合与分发，再结合前馈变换输出预测。共享核心的维度决定被压缩、保留和反馈的信息容量。

## 适用问题

适合多变量预测以及研究集中式变量交互，可以与通道独立 MLP 和成对注意力比较，分析交互方式、核心宽度与变量数量的影响。

## 局限与边界

共享核心会构成信息瓶颈，少数局部关系可能在聚合中被稀释。减少成对交互的设计动机不意味着所有规模下都有精度或速度优势。

## 阅读建议

先画清变量表示、核心表示及分发后表示的形状，再看聚合是否含随机机制。比较时同时测试相关变量较多和较少的数据。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2404.14197)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-10/neuralforecast/models/softs.py) | `SOFTS` | [查看](../../../_sources/source-10/README.md) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/softs/_softs_forecaster_v2.py) | `SOFTSForecaster` | [查看](../../../_sources/source-11/README.md) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/softs/_softs_v2.py) | `SOFTS` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
