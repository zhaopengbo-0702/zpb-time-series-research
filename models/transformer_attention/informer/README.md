# Informer

用 ProbSparse 选择重要 query，并通过编码器蒸馏压缩长序列。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

Informer 试图减少长序列中大量相似的注意力计算。它优先精算较有区分度的 query，并逐层压缩历史表示，用于较长范围的预测。

## 核心思路

ProbSparse 注意力借助采样估计 query 的重要性，只对一部分 query 进行较完整的注意力计算。编码器可使用卷积与下采样蒸馏，解码器一次输出预测区间。

## 适用问题

适合研究长序列预测、注意力稀疏化和编码器蒸馏，并与标准 Transformer 在相同窗口下比较。

## 局限与边界

稀疏采样和下采样可能遗漏短暂细节；实际成本还受窗口、批量与实现影响。不同实现对长短期任务、时间特征和输出头的处理并不完全一致。

## 阅读建议

先对比 ProbAttention 与 FullAttention，再看蒸馏层是否开启，最后沿模型 forward 追踪编码器输入、解码器已知区间与待预测区间。

## 阅读材料

[模型论文](https://arxiv.org/abs/2012.07436)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-03/models/model.py) | `Model` | [查看](../../../_sources/source-03/README.md) |
| 实现2 | [核心文件](../../../_sources/source-07/models/Informer.py) | `Model` | [查看](../../../_sources/source-07/README.md) |
| 实现3 | [核心文件](../../../_sources/source-08/models/Informer.py) | `Model` | [查看](../../../_sources/source-08/README.md) |
| 实现4 | [核心文件](../../../_sources/source-10/neuralforecast/models/informer.py) | `Informer` | [查看](../../../_sources/source-10/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-03/main_informer.py)
- 实现2：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-08/run.py)
- 实现4：[入口与使用说明](../../../_sources/source-10/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
