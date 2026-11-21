# TransformerRNNPlus

将 Transformer 编码与 RNN 循环结构结合的时序网络。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TransformerRNNPlus 先让注意力观察整个窗口，再用普通循环网络按顺序整理表示。它把全局关系和循环递推放在同一条编码路径上。

## 核心思路

通道输入经线性投影和可学习位置编码，经过 Transformer 编码层后接 RNN 层，最后由可配置头输出。可选双向递推会改变隐藏维度。

## 适用问题

适合序列分类、回归，以及比较注意力后再做顺序递推是否有效。

## 局限与边界

循环层带来顺序计算成本。双向层可读取窗口内部后续位置，只能用于已观测窗口，不能在逐时因果预测中无条件复用。

## 阅读建议

先追踪输入在 batch、时间、通道间的转置，再看 Transformer 与 RNN 的连接，最后核对 bidirectional 与 head_nf。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/TransformerRNNPlus.py) | `TransformerRNNPlus` | [查看](../../../_sources/source-09/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
