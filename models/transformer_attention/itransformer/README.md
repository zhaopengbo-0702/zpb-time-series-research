# iTransformer

把每个变量的历史作为一个 token，让注意力直接学习变量之间的关系。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

iTransformer 把常见 Transformer 的观察方向转了过来。一个 token 代表一条变量的整段历史，注意力主要比较变量之间的关系。

## 核心思路

倒置嵌入将时间维映射到隐藏特征，编码器在变量 token 间做注意力，前馈层处理每条变量的历史表示，预测头输出每个变量的未来。

## 适用问题

适合多变量预测和通道关系研究，尤其可与把时间点作为 token 的模型进行直接比较。

## 局限与边界

变量很多时注意力开销随变量数增长，历史长度通常进入嵌入层的输入维度。单变量场景中，跨变量注意力可利用的结构会显著减少。

## 阅读建议

重点核对输入转置前后的形状，再读倒置嵌入与预测投影，最后比较时间 token 与变量 token 两种设置。

## 阅读材料

[模型论文](https://arxiv.org/abs/2310.06625)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/iTransformer.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现2 | [核心文件](../../../_sources/source-08/models/iTransformer.py) | `Model` | [查看](../../../_sources/source-08/README.md) |
| 实现3 | [核心文件](../../../_sources/source-10/neuralforecast/models/itransformer.py) | `iTransformer` | [查看](../../../_sources/source-10/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现2：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-10/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
