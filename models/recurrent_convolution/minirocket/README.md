# MiniRocket

用固定形式的卷积核和阈值统计快速生成分类或回归特征。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

MiniRocket 用一组规则化的固定卷积核快速把序列变成很多数字特征，再训练一个较简单的预测头。主要学习负担从深层网络转向特征后的决策。

## 核心思路

特征提取器使用固定模式卷积、多种膨胀率和从训练数据拟合的阈值，统计响应超过阈值的比例；收录实现包括分类、回归封装及带线性头的版本。

## 适用问题

适合作为时间序列分类与回归的特征型基线，也适合在有限预算下检验复杂端到端模型是否必要。

## 局限与边界

阈值拟合必须只使用训练数据，特征数、采样和随机状态影响可复现性。高维特征不直接保留完整时间顺序，不同后端的接口和输出形式也不完全一致。

## 阅读建议

先看特征提取器的 fit，再看 dilation、阈值和比例统计。随后确认分类器或回归器真正训练哪些参数，并区分离线特征流水线与在线线性头。

## 阅读材料

[模型论文](https://arxiv.org/abs/2102.00457)

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/MINIROCKET.py) | `MiniRocketClassifier` | [查看](../../../_sources/source-09/) |
| 实现2 | [核心文件](../../../_sources/source-09/tsai/models/MINIROCKET.py) | `MiniRocketRegressor` | [查看](../../../_sources/source-09/) |
| 实现3 | [核心文件](../../../_sources/source-09/tsai/models/MINIROCKET_Pytorch.py) | `MiniRocket` | [查看](../../../_sources/source-09/) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
