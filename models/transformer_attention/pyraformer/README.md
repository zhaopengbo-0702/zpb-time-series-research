# Pyraformer

构建多尺度金字塔，在层内与层间设置稀疏连接以传递长期信息。

**类别：** Transformer与注意力

[返回分类目录](../../../docs/model-catalog.md#category-transformer_attention)

## 这是什么

Pyraformer 把一条长序列组织成金字塔。底层看细节，上层看更粗的时间范围，让相隔很远的信息可以经过少量层间连接传递。

## 核心思路

模型先构造多尺度节点，再通过层内邻居和父子节点形成稀疏注意力。粗尺度聚合与金字塔注意力共同形成表示，随后由长预测或单步预测头输出结果。

## 适用问题

适合比较长历史预测中的多尺度归纳偏置与稀疏连接，尤其是希望控制全注意力开销的实验。

## 局限与边界

窗口大小、尺度层数和内层邻域决定连接结构，不能直接套到任意序列长度。可选加速实现另有平台依赖，标准计算路径与加速路径应分别验证。

## 阅读建议

先画出金字塔各层节点数量，再读注意力 mask 与索引生成。长预测和单步预测是不同入口，比较结果时要核对任务、数据和解码设置。

## 阅读材料

[模型论文](https://openreview.net/forum?id=0EXmFzUn5I)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-02/pyraformer/Pyraformer_LR.py) · [单步核心](../../../_sources/source-02/pyraformer/Pyraformer_SS.py) | `Model` | [查看](../../../_sources/source-02/) |
| 实现2 | [核心文件](../../../_sources/source-07/models/Pyraformer.py) | `Model` | [查看](../../../_sources/source-07/) |
| 实现3 | [核心文件](../../../_sources/source-08/models/Pyraformer.py) | `Model` | [查看](../../../_sources/source-08/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-02/long_range_main.py) · [单步入口](../../../_sources/source-02/single_step_main.py)
- 实现2：[入口与使用说明](../../../_sources/source-07/run.py)
- 实现3：[入口与使用说明](../../../_sources/source-08/run.py)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
