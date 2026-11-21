# ModernTCN

用现代深度卷积分别组织时间、变量和特征维的信息。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

ModernTCN 用较大的时间卷积核看更长的局部上下文，同时把时间、变量与特征的混合拆开安排，借鉴现代卷积结构来处理时序数据。

## 核心思路

当前实现先按 patch 嵌入，再通过可重参数化的大核深度卷积与逐点前馈块加工表示，配合可逆实例归一化和展开预测头，可选择变量独立的输出投影。

## 适用问题

适合检验纯卷积在长期预测中的作用，也便于研究 patch 长度、大核大小和分组混合方式对性能与成本的影响。

## 局限与边界

大核不自动保证有效利用全部历史，补齐与 patch 边界也会影响细节。训练期多分支与部署期重参数化若被使用，需要核实具体实现是否完成融合。

## 阅读建议

先看 patch stem 与四维张量的轴，再追踪大核卷积及两个前馈块分别混合哪个维度，最后检查 RevIN 的还原和 Flatten_Head 的输出形状。

## 阅读材料

[模型论文](https://arxiv.org/abs/2401.17593)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/modern_tcn/_modern_tcn_forecaster_v2.py) | `ModernTCNForecaster` | [查看](../../../_sources/source-11/) |
| 实现2 | [核心文件](../../../_sources/source-11/pytorch_forecasting/models/modern_tcn/_modern_tcn_v2.py) | `ModernTCN` | [查看](../../../_sources/source-11/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-11/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-11/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
