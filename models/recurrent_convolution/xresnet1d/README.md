# XResNet1d

将 xresnet 架构适配为一维卷积，保留多种深度工厂。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

XResNet1d 把改进型残差卷积架构用于一维序列。它提供不同深度的构造方式，让相同的残差建模思路可以在不同模型规模下使用。

## 核心思路

收录文件将 xresnet 构造器配置为一维卷积，提供十八、三十四、五十等层级以及更深的变体；具体 stem、残差块与输出头由对应构造器决定。

## 适用问题

适合序列分类与回归中的深度残差基线，也适合控制数据和训练协议后研究网络深度与容量的影响。

## 局限与边界

家族页面中的多个构造函数不是同一个模型规模，训练成本与参数量应分别报告。使用一维残差网络也不自动获得任意长历史依赖或因果预测能力。

## 阅读建议

先定位实际调用的构造函数，查看传入的 ndim、c_in 与 n_out，再沿依赖读 residual block 与 stem。记录具体深度和 head，避免只写家族名称。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d101` | [查看](../../../_sources/source-09/README.md) |
| 实现2 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d152` | [查看](../../../_sources/source-09/README.md) |
| 实现3 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d18` | [查看](../../../_sources/source-09/README.md) |
| 实现4 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d18_deep` | [查看](../../../_sources/source-09/README.md) |
| 实现5 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d18_deeper` | [查看](../../../_sources/source-09/README.md) |
| 实现6 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d34` | [查看](../../../_sources/source-09/README.md) |
| 实现7 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d34_deep` | [查看](../../../_sources/source-09/README.md) |
| 实现8 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d34_deeper` | [查看](../../../_sources/source-09/README.md) |
| 实现9 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d50` | [查看](../../../_sources/source-09/README.md) |
| 实现10 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d50_deep` | [查看](../../../_sources/source-09/README.md) |
| 实现11 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1d.py) | `xresnet1d50_deeper` | [查看](../../../_sources/source-09/README.md) |

<a id="运行方式"></a>

## 运行方式

选择对应实现，进入其完整目录后按参数脚本或使用文档运行。各实现的相对导入、数据路径和依赖保持原样。

- 实现1：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现2：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现3：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现4：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现5：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现6：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现7：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现8：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现9：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现10：[入口与使用说明](../../../_sources/source-09/README.md)
- 实现11：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
