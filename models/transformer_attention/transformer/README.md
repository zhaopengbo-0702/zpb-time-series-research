# Transformer

使用标准编码器和解码器注意力结构，作为其他改造模型的对照。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

这里的 Transformer 是用标准注意力结构处理数值序列的模型家族。每个位置可以比较其他位置，学习哪些历史信息与当前预测有关。

## 核心思路

数值与时间信息被嵌入为 token，经过多头注意力、前馈网络和残差连接。编码器或编码器解码器结构由具体实现决定，任务头生成未来值或其他任务输出。

## 适用问题

适合作为稀疏注意力、分解、patch 和状态空间改造的基础对照，也方便学习注意力模型的数据流。

## 局限与边界

标准全注意力随 token 数增长较快；位置编码、解码器输入和掩码容易造成实现差异。多个实现共享方法名称，不代表预测协议和参数默认值相同。

## 阅读建议

先弄清每个 token 对应时间点还是变量，再看掩码与解码器输入。以相同历史长度、预测长度和损失比较各项改造。

## 阅读材料

[模型论文](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/Transformer.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/Transformer.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/vanillatransformer.py) | `VanillaTransformer` | [查看](../../../_sources/source-10/) |
| 实现4 | [核心文件](../../../_sources/source-12/darts/models/forecasting/transformer_model.py) | `TransformerModel` | [查看](../../../_sources/source-12/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
