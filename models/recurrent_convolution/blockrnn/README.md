# BlockRNN

循环编码历史窗口，再以块输出同时预测多个未来点。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

BlockRNN 先让循环网络读完一段历史，再一次性给出一整块未来。它与逐点滚动输出的循环预测器不同，预测块内部通常由同一个输出头直接生成。

## 核心思路

编码器可使用 RNN、LSTM 或 GRU，取历史编码状态，经全连接层映射到 output_chunk_length 对应的多步输出；更长预测可能通过多个输出块继续展开。

## 适用问题

适合研究直接多步预测与自回归逐步预测的区别，也适合在固定预测窗口下作为门控循环结构的清晰对照。

## 局限与边界

输出块长度会影响参数量和可学习的预测关系，跨多个块外推仍可能累计误差。支持哪些协变量要按所选实现检查，不能从其他循环模型推断。

## 阅读建议

重点看编码器最后状态如何选择，以及全连接输出如何 reshape 为时间与变量轴。再核对 input_chunk_length、output_chunk_length 和多块预测的调用逻辑。

## 阅读材料

[相关论文](https://openreview.net/forum?id=cGDAkQo1C0p)

此链接是源码引用的 TiDE 相关架构文献，不是 BlockRNN 的独立论文。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-12/darts/models/forecasting/block_rnn_model.py) | `BlockRNNModel` | [查看](../../../_sources/source-12/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
