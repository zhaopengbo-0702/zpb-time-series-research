# xLSTMTime

面向时间序列预测的 xLSTM 适配结构，与通用 xLSTM 分开保留。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

xLSTMTime 将扩展循环记忆用于时间序列预测，并配合分解和归一化处理。可以把它理解为先整理序列的变化，再用更丰富的记忆单元生成未来表示。

## 核心思路

实现提供 sLSTM 与 mLSTM 风格的网络组件，结合时序分解、归一化及预测映射；不同接口版本的元数据、输入包装与预测输出形式有所区别。

## 适用问题

适合研究扩展记忆与时序分解的组合，也适合与相同输入窗口的普通 LSTM、分解线性模型做结构消融。

## 局限与边界

它不是普通 LSTM 改个名字，记忆类型与接口版本会影响实际计算。长预测任务需要检查输出长度、反归一化和协变量处理，不能混用不同版本的构造方式。

## 阅读建议

先确认选中实现的模型类和数据接口，再读分解、sLSTM 或 mLSTM 层、预测头的连接。把归一化前后张量单位与预测长度写清楚后再做修改。

## 阅读材料

[模型论文](https://arxiv.org/pdf/2407.10240)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm.py) | `xLSTMTime` | [查看](../../../_sources/source-11/) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_forecaster_v2.py) | `xLSTMTimeForecaster` | [查看](../../../_sources/source-11/) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_pkg.py) | `xLSTMTime_pkg` | [查看](../../../_sources/source-11/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_v2.py) | `xLSTMTime_v2` | [查看](../../../_sources/source-11/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
