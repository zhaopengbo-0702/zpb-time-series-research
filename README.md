# zpb-time-series-research

个人时间序列预测研究工作区，集中整理 **EMAformer、Pyraformer、Informer2020、Autoformer、ETSformer** 五份上游源码，便于阅读、对比和开展改进实验。

## 从这里开始

| 想做什么 | 去哪里 |
| --- | --- |
| 查模型、注意力、嵌入、数据加载代码 | [五模型源码导航](docs/model-guide.md) |
| 查环境、数据位置和训练命令 | [运行指南](docs/running-baselines.md) |
| 查上游版本、导入范围和来源校验 | [来源记录](docs/upstream-sources.md) · [版本锁定清单](sources.lock.json) |
| 写自己的模型和改进思路 | [研究工作区](research/README.md) |
| 记录配置、消融实验与结果 | [实验管理](experiments/README.md) |
| 整理数据来源、划分和预处理 | [数据索引](data/README.md) |

## 五个基线

| 模型 | 主要思路 | 原版源码 | 核心模型 | 训练入口 | 论文 / 上游 |
| --- | --- | --- | --- | --- | --- |
| EMAformer | 用通道、相位及联合嵌入增强变量之间的建模 | [EMAformer](baselines/EMAformer/) | [model/EMAformer.py](baselines/EMAformer/model/EMAformer.py) | [run.py](baselines/EMAformer/run.py) | [论文](https://arxiv.org/abs/2511.08396) · [上游](https://github.com/PlanckChang/EMAformer) |
| Pyraformer | 金字塔式多尺度结构与稀疏注意力 | [Pyraformer](baselines/Pyraformer/) | [Pyraformer_LR.py](baselines/Pyraformer/pyraformer/Pyraformer_LR.py) · [Pyraformer_SS.py](baselines/Pyraformer/pyraformer/Pyraformer_SS.py) | [长预测](baselines/Pyraformer/long_range_main.py) · [单步预测](baselines/Pyraformer/single_step_main.py) | [论文](https://openreview.net/forum?id=0EXmFzUn5I) · [上游](https://github.com/ant-research/Pyraformer) |
| Informer2020 | ProbSparse 注意力、编码器蒸馏及生成式解码 | [Informer2020](baselines/Informer2020/) | [models/model.py](baselines/Informer2020/models/model.py) | [main_informer.py](baselines/Informer2020/main_informer.py) | [论文](https://arxiv.org/abs/2012.07436) · [上游](https://github.com/zhouhaoyi/Informer2020) |
| Autoformer | 趋势与季节分解，加上基于时延的 Auto-Correlation | [Autoformer](baselines/Autoformer/) | [models/Autoformer.py](baselines/Autoformer/models/Autoformer.py) | [run.py](baselines/Autoformer/run.py) | [论文](https://arxiv.org/abs/2106.13008) · [上游](https://github.com/thuml/Autoformer) |
| ETSformer | 指数平滑与频率注意力，分解水平、增长与季节项 | [ETSformer](baselines/ETSformer/) | [models/etsformer/model.py](baselines/ETSformer/models/etsformer/model.py) | [run.py](baselines/ETSformer/run.py) | [论文](https://arxiv.org/abs/2202.01381) · [上游](https://github.com/azkanaon/etsformer) |

按技术主题查找时：嵌入设计先看 EMAformer，多尺度结构先看 Pyraformer，稀疏注意力先看 Informer，分解与周期聚合先看 Autoformer，指数平滑与频率建模先看 ETSformer。它们是分别固定版本的源码快照；Autoformer 自带的其他基线也保留在其原目录内。

## 目录结构

```text
zpb-time-series-research/
├── baselines/                 # 五份原始源码，保留原文件名与目录
│   ├── EMAformer/
│   ├── Pyraformer/
│   ├── Informer2020/
│   ├── Autoformer/
│   └── ETSformer/
├── docs/                      # 源码导航、运行指南、来源记录
├── research/
│   ├── models/                # 自己的模型和改动说明
│   └── notes/                 # 论文笔记、想法和代码阅读记录
├── experiments/
│   ├── templates/             # 可复制的实验记录模板
│   └── results/               # 小型指标汇总；大文件留在本地
├── data/                      # 数据来源与划分索引
├── tools/verify_sources.py    # 原始源码完整性校验
├── sources.lock.json          # 上游提交、文件哈希与模式
├── LICENSES.md                # 各上游的许可证与署名
└── CHANGELOG.md               # 本研究工作区的变更记录
```

## 获取与使用

```bash
git clone https://github.com/zhaopengbo-0702/zpb-time-series-research.git
cd zpb-time-series-research
python tools/verify_sources.py
```

阅读代码无需安装训练依赖。开始运行时，进入对应的 `baselines/<模型名>/` 目录，按[运行指南](docs/running-baselines.md)分别准备环境与数据；本仓库根目录不提供合并的 `requirements.txt`。

当前已完成五份源码的归档与逐文件来源校验，共 **260 个原始文件**。模型训练和论文指标复现尚未执行。Pyraformer 的可选 TVM gitlink 未包含依赖源码，具体状态见[来源记录](docs/upstream-sources.md)。

后续改进可先在 `research/` 下建立独立版本，通过实验记录保存基线提交、配置和结果。各上游论文的引用条目保留在对应原 README 中；许可证说明见 [LICENSES.md](LICENSES.md)。
