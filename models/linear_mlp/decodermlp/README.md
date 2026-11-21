# DecoderMLP

使用解码区间可用的协变量构建前馈预测。

**类别：** 线性与MLP

[返回分类目录](../../../docs/model-catalog.md#category-linear_mlp)

## 这是什么

只看预测阶段能取得的特征，用 MLP 逐步给出未来目标。它不是先把历史全部编码再预测，而是把重点放在未来已知条件本身。

## 核心思路

从解码阶段可用的连续特征、类别嵌入等构造输入，再通过全连接模块形成输出。实际能输入什么由数据集对已知变量的定义决定。

## 适用问题

适合评估日历、静态属性和计划特征本身能够解释多少目标变化，也适合给使用完整历史编码的模型建立一个信息较少的参照。

## 局限与边界

历史动态信息不足时会限制预测能力；如果把实际预测时未知的未来目标或衍生变量当解码特征，结果将有泄漏。它的输入约束必须先说明。

## 阅读建议

从数据集的 decoder 字段开始，逐一核对部署时可否获得。与历史模型比较时，分别标明信息集合差异和网络结构差异。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp.py) | `DecoderMLP` | [查看](../../../_sources/source-11/) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_forecaster_v2.py) | `DecoderMLPForecaster` | [查看](../../../_sources/source-11/) |
| 实现3 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_pkg.py) | `DecoderMLP_pkg` | [查看](../../../_sources/source-11/) |
| 实现4 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_v2.py) | `DecoderMLP_v2` | [查看](../../../_sources/source-11/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
