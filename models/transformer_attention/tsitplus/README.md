# TSiTPlus

将 ViT 式 token 和 Transformer 结构适配到时间序列。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

TSiTPlus 将视觉 Transformer 一类的 token 编码思路适配到时间序列。它是可配置的时序网络变体，不应把基础方法论文自动当作这个变体的专属论文。

## 核心思路

输入通过可配置 token 表示进入带位置编码的 Transformer，编码块支持注意力与前馈网络，并可配置分类 token、池化或任务头等结构。

## 适用问题

适合序列分类和回归，尤其是比较不同 token 化、位置编码和输出汇聚方式的研究。

## 局限与边界

可配置项很多，名称相同的实验也可能采用不同结构。token 数与窗口长度影响计算成本，任务能力由所选头部决定。

## 阅读建议

先固定 token 构造与输出头，读清编码块再逐项开启可选设置，避免同时改变多个因素后无法解释收益。

## 阅读材料

[相关论文](https://arxiv.org/abs/2010.11929)

由所链接的方法适配而来，不宣称此时序变体有独立论文。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/TSiTPlus.py) | `TSiTPlus` | [查看](../../../_sources/source-09/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
