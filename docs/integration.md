# 统一研究与实验流程

## 已整合的内容

模型目录按建模机制组织，点击名称先读中文介绍，再选具体实现。187 个模型家族和 326 个实现进入同一个注册表，可按名称、分类查找，不依赖安装所有模型环境。

实验层提供统一 CSV、时间划分、预测窗口、指标和结果文件。当前已实际接通以下五种方法；它们共享同一协议。

| 方法 | 执行方式 | 接入内容 |
| --- | --- | --- |
| NaiveMean | `reference` | 工作区参考实现，用训练段均值预测 |
| NaiveSeasonal | `reference` | 工作区参考实现，重复窗口末尾的季节周期 |
| NaiveDrift | `reference` | 工作区参考实现，外推当前历史窗口首尾斜率 |
| DLinear | `torch_source` | 加载本地锁定原始模型，统一切窗、训练和预测 |
| TSMixer | `torch_source` | 加载本地锁定原始模型，统一切窗、训练和预测 |

其余模型已整合介绍和源码注册信息，运行适配需要逐个补充。模型分类地位相同；运行适配进度单独记录。

## 快速使用

在仓库根目录执行。浏览模型只用 Python 标准库；统一实验需 NumPy，原始神经模型另需 PyTorch。

```bash
python -m pip install -r requirements-workspace.txt
python -m pip install torch
python -m zpbts list --category linear_mlp
python -m zpbts show DLinear
python -m zpbts run examples/forecasting/configs/dlinear.json --output experiments/local/dlinear
python -m zpbts run examples/forecasting/configs/tsmixer.json --output experiments/local/tsmixer
python -m zpbts compare experiments/local/dlinear experiments/local/tsmixer
```

配置中的数据路径相对于配置文件。输出目录须为空，以免覆盖已有实验。每个来源在隔离子进程中加载，避免不同实现的 `models`、`layers`、`utils` 顶层包互相串用。

## 配置协议

```json
{
  "schema_version": 1,
  "model": "DLinear",
  "adapter": "torch_source",
  "data": {
    "path": "../synthetic.csv",
    "time_column": "date",
    "columns": ["signal", "trend"],
    "train_end": 120,
    "test_start": 144
  },
  "evaluation": {"lookback": 24, "horizon": 12, "stride": 12, "mase_period": 24},
  "options": {"epochs": 5, "batch_size": 32, "seed": 7, "device": "cpu"}
}
```

训练段是行区间 $`[0,T_{\mathrm{train}})`$，测试从 $`T_{\mathrm{test}}`$ 开始，要求 $`L\leq T_{\mathrm{train}}\leq T_{\mathrm{test}}<T`$。神经模型训练段至少包含 $`L+H`$ 行。测试起点集合为

```math
\mathcal{O}=\left\{T_{\mathrm{test}}+ks:\ k\in\mathbb{Z}_{\geq0},\ T_{\mathrm{test}}+ks+H\leq T\right\}.
```

每个起点 $`o`$ 的输入为 $`[o-L,o)`$，目标为 $`[o,o+H)`$。模型只在训练段拟合一次；后续起点允许读取当时已观测的测试历史，参数保持固定。这是滚动历史预测协议。预留验证段仅作为历史观测，不参与拟合；本版采用固定 epoch，尚未加入早停和自动调参。

训练标准化逐变量使用训练段均值、标准差，常数列缩放设为 1。输出恢复到原始单位后评价。CSV 必须是严格递增、无重复的 ISO 8601 时间及有限数值；缺失值需预先处理。

输入窗、预测窗和季节周期均以数据行数计。程序检查时间顺序，但不自动重采样；需要固定时间间隔的任务应先将数据整理到统一频率。

`torch_source` 支持 `epochs`、`batch_size`、`learning_rate`、`seed`、`device`、`moving_avg`、`d_model`、`e_layers`、`dropout`、`threads`、`timeout_seconds`、`python_executable`、`source_directory`。默认 CPU；可指定单个 `cuda:0`。当前固定来源为 `_sources/source-07`。DLinear 使用共享通道线性层，`moving_avg` 须正奇数；TSMixer 使用 `d_model`、`e_layers`、`dropout`。完整默认值见 [适配器](../zpbts/adapters.py)。

## 指标定义

令 $`e_i=\hat{y}_i-y_i`$。用 $`K`$ 表示测试起点数，$`H`$ 表示预测步数，$`C`$ 表示目标变量数，总评价数量为 $`N=KHC`$，即对所有起点、预测步和变量等权聚合。

```math
\mathrm{MAE}=\frac{1}{N}\sum_{i=1}^{N}\left|e_i\right|.
```

```math
\mathrm{MSE}=\frac{1}{N}\sum_{i=1}^{N}e_i^2,\qquad
\mathrm{RMSE}=\sqrt{\mathrm{MSE}}.
```

```math
\mathrm{sMAPE}=\frac{100}{N}\sum_{i=1}^{N}\frac{2\left|e_i\right|}{\left|y_i\right|+\left|\hat{y}_i\right|}.
```

分母同时为零的项记作零。对第 $`c`$ 个变量，以配置中的周期 $`m`$ 计算训练段标尺：

```math
d_c=\frac{1}{T_{\mathrm{train}}-m}\sum_{t=m}^{T_{\mathrm{train}}-1}\left|y_{t,c}-y_{t-m,c}\right|.
```

再对所有测试起点、预测步和变量求平均：

```math
\mathrm{MASE}=\frac{1}{KHC}\sum_{o\in\mathcal{O}}\sum_{h=1}^{H}\sum_{c=1}^{C}\frac{\left|\hat{y}_{o,h,c}-y_{o,h,c}\right|}{d_c}.
```

这里 $`y_{o,h,c}`$ 表示从起点 $`o`$ 预测的第 $`h`$ 步、第 $`c`$ 个变量的真实值。任一变量的 $`d_c=0`$ 时总体 MASE 记为 `null`，避免把无定义值伪装成零。逐变量、逐预测步指标也保存在结果中。不同变量的单位差异会影响 MAE/MSE 的总体值，阅读时同时看逐变量结果。

## 结果与公平比较

每次输出：

- `config.json`：保留参数，数据路径重定位，可再次运行。
- `metrics.json`：指标、数据协议指纹、模型实现和提交、训练种子、软件版本、归一化参数、训练窗口数、优化步数、逐轮损失。
- `predictions.csv`：预测时刻、目标时刻、预测步、变量、真值与预测值。

`compare` 逐项核对整个评价协议，不同数据文件、变量顺序、划分、窗口、步长、MASE 周期或预测起点均拒绝混排。训练预算和种子随结果保留，正式研究还应自行固定预算、设计消融及重复运行。

结果中的 `fit_seconds` 记录整个适配器调用，包含子进程启动、来源校验、训练和全部预测，不能当作纯训练耗时比较。

## 添加自己的改进

1. 在 `research/models/` 写新模块，保留原始实现供对照。
2. 在 `zpbts/adapters.py` 增加适配：输入训练段和历史窗口，输出原尺度的 `[起点数, 预测步, 变量数]` 数组。
3. 训练状态只能从训练段得到，并返回来源、配置和诊断信息。
4. 复用现有配置、预测导出和指标，不另写一套口径。
5. 用未来目标扰动测试检查泄漏，再做多种子和消融实验。

[示例与实测结果](../examples/forecasting/README.md) · [模型目录](model-catalog.md)
