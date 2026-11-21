# TabFusionTransformer

将类别和连续特征编码为 token，再用注意力融合。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TabFusionTransformer 把类别和连续属性都转为 token，让它们在同一注意力空间里互相参考。它面向混合类型的表格输入。

## 核心思路

类别特征采用嵌入，连续特征通过映射形成表示，融合编码器以多头注意力处理这些 token，任务头生成最终分类或回归输出。

## 适用问题

适合静态表格预测，或研究连续与类别信息怎样联合表示；可与只上下文化类别特征的 TabTransformer 对照。

## 局限与边界

特征 token 的关系不是时间顺序。应用到未来预测时，需要额外的数据窗口与时序分支，不能从名称中的 Transformer 推断已支持预测。

## 阅读建议

先看 TabFusionBackbone 的 token 构造，再确认连续变量如何映射，最后追踪 flatten 与预测头对应的字段数量。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/TabFusionTransformer.py) | `TabFusionTransformer` | [查看](../../../_sources/source-09/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
