# TransformerLSTMPlus

将 Transformer 编码与 LSTM 循环结构结合的时序网络。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TransformerLSTMPlus 在注意力编码后接 LSTM，用带门控的记忆状态汇总窗口信息。它是同一混合结构中的 LSTM 变体。

## 核心思路

共享的混合编码器完成投影、位置编码和 Transformer 处理，循环单元改为 LSTM，再接统一可配置头。门控状态控制哪些编码信息继续保留。

## 适用问题

适合序列分类、回归和 RNN、LSTM、GRU 三种循环单元的受控比较。

## 局限与边界

增加门控与隐藏状态会增加训练成本，未必改善每种数据。双向配置的可见范围及输入轴顺序需特别核实。

## 阅读建议

与 TransformerRNNPlus 对照，确认主要变化是 _cell=nn.LSTM；再核对循环层数、双向维度和任务头。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/TransformerRNNPlus.py) | `TransformerLSTMPlus` | [查看](../../../_sources/source-09/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
