# 基线运行与实验对齐

以下命令按首次整理版本的源码核对。当前锁定提交见[版本状态](upstream-status.md)；自动同步更新源码后，参数和环境以该提交的原 README、解析器及脚本为准。

[返回首页](../README.md) · [源码导航](model-guide.md)

本仓库已整理六个独立模型项目，以及完整的 Time-Series-Library 多模型实验库。本页命令经过源码参数和路径核对，尚未安装环境、下载外部数据或执行模型训练；训练效果与依赖兼容性需在对应环境中验证。

## 1. 分别建立环境

六个模型项目和一个实验库保留各自的导入方式、相对路径和依赖文件。每个项目使用独立环境，并在它自己的目录内执行命令。Time-Series-Library 是一个包含多种模型和任务的代码库，应与六个独立基线分别管理。

| 模型 | 上游声明的 Python / PyTorch | 本次快照中的依赖文件 | 需要留意 |
| --- | --- | --- | --- |
| EMAformer | Python 3.8；README 写 PyTorch ≥ 2.0.0，依赖固定为 2.0.0 | [requirements.txt](../baselines/EMAformer/requirements.txt) | NumPy 1.23.5、pandas 1.5.3、scikit-learn 1.2.2；README 另写 CUDA ≥ 12.0，实际 PyTorch 包与驱动组合需单独确认 |
| Pyraformer | Python 3.7 / PyTorch 1.8.0；README 使用 Ubuntu / CUDA 11.1 | [requirements.txt](../baselines/Pyraformer/requirements.txt) | NumPy 1.21.2、pandas 1.3.3；TVM 为可选路径，见下文 |
| Informer2020 | Python 3.6 / PyTorch 1.8.0 | [requirements.txt](../baselines/Informer2020/requirements.txt)、[environment.yml](../baselines/Informer2020/environment.yml) | NumPy 1.19.4、pandas 0.25.1、scikit-learn 0.21.3；属于旧环境 |
| Autoformer | README 写 Python 3.6 / PyTorch 1.9.0 | [requirements.txt](../baselines/Autoformer/requirements.txt) | 该文件没有固定版本，也没有单列 `torch`，但列了 `torchvision`；应明确记录实际安装的 torch / torchvision 配对版本 |
| ETSformer | Python 3.8 / PyTorch 1.11.0 | [requirements.txt](../baselines/ETSformer/requirements.txt) | pandas 1.4.2、scikit-learn 1.0.2、SciPy 1.7.3、einops 0.4.1；NumPy 未固定版本。指数平滑模块用 SciPy 的 `next_fast_len` 选择变换长度，用 `torch.fft` 执行 FFT，并使用 einops |
| Time-LLM | Python 3.11 / PyTorch 2.2.2 | [requirements.txt](../baselines/Time-LLM/requirements.txt) | accelerate 0.28.0、DeepSpeed 0.14.0、transformers 4.31.0、peft 0.4.0、sentencepiece 0.2.0；还需独立获取预训练语言模型权重与 tokenizer |
| Time-Series-Library（实验库） | README 建议 Python 3.11 / PyTorch 2.5.1 | [requirements.txt](../libraries/Time-Series-Library/requirements.txt) | NumPy 2.1.2、pandas 2.3.3、transformers 4.57.3 等，与 Time-LLM 的依赖明显不同；PyTorch 需另行匹配安装，部分模型还需专用包和预训练权重 |

进入项目目录并激活其独立环境后，再使用该目录下的 `requirements.txt`。不要把七份依赖拼在一起安装。后续成功运行后，保存实际的 Python、PyTorch、CUDA、依赖版本和设备信息，形成自己的环境记录。

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
| Time-LLM | `baselines/Time-LLM/dataset/ETT-small/ETTh1.csv` | `--root_path ./dataset/ETT-small/ --data_path ETTh1.csv` |
| Time-Series-Library（实验库） | `libraries/Time-Series-Library/dataset/ETT-small/ETTh1.csv` | `--root_path ./dataset/ETT-small/ --data_path ETTh1.csv` |

可以改 `root_path` 指向同一份本地数据，避免重复存储。先确认 CSV 的时间列、变量列、顺序与对应加载器一致；原版模型需要的完整外部数据集并未随源码一起收集。Pyraformer 原仓库自带的 `data/app_zone_rpc_hour_encrypted.zip` 已按原样保留，它与 ETT 数据不同。

## 3. 六个独立模型的 ETTh1 入口示例

以下每个代码块都从研究仓库根目录开始。它们用于定位原版流程，参数来自对应解析器与上游脚本；各命令的预测长度、预训练资源和默认训练策略不同，不能直接用输出做公平排名。

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

原版长预测脚本：[scripts/Pyraformer_LR.sh](../baselines/Pyraformer/scripts/Pyraformer_LR.sh)；单步预测脚本：[scripts/Pyraformer_SS.sh](../baselines/Pyraformer/scripts/Pyraformer_SS.sh)。原 README 提到的 `scripts/Pyraformer_LR_FC.sh` 在此上游快照中不存在，应使用实际文件 `scripts/Pyraformer_LR.sh`。注意 Pyraformer 的参数使用单短横线，如 `-input_size`；其余项目使用双短横线。

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

### Time-LLM

原版 ETTh1 脚本会执行多组实验，默认使用 **8 个 GPU 进程、bf16、32 层 Llama**。下面给出对应第一组实验的展开命令，用于明确实际启动入口；运行前需按自己的 GPU 数量、bf16 支持、可用显存和预训练模型修改配置。

```bash
cd baselines/Time-LLM
accelerate launch --multi_gpu --mixed_precision bf16 --num_processes 8 --main_process_port 97 run_main.py --task_name long_term_forecast --is_training 1 --root_path ./dataset/ETT-small/ --data_path ETTh1.csv --model_id ETTh1_512_96 --model TimeLLM --data ETTh1 --features M --seq_len 512 --label_len 48 --pred_len 96 --factor 3 --enc_in 7 --dec_in 7 --c_out 7 --des Exp --itr 1 --d_model 32 --d_ff 128 --batch_size 24 --learning_rate 0.01 --llm_model LLAMA --llm_dim 4096 --llm_layers 32 --train_epochs 100 --model_comment TimeLLM-ETTh1
```

原版脚本：[scripts/TimeLLM_ETTh1.sh](../baselines/Time-LLM/scripts/TimeLLM_ETTh1.sh)。[run_main.py](../baselines/Time-LLM/run_main.py) 主动创建 `Accelerator` 与 `DeepSpeedPlugin`，读取当前目录下的 [ds_config_zero2.json](../baselines/Time-LLM/ds_config_zero2.json)；后者启用 bf16 和 ZeRO stage 2。只改启动命令的精度或进程数，并不等于同步改好了内部 DeepSpeed 配置。Windows 上建议先为这套分布式依赖选择可支持的 Linux/WSL 环境，再验证运行。

[models/TimeLLM.py](../baselines/Time-LLM/models/TimeLLM.py) 中固定了三种 Hugging Face 模型标识：`huggyllama/llama-7b`、`openai-community/gpt2`、`google-bert/bert-base-uncased`。模型权重和 tokenizer 不包含在此仓库中，代码会先查本地缓存，缺失时尝试联网下载；配置本身也通过 `from_pretrained` 读取。需准备对应模型访问权限、磁盘缓存和运行内存，并遵守相应权重的许可条件。切换骨干要配套修改 `--llm_model` 与 `--llm_dim`，如 GPT2/768 或 BERT/768，同时核对 `--llm_layers` 与所用模型配置。冻结语言模型参数仍然需要加载权重并执行前向和相关反向传播，不能据此直接判断显存需求。

提示文本位于 `dataset/prompt_bank/`，ETT 任务读取 [ETT.txt](../baselines/Time-LLM/dataset/prompt_bank/ETT.txt)，这也要求从 Time-LLM 目录运行。原版 `run_main.py` 在结尾调用 `del_files('./checkpoints')`，其实现是删除整个目录；需要保留实验检查点时，先在自己的工作副本中修改该清理逻辑，再启动长时间实验。此处的原版快照保持原样。

另外，`run_main.py` 在构建模型后才设置 `args.content`，而模型在 `--prompt_domain 1` 时会在初始化阶段读取该字段。使用领域提示前，需在自己的运行副本中将内容加载提前到模型构造之前；默认 `--prompt_domain 0` 不走这条读取分支。

## 4. Time-Series-Library 多任务实验库

### 单独进入库目录运行

下面使用库内的 DLinear 做一次 ETTh1 长期预测入口示例，完整原版参数来源为 [DLinear_ETTh1.sh](../libraries/Time-Series-Library/scripts/long_term_forecast/ETT_script/DLinear_ETTh1.sh)。原脚本设置 GPU 2，以下 Python 命令不包含这个环境变量。

```bash
cd libraries/Time-Series-Library
python -u run.py --task_name long_term_forecast --is_training 1 --root_path ./dataset/ETT-small/ --data_path ETTh1.csv --model_id ETTh1_96_96 --model DLinear --data ETTh1 --features M --seq_len 96 --label_len 48 --pred_len 96 --e_layers 2 --d_layers 1 --factor 3 --enc_in 7 --dec_in 7 --c_out 7 --des Exp --itr 1
```

这份库中包含 Autoformer、Informer、Pyraformer、ETSformer 等实现，但它们与 `baselines/` 下各自原仓库的版本、参数和训练流程分别维护。比较结果时记录使用的是哪一份实现。

### 按任务查找

[run.py](../libraries/Time-Series-Library/run.py) 根据 `--task_name` 选择实验类，实际分支比其参数帮助文本更完整：

| 任务参数 | 实验类文件 | 上游脚本位置 |
| --- | --- | --- |
| `long_term_forecast` | [exp_long_term_forecasting.py](../libraries/Time-Series-Library/exp/exp_long_term_forecasting.py) | [scripts/long_term_forecast/](../libraries/Time-Series-Library/scripts/long_term_forecast/) |
| `short_term_forecast` | [exp_short_term_forecasting.py](../libraries/Time-Series-Library/exp/exp_short_term_forecasting.py) | [scripts/short_term_forecast/](../libraries/Time-Series-Library/scripts/short_term_forecast/)；包含 M4 脚本 |
| `imputation` | [exp_imputation.py](../libraries/Time-Series-Library/exp/exp_imputation.py) | [scripts/imputation/](../libraries/Time-Series-Library/scripts/imputation/) |
| `anomaly_detection` | [exp_anomaly_detection.py](../libraries/Time-Series-Library/exp/exp_anomaly_detection.py) | [scripts/anomaly_detection/](../libraries/Time-Series-Library/scripts/anomaly_detection/) |
| `classification` | [exp_classification.py](../libraries/Time-Series-Library/exp/exp_classification.py) | [scripts/classification/](../libraries/Time-Series-Library/scripts/classification/) |
| `zero_shot_forecast` | [exp_zero_shot_forecasting.py](../libraries/Time-Series-Library/exp/exp_zero_shot_forecasting.py) | [LTSM.sh](../libraries/Time-Series-Library/scripts/long_term_forecast/ETT_script/LTSM.sh)；需模型对应的权重/依赖 |

外生变量预测脚本另集中在 [scripts/exogenous_forecast/](../libraries/Time-Series-Library/scripts/exogenous_forecast/)，应查看具体脚本内使用的任务与特征参数。每种模型并不一定实现上述全部任务，需核查其 `forward` 的任务分支与对应脚本。

### 查模型、添加模型与数据

- 模型实现在 [models/](../libraries/Time-Series-Library/models/)。当前快照的 [exp/exp_basic.py](../libraries/Time-Series-Library/exp/exp_basic.py) 自动扫描此目录的 `.py` 文件，并通过 `LazyModelDict` 按需导入。添加个人模型时提供 `Model` 类（或与模块同名的类），符合所选实验类的构造与 `forward` 接口，再用 `--model 文件名去掉.py` 选择；此版本无需手写一个统一 `model_dict` 注册项。
- 数据映射在 [data_provider/data_factory.py](../libraries/Time-Series-Library/data_provider/data_factory.py) 的 `data_dict`，加载器在 [data_provider/data_loader.py](../libraries/Time-Series-Library/data_provider/data_loader.py)。新增数据要登记相应类型，并处理所用任务的批处理格式；分类与异常检测的数据组织与 ETT CSV 不同。
- 模型额外依赖以所选模块和上游说明为准。例如 Mamba 需 `mamba_ssm` 的适配环境，上游给出的安装包是 Linux/CUDA 版本；Moirai 需另装 `uni2ts`。大时序模型的 zero-shot 评估还可能下载预训练权重。库内模型源码齐全不代表这些外部包、权重和数据已随源码下载。

## 5. 建立自己的公平比较

建议先选同一份 ETTh1 文件，记录其校验值，确定一套实验协议，再逐一接入需要比较的模型。Time-LLM 使用预训练语言模型时，还要记录骨干、权重版本、预训练来源和实际使用层数，与从头训练模型的资源条件一起报告。

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

参数名称不能简单等同：多数项目用 `seq_len` / `pred_len`，Pyraformer 用 `input_size` / `predict_step`。入口也有不同默认种子和重复次数，例如 EMAformer 固定种子 2023，Autoformer 固定种子 2021；ETSformer 第 `ii` 次重复分别使用 `ii`、`ii + 1`、`ii + 2` 作为 Python、NumPy、PyTorch 种子。Time-LLM 的 `run_main.py` 虽有 `--seed` 参数，但本次快照实际初始化使用的是前面写定的 `fix_seed = 2021`。这些原始脚本没有自动统一种子设置。

建议每次实验建立单独编号，把配置、命令、环境、日志索引和结果放到自己的实验记录目录；先完成一个原版基线的运行与评估核对，再比较个人改进和消融实验。查找具体修改位置见[源码导航](model-guide.md)。
