# zpb-time-series-research

个人时间序列研究工作区，将收录的模型逐个展开，按技术路线统一分类。每个模型使用相同的展示字段；同名模型的各个实现入口放在同一行，方便阅读、对比和改进。

收录六个独立项目与六套完整模型库。源码版本和逐文件记录保存在 [sources.lock.json](sources.lock.json)，库的使用与结构见[模型库指南](docs/library-guide.md)。

## 从这里开始

| 想做什么 | 去哪里 |
| --- | --- |
| 按名称查模型，区分原版与库内实现 | [全部模型与任务索引](docs/model-catalog.md) |
| 查模型、注意力、嵌入、数据加载代码 | [源码导航](docs/model-guide.md) |
| 查环境、数据位置和训练命令 | [运行指南](docs/running-baselines.md) |
| 查上游版本、导入范围和来源校验 | [来源记录](docs/upstream-sources.md) · [版本锁定清单](sources.lock.json) |
| 查各模型库的入口、依赖与教程 | [模型库指南](docs/library-guide.md) |
| 写自己的模型和改进思路 | [研究工作区](research/README.md) |
| 记录配置、消融实验与结果 | [实验管理](experiments/README.md) |
| 整理数据来源、划分和预处理 | [数据索引](data/README.md) |

## 全部模型，按技术路线分类

**从[统一模型目录](docs/model-catalog.md)开始**。各来源的公开模型入口合并整理，同名模型以一个条目保留不同实现。下方总数和各分类清单由本地来源清单生成。

<!-- MODEL_CATALOG_START -->

当前 **187 个模型家族**、**326 个实现入口**。每个模型名称直接链接到源码。

| 分类 | 全部模型 |
| --- | --- |
| [线性与MLP](docs/model-catalog.md#category-linear_mlp) | [DecoderMLP](libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp.py) · [DeepNPTS](libraries/neuralforecast/neuralforecast/models/deepnpts.py) · [DLinear](libraries/Time-Series-Library/models/DLinear.py) · [gMLP](libraries/tsai/tsai/models/gMLP.py) · [KAN](libraries/neuralforecast/neuralforecast/models/kan.py) · [LightTS](libraries/Time-Series-Library/models/LightTS.py) · [MLP](libraries/tsai/tsai/models/MLP.py) · [MLPMultivariate](libraries/neuralforecast/neuralforecast/models/mlpmultivariate.py) · [NBEATS](libraries/neuralforecast/neuralforecast/models/nbeats.py) · [NBEATSKAN](libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeatskan.py) · [NBEATSx](libraries/neuralforecast/neuralforecast/models/nbeatsx.py) · [NHITS](libraries/neuralforecast/neuralforecast/models/nhits.py) · [NLinear](libraries/neuralforecast/neuralforecast/models/nlinear.py) · [RMoK](libraries/neuralforecast/neuralforecast/models/rmok.py) · [SOFTS](libraries/neuralforecast/neuralforecast/models/softs.py) · [SOFTSSharp](libraries/neuralforecast/neuralforecast/models/softssharp.py) · [TabModel](libraries/tsai/tsai/models/TabModel.py) · [TiDE](libraries/Time-Series-Library/models/TiDE.py) · [TSMixer](libraries/Time-Series-Library/models/TSMixer.py) · [TSMixerx](libraries/neuralforecast/neuralforecast/models/tsmixerx.py) · [XLinear](libraries/neuralforecast/neuralforecast/models/xlinear.py) |
| [循环与卷积](docs/model-catalog.md#category-recurrent_convolution) | [BiTCN](libraries/neuralforecast/neuralforecast/models/bitcn.py) · [BlockRNN](libraries/darts/darts/models/forecasting/block_rnn_model.py) · [DeepAR](libraries/neuralforecast/neuralforecast/models/deepar.py) · [DilatedRNN](libraries/neuralforecast/neuralforecast/models/dilated_rnn.py) · [FCN](libraries/tsai/tsai/models/FCN.py) · [FCNPlus](libraries/tsai/tsai/models/FCNPlus.py) · [GRU](libraries/tsai/tsai/models/RNN.py) · [GRU_FCN](libraries/tsai/tsai/models/RNN_FCN.py) · [GRU_FCNPlus](libraries/tsai/tsai/models/RNN_FCNPlus.py) · [GRUAttention](libraries/tsai/tsai/models/RNNAttention.py) · [GRUAttentionPlus](libraries/tsai/tsai/models/RNNAttentionPlus.py) · [GRUPlus](libraries/tsai/tsai/models/RNNPlus.py) · [HydraMultiRocketPlus](libraries/tsai/tsai/models/HydraMultiRocketPlus.py) · [HydraPlus](libraries/tsai/tsai/models/HydraPlus.py) · [InceptionRocketPlus](libraries/tsai/tsai/models/MINIROCKETPlus_Pytorch.py) · [InceptionTime](libraries/tsai/tsai/models/InceptionTime.py) · [InceptionTimePlus](libraries/tsai/tsai/models/InceptionTimePlus.py) · [InCoordTime](libraries/tsai/tsai/models/InceptionTimePlus.py) · [LSTM](libraries/tsai/tsai/models/RNN.py) · [LSTM_FCN](libraries/tsai/tsai/models/RNN_FCN.py) · [LSTM_FCNPlus](libraries/tsai/tsai/models/RNN_FCNPlus.py) · [LSTMAttention](libraries/tsai/tsai/models/RNNAttention.py) · [LSTMAttentionPlus](libraries/tsai/tsai/models/RNNAttentionPlus.py) · [LSTMPlus](libraries/tsai/tsai/models/RNNPlus.py) · [MGRU_FCN](libraries/tsai/tsai/models/RNN_FCN.py) · [MGRU_FCNPlus](libraries/tsai/tsai/models/RNN_FCNPlus.py) · [MICN](libraries/Time-Series-Library/models/MICN.py) · [MiniRocket](libraries/tsai/tsai/models/MINIROCKET.py) · [MiniRocketPlus](libraries/tsai/tsai/models/MINIROCKETPlus_Pytorch.py) · [MLSTM_FCN](libraries/tsai/tsai/models/RNN_FCN.py) · [MLSTM_FCNPlus](libraries/tsai/tsai/models/RNN_FCNPlus.py) · [ModernTCN](libraries/pytorch-forecasting/pytorch_forecasting/models/modern_tcn/_modern_tcn_v2.py) · [MRNN_FCN](libraries/tsai/tsai/models/RNN_FCN.py) · [MRNN_FCNPlus](libraries/tsai/tsai/models/RNN_FCNPlus.py) · [MultiRocketPlus](libraries/tsai/tsai/models/MultiRocketPlus.py) · [OmniScaleCNN](libraries/tsai/tsai/models/OmniScaleCNN.py) · [RecurrentNetwork](libraries/pytorch-forecasting/pytorch_forecasting/models/rnn/_rnn.py) · [ResCNN](libraries/tsai/tsai/models/ResCNN.py) · [ResNet](libraries/tsai/tsai/models/ResNet.py) · [ResNetPlus](libraries/tsai/tsai/models/ResNetPlus.py) · [RNN](libraries/tsai/tsai/models/RNN.py) · [RNN_FCN](libraries/tsai/tsai/models/RNN_FCN.py) · [RNN_FCNPlus](libraries/tsai/tsai/models/RNN_FCNPlus.py) · [RNNAttention](libraries/tsai/tsai/models/RNNAttention.py) · [RNNAttentionPlus](libraries/tsai/tsai/models/RNNAttentionPlus.py) · [RNNPlus](libraries/tsai/tsai/models/RNNPlus.py) · [ROCKET](libraries/tsai/tsai/models/ROCKET.py) · [SCINet](libraries/Time-Series-Library/models/SCINet.py) · [SegRNN](libraries/Time-Series-Library/models/SegRNN.py) · [TCN](libraries/tsai/tsai/models/TCN.py) · [TimesNet](libraries/Time-Series-Library/models/TimesNet.py) · [TSSequencerPlus](libraries/tsai/tsai/models/TSSequencerPlus.py) · [XceptionTime](libraries/tsai/tsai/models/XceptionTime.py) · [XceptionTimePlus](libraries/tsai/tsai/models/XceptionTimePlus.py) · [XCM](libraries/tsai/tsai/models/XCM.py) · [XCMPlus](libraries/tsai/tsai/models/XCMPlus.py) · [XCoordTime](libraries/tsai/tsai/models/InceptionTimePlus.py) · [xLSTM](libraries/neuralforecast/neuralforecast/models/xlstm.py) · [xLSTMTime](libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm.py) · [XResNet1d](libraries/tsai/tsai/models/XResNet1d.py) · [XResNet1dPlus](libraries/tsai/tsai/models/XResNet1dPlus.py) |
| [Transformer与注意力](docs/model-catalog.md#category-transformer_attention) | [ConvTranPlus](libraries/tsai/tsai/models/ConvTranPlus.py) · [Crossformer](libraries/Time-Series-Library/models/Crossformer.py) · [EMAformer](baselines/EMAformer/model/EMAformer.py) · [GatedTabTransformer](libraries/tsai/tsai/models/GatedTabTransformer.py) · [Informer](baselines/Informer2020/models/model.py) · [iTransformer](libraries/Time-Series-Library/models/iTransformer.py) · [MultiPatchFormer](libraries/Time-Series-Library/models/MultiPatchFormer.py) · [Nonstationary_Transformer](libraries/Time-Series-Library/models/Nonstationary_Transformer.py) · [PatchTST](libraries/Time-Series-Library/models/PatchTST.py) · [PAttn](libraries/Time-Series-Library/models/PAttn.py) · [Pyraformer](baselines/Pyraformer/pyraformer/Pyraformer_LR.py) · [Reformer](libraries/Time-Series-Library/models/Reformer.py) · [Samformer](libraries/pytorch-forecasting/pytorch_forecasting/models/samformer/_samformer_v2.py) · [TabFusionTransformer](libraries/tsai/tsai/models/TabFusionTransformer.py) · [TabTransformer](libraries/tsai/tsai/models/TabTransformer.py) · [TemporalFusionTransformer](libraries/Time-Series-Library/models/TemporalFusionTransformer.py) · [TimeXer](libraries/Time-Series-Library/models/TimeXer.py) · [Transformer](libraries/Time-Series-Library/models/Transformer.py) · [TransformerGRUPlus](libraries/tsai/tsai/models/TransformerRNNPlus.py) · [TransformerLSTMPlus](libraries/tsai/tsai/models/TransformerRNNPlus.py) · [TransformerModel](libraries/tsai/tsai/models/TransformerModel.py) · [TransformerRNNPlus](libraries/tsai/tsai/models/TransformerRNNPlus.py) · [TSiTPlus](libraries/tsai/tsai/models/TSiTPlus.py) · [TSPerceiver](libraries/tsai/tsai/models/TSPerceiver.py) · [TST](libraries/tsai/tsai/models/TST.py) · [TSTabFusionTransformer](libraries/tsai/tsai/models/TabFusionTransformer.py) · [TSTPlus](libraries/tsai/tsai/models/TSTPlus.py) · [UniTS](libraries/pytorch-forecasting/pytorch_forecasting/models/units/_units_v2.py) |
| [分解平滑频域](docs/model-catalog.md#category-decomposition_frequency) | [Autoformer](baselines/Autoformer/models/Autoformer.py) · [ETSformer](baselines/ETSformer/models/etsformer/model.py) · [FEDformer](libraries/Time-Series-Library/models/FEDformer.py) · [FFT](libraries/darts/darts/models/forecasting/fft.py) · [FreTS](libraries/Time-Series-Library/models/FreTS.py) · [mWDN](libraries/tsai/tsai/models/mWDN.py) · [mWDNPlus](libraries/tsai/tsai/models/mWDN.py) · [TimeMixer](libraries/Time-Series-Library/models/TimeMixer.py) · [WPMixer](libraries/Time-Series-Library/models/WPMixer.py) |
| [状态空间动力学](docs/model-catalog.md#category-state_space_dynamics) | [FiLM](libraries/Time-Series-Library/models/FiLM.py) · [KalmanForecaster](libraries/darts/darts/models/forecasting/kalman_forecaster.py) · [Koopa](libraries/Time-Series-Library/models/Koopa.py) · [Mamba](libraries/Time-Series-Library/models/Mamba.py) · [MambaSimple](libraries/Time-Series-Library/models/MambaSimple.py) · [MambaSingleLayer](libraries/Time-Series-Library/models/MambaSingleLayer.py) |
| [图结构](docs/model-catalog.md#category-graph) | [MSGNet](libraries/Time-Series-Library/models/MSGNet.py) · [StemGNN](libraries/neuralforecast/neuralforecast/models/stemgnn.py) · [TimeFilter](libraries/Time-Series-Library/models/TimeFilter.py) |
| [LLM重编程](docs/model-catalog.md#category-llm_reprogramming) | [Time-LLM](baselines/Time-LLM/models/TimeLLM.py) |
| [预训练时序模型](docs/model-catalog.md#category-pretrained_foundation) | [Chronos](libraries/Time-Series-Library/models/Chronos.py) · [Chronos2](libraries/Time-Series-Library/models/Chronos2.py) · [Moirai](libraries/Time-Series-Library/models/Moirai.py) · [PatchTSTFMModel](libraries/darts/darts/models/forecasting/patchtst_fm_model.py) · [Sundial](libraries/Time-Series-Library/models/Sundial.py) · [T0](libraries/darts/darts/models/forecasting/t0_model.py) · [TimeMoE](libraries/Time-Series-Library/models/TimeMoE.py) · [TimesFM](libraries/Time-Series-Library/models/TimesFM.py) · [TimesFM2p5](libraries/darts/darts/models/forecasting/timesfm2p5_model.py) · [TimesFM3](libraries/darts/darts/models/forecasting/timesfm3_model.py) · [TiRex](libraries/Time-Series-Library/models/TiRex.py) · [TiRex2](libraries/darts/darts/models/forecasting/tirex2_model.py) |
| [专用异常检测](docs/model-catalog.md#category-anomaly_specialized) | [KANAD](libraries/Time-Series-Library/models/KANAD.py) |
| [统计与朴素基线](docs/model-catalog.md#category-statistical) | [ARIMA](libraries/darts/darts/models/forecasting/arima.py) · [AutoARIMA](libraries/darts/darts/models/forecasting/sf_auto_arima.py) · [AutoCES](libraries/darts/darts/models/forecasting/sf_auto_ces.py) · [AutoETS](libraries/darts/darts/models/forecasting/sf_auto_ets.py) · [AutoMFLES](libraries/darts/darts/models/forecasting/sf_auto_mfles.py) · [AutoTBATS](libraries/darts/darts/models/forecasting/sf_auto_tbats.py) · [AutoTheta](libraries/darts/darts/models/forecasting/sf_auto_theta.py) · [Baseline](libraries/pytorch-forecasting/pytorch_forecasting/models/baseline.py) · [Croston](libraries/darts/darts/models/forecasting/sf_croston.py) · [ExponentialSmoothing](libraries/darts/darts/models/forecasting/exponential_smoothing.py) · [FourTheta](libraries/darts/darts/models/forecasting/theta.py) · [GlobalNaiveAggregate](libraries/darts/darts/models/forecasting/global_baseline_models.py) · [GlobalNaiveDrift](libraries/darts/darts/models/forecasting/global_baseline_models.py) · [GlobalNaiveSeasonal](libraries/darts/darts/models/forecasting/global_baseline_models.py) · [NaiveDrift](libraries/darts/darts/models/forecasting/baselines.py) · [NaiveMean](libraries/darts/darts/models/forecasting/baselines.py) · [NaiveMovingAverage](libraries/darts/darts/models/forecasting/baselines.py) · [NaiveSeasonal](libraries/darts/darts/models/forecasting/baselines.py) · [Prophet](libraries/darts/darts/models/forecasting/prophet_model.py) · [TBATS](libraries/darts/darts/models/forecasting/sf_tbats.py) · [Theta](libraries/darts/darts/models/forecasting/theta.py) · [VARIMA](libraries/darts/darts/models/forecasting/varima.py) |
| [树模型与回归](docs/model-catalog.md#category-machine_learning) | [CatBoostClassifierModel](libraries/darts/darts/models/forecasting/catboost_model.py) · [CatBoostModel](libraries/darts/darts/models/forecasting/catboost_model.py) · [LightGBMClassifierModel](libraries/darts/darts/models/forecasting/lgbm.py) · [LightGBMModel](libraries/darts/darts/models/forecasting/lgbm.py) · [LinearRegressionModel](libraries/darts/darts/models/forecasting/linear_regression_model.py) · [RandomForestModel](libraries/darts/darts/models/forecasting/random_forest.py) · [XGBClassifierModel](libraries/darts/darts/models/forecasting/xgboost.py) · [XGBModel](libraries/darts/darts/models/forecasting/xgboost.py) |
| [集成与校准](docs/model-catalog.md#category-ensemble_calibration) | [ConformalNaiveModel](libraries/darts/darts/models/forecasting/conformal_models.py) · [ConformalQRModel](libraries/darts/darts/models/forecasting/conformal_models.py) · [HINT](libraries/neuralforecast/neuralforecast/models/hint.py) · [MiniRocketVotingClassifier](libraries/tsai/tsai/models/MINIROCKET.py) · [MiniRocketVotingRegressor](libraries/tsai/tsai/models/MINIROCKET.py) · [MultiInceptionTimePlus](libraries/tsai/tsai/models/InceptionTimePlus.py) · [NaiveEnsembleModel](libraries/darts/darts/models/forecasting/naive_ensemble_model.py) · [RegressionEnsembleModel](libraries/darts/darts/models/forecasting/regression_ensemble_model.py) |
| [通用模型适配器](docs/model-catalog.md#category-model_adapter) | [MultiInputNet](libraries/tsai/tsai/models/MultiInputNet.py) · [MultiTSTPlus](libraries/tsai/tsai/models/TSTPlus.py) · [MultivariateModel](libraries/darts/darts/models/forecasting/multivariate_model.py) · [NeuralForecastModel](libraries/darts/darts/models/forecasting/nf_model.py) · [SKLearnClassifierModel](libraries/darts/darts/models/forecasting/sklearn_model.py) · [SKLearnModel](libraries/darts/darts/models/forecasting/sklearn_model.py) · [StatsForecastModel](libraries/darts/darts/models/forecasting/sf_model.py) |

<!-- MODEL_CATALOG_END -->

各分类的完整模型、特点与源码入口均在[统一模型目录](docs/model-catalog.md)逐项展开。端到端模型、可直接使用的预测器与有名称的网络变体逐项列出，同名实现合并保留；辅助层、损失函数与抽象基类在各库原目录中完整保留。

## 全部模型明细

<!-- MODEL_DETAILS_START -->

共 **187 个模型家族**，每个模型一行，所有来源使用相同六个字段。同一模型的各库实现全部并列保留；悬停短链接可查看完整路径或类名。

<table>
<thead><tr>
<th width="100" align="left">模型</th>
<th width="220" align="left">主要思路</th>
<th width="110" align="left">源码</th>
<th width="130" align="left">核心模型</th>
<th width="120" align="left">运行入口</th>
<th width="100" align="left">论文 / 项目</th>
</tr></thead>
<tbody>
<tr>
<td align="left">ARIMA</td>
<td align="left">通过自回归、差分和移动平均描述时间依赖。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/arima.py" title="libraries/darts/darts/models/forecasting/arima.py :: ARIMA">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">AutoARIMA</td>
<td align="left">自动选择 ARIMA 配置并生成统计预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_auto_arima.py" title="libraries/darts/darts/models/forecasting/sf_auto_arima.py :: AutoARIMA">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">AutoCES</td>
<td align="left">调用自动复指数平滑预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_auto_ces.py" title="libraries/darts/darts/models/forecasting/sf_auto_ces.py :: AutoCES">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">AutoETS</td>
<td align="left">自动选择误差、趋势与季节结构的指数平滑模型。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_auto_ets.py" title="libraries/darts/darts/models/forecasting/sf_auto_ets.py :: AutoETS">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Autoformer</td>
<td align="left">逐层拆分趋势与季节变化，再用自相关选择时延并聚合序列。</td>
<td align="left"><a href="baselines/Autoformer/" title="baselines/Autoformer">原&#8288;版</a><br><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="baselines/Autoformer/models/Autoformer.py" title="baselines/Autoformer/models/Autoformer.py">原&#8288;版</a><br><a href="libraries/Time-Series-Library/models/Autoformer.py" title="libraries/Time-Series-Library/models/Autoformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Autoformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Autoformer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/autoformer.py" title="libraries/neuralforecast/neuralforecast/models/autoformer.py :: Autoformer">N&#8288;F</a></td>
<td align="left"><a href="baselines/Autoformer/run.py" title="baselines/Autoformer/run.py; 具体参数与任务按对应实现配置">原&#8288;版</a><br><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2106.13008" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Autoformer">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">AutoMFLES</td>
<td align="left">自动配置 MFLES 多成分拟合并产生统计预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_auto_mfles.py" title="libraries/darts/darts/models/forecasting/sf_auto_mfles.py :: AutoMFLES">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">AutoTBATS</td>
<td align="left">自动选择含三角季节项、趋势等成分的 TBATS 配置。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_auto_tbats.py" title="libraries/darts/darts/models/forecasting/sf_auto_tbats.py :: AutoTBATS">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">AutoTheta</td>
<td align="left">自动配置 Theta 方法，预测并组合分解后的成分。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_auto_theta.py" title="libraries/darts/darts/models/forecasting/sf_auto_theta.py :: AutoTheta">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Baseline</td>
<td align="left">重复最后一个历史观测值，作为朴素预测对照。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting; 重复最后一个观测值的朴素预测基线。">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/baseline.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/baseline.py :: Baseline">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">BiTCN</td>
<td align="left">以时间卷积分支处理历史和已知未来协变量，产生概率预测。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/bitcn.py" title="libraries/neuralforecast/neuralforecast/models/bitcn.py :: BiTCN">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://doi.org/10.1016/j.ijforecast.2021.11.011" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">BlockRNN<br><sub>BlockRNNModel</sub></td>
<td align="left">循环编码历史窗口，再以块输出同时预测多个未来点。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/block_rnn_model.py" title="libraries/darts/darts/models/forecasting/block_rnn_model.py :: BlockRNNModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://openreview.net/forum?id=cGDAkQo1C0p" title="此链接是源码引用的 TiDE 相关架构文献，不是 BlockRNN 的独立论文。">论&#8288;文</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">CatBoostClassifierModel</td>
<td align="left">用 CatBoost 分类接口预测序列离散标签。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/catboost_model.py" title="libraries/darts/darts/models/forecasting/catboost_model.py :: CatBoostClassifierModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">CatBoostModel</td>
<td align="left">以 CatBoost 提升树学习带滞后和协变量的预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/catboost_model.py" title="libraries/darts/darts/models/forecasting/catboost_model.py :: CatBoostModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Chronos</td>
<td align="left">调用预训练 Chronos，把数值序列交给其预测管线，库内入口用于零样本预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Chronos.py" title="libraries/Time-Series-Library/models/Chronos.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2403.07815" title="链接为上游 README 列出的 Chronos 系列论文；当前接口实际加载 chronos-bolt-base，不将该链接标成该权重的专属论文。">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Chronos2<br><sub>Chronos-2 / Chronos2Model</sub></td>
<td align="left">调用 Chronos-2 预训练预测管线，与第一代 Chronos 分开保留接口。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Chronos2.py" title="libraries/Time-Series-Library/models/Chronos2.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/darts/darts/models/forecasting/chronos2_model.py" title="libraries/darts/darts/models/forecasting/chronos2_model.py :: Chronos2Model">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/2510.15821" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ConformalNaiveModel</td>
<td align="left">对基础预测历史误差做保形校准，调整区间覆盖目标。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/conformal_models.py" title="libraries/darts/darts/models/forecasting/conformal_models.py :: ConformalNaiveModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ConformalQRModel</td>
<td align="left">在分位数预测上做保形校准，修正预测区间。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/conformal_models.py" title="libraries/darts/darts/models/forecasting/conformal_models.py :: ConformalQRModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ConvTranPlus</td>
<td align="left">结合卷积嵌入、时序绝对位置和相对位置注意力。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/ConvTranPlus.py" title="libraries/tsai/tsai/models/ConvTranPlus.py :: ConvTranPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2305.16642v1" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Crossformer</td>
<td align="left">把每个变量的序列切成片段，用分层和两阶段注意力处理时间与变量关系。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Crossformer.py" title="libraries/Time-Series-Library/models/Crossformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Crossformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Crossformer.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=vSVLM2j9eie" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Croston</td>
<td align="left">分别估计间歇需求大小和到达间隔，处理大量零值需求。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_croston.py" title="libraries/darts/darts/models/forecasting/sf_croston.py :: Croston">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">DecoderMLP<br><sub>DecoderMLPForecaster / DecoderMLP_pkg / DecoderMLP_v2</sub></td>
<td align="left">使用解码区间可用的协变量构建前馈预测。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp.py :: DecoderMLP">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp_pkg.py :: DecoderMLP_pkg">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp_v2.py :: DecoderMLP_v2">P&#8288;F&#8288;³</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/mlp/_decodermlp_forecaster_v2.py :: DecoderMLPForecaster">P&#8288;F&#8288;⁴</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">DeepAR<br><sub>DeepAR_pkg</sub></td>
<td align="left">用自回归循环网络学习未来值的概率分布。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/deepar.py" title="libraries/neuralforecast/neuralforecast/models/deepar.py :: DeepAR">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/deepar/_deepar.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/deepar/_deepar.py :: DeepAR">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/deepar/_deepar_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/deepar/_deepar_pkg.py :: DeepAR_pkg">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/pii/S0169207019301888" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">DeepNPTS</td>
<td align="left">学习历史观测的权重，以非参数方式形成预测分布。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/deepnpts.py" title="libraries/neuralforecast/neuralforecast/models/deepnpts.py :: DeepNPTS">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2312.14657" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">DilatedRNN</td>
<td align="left">以不同时间跨度的循环连接捕捉长期依赖。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/dilated_rnn.py" title="libraries/neuralforecast/neuralforecast/models/dilated_rnn.py :: DilatedRNN">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/pdf/1710.02224" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">DLinear<br><sub>DLinearForecaster / DLinearModel</sub></td>
<td align="left">先分解趋势与剩余变化，再分别做线性预测，是结构简单的对照模型。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/DLinear.py" title="libraries/Time-Series-Library/models/DLinear.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/DLinear.py" title="libraries/TimeSeriesLibrary-ZJ/models/DLinear.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/dlinear.py" title="libraries/neuralforecast/neuralforecast/models/dlinear.py :: DLinear">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/dlinear/_dlinear_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/dlinear/_dlinear_v2.py :: DLinear">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/dlinear/_dlinear_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/dlinear/_dlinear_forecaster_v2.py :: DLinearForecaster">P&#8288;F&#8288;²</a><br><a href="libraries/darts/darts/models/forecasting/dlinear.py" title="libraries/darts/darts/models/forecasting/dlinear.py :: DLinearModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2205.13504.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">EMAformer</td>
<td align="left">在变量 token 上叠加通道、相位和联合嵌入，再用 Transformer 预测。</td>
<td align="left"><a href="baselines/EMAformer/" title="baselines/EMAformer">原&#8288;版</a></td>
<td align="left"><a href="baselines/EMAformer/model/EMAformer.py" title="baselines/EMAformer/model/EMAformer.py">原&#8288;版</a></td>
<td align="left"><a href="baselines/EMAformer/run.py" title="baselines/EMAformer/run.py; 具体参数与任务按对应实现配置">原&#8288;版</a></td>
<td align="left"><a href="https://arxiv.org/abs/2511.08396" title="模型论文">论&#8288;文</a><br><a href="https://github.com/PlanckChang/EMAformer">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ETSformer</td>
<td align="left">将水平、增长和季节项分开建模，结合可学习指数平滑、傅里叶外推与增长阻尼。</td>
<td align="left"><a href="baselines/ETSformer/" title="baselines/ETSformer">原&#8288;版</a><br><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="baselines/ETSformer/models/etsformer/model.py" title="baselines/ETSformer/models/etsformer/model.py">原&#8288;版</a><br><a href="libraries/Time-Series-Library/models/ETSformer.py" title="libraries/Time-Series-Library/models/ETSformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/ETSformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/ETSformer.py">Z&#8288;J</a></td>
<td align="left"><a href="baselines/ETSformer/run.py" title="baselines/ETSformer/run.py; 具体参数与任务按对应实现配置">原&#8288;版</a><br><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/abs/2202.01381" title="模型论文">论&#8288;文</a><br><a href="https://github.com/azkanaon/etsformer">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ExponentialSmoothing</td>
<td align="left">用递减权重估计水平、趋势和季节变化并外推。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/exponential_smoothing.py" title="libraries/darts/darts/models/forecasting/exponential_smoothing.py :: ExponentialSmoothing">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FCN</td>
<td align="left">用多层一维卷积和全局池化提取序列特征。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/FCN.py" title="libraries/tsai/tsai/models/FCN.py :: FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FCNPlus</td>
<td align="left">用多层一维卷积和全局池化提取序列特征。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/FCNPlus.py" title="libraries/tsai/tsai/models/FCNPlus.py :: FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FEDformer</td>
<td align="left">在趋势季节分解的基础上，用傅里叶或小波模块处理长期依赖。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/FEDformer.py" title="libraries/Time-Series-Library/models/FEDformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/FEDformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/FEDformer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/fedformer.py" title="libraries/neuralforecast/neuralforecast/models/fedformer.py :: FEDformer">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://proceedings.mlr.press/v162/zhou22g.html" title="模型论文">论&#8288;文</a><br><a href="https://github.com/MAZiqing/FEDformer">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FFT</td>
<td align="left">在去趋势等处理后选择傅里叶成分并外推周期变化。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/fft.py" title="libraries/darts/darts/models/forecasting/fft.py :: FFT">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FiLM</td>
<td align="left">用 Legendre/HiPPO 状态投影压缩历史，再以频域处理提取预测信息。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/FiLM.py" title="libraries/Time-Series-Library/models/FiLM.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/FiLM.py" title="libraries/TimeSeriesLibrary-ZJ/models/FiLM.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://openreview.net/forum?id=zTQdHSQUQWc" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FourTheta</td>
<td align="left">组合多条 Theta 变换线及其配置产生预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/theta.py" title="libraries/darts/darts/models/forecasting/theta.py :: FourTheta">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">FreTS<br><sub>FreTSForecaster</sub></td>
<td align="left">把序列变到频域，用复数 MLP 混合时间和通道信息，再还原预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/FreTS.py" title="libraries/Time-Series-Library/models/FreTS.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/FreTS.py" title="libraries/TimeSeriesLibrary-ZJ/models/FreTS.py">Z&#8288;J</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/frets/_frets_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/frets/_frets_v2.py :: FreTS">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/frets/_frets_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/frets/_frets_forecaster_v2.py :: FreTSForecaster">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2311.06184.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GatedTabTransformer</td>
<td align="left">以门控和注意力表示表格变量，可用于带静态属性任务。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/GatedTabTransformer.py" title="libraries/tsai/tsai/models/GatedTabTransformer.py :: GatedTabTransformer">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2201.00199" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GlobalNaiveAggregate</td>
<td align="left">在全局模型接口中对输入窗口做指定聚合。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/global_baseline_models.py" title="libraries/darts/darts/models/forecasting/global_baseline_models.py :: GlobalNaiveAggregate">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GlobalNaiveDrift</td>
<td align="left">在全局模型接口中延伸输入窗口的漂移趋势。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/global_baseline_models.py" title="libraries/darts/darts/models/forecasting/global_baseline_models.py :: GlobalNaiveDrift">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GlobalNaiveSeasonal</td>
<td align="left">在全局模型接口中重复窗口中的季节观测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/global_baseline_models.py" title="libraries/darts/darts/models/forecasting/global_baseline_models.py :: GlobalNaiveSeasonal">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">gMLP</td>
<td align="left">通过空间门控前馈模块混合序列位置，替代完整注意力。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/gMLP.py" title="libraries/tsai/tsai/models/gMLP.py :: gMLP">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2105.08050" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GRU</td>
<td align="left">以更新门和重置门递推隐藏状态，学习序列信息。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN.py" title="libraries/tsai/tsai/models/RNN.py :: GRU">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/neuralforecast/models/gru.py" title="libraries/neuralforecast/neuralforecast/models/gru.py :: GRU">N&#8288;F</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/1412.3555" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GRU_FCN</td>
<td align="left">融合 GRU 循环分支与全卷积分支的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCN.py" title="libraries/tsai/tsai/models/RNN_FCN.py :: GRU_FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1812.07683" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GRU_FCNPlus</td>
<td align="left">融合 GRU 循环分支与全卷积分支的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCNPlus.py" title="libraries/tsai/tsai/models/RNN_FCNPlus.py :: GRU_FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1812.07683" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GRUAttention</td>
<td align="left">结合 GRU 循环表示和注意力编码模块的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNAttention.py" title="libraries/tsai/tsai/models/RNNAttention.py :: GRUAttention">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GRUAttentionPlus</td>
<td align="left">结合 GRU 循环表示和注意力编码模块的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNAttentionPlus.py" title="libraries/tsai/tsai/models/RNNAttentionPlus.py :: GRUAttentionPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">GRUPlus</td>
<td align="left">GRU 的 tsai 可配置骨干与任务头变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNPlus.py" title="libraries/tsai/tsai/models/RNNPlus.py :: GRUPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1412.3555" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">HINT</td>
<td align="left">结合基础预测与层级协调，使不同聚合层级的预测一致。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/hint.py" title="libraries/neuralforecast/neuralforecast/models/hint.py :: HINT">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2305.07089" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">HydraMultiRocketPlus</td>
<td align="left">融合 Hydra 竞争卷积和 MultiRocket 统计特征。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/HydraMultiRocketPlus.py" title="libraries/tsai/tsai/models/HydraMultiRocketPlus.py :: HydraMultiRocketPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">HydraPlus</td>
<td align="left">通过分组随机卷积的竞争响应生成特征，再接任务头。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/HydraPlus.py" title="libraries/tsai/tsai/models/HydraPlus.py :: HydraPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">InceptionRocketPlus</td>
<td align="left">将多尺度卷积特征与 Rocket 风格任务头结合。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MINIROCKETPlus_Pytorch.py" title="libraries/tsai/tsai/models/MINIROCKETPlus_Pytorch.py :: InceptionRocketPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">InceptionTime</td>
<td align="left">并行使用不同长度的一维卷积核提取多尺度模式。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/InceptionTime.py" title="libraries/tsai/tsai/models/InceptionTime.py :: InceptionTime">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1909.04939" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">InceptionTimePlus<br><sub>InceptionTimePlus17x17 / InceptionTimePlus32x32 / InceptionTimePlus47x47 / InceptionTimePlus62x62 / InceptionTimeXLPlus</sub></td>
<td align="left">并行使用不同长度的一维卷积核提取多尺度模式。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; InceptionTimePlus 的深度或宽度配置变体；不另计新算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InceptionTimePlus17x17">t&#8288;s&#8288;a&#8288;i&#8288;¹</a><br><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InceptionTimePlus32x32">t&#8288;s&#8288;a&#8288;i&#8288;²</a><br><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InceptionTimePlus47x47">t&#8288;s&#8288;a&#8288;i&#8288;³</a><br><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InceptionTimePlus62x62">t&#8288;s&#8288;a&#8288;i&#8288;⁴</a><br><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InceptionTimeXLPlus">t&#8288;s&#8288;a&#8288;i&#8288;⁵</a><br><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InceptionTimePlus">t&#8288;s&#8288;a&#8288;i&#8288;⁶</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1909.04939" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">InCoordTime</td>
<td align="left">在 InceptionTimePlus 中加入坐标卷积信息的变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: InCoordTime">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Informer<br><sub>Informer2020</sub></td>
<td align="left">用 ProbSparse 选择重要 query，并通过编码器蒸馏压缩长序列。</td>
<td align="left"><a href="baselines/Informer2020/" title="baselines/Informer2020">原&#8288;版</a><br><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="baselines/Informer2020/models/model.py" title="baselines/Informer2020/models/model.py">原&#8288;版</a><br><a href="libraries/Time-Series-Library/models/Informer.py" title="libraries/Time-Series-Library/models/Informer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Informer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Informer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/informer.py" title="libraries/neuralforecast/neuralforecast/models/informer.py :: Informer">N&#8288;F</a></td>
<td align="left"><a href="baselines/Informer2020/main_informer.py" title="baselines/Informer2020/main_informer.py; 具体参数与任务按对应实现配置">原&#8288;版</a><br><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2012.07436" title="模型论文">论&#8288;文</a><br><a href="https://github.com/zhouhaoyi/Informer2020">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">iTransformer</td>
<td align="left">把每个变量的历史作为一个 token，让注意力直接学习变量之间的关系。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/iTransformer.py" title="libraries/Time-Series-Library/models/iTransformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/iTransformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/iTransformer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/itransformer.py" title="libraries/neuralforecast/neuralforecast/models/itransformer.py :: iTransformer">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.06625" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">KalmanForecaster</td>
<td align="left">估计状态空间模型的隐状态，再以 Kalman 模型递推未来。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/kalman_forecaster.py" title="libraries/darts/darts/models/forecasting/kalman_forecaster.py :: KalmanForecaster">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">KAN</td>
<td align="left">用可学习的一元函数替代普通 MLP 边权拟合非线性关系。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/kan.py" title="libraries/neuralforecast/neuralforecast/models/kan.py :: KAN">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2404.19756" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">KANAD</td>
<td align="left">结合周期余弦特征和卷积重建序列，当前库内模型只实现异常检测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/KANAD.py" title="libraries/Time-Series-Library/models/KANAD.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/abs/2411.00278" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Koopa</td>
<td align="left">分离不同变化成分，用可学习和动态估计的 Koopman 算子推进隐状态。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Koopa.py" title="libraries/Time-Series-Library/models/Koopa.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Koopa.py" title="libraries/TimeSeriesLibrary-ZJ/models/Koopa.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2305.18803.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LightGBMClassifierModel</td>
<td align="left">以 LightGBM 分类器预测离散目标。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/lgbm.py" title="libraries/darts/darts/models/forecasting/lgbm.py :: LightGBMClassifierModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LightGBMModel</td>
<td align="left">以 LightGBM 梯度提升树对滞后窗口回归。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/lgbm.py" title="libraries/darts/darts/models/forecasting/lgbm.py :: LightGBMModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LightTS</td>
<td align="left">通过连续与间隔采样提取序列片段，用 MLP 混合局部和跨片段信息。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/LightTS.py" title="libraries/Time-Series-Library/models/LightTS.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/LightTS.py" title="libraries/TimeSeriesLibrary-ZJ/models/LightTS.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/abs/2207.01186" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LinearRegressionModel</td>
<td align="left">将滞后值与协变量展开为监督样本，用线性回归预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/linear_regression_model.py" title="libraries/darts/darts/models/forecasting/linear_regression_model.py :: LinearRegressionModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LSTM</td>
<td align="left">用输入、遗忘和输出门维护长期记忆，学习序列映射。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN.py" title="libraries/tsai/tsai/models/RNN.py :: LSTM">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/neuralforecast/models/lstm.py" title="libraries/neuralforecast/neuralforecast/models/lstm.py :: LSTM">N&#8288;F</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://ieeexplore.ieee.org/abstract/document/6795963/" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LSTM_FCN</td>
<td align="left">融合 LSTM 循环分支与全卷积分支的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCN.py" title="libraries/tsai/tsai/models/RNN_FCN.py :: LSTM_FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1709.05206" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LSTM_FCNPlus</td>
<td align="left">融合 LSTM 循环分支与全卷积分支的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCNPlus.py" title="libraries/tsai/tsai/models/RNN_FCNPlus.py :: LSTM_FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1709.05206" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LSTMAttention</td>
<td align="left">结合 LSTM 循环表示和注意力编码模块的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNAttention.py" title="libraries/tsai/tsai/models/RNNAttention.py :: LSTMAttention">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LSTMAttentionPlus</td>
<td align="left">结合 LSTM 循环表示和注意力编码模块的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNAttentionPlus.py" title="libraries/tsai/tsai/models/RNNAttentionPlus.py :: LSTMAttentionPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">LSTMPlus</td>
<td align="left">LSTM 的 tsai 可配置骨干与任务头变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNPlus.py" title="libraries/tsai/tsai/models/RNNPlus.py :: LSTMPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://ieeexplore.ieee.org/abstract/document/6795963/" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Mamba</td>
<td align="left">用 Mamba 的选择性状态空间模块递推处理序列，减少对全量注意力的依赖。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Mamba.py" title="libraries/Time-Series-Library/models/Mamba.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Mamba.py" title="libraries/TimeSeriesLibrary-ZJ/models/Mamba.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/abs/2312.00752" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MambaSimple</td>
<td align="left">在库内保留较简化的 Mamba 与扫描计算实现，便于阅读状态递推机制。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/MambaSimple.py" title="libraries/Time-Series-Library/models/MambaSimple.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/MambaSimple.py" title="libraries/TimeSeriesLibrary-ZJ/models/MambaSimple.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/abs/2312.00752" title="共用 Mamba 方法论文；当前文件是简化实现，参考 mamba-minimal，不宣称另有独立论文。">论&#8288;文</a><br><a href="https://github.com/johnma2006/mamba-minimal/">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MambaSingleLayer<br><sub>MambaSL</sub></td>
<td align="left">用单层 Mamba 做序列分类，当前构造和前向路径限定分类任务。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/MambaSingleLayer.py" title="libraries/Time-Series-Library/models/MambaSingleLayer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://openreview.net/forum?id=YDl4vqQqGP" title="当前模块对应 MambaSL 分类论文；文件名 MambaSingleLayer 与论文模型名 MambaSL 分别保留。">论&#8288;文</a><br><a href="https://github.com/yoom618/MambaSL">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MGRU_FCN</td>
<td align="left">面向多变量序列的 GRU 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCN.py" title="libraries/tsai/tsai/models/RNN_FCN.py :: MGRU_FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MGRU_FCNPlus</td>
<td align="left">面向多变量序列的 GRU 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCNPlus.py" title="libraries/tsai/tsai/models/RNN_FCNPlus.py :: MGRU_FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MICN</td>
<td align="left">用多尺度下采样、等距和上采样卷积提取局部与全局变化，并结合序列分解。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/MICN.py" title="libraries/Time-Series-Library/models/MICN.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/MICN.py" title="libraries/TimeSeriesLibrary-ZJ/models/MICN.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=zt53IDUR1U" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MiniRocket<br><sub>MiniRocketClassifier / MiniRocketRegressor</sub></td>
<td align="left">用固定形式的卷积核和阈值统计快速生成分类或回归特征。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MINIROCKET.py" title="libraries/tsai/tsai/models/MINIROCKET.py :: MiniRocketClassifier">t&#8288;s&#8288;a&#8288;i&#8288;¹</a><br><a href="libraries/tsai/tsai/models/MINIROCKET.py" title="libraries/tsai/tsai/models/MINIROCKET.py :: MiniRocketRegressor">t&#8288;s&#8288;a&#8288;i&#8288;²</a><br><a href="libraries/tsai/tsai/models/MINIROCKET_Pytorch.py" title="libraries/tsai/tsai/models/MINIROCKET_Pytorch.py :: MiniRocket">t&#8288;s&#8288;a&#8288;i&#8288;³</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2102.00457" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MiniRocketPlus</td>
<td align="left">用固定形式的卷积核和阈值统计快速生成分类或回归特征。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MINIROCKETPlus_Pytorch.py" title="libraries/tsai/tsai/models/MINIROCKETPlus_Pytorch.py :: MiniRocketPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2102.00457" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MiniRocketVotingClassifier</td>
<td align="left">通过投票组合多个 MiniRocket 分类器。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; 公开集成/多输入模型封装；不宣称独立论文算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MINIROCKET.py" title="libraries/tsai/tsai/models/MINIROCKET.py :: MiniRocketVotingClassifier">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MiniRocketVotingRegressor</td>
<td align="left">通过投票或平均组合多个 MiniRocket 回归器。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; 公开集成/多输入模型封装；不宣称独立论文算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MINIROCKET.py" title="libraries/tsai/tsai/models/MINIROCKET.py :: MiniRocketVotingRegressor">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MLP</td>
<td align="left">将历史窗口或表格变量交给多层前馈网络，作为非线性对照。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MLP.py" title="libraries/tsai/tsai/models/MLP.py :: MLP">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/neuralforecast/models/mlp.py" title="libraries/neuralforecast/neuralforecast/models/mlp.py :: MLP">N&#8288;F</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MLPMultivariate</td>
<td align="left">将多条序列的历史合并输入 MLP，联合产生多变量预测。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/mlpmultivariate.py" title="libraries/neuralforecast/neuralforecast/models/mlpmultivariate.py :: MLPMultivariate">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MLSTM_FCN</td>
<td align="left">面向多变量序列的 LSTM 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCN.py" title="libraries/tsai/tsai/models/RNN_FCN.py :: MLSTM_FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0893608019301200" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MLSTM_FCNPlus</td>
<td align="left">面向多变量序列的 LSTM 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCNPlus.py" title="libraries/tsai/tsai/models/RNN_FCNPlus.py :: MLSTM_FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0893608019301200" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ModernTCN<br><sub>ModernTCNForecaster</sub></td>
<td align="left">用现代深度卷积分别组织时间、变量和特征维的信息。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/modern_tcn/_modern_tcn_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/modern_tcn/_modern_tcn_v2.py :: ModernTCN">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/modern_tcn/_modern_tcn_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/modern_tcn/_modern_tcn_forecaster_v2.py :: ModernTCNForecaster">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2401.17593" title="模型论文">论&#8288;文</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Moirai</td>
<td align="left">调用 uni2ts 的预训练 Moirai 模型，库内接口用于零样本预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Moirai.py" title="libraries/Time-Series-Library/models/Moirai.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2402.02592" title="链接为上游 README 列出的 Moirai 系列论文；当前接口实际加载 moirai-2.0-R-small，具体版本以源码和权重标识为准。">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MRNN_FCN</td>
<td align="left">面向多变量序列的 RNN 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCN.py" title="libraries/tsai/tsai/models/RNN_FCN.py :: MRNN_FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MRNN_FCNPlus</td>
<td align="left">面向多变量序列的 RNN 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCNPlus.py" title="libraries/tsai/tsai/models/RNN_FCNPlus.py :: MRNN_FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MSGNet</td>
<td align="left">先发现不同周期尺度，再通过图卷积和注意力学习多变量之间的关系。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/MSGNet.py" title="libraries/Time-Series-Library/models/MSGNet.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://dl.acm.org/doi/10.1609/aaai.v38i10.28991" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MultiInceptionTimePlus</td>
<td align="left">以多个 InceptionTimePlus 分支处理输入组并融合输出。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; 公开集成/多输入模型封装；不宣称独立论文算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: MultiInceptionTimePlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MultiInputNet</td>
<td align="left">将多个输入分支或骨干连接到统一输出头的封装。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; 公开集成/多输入模型封装；不宣称独立论文算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MultiInputNet.py" title="libraries/tsai/tsai/models/MultiInputNet.py :: MultiInputNet">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MultiPatchFormer</td>
<td align="left">用多种 patch 尺度表示序列，再结合注意力组织不同尺度与通道信息。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/MultiPatchFormer.py" title="libraries/Time-Series-Library/models/MultiPatchFormer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/MultiPatchFormer.py" title="libraries/TimeSeriesLibrary-ZJ/models/MultiPatchFormer.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://www.nature.com/articles/s41598-024-82417-4" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MultiRocketPlus</td>
<td align="left">联合原序列与差分序列的多种卷积池化统计特征。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/MultiRocketPlus.py" title="libraries/tsai/tsai/models/MultiRocketPlus.py :: MultiRocketPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MultiTSTPlus</td>
<td align="left">对输入组分别应用 TSTPlus，再融合表示的封装。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; 公开集成/多输入模型封装；不宣称独立论文算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TSTPlus.py" title="libraries/tsai/tsai/models/TSTPlus.py :: MultiTSTPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">MultivariateModel</td>
<td align="left">将多个单变量预测器组合为统一多变量模型。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/multivariate_model.py" title="libraries/darts/darts/models/forecasting/multivariate_model.py :: MultivariateModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">mWDN</td>
<td align="left">以可训练小波分解形成多分辨率表示，再接序列任务网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/mWDN.py" title="libraries/tsai/tsai/models/mWDN.py :: mWDN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3219819.3220060" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">mWDNPlus</td>
<td align="left">以可训练小波分解形成多分辨率表示，再接序列任务网络。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/mWDN.py" title="libraries/tsai/tsai/models/mWDN.py :: mWDNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3219819.3220060" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NaiveDrift</td>
<td align="left">将首尾观测确定的平均变化速率延伸到未来。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/baselines.py" title="libraries/darts/darts/models/forecasting/baselines.py :: NaiveDrift">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NaiveEnsembleModel</td>
<td align="left">训练多个基础预测器，对预测结果做简单平均。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/naive_ensemble_model.py" title="libraries/darts/darts/models/forecasting/naive_ensemble_model.py :: NaiveEnsembleModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NaiveMean</td>
<td align="left">以历史平均值预测未来。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/baselines.py" title="libraries/darts/darts/models/forecasting/baselines.py :: NaiveMean">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NaiveMovingAverage</td>
<td align="left">利用末段窗口的移动平均递推预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/baselines.py" title="libraries/darts/darts/models/forecasting/baselines.py :: NaiveMovingAverage">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NaiveSeasonal</td>
<td align="left">重复最后一个季节周期的观测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/baselines.py" title="libraries/darts/darts/models/forecasting/baselines.py :: NaiveSeasonal">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NBEATS<br><sub>NBEATSModel / NBeats / NBeats_pkg</sub></td>
<td align="left">堆叠残差前馈块，分别拟合历史与预测基函数并累加结果。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/nbeats.py" title="libraries/neuralforecast/neuralforecast/models/nbeats.py :: NBEATS">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeats.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeats.py :: NBeats">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeats_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeats_pkg.py :: NBeats_pkg">P&#8288;F&#8288;²</a><br><a href="libraries/darts/darts/models/forecasting/nbeats.py" title="libraries/darts/darts/models/forecasting/nbeats.py :: NBEATSModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/1905.10437" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NBEATSKAN<br><sub>NBeatsKAN / NBeatsKAN_pkg</sub></td>
<td align="left">在 N-BEATS 式残差结构中使用 KAN 层的变体。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeatskan.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeatskan.py :: NBeatsKAN">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeatskan_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nbeats/_nbeatskan_pkg.py :: NBeatsKAN_pkg">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NBEATSx</td>
<td align="left">在 N-BEATS 中加入历史和未来外生变量。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/nbeatsx.py" title="libraries/neuralforecast/neuralforecast/models/nbeatsx.py :: NBEATSx">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2104.05522" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NeuralForecastModel</td>
<td align="left">把 NeuralForecast 模型接入 Darts 的训练和预测接口。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/nf_model.py" title="libraries/darts/darts/models/forecasting/nf_model.py :: NeuralForecastModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://openreview.net/forum?id=cGDAkQo1C0p" title="此链接是源码列出的 TiDE 相关文献；本项是 NeuralForecast 接口适配器，不是该论文方法。">论&#8288;文</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NHITS<br><sub>NHiTS / NHiTSForecaster / NHiTSModel / NHiTS_pkg / NHiTS_v2</sub></td>
<td align="left">以多分辨率采样和分层插值组合短期细节与长期预测。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/nhits.py" title="libraries/neuralforecast/neuralforecast/models/nhits.py :: NHITS">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits.py :: NHiTS">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits_pkg.py :: NHiTS_pkg">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits_v2.py :: NHiTS_v2">P&#8288;F&#8288;³</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/nhits/_nhits_forecaster_v2.py :: NHiTSForecaster">P&#8288;F&#8288;⁴</a><br><a href="libraries/darts/darts/models/forecasting/nhits.py" title="libraries/darts/darts/models/forecasting/nhits.py :: NHiTSModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/2201.12886" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">NLinear<br><sub>NLinearModel</sub></td>
<td align="left">减去窗口最后一个值后线性预测变化，再加回该值。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/nlinear.py" title="libraries/neuralforecast/neuralforecast/models/nlinear.py :: NLinear">N&#8288;F</a><br><a href="libraries/darts/darts/models/forecasting/nlinear.py" title="libraries/darts/darts/models/forecasting/nlinear.py :: NLinearModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/26317" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Nonstationary_Transformer<br><sub>Non-stationary Transformer</sub></td>
<td align="left">在归一化输入之外学习去平稳注意力因子，补回序列的非平稳信息。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Nonstationary_Transformer.py" title="libraries/Time-Series-Library/models/Nonstationary_Transformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Nonstationary_Transformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Nonstationary_Transformer.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=ucNDIDRNjjv" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Nonstationary_Transformers">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">OmniScaleCNN</td>
<td align="left">组合不同尺度的一维卷积核，减少手工选择尺度的依赖。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/OmniScaleCNN.py" title="libraries/tsai/tsai/models/OmniScaleCNN.py :: OmniScaleCNN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2002.10061" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">PatchTST<br><sub>PatchTSTForecaster / PatchTST_pkg / PatchTST_v2</sub></td>
<td align="left">把连续时间点切为 patch，并以通道独立的 Transformer 建模长历史。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/PatchTST.py" title="libraries/Time-Series-Library/models/PatchTST.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/PatchTST.py" title="libraries/TimeSeriesLibrary-ZJ/models/PatchTST.py">Z&#8288;J</a><br><a href="libraries/tsai/tsai/models/PatchTST.py" title="libraries/tsai/tsai/models/PatchTST.py :: PatchTST">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/neuralforecast/models/patchtst.py" title="libraries/neuralforecast/neuralforecast/models/patchtst.py :: PatchTST">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/patch_tst.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/patch_tst.py :: PatchTST">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/_patch_tst_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/_patch_tst_v2.py :: PatchTST_v2">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/_patch_tst_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/_patch_tst_pkg.py :: PatchTST_pkg">P&#8288;F&#8288;³</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/_patch_tst_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/patch_tst/_patch_tst_forecaster_v2.py :: PatchTSTForecaster">P&#8288;F&#8288;⁴</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=Jbdc0vTOcol" title="模型论文">论&#8288;文</a><br><a href="https://github.com/yuqinie98/PatchTST">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">PatchTSTFMModel</td>
<td align="left">调用预训练 PatchTST foundation model，与从头训练版本区分。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/patchtst_fm_model.py" title="libraries/darts/darts/models/forecasting/patchtst_fm_model.py :: PatchTSTFMModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/2602.06909" title="模型论文">论&#8288;文</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">PAttn</td>
<td align="left">用 patch 嵌入和单层注意力进行预测，提供无需调用语言模型的对照入口。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/PAttn.py" title="libraries/Time-Series-Library/models/PAttn.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/PAttn.py" title="libraries/TimeSeriesLibrary-ZJ/models/PAttn.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2406.16964" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Prophet</td>
<td align="left">组合可分解的趋势、季节与节假日成分预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/prophet_model.py" title="libraries/darts/darts/models/forecasting/prophet_model.py :: Prophet">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Pyraformer</td>
<td align="left">构建多尺度金字塔，在层内与层间设置稀疏连接以传递长期信息。</td>
<td align="left"><a href="baselines/Pyraformer/" title="baselines/Pyraformer">原&#8288;版</a><br><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="baselines/Pyraformer/pyraformer/Pyraformer_LR.py" title="baselines/Pyraformer/pyraformer/Pyraformer_LR.py">原&#8288;版</a><br><a href="baselines/Pyraformer/pyraformer/Pyraformer_SS.py" title="baselines/Pyraformer/pyraformer/Pyraformer_SS.py">原&#8288;版&#8288;·&#8288;单&#8288;步</a><br><a href="libraries/Time-Series-Library/models/Pyraformer.py" title="libraries/Time-Series-Library/models/Pyraformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Pyraformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Pyraformer.py">Z&#8288;J</a></td>
<td align="left"><a href="baselines/Pyraformer/long_range_main.py" title="baselines/Pyraformer/long_range_main.py; 具体参数与任务按对应实现配置">原&#8288;版</a><br><a href="baselines/Pyraformer/single_step_main.py" title="baselines/Pyraformer/single_step_main.py">原&#8288;版&#8288;·&#8288;单&#8288;步</a><br><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://openreview.net/forum?id=0EXmFzUn5I" title="模型论文">论&#8288;文</a><br><a href="https://github.com/ant-research/Pyraformer">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RandomForestModel</td>
<td align="left">以随机森林学习滞后值和协变量到未来值的映射。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/random_forest.py" title="libraries/darts/darts/models/forecasting/random_forest.py :: RandomForestModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RecurrentNetwork<br><sub>RecurrentNetwork_pkg</sub></td>
<td align="left">以可配置的 LSTM 或 GRU 网络进行多步预测。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/rnn/_rnn.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/rnn/_rnn.py :: RecurrentNetwork">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/rnn/_rnn_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/rnn/_rnn_pkg.py :: RecurrentNetwork_pkg">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Reformer</td>
<td align="left">使用 Reformer 的局部敏感哈希注意力处理长序列。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Reformer.py" title="libraries/Time-Series-Library/models/Reformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Reformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Reformer.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://openreview.net/forum?id=rkgNKkHtvB" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RegressionEnsembleModel</td>
<td align="left">学习回归式组合器，融合多个基础预测结果。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/regression_ensemble_model.py" title="libraries/darts/darts/models/forecasting/regression_ensemble_model.py :: RegressionEnsembleModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ResCNN</td>
<td align="left">结合一维卷积和残差连接的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/ResCNN.py" title="libraries/tsai/tsai/models/ResCNN.py :: ResCNN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/pii/S0925231219311506" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ResNet</td>
<td align="left">通过残差一维卷积堆叠提取时间序列特征。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/ResNet.py" title="libraries/tsai/tsai/models/ResNet.py :: ResNet">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ResNetPlus</td>
<td align="left">通过残差一维卷积堆叠提取时间序列特征。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/ResNetPlus.py" title="libraries/tsai/tsai/models/ResNetPlus.py :: ResNetPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RMoK</td>
<td align="left">通过路由组合多种 KAN 专家，利用不同函数基预测。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/rmok.py" title="libraries/neuralforecast/neuralforecast/models/rmok.py :: RMoK">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2408.11306" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RNN<br><sub>RNNModel</sub></td>
<td align="left">通过循环隐藏状态编码历史，再预测未来或输出任务标签。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN.py" title="libraries/tsai/tsai/models/RNN.py :: RNN">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/neuralforecast/models/rnn.py" title="libraries/neuralforecast/neuralforecast/models/rnn.py :: RNN">N&#8288;F</a><br><a href="libraries/darts/darts/models/forecasting/rnn_model.py" title="libraries/darts/darts/models/forecasting/rnn_model.py :: RNNModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RNN_FCN</td>
<td align="left">融合 RNN 循环分支与全卷积分支的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCN.py" title="libraries/tsai/tsai/models/RNN_FCN.py :: RNN_FCN">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RNN_FCNPlus</td>
<td align="left">融合 RNN 循环分支与全卷积分支的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNN_FCNPlus.py" title="libraries/tsai/tsai/models/RNN_FCNPlus.py :: RNN_FCNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RNNAttention</td>
<td align="left">结合 RNN 循环表示和注意力编码模块的序列网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNAttention.py" title="libraries/tsai/tsai/models/RNNAttention.py :: RNNAttention">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RNNAttentionPlus</td>
<td align="left">结合 RNN 循环表示和注意力编码模块的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNAttentionPlus.py" title="libraries/tsai/tsai/models/RNNAttentionPlus.py :: RNNAttentionPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">RNNPlus</td>
<td align="left">RNN 的 tsai 可配置骨干与任务头变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/RNNPlus.py" title="libraries/tsai/tsai/models/RNNPlus.py :: RNNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">ROCKET<br><sub>RocketClassifier / RocketRegressor</sub></td>
<td align="left">用大量随机卷积核生成统计特征，再接线性分类或回归器。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/ROCKET.py" title="libraries/tsai/tsai/models/ROCKET.py :: RocketClassifier">t&#8288;s&#8288;a&#8288;i&#8288;¹</a><br><a href="libraries/tsai/tsai/models/ROCKET.py" title="libraries/tsai/tsai/models/ROCKET.py :: RocketRegressor">t&#8288;s&#8288;a&#8288;i&#8288;²</a><br><a href="libraries/tsai/tsai/models/ROCKET_Pytorch.py" title="libraries/tsai/tsai/models/ROCKET_Pytorch.py :: ROCKET">t&#8288;s&#8288;a&#8288;i&#8288;³</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1910.13051" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Samformer<br><sub>SamformerForecaster</sub></td>
<td align="left">以浅层注意力组织变量关系，结合对应训练策略预测。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/samformer/_samformer_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/samformer/_samformer_v2.py :: Samformer">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/samformer/_samformer_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/samformer/_samformer_forecaster_v2.py :: SamformerForecaster">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">SCINet<br><sub>SCINetForecaster / SCINet_v2</sub></td>
<td align="left">递归拆分奇偶时间点，用交互卷积交换信息后重新合并序列。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting; 同家族的接口或版本适配类，保留类名与源码位置，不另计新算法家族。">P&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/SCINet.py" title="libraries/Time-Series-Library/models/SCINet.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/SCINet.py" title="libraries/TimeSeriesLibrary-ZJ/models/SCINet.py">Z&#8288;J</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/scinet/_scinet_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/scinet/_scinet_v2.py :: SCINet_v2">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/scinet/_scinet_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/scinet/_scinet_forecaster_v2.py :: SCINetForecaster">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=AyajSjTAzmg" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">SegRNN</td>
<td align="left">将序列分段后交给 GRU 编码，再按预测片段输出未来值。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/SegRNN.py" title="libraries/Time-Series-Library/models/SegRNN.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/SegRNN.py" title="libraries/TimeSeriesLibrary-ZJ/models/SegRNN.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/abs/2308.11200.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">SKLearnClassifierModel</td>
<td align="left">将 scikit-learn 分类器接入序列预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sklearn_model.py" title="libraries/darts/darts/models/forecasting/sklearn_model.py :: SKLearnClassifierModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">SKLearnModel</td>
<td align="left">将 scikit-learn 回归器接入滞后特征预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sklearn_model.py" title="libraries/darts/darts/models/forecasting/sklearn_model.py :: SKLearnModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">SOFTS<br><sub>SOFTSForecaster</sub></td>
<td align="left">将多变量聚合到共享核心，再融合回各变量，控制交互成本。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/softs.py" title="libraries/neuralforecast/neuralforecast/models/softs.py :: SOFTS">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/softs/_softs_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/softs/_softs_v2.py :: SOFTS">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/softs/_softs_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/softs/_softs_forecaster_v2.py :: SOFTSForecaster">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2404.14197" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">SOFTSSharp</td>
<td align="left">在 SOFTS 类结构中加入随机变量位置编码。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/softssharp.py" title="libraries/neuralforecast/neuralforecast/models/softssharp.py :: SOFTSSharp">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://github.com/hljubic/SOFTSsharp">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">StatsForecastModel</td>
<td align="left">把 StatsForecast 统计模型接入 Darts 接口。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts; 公开预测适配器、集成或校准封装；不是独立神经网络结构。">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_model.py" title="libraries/darts/darts/models/forecasting/sf_model.py :: StatsForecastModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">StemGNN</td>
<td align="left">结合图傅里叶与时间傅里叶变换，学习变量关系和时间依赖。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/stemgnn.py" title="libraries/neuralforecast/neuralforecast/models/stemgnn.py :: StemGNN">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://proceedings.neurips.cc/paper/2020/hash/cdf6581cb7aca4b7e19ef136c6e601a5-Abstract.html" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Sundial</td>
<td align="left">调用外部预训练 Sundial 时序模型，保留其零样本预测适配接口。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Sundial.py" title="libraries/Time-Series-Library/models/Sundial.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2502.00816" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">T0<br><sub>T0Model</sub></td>
<td align="left">调用 T0 预训练时序模型，支持多变量和协变量。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/t0_model.py" title="libraries/darts/darts/models/forecasting/t0_model.py :: T0Model">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TabFusionTransformer</td>
<td align="left">将类别和连续特征编码为 token，再用注意力融合。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TabFusionTransformer.py" title="libraries/tsai/tsai/models/TabFusionTransformer.py :: TabFusionTransformer">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TabModel</td>
<td align="left">对类别嵌入和连续表格变量进行前馈建模。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TabModel.py" title="libraries/tsai/tsai/models/TabModel.py :: TabModel">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TabTransformer</td>
<td align="left">以注意力上下文化类别变量，再结合连续变量输出。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TabTransformer.py" title="libraries/tsai/tsai/models/TabTransformer.py :: TabTransformer">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2012.06678" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TBATS</td>
<td align="left">组合变换、趋势、ARMA 误差和三角季节项。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/sf_tbats.py" title="libraries/darts/darts/models/forecasting/sf_tbats.py :: TBATS">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TCN<br><sub>TCNModel</sub></td>
<td align="left">叠加因果与扩张卷积，扩展时间感受野。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TCN.py" title="libraries/tsai/tsai/models/TCN.py :: TCN">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/neuralforecast/models/tcn.py" title="libraries/neuralforecast/neuralforecast/models/tcn.py :: TCN">N&#8288;F</a><br><a href="libraries/darts/darts/models/forecasting/tcn_model.py" title="libraries/darts/darts/models/forecasting/tcn_model.py :: TCNModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/1803.01271" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TemporalFusionTransformer<br><sub>TFT / TFTForecaster / TFTModel / TemporalFusionTransformer_pkg</sub></td>
<td align="left">通过变量选择、门控循环层和注意力融合历史与时间协变量。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TemporalFusionTransformer.py" title="libraries/Time-Series-Library/models/TemporalFusionTransformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/TemporalFusionTransformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/TemporalFusionTransformer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/tft.py" title="libraries/neuralforecast/neuralforecast/models/tft.py :: TFT">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft.py :: TemporalFusionTransformer">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft_forecaster_v2.py :: TFTForecaster">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/temporal_fusion_transformer/_tft_pkg.py :: TemporalFusionTransformer_pkg">P&#8288;F&#8288;³</a><br><a href="libraries/darts/darts/models/forecasting/tft_model.py" title="libraries/darts/darts/models/forecasting/tft_model.py :: TFTModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/1912.09363" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Theta</td>
<td align="left">组合趋势与平滑后的 Theta 线进行外推。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/theta.py" title="libraries/darts/darts/models/forecasting/theta.py :: Theta">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TiDE<br><sub>TIDE / TIDEForecaster / TiDEModel / TiDEModel_pkg</sub></td>
<td align="left">用残差 MLP 编码历史和协变量，再通过稠密解码与时间投影得到预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TiDE.py" title="libraries/Time-Series-Library/models/TiDE.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/TiDE.py" title="libraries/TimeSeriesLibrary-ZJ/models/TiDE.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/tide.py" title="libraries/neuralforecast/neuralforecast/models/tide.py :: TiDE">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide.py :: TiDEModel">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide_pkg.py :: TiDEModel_pkg">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide_dsipts/_tide_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide_dsipts/_tide_v2.py :: TIDE">P&#8288;F&#8288;³</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide_dsipts/_tide_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/tide/_tide_dsipts/_tide_forecaster_v2.py :: TIDEForecaster">P&#8288;F&#8288;⁴</a><br><a href="libraries/darts/darts/models/forecasting/tide_model.py" title="libraries/darts/darts/models/forecasting/tide_model.py :: TiDEModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2304.08424.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Time-LLM<br><sub>TimeLLM</sub></td>
<td align="left">把时序 patch 对齐到文本原型，并用提示词与冻结语言模型生成预测表示。</td>
<td align="left"><a href="baselines/Time-LLM/" title="baselines/Time-LLM">原&#8288;版</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="baselines/Time-LLM/models/TimeLLM.py" title="baselines/Time-LLM/models/TimeLLM.py">原&#8288;版</a><br><a href="libraries/neuralforecast/neuralforecast/models/timellm.py" title="libraries/neuralforecast/neuralforecast/models/timellm.py :: TimeLLM">N&#8288;F</a></td>
<td align="left"><a href="baselines/Time-LLM/run_main.py" title="baselines/Time-LLM/run_main.py; 具体参数与任务按对应实现配置">原&#8288;版</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.01728" title="模型论文">论&#8288;文</a><br><a href="https://github.com/KimMeen/Time-LLM">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimeFilter</td>
<td align="left">将时序 patch 组织成图，用邻接构造和路由过滤关系后预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TimeFilter.py" title="libraries/Time-Series-Library/models/TimeFilter.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/abs/2501.13041" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimeMixer</td>
<td align="left">将序列分为多个尺度和趋势季节成分，通过 MLP 混合并汇总多尺度预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TimeMixer.py" title="libraries/Time-Series-Library/models/TimeMixer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/TimeMixer.py" title="libraries/TimeSeriesLibrary-ZJ/models/TimeMixer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/timemixer.py" title="libraries/neuralforecast/neuralforecast/models/timemixer.py :: TimeMixer">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=7oLshfEIC2" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimeMoE<br><sub>Time-MoE</sub></td>
<td align="left">调用预训练 TimeMoE 混合专家时序模型，库内入口用于零样本预测。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TimeMoE.py" title="libraries/Time-Series-Library/models/TimeMoE.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2409.16040" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimesFM</td>
<td align="left">调用预训练 TimesFM 预测接口，外部权重与运行依赖单独加载。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TimesFM.py" title="libraries/Time-Series-Library/models/TimesFM.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.10688" title="链接为上游 README 列出的 TimesFM 系列论文；当前接口实际调用 TimesFM 2.5，具体版本以源码和权重标识为准。">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimesFM2p5<br><sub>TimesFM2p5Model</sub></td>
<td align="left">调用 TimesFM 2.5 预训练模型，保留版本特定接口。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/timesfm2p5_model.py" title="libraries/darts/darts/models/forecasting/timesfm2p5_model.py :: TimesFM2p5Model">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.10688" title="TimesFM 系列基础论文，不将其标为 2.5 权重版本的专属论文。">论&#8288;文</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimesFM3<br><sub>TimesFM3Model</sub></td>
<td align="left">调用 TimesFM 3.0 预训练模型，与早期版本分开索引。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/timesfm3_model.py" title="libraries/darts/darts/models/forecasting/timesfm3_model.py :: TimesFM3Model">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.10688" title="TimesFM 系列基础论文，不将其标为 3.0 权重版本的专属论文。">论&#8288;文</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimesNet</td>
<td align="left">用 FFT 寻找周期，将序列按周期重排为二维，再用 Inception 卷积提取变化。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TimesNet.py" title="libraries/Time-Series-Library/models/TimesNet.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/TimesNet.py" title="libraries/TimeSeriesLibrary-ZJ/models/TimesNet.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/timesnet.py" title="libraries/neuralforecast/neuralforecast/models/timesnet.py :: TimesNet">N&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=ju_Uqw384Oq" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TimeXer<br><sub>TimeXerForecaster / TimeXer_pkg</sub></td>
<td align="left">结合目标序列的 patch 与外生变量表示，用注意力融合两类信息。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TimeXer.py" title="libraries/Time-Series-Library/models/TimeXer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/TimeXer.py" title="libraries/TimeSeriesLibrary-ZJ/models/TimeXer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/timexer.py" title="libraries/neuralforecast/neuralforecast/models/timexer.py :: TimeXer">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/timexer/_timexer.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/timexer/_timexer.py :: TimeXer">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/timexer/_timexer_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/timexer/_timexer_pkg.py :: TimeXer_pkg">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/timexer/_timexer_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/timexer/_timexer_forecaster_v2.py :: TimeXerForecaster">P&#8288;F&#8288;³</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2402.19072" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TiRex<br><sub>TiRexModel</sub></td>
<td align="left">调用 tirex-ts 的预训练模型，为库内零样本预测提供接口。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TiRex.py" title="libraries/Time-Series-Library/models/TiRex.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/darts/darts/models/forecasting/tirex_model.py" title="libraries/darts/darts/models/forecasting/tirex_model.py :: TiRexModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2505.23719" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TiRex2<br><sub>TiRex2Model</sub></td>
<td align="left">调用 TiRex-2，支持多变量及过去、未来协变量预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/tirex2_model.py" title="libraries/darts/darts/models/forecasting/tirex2_model.py :: TiRex2Model">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/abs/2607.01204" title="模型论文">论&#8288;文</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">Transformer<br><sub>TransformerModel / VanillaTransformer</sub></td>
<td align="left">使用标准编码器和解码器注意力结构，作为其他改造模型的对照。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/Transformer.py" title="libraries/Time-Series-Library/models/Transformer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/Transformer.py" title="libraries/TimeSeriesLibrary-ZJ/models/Transformer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/vanillatransformer.py" title="libraries/neuralforecast/neuralforecast/models/vanillatransformer.py :: VanillaTransformer">N&#8288;F</a><br><a href="libraries/darts/darts/models/forecasting/transformer_model.py" title="libraries/darts/darts/models/forecasting/transformer_model.py :: TransformerModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TransformerGRUPlus</td>
<td align="left">将 Transformer 编码与 GRU 循环结构结合的时序网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TransformerRNNPlus.py" title="libraries/tsai/tsai/models/TransformerRNNPlus.py :: TransformerGRUPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TransformerLSTMPlus</td>
<td align="left">将 Transformer 编码与 LSTM 循环结构结合的时序网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TransformerRNNPlus.py" title="libraries/tsai/tsai/models/TransformerRNNPlus.py :: TransformerLSTMPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TransformerModel</td>
<td align="left">tsai 的通用序列 Transformer 接口，与其他库实现分别保留。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TransformerModel.py" title="libraries/tsai/tsai/models/TransformerModel.py :: TransformerModel">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TransformerRNNPlus</td>
<td align="left">将 Transformer 编码与 RNN 循环结构结合的时序网络。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TransformerRNNPlus.py" title="libraries/tsai/tsai/models/TransformerRNNPlus.py :: TransformerRNNPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSiTPlus</td>
<td align="left">将 ViT 式 token 和 Transformer 结构适配到时间序列。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TSiTPlus.py" title="libraries/tsai/tsai/models/TSiTPlus.py :: TSiTPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2010.11929" title="由所链接的方法适配而来，不宣称此时序变体有独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSMixer<br><sub>TSMixerForecaster / TSMixerModel</sub></td>
<td align="left">交替沿时间轴和变量轴使用 MLP 混合信息，再映射到预测窗口。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a><br><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a><br><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/TSMixer.py" title="libraries/Time-Series-Library/models/TSMixer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/TSMixer.py" title="libraries/TimeSeriesLibrary-ZJ/models/TSMixer.py">Z&#8288;J</a><br><a href="libraries/neuralforecast/neuralforecast/models/tsmixer.py" title="libraries/neuralforecast/neuralforecast/models/tsmixer.py :: TSMixer">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/tsmixer/_tsmixer_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/tsmixer/_tsmixer_v2.py :: TSMixer">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/tsmixer/_tsmixer_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/tsmixer/_tsmixer_forecaster_v2.py :: TSMixerForecaster">P&#8288;F&#8288;²</a><br><a href="libraries/darts/darts/models/forecasting/tsmixer_model.py" title="libraries/darts/darts/models/forecasting/tsmixer_model.py :: TSMixerModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a><br><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a><br><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a><br><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2303.06053.pdf" title="模型论文">论&#8288;文</a><br><a href="https://github.com/thuml/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b&#8288;项&#8288;目</a><br><a href="https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary">Z&#8288;J&#8288;项&#8288;目</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a><br><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSMixerx</td>
<td align="left">在时间与变量混合 MLP 中接入外生变量和静态特征。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/tsmixerx.py" title="libraries/neuralforecast/neuralforecast/models/tsmixerx.py :: TSMixerx">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2303.06053" title="引用当前实现列出的基础方法或相关工作，不宣称变体另有专属论文。">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSPerceiver</td>
<td align="left">以交叉注意力将长输入压缩到潜在表示，再在潜在空间建模。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TSPerceiver.py" title="libraries/tsai/tsai/models/TSPerceiver.py :: TSPerceiver">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2107.14795" title="由所链接的方法适配而来，不宣称此时序变体有独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSSequencerPlus</td>
<td align="left">以双向 LSTM 混合序列位置，并结合前馈块。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TSSequencerPlus.py" title="libraries/tsai/tsai/models/TSSequencerPlus.py :: TSSequencerPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/2205.01972" title="由所链接的方法适配而来，不宣称此时序变体有独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TST</td>
<td align="left">使用时序嵌入和编码器注意力构建序列分类或回归。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TST.py" title="libraries/tsai/tsai/models/TST.py :: TST">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3447548.3467401" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSTabFusionTransformer</td>
<td align="left">通过 Transformer 融合时间序列与表格特征。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TabFusionTransformer.py" title="libraries/tsai/tsai/models/TabFusionTransformer.py :: TSTabFusionTransformer">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">TSTPlus</td>
<td align="left">使用时序嵌入和编码器注意力构建序列分类或回归。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/TSTPlus.py" title="libraries/tsai/tsai/models/TSTPlus.py :: TSTPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3447548.3467401" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">UniTS<br><sub>UniTSForecaster</sub></td>
<td align="left">以统一时序表示和结构适配多种序列任务。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/units/_units_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/units/_units_v2.py :: UniTS">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/units/_units_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/units/_units_forecaster_v2.py :: UniTSForecaster">P&#8288;F&#8288;²</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2403.00131" title="模型论文">论&#8288;文</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">VARIMA</td>
<td align="left">把多个序列联合建模为向量自回归、差分和移动平均过程。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/varima.py" title="libraries/darts/darts/models/forecasting/varima.py :: VARIMA">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">WPMixer</td>
<td align="left">先用离散小波拆分序列，再对不同分量做 patch 混合与预测重建。</td>
<td align="left"><a href="libraries/Time-Series-Library/" title="libraries/Time-Series-Library">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/" title="libraries/TimeSeriesLibrary-ZJ">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/models/WPMixer.py" title="libraries/Time-Series-Library/models/WPMixer.py">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/models/WPMixer.py" title="libraries/TimeSeriesLibrary-ZJ/models/WPMixer.py">Z&#8288;J</a></td>
<td align="left"><a href="libraries/Time-Series-Library/run.py" title="libraries/Time-Series-Library/run.py; 具体参数与任务按对应实现配置">T&#8288;S&#8288;L&#8288;i&#8288;b</a><br><a href="libraries/TimeSeriesLibrary-ZJ/run.py" title="libraries/TimeSeriesLibrary-ZJ/run.py; 具体参数与任务按对应实现配置">Z&#8288;J</a></td>
<td align="left"><a href="https://arxiv.org/abs/2412.17176" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Secure-and-Intelligent-Systems-Lab/WPMixer">原&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XceptionTime</td>
<td align="left">将深度可分离卷积与多尺度时序模块结合。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/XceptionTime.py" title="libraries/tsai/tsai/models/XceptionTime.py :: XceptionTime">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1911.03803" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XceptionTimePlus</td>
<td align="left">将深度可分离卷积与多尺度时序模块结合。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/XceptionTimePlus.py" title="libraries/tsai/tsai/models/XceptionTimePlus.py :: XceptionTimePlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://arxiv.org/abs/1911.03803" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XCM</td>
<td align="left">同时提取时间与变量卷积特征，支持解释序列分类结果。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/XCM.py" title="libraries/tsai/tsai/models/XCM.py :: XCM">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://hal.inria.fr/hal-03469487/document" title="模型论文">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XCMPlus</td>
<td align="left">同时提取时间与变量卷积特征，支持解释序列分类结果。 此项为 tsai 的 Plus 可配置变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/XCMPlus.py" title="libraries/tsai/tsai/models/XCMPlus.py :: XCMPlus">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://hal.inria.fr/hal-03469487/document" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">论&#8288;文</a><br><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XCoordTime</td>
<td align="left">结合坐标信息与可分离卷积的 InceptionTimePlus 变体。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/InceptionTimePlus.py" title="libraries/tsai/tsai/models/InceptionTimePlus.py :: XCoordTime">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XGBClassifierModel</td>
<td align="left">以 XGBoost 分类器处理离散目标预测。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/xgboost.py" title="libraries/darts/darts/models/forecasting/xgboost.py :: XGBClassifierModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XGBModel</td>
<td align="left">以 XGBoost 提升树对滞后特征和协变量回归。</td>
<td align="left"><a href="libraries/darts/" title="libraries/darts">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/darts/models/forecasting/xgboost.py" title="libraries/darts/darts/models/forecasting/xgboost.py :: XGBModel">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="libraries/darts/README.md" title="libraries/darts/README.md; 具体参数与任务按对应实现配置">D&#8288;a&#8288;r&#8288;t&#8288;s</a></td>
<td align="left"><a href="https://github.com/unit8co/darts">D&#8288;a&#8288;r&#8288;t&#8288;s&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XLinear</td>
<td align="left">以轻量 MLP 结合历史和外生输入，直接输出未来窗口。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/xlinear.py" title="libraries/neuralforecast/neuralforecast/models/xlinear.py :: XLinear">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2601.09237" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">xLSTM</td>
<td align="left">使用扩展 LSTM 记忆结构处理历史，再接入预测头。</td>
<td align="left"><a href="libraries/neuralforecast/" title="libraries/neuralforecast">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/neuralforecast/models/xlstm.py" title="libraries/neuralforecast/neuralforecast/models/xlstm.py :: xLSTM">N&#8288;F</a></td>
<td align="left"><a href="libraries/neuralforecast/README.md" title="libraries/neuralforecast/README.md; 具体参数与任务按对应实现配置">N&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/abs/2405.04517" title="模型论文">论&#8288;文</a><br><a href="https://github.com/Nixtla/neuralforecast">N&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">xLSTMTime<br><sub>xLSTMTimeForecaster / xLSTMTime_pkg / xLSTMTime_v2</sub></td>
<td align="left">面向时间序列预测的 xLSTM 适配结构，与通用 xLSTM 分开保留。</td>
<td align="left"><a href="libraries/pytorch-forecasting/" title="libraries/pytorch-forecasting">P&#8288;F</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm.py :: xLSTMTime">P&#8288;F&#8288;¹</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm_v2.py :: xLSTMTime_v2">P&#8288;F&#8288;²</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm_pkg.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm_pkg.py :: xLSTMTime_pkg">P&#8288;F&#8288;³</a><br><a href="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm_forecaster_v2.py" title="libraries/pytorch-forecasting/pytorch_forecasting/models/xlstm/_xlstm_forecaster_v2.py :: xLSTMTimeForecaster">P&#8288;F&#8288;⁴</a></td>
<td align="left"><a href="libraries/pytorch-forecasting/README.md" title="libraries/pytorch-forecasting/README.md; 具体参数与任务按对应实现配置">P&#8288;F</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2407.10240" title="模型论文">论&#8288;文</a><br><a href="https://github.com/sktime/pytorch-forecasting">P&#8288;F&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XResNet1d<br><sub>xresnet1d101 / xresnet1d152 / xresnet1d18 / xresnet1d18_deep / xresnet1d18_deeper / xresnet1d34 / xresnet1d34_deep / xresnet1d34_deeper / xresnet1d50 / xresnet1d50_deep / xresnet1d50_deeper</sub></td>
<td align="left">将 xresnet 架构适配为一维卷积，保留多种深度工厂。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai; 同家族的深度或宽度配置工厂，保留真实调用名称；不另计新算法。">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d18">t&#8288;s&#8288;a&#8288;i&#8288;¹</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d34">t&#8288;s&#8288;a&#8288;i&#8288;²</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d50">t&#8288;s&#8288;a&#8288;i&#8288;³</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d101">t&#8288;s&#8288;a&#8288;i&#8288;⁴</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d152">t&#8288;s&#8288;a&#8288;i&#8288;⁵</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d18_deep">t&#8288;s&#8288;a&#8288;i&#8288;⁶</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d34_deep">t&#8288;s&#8288;a&#8288;i&#8288;⁷</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d50_deep">t&#8288;s&#8288;a&#8288;i&#8288;⁸</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d18_deeper">t&#8288;s&#8288;a&#8288;i&#8288;⁹</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d34_deeper">t&#8288;s&#8288;a&#8288;i&#8288;¹&#8288;⁰</a><br><a href="libraries/tsai/tsai/models/XResNet1d.py" title="libraries/tsai/tsai/models/XResNet1d.py :: xresnet1d50_deeper">t&#8288;s&#8288;a&#8288;i&#8288;¹&#8288;¹</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
<tr>
<td align="left">XResNet1dPlus<br><sub>xresnet1d101plus / xresnet1d152plus / xresnet1d18_deeperplus / xresnet1d18_deepplus / xresnet1d18plus / xresnet1d34_deeperplus / xresnet1d34_deepplus / xresnet1d34plus / xresnet1d50_deeperplus / xresnet1d50_deepplus / xresnet1d50plus</sub></td>
<td align="left">一维 xresnet 的增强版本，保留可配置头和深度工厂。</td>
<td align="left"><a href="libraries/tsai/" title="libraries/tsai">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: XResNet1dPlus">t&#8288;s&#8288;a&#8288;i&#8288;¹</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d18plus">t&#8288;s&#8288;a&#8288;i&#8288;²</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d34plus">t&#8288;s&#8288;a&#8288;i&#8288;³</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d50plus">t&#8288;s&#8288;a&#8288;i&#8288;⁴</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d101plus">t&#8288;s&#8288;a&#8288;i&#8288;⁵</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d152plus">t&#8288;s&#8288;a&#8288;i&#8288;⁶</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d18_deepplus">t&#8288;s&#8288;a&#8288;i&#8288;⁷</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d34_deepplus">t&#8288;s&#8288;a&#8288;i&#8288;⁸</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d50_deepplus">t&#8288;s&#8288;a&#8288;i&#8288;⁹</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d18_deeperplus">t&#8288;s&#8288;a&#8288;i&#8288;¹&#8288;⁰</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d34_deeperplus">t&#8288;s&#8288;a&#8288;i&#8288;¹&#8288;¹</a><br><a href="libraries/tsai/tsai/models/XResNet1dPlus.py" title="libraries/tsai/tsai/models/XResNet1dPlus.py :: xresnet1d50_deeperplus">t&#8288;s&#8288;a&#8288;i&#8288;¹&#8288;²</a></td>
<td align="left"><a href="libraries/tsai/README.md" title="libraries/tsai/README.md; 具体参数与任务按对应实现配置">t&#8288;s&#8288;a&#8288;i</a></td>
<td align="left"><a href="https://github.com/timeseriesAI/tsai">t&#8288;s&#8288;a&#8288;i&#8288;项&#8288;目</a></td>
</tr>
</tbody>
</table>

运行入口指向该实现的命令脚本或使用文档；支持任务与参数以对应源码为准。系列论文和加载变体的区别见论文链接的悬停说明。

<!-- MODEL_DETAILS_END -->

## 完整模型库与教程

| 模型库 | 主要内容 | 原始目录 |
| --- | --- | --- |
| Time-Series-Library | 多任务时序模型、预测、插补、异常检测、分类与预训练模型接口 | [TSLib](libraries/Time-Series-Library/) |
| TimeSeriesLibrary · ZJ | 保留该项目完整模型、组件、任务脚本和教程，提供另一套实现入口 | [ZJ 库](libraries/TimeSeriesLibrary-ZJ/) |
| tsai | 时间序列分类、回归、预测、数据变换与大量网络变体 | [tsai](libraries/tsai/) |
| NeuralForecast | 神经预测、训练与滚动评估接口 | [NeuralForecast](libraries/neuralforecast/) |
| PyTorch Forecasting | 数据集、神经预测器、概率损失与训练接口 | [PyTorch Forecasting](libraries/pytorch-forecasting/) |
| Darts | 统计预测、机器学习、深度预测、集成与预训练接口 | [Darts](libraries/darts/) |

六个库均完整保留固定提交受 Git 跟踪的文件，包括源码、教程、测试、示例和仓库内已有的数据资源。各库的模型入口见[统一目录](docs/model-catalog.md)，环境与任务流程见[模型库指南](docs/library-guide.md)。

## 目录结构

```text
zpb-time-series-research/
├── baselines/                 # 六个独立项目，保留原文件名与目录
│   ├── EMAformer/
│   ├── Pyraformer/
│   ├── Informer2020/
│   ├── Autoformer/
│   ├── ETSformer/
│   └── Time-LLM/
├── libraries/
│   ├── Time-Series-Library/
│   ├── TimeSeriesLibrary-ZJ/
│   ├── tsai/
│   ├── neuralforecast/
│   ├── pytorch-forecasting/
│   └── darts/
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

已建立 **12 个来源、2503 个原始文件**的归档与逐文件来源校验，具体版本见[来源记录](docs/upstream-sources.md)。完整范围是锁定提交中受 Git 跟踪的全部文件；外部训练数据和模型权重按各项目要求另行准备。模型训练和论文指标复现尚未执行。Pyraformer 的可选 TVM gitlink 状态见来源记录。

后续改进可先在 `research/` 下建立独立版本，通过实验记录保存基线提交、配置和结果。各上游论文的引用条目保留在对应原 README 中；许可证说明见 [LICENSES.md](LICENSES.md)。
