# GatedTabTransformer

以门控和注意力表示表格变量，可用于带静态属性任务。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

GatedTabTransformer 主要处理表格变量，而不是天然处理按时间展开的历史。它先让类别特征形成上下文化表示，再用门控 MLP 组合特征。

## 核心思路

实现继承类别嵌入与 Transformer 表示部分，把类别嵌入和连续特征拼接后送入 gMLP 头。门控发生在后续特征混合中。

## 适用问题

适合包含类别属性和连续属性的分类或回归，可作为时序任务中静态特征分支的候选组件。

## 局限与边界

输入是表格特征结构，不能直接把多步历史当成原生时间模型。类别字典与连续特征顺序必须一致，未出现类别的处理依赖数据编码。

## 阅读建议

先理解 TabTransformer 的输入字段，再看本类怎样替换 MLP 为 gMLP，确认门控头接收到的展平维度。

## 阅读材料

[模型论文](https://arxiv.org/abs/2201.00199)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/GatedTabTransformer.py) | `GatedTabTransformer` | [查看](../../../_sources/source-09/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
