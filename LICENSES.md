# 第三方源码与许可证索引

本仓库汇集十二个上游项目的固定提交源码，包括六个独立模型仓库和六个时间序列库。各自的许可证、版权与原始说明保留在对应目录中。下表是文件索引，不以一份根目录许可证覆盖全部上游内容。

| 项目 | 上游仓库 | 快照内的许可证文件 | 需一并保留的说明 |
| --- | --- | --- | --- |
| EMAformer | [PlanckChang/EMAformer](https://github.com/PlanckChang/EMAformer) | [MIT LICENSE](baselines/EMAformer/LICENSE) | 原版权声明：2025 Zhiwei Zhang @ Beijing Jiaotong University |
| Pyraformer | [ant-research/Pyraformer](https://github.com/ant-research/Pyraformer) | [Apache-2.0 LICENSE](baselines/Pyraformer/LICENSE) | [LEGAL.md](baselines/Pyraformer/LEGAL.md) 与原源码版权声明 |
| Informer2020 | [zhouhaoyi/Informer2020](https://github.com/zhouhaoyi/Informer2020) | [Apache-2.0 LICENSE](baselines/Informer2020/LICENSE) | [原 README](baselines/Informer2020/README.md) 中的许可证徽章存在下述不一致 |
| Autoformer | [thuml/Autoformer](https://github.com/thuml/Autoformer) | [MIT LICENSE](baselines/Autoformer/LICENSE) | 原源码版权与引用信息 |
| ETSformer | [azkanaon/etsformer](https://github.com/azkanaon/etsformer) | [BSD-3-Clause LICENSE.txt](baselines/ETSformer/LICENSE.txt) | 原版权声明：2022 Salesforce.com, Inc.，许可证中的三项条件与原声明 |
| Time-LLM | [KimMeen/Time-LLM](https://github.com/KimMeen/Time-LLM) | [Apache-2.0 LICENSE](baselines/Time-LLM/LICENSE) | [LEGAL.md](baselines/Time-LLM/LEGAL.md) 与原源码声明；外部大模型权重另有其条款 |
| Time-Series-Library | [thuml/Time-Series-Library](https://github.com/thuml/Time-Series-Library) | [MIT LICENSE](libraries/Time-Series-Library/LICENSE) | 原版权声明：2021 THUML @ Tsinghua University，以及源码内保留的第三方声明 |
| TimeSeriesLibrary-ZJ | [ZJ-LuoGuangQing/TimeSeriesLibrary](https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary) | [MIT LICENSE](libraries/TimeSeriesLibrary-ZJ/LICENSE) | 原版权声明：2021 THUML @ Tsinghua University；保留该来源快照内的原声明 |
| tsai | [timeseriesAI/tsai](https://github.com/timeseriesAI/tsai) | [Apache-2.0 LICENSE](libraries/tsai/LICENSE) | 原源码声明、项目引用与文档 |
| neuralforecast | [Nixtla/neuralforecast](https://github.com/Nixtla/neuralforecast) | [Apache-2.0 LICENSE](libraries/neuralforecast/LICENSE) | [THIRD_PARTY_LICENSES.md](libraries/neuralforecast/THIRD_PARTY_LICENSES.md) 与原源码声明 |
| pytorch-forecasting | [sktime/pytorch-forecasting](https://github.com/sktime/pytorch-forecasting) | [MIT LICENSE](libraries/pytorch-forecasting/LICENSE) | 原版权声明：pytorch-forecasting developers、Jan Beitner，以及文件内声明 |
| darts | [unit8co/darts](https://github.com/unit8co/darts) | [Apache-2.0 LICENSE](libraries/darts/LICENSE) | 原源码声明、项目引用与文档 |

## Informer2020 的许可证标注差异

导入提交中的 `LICENSE` 正文是 Apache License 2.0，但原 README 顶部的徽章写着 `CC BY-NC-SA`。两份上游文件均原样保留；这里如实记录差异，没有替原作者消除或改写该差异。具体使用与再分发应结合原文件内容；需要确定授权范围时，以原作者的澄清为准。

## 固定版本与后续修改

每个上游提交、原始文件的 Git blob SHA-1 和文件模式列在 [sources.lock.json](sources.lock.json)。来源与导入范围见 [来源记录](docs/upstream-sources.md)。第三方源码发生后续修改时，保留适用的原许可证和声明，并在修改记录中写清来源及改动。

Pyraformer 的可选 `pyraformer/tvm` gitlink 仅记录提交，不包含其依赖源码；该依赖不在本次第三方源码导入范围内。各项目引用的外部数据集、预训练权重与后续另行安装的依赖分别遵循其自己的条款。

neuralforecast 的 `THIRD_PARTY_LICENSES.md` 列出了另行安装的依赖许可证，其中 `mlstm_kernels` 标注为 NXAI Community License Agreement。该依赖清单原样保留，不将依赖许可证改写为仓库主许可证，也未在本次源码快照中额外打包这些依赖。
