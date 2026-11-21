# MambaSingleLayer

用单层 Mamba 做序列分类，当前构造和前向路径限定分类任务。

**类别：** 状态空间动力学

[返回分类目录](../../../docs/model-catalog.md#category-state_space_dynamics)

## 这是什么

MambaSingleLayer 用单层状态空间模块做序列分类，关注一个较浅结构可以提取多少判别信息。当前接口专门面向分类。

## 核心思路

序列嵌入后经过单层 Mamba，逐时间位置产生类别相关表示，再用注意力权重加权汇聚。padding mask 用于去掉补齐位置的影响。

## 适用问题

适合多变量序列分类和单层结构消融，尤其可比较不同状态更新开关与汇聚方式。

## 局限与边界

构造和 forward 都限定 classification，不能直接当作预测模型。单层结构简洁不等于所有数据都足够表达，mask 和变长输入协议需要正确配置。

## 阅读建议

先核对任务检查与嵌入，再看 Mamba_TimeVariant 的开关，最后检查类别 logit 与时间权重怎样共同汇聚。

## 阅读材料

[相关论文](https://openreview.net/forum?id=YDl4vqQqGP)

当前模块对应 MambaSL 分类论文；文件名 MambaSingleLayer 与论文模型名 MambaSL 分别保留。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-07/models/MambaSingleLayer.py) | `Model` | [查看](../../../_sources/source-07/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-07/run.py)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
