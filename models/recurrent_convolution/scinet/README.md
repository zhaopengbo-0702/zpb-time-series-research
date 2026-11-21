# SCINet

递归拆分奇偶时间点，用交互卷积交换信息后重新合并序列。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

SCINet 的想法是把时间交错的观测拆成两组，让它们分别加工后互相交流，再拼回一条序列。递归重复这个过程，相当于在多个疏密层次上组织信息。

## 核心思路

网络按奇偶位置拆分输入，通过卷积分支学习两组之间的交互变换，在树状层级中递归处理，随后交错合并；残差与投影层把加工后的历史转换成预测输出。

## 适用问题

适合检验交错采样和层级交互对长窗口预测的作用，也适合对比普通卷积堆叠与显式多层时间拆分的差别。

## 局限与边界

递归层数与输入长度需要兼容，奇偶拆分也不能代替不规则时间处理。不同实现的堆叠、残差和预测头可能不同，不能仅靠模型名判断输出行为。

## 阅读建议

从 splitting 和交互块读起，手算一个短序列被拆分与还原的顺序，再看递归层数、padding 和投影形状；这样容易发现时间位置是否被正确拼回。

## 阅读材料

[模型论文](https://openreview.net/pdf?id=AyajSjTAzmg)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/SCINet.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现2 | [核心文件](../../../_sources/source-08/models/SCINet.py) | `Model` | [查看](../../../_sources/source-08/README.md) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/scinet/_scinet_forecaster_v2.py) | `SCINetForecaster` | [查看](../../../_sources/source-11/README.md) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/scinet/_scinet_v2.py) | `SCINet_v2` | [查看](../../../_sources/source-11/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
