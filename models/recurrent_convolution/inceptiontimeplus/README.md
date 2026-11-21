# InceptionTimePlus

并行使用不同长度的一维卷积核提取多尺度模式。 此项为 的 Plus 可配置变体。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

InceptionTimePlus 将多尺度卷积模型拆成骨干和任务头，并开放更多结构配置。它保留同时观察不同时间宽度的核心思路，方便按任务调整输出。

## 核心思路

实现使用可配置的多分支卷积与残差堆叠，支持卷积形式、注意力或通道重标定等开关，并允许自定义头；同一条目还收录不同深度和宽度的构造函数。

## 适用问题

适合研究 Inception 骨干上的结构消融，或在分类与片段回归间复用表示；也适合比较固定模型容量下不同卷积与头部设计。

## 局限与边界

增强选项并非默认全部开启，不同构造函数也不代表相同网络。固定序列长度的展平头会改变容量，应把所有开关与头部参数完整记录。

## 阅读建议

先从实际调用的构造函数读取参数，确认 depth、nf 和各增强开关，再分别查看 backbone 与 head；不要把 Plus 作为一个无需展开的性能标签。

## 阅读材料

[相关论文](https://arxiv.org/abs/1909.04939)

引用基础方法论文；此项是 Plus 变体，未核实独立论文。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/InceptionTimePlus.py) | `InceptionTimePlus` | [查看](../../../_sources/source-09/README.md) |
| 实现2 | [核心文件](../../../_sources/source-09/tsai/models/InceptionTimePlus.py) | `InceptionTimePlus17x17` | [查看](../../../_sources/source-09/README.md) |
| 实现3 | [核心文件](../../../_sources/source-09/tsai/models/InceptionTimePlus.py) | `InceptionTimePlus32x32` | [查看](../../../_sources/source-09/README.md) |
| 实现4 | [核心文件](../../../_sources/source-09/tsai/models/InceptionTimePlus.py) | `InceptionTimePlus47x47` | [查看](../../../_sources/source-09/README.md) |
| 实现5 | [核心文件](../../../_sources/source-09/tsai/models/InceptionTimePlus.py) | `InceptionTimePlus62x62` | [查看](../../../_sources/source-09/README.md) |
| 实现6 | [核心文件](../../../_sources/source-09/tsai/models/InceptionTimePlus.py) | `InceptionTimeXLPlus` | [查看](../../../_sources/source-09/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
