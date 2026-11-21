# XResNet1dPlus

一维 xresnet 的增强版本，保留可配置头和深度工厂。

**类别：** 循环与卷积

[返回分类目录](../../../docs/model-catalog.md#category-recurrent_convolution)

## 这是什么

XResNet1dPlus 将一维深度残差骨干与更灵活的输出构造结合。它保留多尺度逐层提取和捷径相加的路线，同时为任务头及网络规模提供配置。

## 核心思路

实现提供多个深度与扩展构造函数，组织一维残差 stage、特征汇总和可配置头；同一条目还包含 deep、deeper 等不同块数设置。

## 适用问题

适合需要复用残差表示的分类、回归任务，也适合在不同模型容量或输出形式间做明确的对照实验。

## 局限与边界

不同构造器与头部配置会改变容量，Plus 后缀不代表固定结构或确定提升。若用展平头，输入长度会影响参数量，必须与数据窗口一起记录。

## 阅读建议

先确认调用的是哪个深度构造器，再看 stage 数与头部创建逻辑。将骨干参数和输出头参数分别列出，与基础一维残差网络比较时逐项保持一致。

## 阅读材料

可从下方实现的本地使用说明继续阅读。

<a id="实现"></a>

## 实现

| 实现 | 核心模型 | 模型类 | 完整目录 |
| --- | --- | --- | --- |
| 实现1 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `XResNet1dPlus` | [查看](../../../_sources/source-09/) |
| 实现2 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d101plus` | [查看](../../../_sources/source-09/) |
| 实现3 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d152plus` | [查看](../../../_sources/source-09/) |
| 实现4 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d18_deeperplus` | [查看](../../../_sources/source-09/) |
| 实现5 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d18_deepplus` | [查看](../../../_sources/source-09/) |
| 实现6 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d18plus` | [查看](../../../_sources/source-09/) |
| 实现7 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d34_deeperplus` | [查看](../../../_sources/source-09/) |
| 实现8 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d34_deepplus` | [查看](../../../_sources/source-09/) |
| 实现9 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d34plus` | [查看](../../../_sources/source-09/) |
| 实现10 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d50_deeperplus` | [查看](../../../_sources/source-09/) |
| 实现11 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d50_deepplus` | [查看](../../../_sources/source-09/) |
| 实现12 | [核心文件](../../../_sources/source-09/tsai/models/XResNet1dPlus.py) | `xresnet1d50plus` | [查看](../../../_sources/source-09/) |

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
- 实现12：[入口与使用说明](../../../_sources/source-09/README.md)

[完整模型库与教程](../../../README.md#%E5%AE%8C%E6%95%B4%E6%A8%A1%E5%9E%8B%E5%BA%93%E4%B8%8E%E6%95%99%E7%A8%8B)
