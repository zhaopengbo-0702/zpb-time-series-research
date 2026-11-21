# FiLM

用 Legendre/HiPPO 状态投影压缩历史，再以频域处理提取预测信息。

**类别：** 状态空间动力学

[返回分类目录](../../../docs/model-catalog.md#category-state_space_dynamics)

## 这是什么

FiLM 把一段较长历史压缩成一组多项式投影状态，再从这些状态中提取有用的频率变化。它的重点是用结构化记忆保存历史。

## 核心思路

HiPPO/Legendre 投影以递推形式更新状态，频域卷积对状态序列做傅里叶变换和可学习过滤，再重构或映射为预测。投影阶数决定状态容量。

## 适用问题

适合研究长历史压缩、结构化状态表示，以及频域过滤对预测的作用。

## 局限与边界

投影阶数、离散化步长和频率保留范围影响信息损失与计算量。压缩后的表示不保证保留全部短暂事件，设备与缓冲区放置也需检查。

## 阅读建议

先读 transition 与 HiPPO_LegT 的递推，再看 SpectralConv1d 如何处理频率，最后追踪状态重构与预测头。

## 阅读材料

[模型论文](https://openreview.net/forum?id=zTQdHSQUQWc)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/FiLM.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/FiLM.py) | `Model` | [查看](../../../_sources/source-08/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
