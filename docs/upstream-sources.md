# 上游来源与版本

本仓库于 **2026-11-21** 将七个项目整理为固定提交的源码快照：六个独立项目在 `baselines/`，完整 Time-Series-Library 在 `libraries/`。普通 `git clone` 即可取得这些文件。导入的是指定提交的文件内容，不包含七个上游的完整 Git 历史。

## 固定版本

| 目录 | 上游 | 分支 | 固定提交 | 原始文件数 |
| --- | --- | --- | --- | ---: |
| `baselines/EMAformer/` | [PlanckChang/EMAformer](https://github.com/PlanckChang/EMAformer) | `main` | [`b8f37c0c7d089e7263bbaeb681672a94f5afe233`](https://github.com/PlanckChang/EMAformer/tree/b8f37c0c7d089e7263bbaeb681672a94f5afe233) | 71 |
| `baselines/Pyraformer/` | [ant-research/Pyraformer](https://github.com/ant-research/Pyraformer) | `master` | [`84af4dbd93b7b96975b5034f0dde412005260123`](https://github.com/ant-research/Pyraformer/tree/84af4dbd93b7b96975b5034f0dde412005260123) | 35 |
| `baselines/Informer2020/` | [zhouhaoyi/Informer2020](https://github.com/zhouhaoyi/Informer2020) | `main` | [`29f2a739226a509202a092b464163da81fa74960`](https://github.com/zhouhaoyi/Informer2020/tree/29f2a739226a509202a092b464163da81fa74960) | 32 |
| `baselines/Autoformer/` | [thuml/Autoformer](https://github.com/thuml/Autoformer) | `main` | [`51c7d416ae120b805fd5beef2f4ccf7de496a6ff`](https://github.com/thuml/Autoformer/tree/51c7d416ae120b805fd5beef2f4ccf7de496a6ff) | 64 |
| `baselines/ETSformer/` | [azkanaon/etsformer](https://github.com/azkanaon/etsformer) | `main` | [`0df5daa7149bbfcaf33a5325ee249f679bebf268`](https://github.com/azkanaon/etsformer/tree/0df5daa7149bbfcaf33a5325ee249f679bebf268) | 58 |
| `baselines/Time-LLM/` | [KimMeen/Time-LLM](https://github.com/KimMeen/Time-LLM) | `main` | [`b13e881f86cd0475ce1b72c17110430663334955`](https://github.com/KimMeen/Time-LLM/tree/b13e881f86cd0475ce1b72c17110430663334955) | 51 |
| `libraries/Time-Series-Library/` | [thuml/Time-Series-Library](https://github.com/thuml/Time-Series-Library) | `main` | [`4e938a1767106324dd753b2a44832bf870a0252e`](https://github.com/thuml/Time-Series-Library/tree/4e938a1767106324dd753b2a44832bf870a0252e) | 368 |

每个原始文件的 Git blob SHA-1 与文件模式记在根目录的 [sources.lock.json](../sources.lock.json)。原始 README、许可证、脚本、图片、压缩文件及上游已有的隐藏文件均保留；新增导航文档放在原始目录之外。

ETSformer 上游还提交了 Python 缓存、一个 checkpoint 和两个指标数组，本次作为原始快照一起保留；它们来自上游，不代表本仓库已经执行训练或验证指标。后续本地产生的新权重、缓存和结果由忽略规则过滤。

## Time-LLM 与 TSLib 的完整范围

Time-LLM 的 51 个原始文件全部保留，包括模型、数据管道、预训练与 M4 入口、实验脚本、DeepSpeed 配置、论文图及 `LEGAL.md`。LLAMA、GPT-2、BERT 等外部预训练权重不在这份源码内。

Time-Series-Library 的 368 个原始文件全部保留，包括 `models/`、`layers/`、`exp/`、`data_provider/`、`scripts/`、`tutorial/`、`utils/`、中英文 README、许可证与部署文件。未按任务或模型裁剪；41 个模型模块的导航见[全部模型索引](model-catalog.md)。这两个来源中没有 Git 子模块或 LFS 指针文件。

TSLib 内同名模型与独立原版各自保留，来源锁定清单分别记录，便于核对实现差异。新增导航和研究目录将它们组织到同一工作区，训练入口与环境仍按各自源码管理。

## Pyraformer 可选 TVM 引用

Pyraformer 上游树存在以下 gitlink，但指定提交中没有 `.gitmodules`：

```text
path:   pyraformer/tvm
mode:   160000
commit: 1fac10b359dec1bd6ad45ce36541a882aaba586b
```

该依赖的内容未包含在上游归档中，也未导入本仓库；远程地址尚未核实。来源清单记录其路径与提交。本仓库没有把它伪装成可恢复的 Git 子模块，执行 `git submodule update --init` 不能自动补齐它。

`long_range_main.py` 和 `single_step_main.py` 的 `-use_tvm` 默认均为 `False`。如研究需要启用 TVM，应按上游文档另行核实对应版本、源码来源和编译环境。原始 `pyraformer/lib/lib_hierarchical_mm_float32_cuda.so` 已保留，它是 Linux/CUDA 库。

## 校验与更新

在仓库根目录运行：

```bash
python tools/verify_sources.py
```

校验工具用标准库重新计算原始文件的 Git blob 哈希，与清单中的固定版本比较。它用于判断当前基线文件是否仍与导入版本一致，不验证模型数值正确性或实验可复现性。

将来更新某个上游时，建议单独提交：先记录新的上游提交，再更新该项目快照、来源清单和变更日志，最后复查自己的改进与新版本的差异。已有研究实验继续引用其实际使用的旧提交。

## 许可证与数据

七份源码保留各自许可证与作者署名，见 [LICENSES.md](../LICENSES.md)。公开整理并不把它们转换为同一种许可证。

Pyraformer 上游自带的 `data/app_zone_rpc_hour_encrypted.zip` 已随快照保留；其他论文数据、预训练权重和 TVM 源码不因本次整理而自动齐备。下载和使用数据时，单独记录数据来源、版本及使用条件。
