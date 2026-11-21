# Autoformer

逐层拆分趋势与季节变化，再用自相关选择时延并聚合序列。

**类别：** 分解平滑频域

[返回分类目录](../../../docs/model-catalog.md#category-decomposition_frequency)

## 这是什么

边建模边把序列拆成趋势和季节变化，再寻找相隔若干时刻却重复出现的模式。直观上，它更关心“隔多久会重复”，而非只逐点比较相似度。

## 核心思路

在编解码层中反复使用序列分解，利用自相关机制发现时延并聚合对应子序列；趋势与季节路径共同形成预测。实现中的频域运算服务于时延估计。

## 适用问题

适合有重复结构和多尺度走向的长期预测，也适合研究层内分解与时延聚合。可与一次性预分解、普通注意力及线性分解模型对照。

## 局限与边界

周期和时延关系发生变化时，历史重复模式可能不再可靠；分解窗口和输入长度影响学习。自相关表示统计依赖，不意味着发现了真实因果机制。

## 阅读建议

先画出一层的趋势/季节两条路径，再看相关性如何选出时延并移动聚合子序列。比较各实现时核对编解码输入和分解窗口。

## 阅读材料

[模型论文](https://arxiv.org/abs/2106.13008)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-04/models/Autoformer.py) | `Model` | [查看](../../../_sources/source-04/README.md) |
| 实现2 | [核心文件](../../../_sources/source-07/models/Autoformer.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现3 | [核心文件](../../../_sources/source-08/models/Autoformer.py) | `Model` | [查看](../../../_sources/source-08/README.md) |
| 实现4 | [核心文件](../../../_sources/source-10/neuralforecast/models/autoformer.py) | `Autoformer` | [查看](../../../_sources/source-10/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-04/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现4：[入口与使用说明](../../../_sources/source-10/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
