# PAttn

用 patch 嵌入和单层注意力进行预测，提供无需调用语言模型的对照入口。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

PAttn 是一个较直接的 patch 注意力预测模型。它把历史切片后交给一个注意力编码层，用来检验简单序列编码本身能做多少事情。

## 核心思路

每个通道先归一化，经过补边、切片和线性 patch 映射，再用注意力编码器处理片段。展开后的表示由线性头映射到预测长度，最后恢复数值尺度。

## 适用问题

适合做 patch 表示与浅层注意力的对照，或在加入复杂模块前建立较容易检查的预测基线。

## 局限与边界

当前头部与输入 patch 数量绑定，改变历史长度时通常要重新构建模型。它没有自动提供语言理解或预训练知识，也不等同于大型语言模型方法。

## 阅读建议

按归一化、unfold、编码器、展平预测头的顺序读 forward，核对 patch_size、stride 与 patch_num 的关系。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2406.16964)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/PAttn.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现2 | [核心文件](../../../_sources/source-08/models/PAttn.py) | `Model` | [查看](../../../_sources/source-08/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
