# 数据索引

这里记录公共数据来源、文件版本和划分约定。将本地大数据放到 `data/raw/` 或 `data/processed/`；两者已加入忽略规则。六个独立项目与 TSLib 仍使用各自的数据路径参数，根目录中的数据不会自动被它们发现。

## ETT 路径对照

| 模型 | 从模型目录运行时，原 ETTh1 脚本使用的数据文件 |
| --- | --- |
| EMAformer | `dataset/ETT-small/ETTh1.csv` |
| Pyraformer | `data/ETT/ETTh1.csv` |
| Informer2020 | `data/ETT/ETTh1.csv` |
| Autoformer | `dataset/ETT-small/ETTh1.csv` |
| ETSformer | `dataset/ETT-small/ETTh1.csv`（按运行指南显式设置；原脚本提供 ETTm2 示例） |
| Time-LLM | `dataset/ETT-small/ETTh1.csv` |
| Time-Series-Library | `dataset/ETT-small/ETTh1.csv`（相对于库目录） |

ETT 来源：[zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset)。其他数据的上游下载入口保留在各项目原 README 中。下载后可通过各入口的路径参数指向同一份本地数据，详见[运行指南](../docs/running-baselines.md)。

Time-LLM 的 `dataset/prompt_bank/` 是上游提供的文本提示资源，随源码保留；它与训练 CSV 分别管理。TSLib 的预测、插补、分类和异常检测使用不同加载器及数据格式，任务入口见[模型与任务索引](../docs/model-catalog.md)。外部语言模型或大型时间序列模型的权重按对应模型加载要求另行缓存。

## 每份数据建议记录

| 字段 | 内容 |
| --- | --- |
| 名称与版本 | 数据集名称、下载日期、文件名及 SHA-256 |
| 来源与使用条件 | 原始链接、许可或访问要求 |
| 时间范围与采样间隔 | 起止日期、频率、是否存在断点 |
| 字段 | 时间列、目标列、输入变量、单位 |
| 划分 | 训练、验证、测试的边界 |
| 预处理 | 缺失值、异常值、重采样、标准化及拟合范围 |

Pyraformer 上游自带的 `baselines/Pyraformer/data/app_zone_rpc_hour_encrypted.zip` 作为原始快照保留；本次没有额外下载训练数据。
