# FreTS

把序列变到频域，用复数 MLP 混合时间和通道信息，再还原预测。

**类别：** 分解平滑频域

[返回分类目录](../../../docs/model-catalog.md#category-decomposition_frequency)

## 这是什么

先把序列变到频域，让 MLP 学习频率成分之间的关系，再变回来预测。它尝试用频域的紧凑表达同时处理时间与变量联系。

## 核心思路

输入嵌入后沿相关轴做 Fourier 变换，复数 MLP 分别处理实部与虚部并混合，逆变换后经过预测头。通道独立配置决定是否启用部分跨变量操作。

## 适用问题

适合周期信号、多变量关系与频域前馈网络的研究，可对比时间域 MLP、只沿时间变换以及加入变量方向变换的不同效果。

## 局限与边界

输入窗口、频率分辨率与通道独立开关会改变模型行为；有限窗口存在边界问题。频域表示不能保证更适合非周期突变，复数参数也需注意稳定性。

## 阅读建议

先看 FFT 沿哪条轴做，再逐行对应复数乘法的实部虚部公式。检查逆变换长度及最终投影，避免将变量轴和时间轴混淆。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2311.06184.pdf)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/FreTS.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现2 | [核心文件](../../../_sources/source-08/models/FreTS.py) | `Model` | [查看](../../../_sources/source-08/) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/frets/_frets_forecaster_v2.py) | `FreTSForecaster` | [查看](../../../_sources/source-11/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/frets/_frets_v2.py) | `FreTS` | [查看](../../../_sources/source-11/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
