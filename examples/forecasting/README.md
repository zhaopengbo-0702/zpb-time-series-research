# 统一预测实验示例

本示例使用人工生成的两变量、192 行小时序列：一个带缓慢漂移的日周期信号，以及一个叠加半日周期的线性趋势。数据公开在 [synthetic.csv](synthetic.csv)，便于直接检查整个流程。

## 运行

在仓库根目录安装 NumPy；运行 DLinear 和 TSMixer 时还需 PyTorch。配置和数据已经准备好：

```bash
python -m pip install -r requirements-workspace.txt
python -m pip install torch
python -m zpbts run examples/forecasting/configs/naiveseasonal.json --output experiments/local/seasonal
python -m zpbts run examples/forecasting/configs/dlinear.json --output experiments/local/dlinear
python -m zpbts run examples/forecasting/configs/tsmixer.json --output experiments/local/tsmixer
python -m zpbts compare experiments/local/seasonal experiments/local/dlinear experiments/local/tsmixer
```

其他两个配置为 [NaiveMean](configs/naivemean.json) 和 [NaiveDrift](configs/naivedrift.json)。每次使用空输出目录。

## 已运行结果

五个方法使用相同数据与评价协议：前 120 行拟合，120—143 行留作验证区间，测试从第 144 行开始；历史窗 24、预测窗 12、步长 12、MASE 周期 24。模型只拟合一次，测试采用逐起点可见历史。两个神经模型各训练 5 个 epoch、种子 7、CPU。

本地实测环境为 Python 3.9.12、NumPy 1.26.4、PyTorch 2.7.0+cpu。表中误差以原始单位计算。

| 方法 | MAE | RMSE |
| --- | ---: | ---: |
| NaiveSeasonal | 0.300000 | 0.349857 |
| DLinear | 0.562757 | 0.636440 |
| NaiveDrift | 0.568977 | 0.736988 |
| TSMixer | 1.137976 | 1.426294 |
| NaiveMean | 1.436432 | 1.660841 |

该人工数据具有稳定周期，因此季节重复方法表现较好。这里验证的是统一训练和评价管道；五轮训练的单个合成数据结果不用于判定模型的研究表现。

每个结果目录均有配置、完整指标与逐点预测：

- [NaiveMean](https://github.com/zhaopengbo-0702/zpb-time-series-research/tree/main/examples/forecasting/results/naivemean)
- [NaiveSeasonal](https://github.com/zhaopengbo-0702/zpb-time-series-research/tree/main/examples/forecasting/results/naiveseasonal)
- [NaiveDrift](https://github.com/zhaopengbo-0702/zpb-time-series-research/tree/main/examples/forecasting/results/naivedrift)
- [DLinear](https://github.com/zhaopengbo-0702/zpb-time-series-research/tree/main/examples/forecasting/results/dlinear)
- [TSMixer](https://github.com/zhaopengbo-0702/zpb-time-series-research/tree/main/examples/forecasting/results/tsmixer)
- [完整比较表](results/comparison.md)

神经模型记录真实源码路径及提交、训练窗口数、优化步数、每轮损失与训练段归一化参数。公开记录将本机解释器和模型文件的绝对路径改成可移植名称；数值结果保持实测值。发布前运行时工作树有改动，故环境信息保留原 HEAD、dirty 标记及实际工作区代码 SHA-256。

## 检验方式

```bash
python -m unittest discover -s tests -v
python tools/verify_sources.py --strict
```

测试包括真实源码训练、改变预测上下文不改变训练统计、未来目标不参与首个预测、验证区间不参与拟合、从预测 CSV 重算指标，以及不同评价协议拒绝混排。没有 PyTorch 时会跳过真实训练测试。

[统一协议与指标公式](../../docs/integration.md)
