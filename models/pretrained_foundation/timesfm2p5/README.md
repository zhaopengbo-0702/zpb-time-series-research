# TimesFM2p5

调用 TimesFM 2.5 预训练模型，保留版本特定接口。

**类别：** 预训练时序模型

[返回分类目录](../../../docs/model-catalog.md#category-pretrained_foundation)

## 这是什么

TimesFM2p5 明确对应 TimesFM 2.5 的预训练模型适配。它提供比简单系列包装更完整的窗口、分位数与微调配置。

## 核心思路

实现按 patch 组织输入，进行尺度处理，通过预训练主干与投影头输出点预测和分位数，再恢复原尺度。微调与推理会使用不同的分位数选择逻辑。

## 适用问题

适合 TimesFM 2.5 的零样本、概率预测和可控微调实验。

## 局限与边界

权重上下文、输出块和分位数配置有限制，不能任意扩大预测范围而假设行为不变。适配接口是否使用协变量应按支持属性核对；系列基础论文不等于该权重版本的专属说明。

## 阅读建议

先读 input_chunk_length、output_chunk_length 与输出移位，再看量化头和微调分位数处理，记录权重 revision 保证比较可追溯。

## 阅读材料

[相关论文](https://arxiv.org/abs/2310.10688)

TimesFM 系列基础论文，不将其标为 2.5 权重版本的专属论文。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-12/darts/models/forecasting/timesfm2p5_model.py) | `TimesFM2p5Model` | [查看](../../../_sources/source-12/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-12/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
