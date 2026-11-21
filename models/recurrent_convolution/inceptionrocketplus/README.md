# InceptionRocketPlus

将多尺度卷积特征与 Rocket 风格任务头结合。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

InceptionRocketPlus 在多个卷积核长度上分别提取 MiniRocket 风格统计，再把它们合并。它借用多尺度并行的想法，但核心是统计特征而不是普通 Inception 深层卷积。

## 核心思路

实现为不同 kernel_sizes 构造特征提取器，分配各自的特征预算和膨胀率，拟合阈值后拼接统计量，再经归一化、可选 dropout 和线性或自定义头输出。

## 适用问题

适合局部模式时长差异较大的分类或回归，也适合研究固定总特征数下增加卷积尺度是否有用。

## 局限与边界

多尺度会改变特征预算分配，不能只增加核宽而忽略总维度。阈值仅能从训练数据获取，长度过短时部分核会被过滤，需检查实际启用的尺度。

## 阅读建议

先看 kernel_sizes 过滤和特征分配函数，再确认每个子提取器的 fit 与拼接顺序。与 MiniRocket 比较时保持总特征数和输出头一致。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/MINIROCKETPlus_Pytorch.py) | `InceptionRocketPlus` | [查看](../../../_sources/source-09/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
