# NBEATSKAN

在 N-BEATS 式残差结构中使用 KAN 层的变体。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

把 NBEATS 的残差接力框架保留下来，再把部分普通前馈映射换成 KAN 形式。研究重点是可学习的一元函数能否改变块的表达方式。

## 核心思路

趋势块、季节块或通用块仍输出历史解释项和未来贡献，块内部通过 KAN 映射产生展开系数。它是结构组合变体，不应把基础 NBEATS 论文的结果直接移给它。

## 适用问题

适合在固定残差框架下比较 MLP 与 KAN，研究参数化方式、基函数和块类型的影响。当前条目保留实际变体代码及其接口。

## 局限与边界

KAN 的可解释性取决于具体函数与组合方式，并非网络名字自带保证。参数规模、数值稳定性和优化条件需要重新评估，基础模型的最优超参数不能直接照搬。

## 阅读建议

先理解 NBEATS 的双输出与残差，再定位 KAN 替换了哪些层。阅读引用时区分基础框架依据与这个变体的实现依据，并用同预算重新实验。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nbeats/_nbeatskan.py) | `NBeatsKAN` | [查看](../../../_sources/source-11/README.md) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/nbeats/_nbeatskan_pkg.py) | `NBeatsKAN_pkg` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
