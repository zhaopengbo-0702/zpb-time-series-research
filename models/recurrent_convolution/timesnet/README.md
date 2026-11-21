# TimesNet

用 FFT 寻找周期，将序列按周期重排为二维，再用 Inception 卷积提取变化。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

TimesNet 把一维序列换一种摆放方式来观察。先找几个主要周期，再把数据按周期折成二维表，让卷积同时观察周期内部的变化和不同周期之间的变化。

## 核心思路

时间块用 FFT 选择显著频率，将序列补齐并按候选周期重排为二维张量，经过二维 Inception 卷积后还原时间轴；不同周期分支按频率幅度加权，并带残差叠加。

## 适用问题

适合周期性明显但同时存在多种节律的预测或表征任务，也便于研究频率选择、二维卷积和多周期加权分别带来的影响。

## 局限与边界

频谱峰不一定代表稳定的因果周期，趋势、短窗口与噪声会影响周期选择。二维折叠通常要补齐长度，不同任务的输入投影、归一化和输出头也需分别核对。

## 阅读建议

先看 FFT_for_Period 和候选周期生成，再用一个小例子核对补齐、reshape 与还原过程。随后看周期权重来自哪里，最后才读预测或分类任务的输出分支。

## 阅读材料

[模型论文](https://openreview.net/pdf?id=ju_Uqw384Oq)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/TimesNet.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/TimesNet.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/timesnet.py) | `TimesNet` | [查看](../../../_sources/source-10/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
