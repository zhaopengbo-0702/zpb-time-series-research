# TSTabFusionTransformer

通过 Transformer 融合时间序列与表格特征。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TSTabFusionTransformer 尝试把时间序列和静态表格信息一起处理。可以把它理解为把两类输入转换成可被同一注意力模块处理的表示。

## 核心思路

实现以表格融合 Transformer 为基础，增加时序输入的表示路径，将时间序列信息与类别、连续属性组合，再由任务头输出。

## 适用问题

适合序列分类或回归同时拥有对象属性、设备信息等静态字段的场景。

## 局限与边界

必须核对时序张量与表格字段的输入协议，缺失某类输入时并非自动适配。最终头部决定输出任务，不能直接当作任意预测长度的现成模型。

## 阅读建议

把本类与 TabFusionTransformer 的 forward 对照，找出新增时序输入怎样进入 token 组合，并核对样本维是否一一对应。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/TabFusionTransformer.py) | `TSTabFusionTransformer` | [查看](../../../_sources/source-09/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
