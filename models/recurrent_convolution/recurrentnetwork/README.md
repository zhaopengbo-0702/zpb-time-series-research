# RecurrentNetwork

以可配置的 LSTM 或 GRU 网络进行多步预测。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

RecurrentNetwork 把一个循环预测器包装成完整的编码与解码流程。它先读历史，再逐步产生未来值，并把不同变量类型与序列分组信息接入模型。

## 核心思路

核心可选择 LSTM 或 GRU，将目标和协变量送入循环层，利用编码后的状态启动解码预测；训练、目标变换和输出参数由对应模型及损失接口协同管理。

## 适用问题

适合带分组序列和多种协变量的预测实验，也是对照复杂结构时较容易解释的循环基线。需要时可以研究不同单元、隐藏宽度与解码策略。

## 局限与边界

递推式预测可能积累误差，已知与未知未来特征必须正确声明。不同损失产生的输出语义不同，不能把所有输出通道都当作直接预测值。

## 阅读建议

从输入向量构造与目标列位置读起，再看 encode、decode 和循环状态传递。重点确认训练与预测阶段喂给解码器的值是否一致，以及输出如何还原到目标尺度。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/rnn/_rnn.py) | `RecurrentNetwork` | [查看](../../../_sources/source-11/) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/rnn/_rnn_pkg.py) | `RecurrentNetwork_pkg` | [查看](../../../_sources/source-11/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
