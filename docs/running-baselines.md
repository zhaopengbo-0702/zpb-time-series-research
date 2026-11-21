# 基线运行与实验对齐

[返回首页](../README.md) · [源码导航](model-guide.md)

本仓库已整理五个上游项目的源码快照与入口。本页命令经过源码参数和路径核对，尚未安装环境、下载外部数据或执行模型训练；训练效果与依赖兼容性需在对应环境中验证。

## 1. 分别建立环境

五个项目保留各自的导入方式、相对路径和依赖文件。每个项目使用独立环境，并在它自己的目录内执行命令。

| 模型 | 上游声明的 Python / PyTorch | 本次快照中的依赖文件 | 需要留意 |
| --- | --- | --- | --- |
| EMAformer | Python 3.8；README 写 PyTorch ≥ 2.0.0，依赖固定为 2.0.0 | [requirements.txt](../baselines/EMAformer/requirements.txt) | NumPy 1.23.5、pandas 1.5.3、scikit-learn 1.2.2；README 另写 CUDA ≥ 12.0，实际 PyTorch 包与驱动组合需单独确认 |
| Pyraformer | Python 3.7 / PyTorch 1.8.0；README 使用 Ubuntu / CUDA 11.1 | [requirements.txt](../baselines/Pyraformer/requirements.txt) | NumPy 1.21.2、pandas 1.3.3；TVM 为可选路径，见下文 |
| Informer2020 | Python 3.6 / PyTorch 1.8.0 | [requirements.txt](../baselines/Informer2020/requirements.txt)、[environment.yml](../baselines/Informer2020/environment.yml) | NumPy 1.19.4、pandas 0.25.1、scikit-learn 0.21.3；属于旧环境 |
| Autoformer | README 写 Python 3.6 / PyTorch 1.9.0 | [requirements.txt](../baselines/Autoformer/requirements.txt) | 该文件没有固定版本，也没有单列 `torch`，但列了 `torchvision`；应明确记录实际安装的 torch / torchvision 配对版本 |
| ETSformer | Python 3.8 / PyTorch 1.11.0 | [requirements.txt](../baselines/ETSformer/requirements.txt) | pandas 1.4.2、scikit-learn 1.0.2、SciPy 1.7.3、einops 0.4.1；NumPy 未固定版本。指数平滑模块直接使用 SciPy FFT 和 einops |

进入模型目录并激活其独立环境后，再使用该目录下的 `requirements.txt`。不要把五份依赖拼在一起安装。后续成功运行后，保存实际的 Python、PyTorch、CUDA、依赖版本和设备信息，形成自己的环境记录。

下文的 `python` 命令为单行形式，可在已激活环境的 PowerShell 或 Bash 中执行。上游 `.sh` 脚本使用 Bash 语法，Windows 可通过 WSL 或 Git Bash 运行；脚本可能设置特定 GPU 编号并连续执行多组实验，运行前先检查内容。Pyraformer 的可选 `.so` 文件为 Linux/CUDA 编译产物。

## 2. 准备 ETT 数据

ETT 原始来源：[zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset)。本仓库没有自动下载 ETT。下表第二列相对于研究仓库根目录，第三列中的参数路径相对于各自模型目录。

| 模型 | ETTh1 文件位置 | 对应命令参数 |
| --- | --- | --- |
| EMAformer | `baselines/EMAformer/dataset/ETT-small/ETTh1.csv` | `--root_path ./dataset/ETT-small/ --data_path ETTh1.csv` |
| Pyraformer | `baselines/Pyraformer/data/ETT/ETTh1.csv` | `-root_path ./data/ETT/ -data_path ETTh1.csv` |
| Informer2020 | `baselines/Informer2020/data/ETT/ETTh1.csv` | `--root_path ./data/ETT/ --data_path ETTh1.csv` |
| Autoformer | `baselines/Autoformer/dataset/ETT-small/ETTh1.csv` | `--root_path ./dataset/ETT-small/ --data_path ETTh1.csv` |
| ETSformer | `baselines/ETSformer/dataset/ETT-small/ETTh1.csv` | `--root_path ./dataset/ETT-small/ --data_path ETTh1.csv` |

可以改 `root_path` 指向同一份本地数据，避免重复存储。先确认 CSV 的时间列、变量列、顺序与对应加载器一致；原版模型需要的完整外部数据集并未随源码一起收集。Pyraformer 原仓库自带的 `data/app_zone_rpc_hour_encrypted.zip` 已按原样保留，它与 ETT 数据不同。

## 3. 五个 ETTh1 入口示例

以下每个代码块都从研究仓库根目录开始。它们用于定位原版流程，参数来自对应解析器与上游脚本；五条命令的预测长度和默认训练策略不同，不能直接用输出做公平排名。

### EMAformer

```bash
cd baselines/EMAformer
python -u run.py --is_training 1 --root_path ./dataset/ETT-small/ --data_path ETTh1.csv --model_id ETTh1_96_96 --model EMAformer --data ETTh1 --features M --seq_len 96 --pred_len 96 --e_layers 3 --enc_in 7 --dec_in 7 --c_out 7 --des Exp --d_model 256 --n_heads 4 --d_ff 256 --output_proj_dropout 0.3 --itr 1 --cycle 24
```

完整原版脚本：[EMAformer_ETTh1.sh](../baselines/EMAformer/scripts/multivariate_forecasting/ETT/EMAformer_ETTh1.sh)。其他数据集脚本在 `scripts/multivariate_forecasting/`，周期参数 `cycle` 也需随任务设定。

### Pyraformer

```bash
cd baselines/Pyraformer
python long_range_main.py -data ETTh1 -root_path ./data/ETT/ -data_path ETTh1.csv -input_size 168 -predict_step 168 -n_head 6 -iter_num 1
```

原版长预测脚本：[scripts/Pyraformer_LR.sh](../baselines/Pyraformer/scripts/Pyraformer_LR.sh)；单步预测脚本：[scripts/Pyraformer_SS.sh](../baselines/Pyraformer/scripts/Pyraformer_SS.sh)。原 README 提到的 `scripts/Pyraformer_LR_FC.sh` 在此上游快照中不存在，应使用实际文件 `scripts/Pyraformer_LR.sh`。注意 Pyraformer 的参数使用单短横线，如 `-input_size`；其他四项目使用双短横线。

`-use_tvm` 默认关闭，示例沿用普通 PyTorch 路径。上游 Git 树另外引用了 `pyraformer/tvm`，提交为 `1fac10b359dec1bd6ad45ce36541a882aaba586b`，但没有 `.gitmodules` 提供远程地址，因此该可选依赖的内容未包含在此快照中。不能通过此仓库的 `git submodule update --init` 自动恢复它。需要启用 TVM 时，应先核实原上游的获取和编译方式，再单独配置。

### Informer2020

```bash
cd baselines/Informer2020
python -u main_informer.py --model informer --data ETTh1 --root_path ./data/ETT/ --data_path ETTh1.csv --features M --seq_len 48 --label_len 48 --pred_len 24 --e_layers 2 --d_layers 1 --attn prob --des Exp --itr 1 --factor 3
```

完整原版脚本：[scripts/ETTh1.sh](../baselines/Informer2020/scripts/ETTh1.sh)，包含多变量和单变量实验。`--data ETTh1` 会在入口的数据配置表中设置对应文件名和通道数；换自定义数据时需一起核查该配置与加载器。

### Autoformer

```bash
cd baselines/Autoformer
python -u run.py --is_training 1 --root_path ./dataset/ETT-small/ --data_path ETTh1.csv --model_id ETTh1_96_24 --model Autoformer --data ETTh1 --features M --seq_len 96 --label_len 48 --pred_len 24 --e_layers 2 --d_layers 1 --factor 3 --enc_in 7 --dec_in 7 --c_out 7 --des Exp --itr 1
```

完整原版脚本：[scripts/ETT_script/Autoformer_ETTh1.sh](../baselines/Autoformer/scripts/ETT_script/Autoformer_ETTh1.sh)。该原脚本设置 `CUDA_VISIBLE_DEVICES=1`，上面的 Python 入口没有继承这一设置；使用完整脚本前请按实际设备调整。

### ETSformer

```bash
cd baselines/ETSformer
python -u run.py --root_path ./dataset/ETT-small/ --data_path ETTh1.csv --model_id ETTh1_96_96 --model ETSformer --data ETTh1 --features M --seq_len 96 --pred_len 96 --e_layers 2 --d_layers 2 --enc_in 7 --dec_in 7 --c_out 7 --des Exp --K 3 --learning_rate 1e-5 --itr 1
```

此快照没有 ETTh1 专用脚本。以上示例参照实际存在的 [scripts/ETTm2.sh](../baselines/ETSformer/scripts/ETTm2.sh)，将数据名和文件改为加载器支持的 `ETTh1`，并保留原版的模型参数作为入口示例；这组参数未被验证为 ETTh1 的最佳设置。ETSformer 没有 `--is_training` 参数，入口会依次训练、验证和测试。

网格搜索实际入口为 [scripts/grid_search.sh](../baselines/ETSformer/scripts/grid_search.sh)，原 README 的 `./grid_search.sh` 位于错误层级。另外，原始 `scripts/ETTm2_univar.sh` 第一组命令写有 `--pred_len $96`，这会被 Bash 当成变量展开，应在自己的脚本副本中改为明确的数值后使用；原版快照保持原样。

## 4. 建立自己的公平比较

建议先选同一份 ETTh1 文件，记录其校验值，确定一套实验协议，再逐一接入五个模型。

| 项目 | 需要固定和记录的内容 |
| --- | --- |
| 数据划分 | 训练、验证、测试的时间边界；验证/测试窗口可读取的历史上下文；不能让未来信息进入训练或预处理 |
| 数据处理 | 缺失值策略、列顺序、目标变量；归一化统计量仅由训练集拟合；确认各加载器实际行为 |
| 预测任务 | `M` / `S` / `MS`、输入窗、预测长度、输出通道、采样频率；解码器历史长度单独记录 |
| 指标尺度 | MSE / MAE 的具体实现、在归一化尺度还是原始尺度计算、跨样本/通道的聚合方式；核实 `inverse` 的影响 |
| 训练预算 | 批量大小、学习率与调度、训练轮数、早停策略、超参数选择范围及相同的验证规则 |
| 随机性 | Python / NumPy / PyTorch / CUDA / DataLoader 的种子；重复次数；报告均值和波动；固定种子本身不保证完全确定性 |
| 效率测量 | 相同设备与精度、数据加载设置、预热、计时边界、峰值显存，以及输入/输出长度 |
| 版本追踪 | 本仓库提交、所用上游快照、个人改动、完整命令、实际依赖清单及日志位置 |

参数名称不能简单等同：EMAformer、Informer2020、Autoformer、ETSformer 用 `seq_len` / `pred_len`，Pyraformer 用 `input_size` / `predict_step`。入口也有不同默认种子和重复次数，例如 EMAformer 固定种子 2023，Autoformer 固定种子 2021；ETSformer 第 `ii` 次重复分别使用 `ii`、`ii + 1`、`ii + 2` 作为 Python、NumPy、PyTorch 种子。五份原始脚本没有自动统一这些设置。

建议每次实验建立单独编号，把配置、命令、环境、日志索引和结果放到自己的实验记录目录；先完成一个原版基线的运行与评估核对，再比较个人改进和消融实验。查找具体修改位置见[源码导航](model-guide.md)。
