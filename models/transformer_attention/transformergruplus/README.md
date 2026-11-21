# TransformerGRUPlus

将 Transformer 编码与 GRU 循环结构结合的时序网络。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TransformerGRUPlus 用 GRU 汇总 Transformer 已编码的序列。相对 LSTM，它使用另一种门控结构，适合比较混合编码器的复杂度。

## 核心思路

输入经过共同的投影、位置编码和注意力模块，后续循环层使用 GRU，最终任务头将序列表示映射到目标。

## 适用问题

适合序列分类或回归，以及保持注意力部分不变时比较循环单元。

## 局限与边界

GRU 变体并不保证更快或更准，实际表现依赖隐藏维度、序列长度与设备。双向模式同样需要遵守预测时可用信息边界。

## 阅读建议

先读共享 _TransformerRNNPlus，再核对 _cell=nn.GRU，比较三变体时固定隐藏维度、层数和输出头。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/TransformerRNNPlus.py) | `TransformerGRUPlus` | [查看](../../../_sources/source-09/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
