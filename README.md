# zpb-time-series-research

个人时间序列研究工作区，按技术路线整合模型介绍、实现索引和实验流程。**点击模型名称先读中文介绍**，理解核心思路、适用问题与局限，再进入代码和实验。每个模型使用相同展示字段，同名模型的实现并列保留。

当前模型统一按技术路线放在 `models/`：每个模型都有介绍、实现索引和运行说明。完整源码保存在 `_sources/`，版本与文件记录见 [sources.lock.json](sources.lock.json)。

## 从这里开始

| 想做什么 | 去哪里 |
| --- | --- |
| 按名称或分类查模型 | [全部模型与任务索引](docs/model-catalog.md) |
| 查模型、注意力、嵌入、数据加载代码 | [源码导航](docs/model-guide.md) |
| 共用数据划分、训练、指标与结果比较 | [统一实验入口](docs/integration.md) · [可运行示例](examples/forecasting/README.md) |
| 查环境、数据位置和训练命令 | [运行指南](docs/running-baselines.md) |
| 查上游版本、导入范围和来源校验 | [来源记录](docs/upstream-sources.md) · [版本锁定清单](sources.lock.json) |
| 写自己的模型和改进思路 | [研究工作区](research/README.md) |
| 记录配置、消融实验与结果 | [实验管理](experiments/README.md) |
| 整理数据来源、划分和预处理 | [数据索引](data/README.md) |

## 统一研究流程

`python -m zpbts list` 查模型，`show` 查实现，`run` 跑统一配置，`compare` 比较同一数据协议的结果。已实际接通 DLinear、TSMixer 和三个朴素对照方法，统一时间切分、训练归一化、原尺度指标与预测导出。完整命令见[整合实验指南](docs/integration.md)。

## 全部模型，按技术路线分类

**从[统一模型目录](docs/model-catalog.md)开始**。每个模型名称直接打开已渲染的中文介绍，同名模型的不同实现放在介绍后方。

<!-- MODEL_CATALOG_START -->

当前 **187 个模型家族**、**326 个实现入口**。点击模型名称先阅读介绍，再选择实现。

| 分类 | 全部模型 |
| --- | --- |
| [线性与MLP](docs/model-catalog.md#category-linear_mlp) | [DecoderMLP](models/linear_mlp/decodermlp/README.md) · [DeepNPTS](models/linear_mlp/deepnpts/README.md) · [DLinear](models/linear_mlp/dlinear/README.md) · [gMLP](models/linear_mlp/gmlp/README.md) · [KAN](models/linear_mlp/kan/README.md) · [LightTS](models/linear_mlp/lightts/README.md) · [MLP](models/linear_mlp/mlp/README.md) · [MLPMultivariate](models/linear_mlp/mlpmultivariate/README.md) · [NBEATS](models/linear_mlp/nbeats/README.md) · [NBEATSKAN](models/linear_mlp/nbeatskan/README.md) · [NBEATSx](models/linear_mlp/nbeatsx/README.md) · [NHITS](models/linear_mlp/nhits/README.md) · [NLinear](models/linear_mlp/nlinear/README.md) · [RMoK](models/linear_mlp/rmok/README.md) · [SOFTS](models/linear_mlp/softs/README.md) · [SOFTSSharp](models/linear_mlp/softssharp/README.md) · [TabModel](models/linear_mlp/tabmodel/README.md) · [TiDE](models/linear_mlp/tide/README.md) · [TSMixer](models/linear_mlp/tsmixer/README.md) · [TSMixerx](models/linear_mlp/tsmixerx/README.md) · [XLinear](models/linear_mlp/xlinear/README.md) |
| [循环与卷积](docs/model-catalog.md#category-recurrent_convolution) | [BiTCN](models/recurrent_convolution/bitcn/README.md) · [BlockRNN](models/recurrent_convolution/blockrnn/README.md) · [DeepAR](models/recurrent_convolution/deepar/README.md) · [DilatedRNN](models/recurrent_convolution/dilatedrnn/README.md) · [FCN](models/recurrent_convolution/fcn/README.md) · [FCNPlus](models/recurrent_convolution/fcnplus/README.md) · [GRU](models/recurrent_convolution/gru/README.md) · [GRU_FCN](models/recurrent_convolution/gru_fcn/README.md) · [GRU_FCNPlus](models/recurrent_convolution/gru_fcnplus/README.md) · [GRUAttention](models/recurrent_convolution/gruattention/README.md) · [GRUAttentionPlus](models/recurrent_convolution/gruattentionplus/README.md) · [GRUPlus](models/recurrent_convolution/gruplus/README.md) · [HydraMultiRocketPlus](models/recurrent_convolution/hydramultirocketplus/README.md) · [HydraPlus](models/recurrent_convolution/hydraplus/README.md) · [InceptionRocketPlus](models/recurrent_convolution/inceptionrocketplus/README.md) · [InceptionTime](models/recurrent_convolution/inceptiontime/README.md) · [InceptionTimePlus](models/recurrent_convolution/inceptiontimeplus/README.md) · [InCoordTime](models/recurrent_convolution/incoordtime/README.md) · [LSTM](models/recurrent_convolution/lstm/README.md) · [LSTM_FCN](models/recurrent_convolution/lstm_fcn/README.md) · [LSTM_FCNPlus](models/recurrent_convolution/lstm_fcnplus/README.md) · [LSTMAttention](models/recurrent_convolution/lstmattention/README.md) · [LSTMAttentionPlus](models/recurrent_convolution/lstmattentionplus/README.md) · [LSTMPlus](models/recurrent_convolution/lstmplus/README.md) · [MGRU_FCN](models/recurrent_convolution/mgru_fcn/README.md) · [MGRU_FCNPlus](models/recurrent_convolution/mgru_fcnplus/README.md) · [MICN](models/recurrent_convolution/micn/README.md) · [MiniRocket](models/recurrent_convolution/minirocket/README.md) · [MiniRocketPlus](models/recurrent_convolution/minirocketplus/README.md) · [MLSTM_FCN](models/recurrent_convolution/mlstm_fcn/README.md) · [MLSTM_FCNPlus](models/recurrent_convolution/mlstm_fcnplus/README.md) · [ModernTCN](models/recurrent_convolution/moderntcn/README.md) · [MRNN_FCN](models/recurrent_convolution/mrnn_fcn/README.md) · [MRNN_FCNPlus](models/recurrent_convolution/mrnn_fcnplus/README.md) · [MultiRocketPlus](models/recurrent_convolution/multirocketplus/README.md) · [OmniScaleCNN](models/recurrent_convolution/omniscalecnn/README.md) · [RecurrentNetwork](models/recurrent_convolution/recurrentnetwork/README.md) · [ResCNN](models/recurrent_convolution/rescnn/README.md) · [ResNet](models/recurrent_convolution/resnet/README.md) · [ResNetPlus](models/recurrent_convolution/resnetplus/README.md) · [RNN](models/recurrent_convolution/rnn/README.md) · [RNN_FCN](models/recurrent_convolution/rnn_fcn/README.md) · [RNN_FCNPlus](models/recurrent_convolution/rnn_fcnplus/README.md) · [RNNAttention](models/recurrent_convolution/rnnattention/README.md) · [RNNAttentionPlus](models/recurrent_convolution/rnnattentionplus/README.md) · [RNNPlus](models/recurrent_convolution/rnnplus/README.md) · [ROCKET](models/recurrent_convolution/rocket/README.md) · [SCINet](models/recurrent_convolution/scinet/README.md) · [SegRNN](models/recurrent_convolution/segrnn/README.md) · [TCN](models/recurrent_convolution/tcn/README.md) · [TimesNet](models/recurrent_convolution/timesnet/README.md) · [TSSequencerPlus](models/recurrent_convolution/tssequencerplus/README.md) · [XceptionTime](models/recurrent_convolution/xceptiontime/README.md) · [XceptionTimePlus](models/recurrent_convolution/xceptiontimeplus/README.md) · [XCM](models/recurrent_convolution/xcm/README.md) · [XCMPlus](models/recurrent_convolution/xcmplus/README.md) · [XCoordTime](models/recurrent_convolution/xcoordtime/README.md) · [xLSTM](models/recurrent_convolution/xlstm/README.md) · [xLSTMTime](models/recurrent_convolution/xlstmtime/README.md) · [XResNet1d](models/recurrent_convolution/xresnet1d/README.md) · [XResNet1dPlus](models/recurrent_convolution/xresnet1dplus/README.md) |
| [Transformer与注意力](docs/model-catalog.md#category-transformer_attention) | [ConvTranPlus](models/transformer_attention/convtranplus/README.md) · [Crossformer](models/transformer_attention/crossformer/README.md) · [EMAformer](models/transformer_attention/emaformer/README.md) · [GatedTabTransformer](models/transformer_attention/gatedtabtransformer/README.md) · [Informer](models/transformer_attention/informer/README.md) · [iTransformer](models/transformer_attention/itransformer/README.md) · [MultiPatchFormer](models/transformer_attention/multipatchformer/README.md) · [Nonstationary_Transformer](models/transformer_attention/nonstationary_transformer/README.md) · [PatchTST](models/transformer_attention/patchtst/README.md) · [PAttn](models/transformer_attention/pattn/README.md) · [Pyraformer](models/transformer_attention/pyraformer/README.md) · [Reformer](models/transformer_attention/reformer/README.md) · [Samformer](models/transformer_attention/samformer/README.md) · [TabFusionTransformer](models/transformer_attention/tabfusiontransformer/README.md) · [TabTransformer](models/transformer_attention/tabtransformer/README.md) · [TemporalFusionTransformer](models/transformer_attention/temporalfusiontransformer/README.md) · [TimeXer](models/transformer_attention/timexer/README.md) · [Transformer](models/transformer_attention/transformer/README.md) · [TransformerGRUPlus](models/transformer_attention/transformergruplus/README.md) · [TransformerLSTMPlus](models/transformer_attention/transformerlstmplus/README.md) · [TransformerModel](models/transformer_attention/transformermodel/README.md) · [TransformerRNNPlus](models/transformer_attention/transformerrnnplus/README.md) · [TSiTPlus](models/transformer_attention/tsitplus/README.md) · [TSPerceiver](models/transformer_attention/tsperceiver/README.md) · [TST](models/transformer_attention/tst/README.md) · [TSTabFusionTransformer](models/transformer_attention/tstabfusiontransformer/README.md) · [TSTPlus](models/transformer_attention/tstplus/README.md) · [UniTS](models/transformer_attention/units/README.md) |
| [分解平滑频域](docs/model-catalog.md#category-decomposition_frequency) | [Autoformer](models/decomposition_frequency/autoformer/README.md) · [ETSformer](models/decomposition_frequency/etsformer/README.md) · [FEDformer](models/decomposition_frequency/fedformer/README.md) · [FFT](models/decomposition_frequency/fft/README.md) · [FreTS](models/decomposition_frequency/frets/README.md) · [mWDN](models/decomposition_frequency/mwdn/README.md) · [mWDNPlus](models/decomposition_frequency/mwdnplus/README.md) · [TimeMixer](models/decomposition_frequency/timemixer/README.md) · [WPMixer](models/decomposition_frequency/wpmixer/README.md) |
| [状态空间动力学](docs/model-catalog.md#category-state_space_dynamics) | [FiLM](models/state_space_dynamics/film/README.md) · [KalmanForecaster](models/state_space_dynamics/kalmanforecaster/README.md) · [Koopa](models/state_space_dynamics/koopa/README.md) · [Mamba](models/state_space_dynamics/mamba/README.md) · [MambaSimple](models/state_space_dynamics/mambasimple/README.md) · [MambaSingleLayer](models/state_space_dynamics/mambasinglelayer/README.md) |
| [图结构](docs/model-catalog.md#category-graph) | [MSGNet](models/graph/msgnet/README.md) · [StemGNN](models/graph/stemgnn/README.md) · [TimeFilter](models/graph/timefilter/README.md) |
| [LLM重编程](docs/model-catalog.md#category-llm_reprogramming) | [Time-LLM](models/llm_reprogramming/time-llm/README.md) |
| [预训练时序模型](docs/model-catalog.md#category-pretrained_foundation) | [Chronos](models/pretrained_foundation/chronos/README.md) · [Chronos2](models/pretrained_foundation/chronos2/README.md) · [Moirai](models/pretrained_foundation/moirai/README.md) · [PatchTSTFMModel](models/pretrained_foundation/patchtstfmmodel/README.md) · [Sundial](models/pretrained_foundation/sundial/README.md) · [T0](models/pretrained_foundation/t0/README.md) · [TimeMoE](models/pretrained_foundation/timemoe/README.md) · [TimesFM](models/pretrained_foundation/timesfm/README.md) · [TimesFM2p5](models/pretrained_foundation/timesfm2p5/README.md) · [TimesFM3](models/pretrained_foundation/timesfm3/README.md) · [TiRex](models/pretrained_foundation/tirex/README.md) · [TiRex2](models/pretrained_foundation/tirex2/README.md) |
| [专用异常检测](docs/model-catalog.md#category-anomaly_specialized) | [KANAD](models/anomaly_specialized/kanad/README.md) |
| [统计与朴素基线](docs/model-catalog.md#category-statistical) | [ARIMA](models/statistical/arima/README.md) · [AutoARIMA](models/statistical/autoarima/README.md) · [AutoCES](models/statistical/autoces/README.md) · [AutoETS](models/statistical/autoets/README.md) · [AutoMFLES](models/statistical/automfles/README.md) · [AutoTBATS](models/statistical/autotbats/README.md) · [AutoTheta](models/statistical/autotheta/README.md) · [Baseline](models/statistical/baseline/README.md) · [Croston](models/statistical/croston/README.md) · [ExponentialSmoothing](models/statistical/exponentialsmoothing/README.md) · [FourTheta](models/statistical/fourtheta/README.md) · [GlobalNaiveAggregate](models/statistical/globalnaiveaggregate/README.md) · [GlobalNaiveDrift](models/statistical/globalnaivedrift/README.md) · [GlobalNaiveSeasonal](models/statistical/globalnaiveseasonal/README.md) · [NaiveDrift](models/statistical/naivedrift/README.md) · [NaiveMean](models/statistical/naivemean/README.md) · [NaiveMovingAverage](models/statistical/naivemovingaverage/README.md) · [NaiveSeasonal](models/statistical/naiveseasonal/README.md) · [Prophet](models/statistical/prophet/README.md) · [TBATS](models/statistical/tbats/README.md) · [Theta](models/statistical/theta/README.md) · [VARIMA](models/statistical/varima/README.md) |
| [树模型与回归](docs/model-catalog.md#category-machine_learning) | [CatBoostClassifierModel](models/machine_learning/catboostclassifiermodel/README.md) · [CatBoostModel](models/machine_learning/catboostmodel/README.md) · [LightGBMClassifierModel](models/machine_learning/lightgbmclassifiermodel/README.md) · [LightGBMModel](models/machine_learning/lightgbmmodel/README.md) · [LinearRegressionModel](models/machine_learning/linearregressionmodel/README.md) · [RandomForestModel](models/machine_learning/randomforestmodel/README.md) · [XGBClassifierModel](models/machine_learning/xgbclassifiermodel/README.md) · [XGBModel](models/machine_learning/xgbmodel/README.md) |
| [集成与校准](docs/model-catalog.md#category-ensemble_calibration) | [ConformalNaiveModel](models/ensemble_calibration/conformalnaivemodel/README.md) · [ConformalQRModel](models/ensemble_calibration/conformalqrmodel/README.md) · [HINT](models/ensemble_calibration/hint/README.md) · [MiniRocketVotingClassifier](models/ensemble_calibration/minirocketvotingclassifier/README.md) · [MiniRocketVotingRegressor](models/ensemble_calibration/minirocketvotingregressor/README.md) · [MultiInceptionTimePlus](models/ensemble_calibration/multiinceptiontimeplus/README.md) · [NaiveEnsembleModel](models/ensemble_calibration/naiveensemblemodel/README.md) · [RegressionEnsembleModel](models/ensemble_calibration/regressionensemblemodel/README.md) |
| [通用模型适配器](docs/model-catalog.md#category-model_adapter) | [MultiInputNet](models/model_adapter/multiinputnet/README.md) · [MultiTSTPlus](models/model_adapter/multitstplus/README.md) · [MultivariateModel](models/model_adapter/multivariatemodel/README.md) · [NeuralForecastModel](models/model_adapter/neuralforecastmodel/README.md) · [SKLearnClassifierModel](models/model_adapter/sklearnclassifiermodel/README.md) · [SKLearnModel](models/model_adapter/sklearnmodel/README.md) · [StatsForecastModel](models/model_adapter/statsforecastmodel/README.md) |

<!-- MODEL_CATALOG_END -->

各模型介绍统一说明直观含义、工作机制、适用问题、局限与阅读顺序。端到端模型、预测器和有名称的网络变体逐项列出，同名实现合并展示；辅助层、损失函数与抽象基类保留在源码快照中。

## 全部模型明细

<!-- MODEL_DETAILS_START -->

共 **187 个模型家族**，每个模型一行，所有来源使用相同六个字段。名称进入中文介绍页，介绍后的全部实现并列保留；悬停短链接可查看完整路径或类名。

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
<td align="left"><a href="models/statistical/arima/README.md">A&#8288;R&#8288;I&#8288;M&#8288;A</a></td>
<td align="left">通过自回归、差分和移动平均描述时间依赖。</td>
<td align="left"><a href="models/statistical/arima/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/arima.py" title="_sources/source-12/darts/models/forecasting/arima.py :: ARIMA">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/arima/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/arima/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/autoarima/README.md">A&#8288;u&#8288;t&#8288;o&#8288;A&#8288;R&#8288;I&#8288;M&#8288;A</a></td>
<td align="left">自动选择 ARIMA 配置并生成统计预测。</td>
<td align="left"><a href="models/statistical/autoarima/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_auto_arima.py" title="_sources/source-12/darts/models/forecasting/sf_auto_arima.py :: AutoARIMA">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/autoarima/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/autoarima/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/autoces/README.md">A&#8288;u&#8288;t&#8288;o&#8288;C&#8288;E&#8288;S</a></td>
<td align="left">调用自动复指数平滑预测。</td>
<td align="left"><a href="models/statistical/autoces/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_auto_ces.py" title="_sources/source-12/darts/models/forecasting/sf_auto_ces.py :: AutoCES">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/autoces/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/autoces/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/autoets/README.md">A&#8288;u&#8288;t&#8288;o&#8288;E&#8288;T&#8288;S</a></td>
<td align="left">自动选择误差、趋势与季节结构的指数平滑模型。</td>
<td align="left"><a href="models/statistical/autoets/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_auto_ets.py" title="_sources/source-12/darts/models/forecasting/sf_auto_ets.py :: AutoETS">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/autoets/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/autoets/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/autoformer/README.md">A&#8288;u&#8288;t&#8288;o&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">逐层拆分趋势与季节变化，再用自相关选择时延并聚合序列。</td>
<td align="left"><a href="models/decomposition_frequency/autoformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-04/models/Autoformer.py" title="_sources/source-04/models/Autoformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-07/models/Autoformer.py" title="_sources/source-07/models/Autoformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-08/models/Autoformer.py" title="_sources/source-08/models/Autoformer.py">实&#8288;现&#8288;3</a><br><a href="_sources/source-10/neuralforecast/models/autoformer.py" title="_sources/source-10/neuralforecast/models/autoformer.py :: Autoformer">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/decomposition_frequency/autoformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2106.13008" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/autoformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/automfles/README.md">A&#8288;u&#8288;t&#8288;o&#8288;M&#8288;F&#8288;L&#8288;E&#8288;S</a></td>
<td align="left">自动配置 MFLES 多成分拟合并产生统计预测。</td>
<td align="left"><a href="models/statistical/automfles/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_auto_mfles.py" title="_sources/source-12/darts/models/forecasting/sf_auto_mfles.py :: AutoMFLES">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/automfles/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/automfles/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/autotbats/README.md">A&#8288;u&#8288;t&#8288;o&#8288;T&#8288;B&#8288;A&#8288;T&#8288;S</a></td>
<td align="left">自动选择含三角季节项、趋势等成分的 TBATS 配置。</td>
<td align="left"><a href="models/statistical/autotbats/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_auto_tbats.py" title="_sources/source-12/darts/models/forecasting/sf_auto_tbats.py :: AutoTBATS">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/autotbats/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/autotbats/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/autotheta/README.md">A&#8288;u&#8288;t&#8288;o&#8288;T&#8288;h&#8288;e&#8288;t&#8288;a</a></td>
<td align="left">自动配置 Theta 方法，预测并组合分解后的成分。</td>
<td align="left"><a href="models/statistical/autotheta/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_auto_theta.py" title="_sources/source-12/darts/models/forecasting/sf_auto_theta.py :: AutoTheta">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/autotheta/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/autotheta/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/baseline/README.md">B&#8288;a&#8288;s&#8288;e&#8288;l&#8288;i&#8288;n&#8288;e</a></td>
<td align="left">重复最后一个历史观测值，作为朴素预测对照。</td>
<td align="left"><a href="models/statistical/baseline/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/baseline.py" title="_sources/source-11/pytorch_forecasting/models/baseline.py :: Baseline">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/baseline/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/baseline/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/bitcn/README.md">B&#8288;i&#8288;T&#8288;C&#8288;N</a></td>
<td align="left">以时间卷积分支处理历史和已知未来协变量，产生概率预测。</td>
<td align="left"><a href="models/recurrent_convolution/bitcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/bitcn.py" title="_sources/source-10/neuralforecast/models/bitcn.py :: BiTCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/bitcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://doi.org/10.1016/j.ijforecast.2021.11.011" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/bitcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/blockrnn/README.md">B&#8288;l&#8288;o&#8288;c&#8288;k&#8288;R&#8288;N&#8288;N</a><br><sub>BlockRNNModel</sub></td>
<td align="left">循环编码历史窗口，再以块输出同时预测多个未来点。</td>
<td align="left"><a href="models/recurrent_convolution/blockrnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/block_rnn_model.py" title="_sources/source-12/darts/models/forecasting/block_rnn_model.py :: BlockRNNModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/blockrnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/forum?id=cGDAkQo1C0p" title="此链接是源码引用的 TiDE 相关架构文献，不是 BlockRNN 的独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/blockrnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/catboostclassifiermodel/README.md">C&#8288;a&#8288;t&#8288;B&#8288;o&#8288;o&#8288;s&#8288;t&#8288;C&#8288;l&#8288;a&#8288;s&#8288;s&#8288;i&#8288;f&#8288;i&#8288;e&#8288;r&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">用 CatBoost 分类接口预测序列离散标签。</td>
<td align="left"><a href="models/machine_learning/catboostclassifiermodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/catboost_model.py" title="_sources/source-12/darts/models/forecasting/catboost_model.py :: CatBoostClassifierModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/catboostclassifiermodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/catboostclassifiermodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/catboostmodel/README.md">C&#8288;a&#8288;t&#8288;B&#8288;o&#8288;o&#8288;s&#8288;t&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">以 CatBoost 提升树学习带滞后和协变量的预测。</td>
<td align="left"><a href="models/machine_learning/catboostmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/catboost_model.py" title="_sources/source-12/darts/models/forecasting/catboost_model.py :: CatBoostModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/catboostmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/catboostmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/chronos/README.md">C&#8288;h&#8288;r&#8288;o&#8288;n&#8288;o&#8288;s</a></td>
<td align="left">调用预训练 Chronos，把数值序列交给其预测管线，入口用于零样本预测。</td>
<td align="left"><a href="models/pretrained_foundation/chronos/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Chronos.py" title="_sources/source-07/models/Chronos.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/chronos/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2403.07815" title="链接为上游 README 列出的 Chronos 系列论文；当前接口实际加载 chronos-bolt-base，不将该链接标成该权重的专属论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/pretrained_foundation/chronos/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/chronos2/README.md">C&#8288;h&#8288;r&#8288;o&#8288;n&#8288;o&#8288;s&#8288;2</a><br><sub>Chronos-2 / Chronos2Model</sub></td>
<td align="left">调用 Chronos-2 预训练预测管线，与第一代 Chronos 分开保留接口。</td>
<td align="left"><a href="models/pretrained_foundation/chronos2/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Chronos2.py" title="_sources/source-07/models/Chronos2.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-12/darts/models/forecasting/chronos2_model.py" title="_sources/source-12/darts/models/forecasting/chronos2_model.py :: Chronos2Model">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/pretrained_foundation/chronos2/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2510.15821" title="模型论文">论&#8288;文</a><br><a href="models/pretrained_foundation/chronos2/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/conformalnaivemodel/README.md">C&#8288;o&#8288;n&#8288;f&#8288;o&#8288;r&#8288;m&#8288;a&#8288;l&#8288;N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">对基础预测历史误差做保形校准，调整区间覆盖目标。</td>
<td align="left"><a href="models/ensemble_calibration/conformalnaivemodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/conformal_models.py" title="_sources/source-12/darts/models/forecasting/conformal_models.py :: ConformalNaiveModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/conformalnaivemodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/conformalnaivemodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/conformalqrmodel/README.md">C&#8288;o&#8288;n&#8288;f&#8288;o&#8288;r&#8288;m&#8288;a&#8288;l&#8288;Q&#8288;R&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">在分位数预测上做保形校准，修正预测区间。</td>
<td align="left"><a href="models/ensemble_calibration/conformalqrmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/conformal_models.py" title="_sources/source-12/darts/models/forecasting/conformal_models.py :: ConformalQRModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/conformalqrmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/conformalqrmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/convtranplus/README.md">C&#8288;o&#8288;n&#8288;v&#8288;T&#8288;r&#8288;a&#8288;n&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">结合卷积嵌入、时序绝对位置和相对位置注意力。</td>
<td align="left"><a href="models/transformer_attention/convtranplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/ConvTranPlus.py" title="_sources/source-09/tsai/models/ConvTranPlus.py :: ConvTranPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/convtranplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2305.16642v1" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/convtranplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/crossformer/README.md">C&#8288;r&#8288;o&#8288;s&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">把每个变量的序列切成片段，用分层和两阶段注意力处理时间与变量关系。</td>
<td align="left"><a href="models/transformer_attention/crossformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Crossformer.py" title="_sources/source-07/models/Crossformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/Crossformer.py" title="_sources/source-08/models/Crossformer.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/crossformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=vSVLM2j9eie" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/crossformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/croston/README.md">C&#8288;r&#8288;o&#8288;s&#8288;t&#8288;o&#8288;n</a></td>
<td align="left">分别估计间歇需求大小和到达间隔，处理大量零值需求。</td>
<td align="left"><a href="models/statistical/croston/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_croston.py" title="_sources/source-12/darts/models/forecasting/sf_croston.py :: Croston">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/croston/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/croston/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/decodermlp/README.md">D&#8288;e&#8288;c&#8288;o&#8288;d&#8288;e&#8288;r&#8288;M&#8288;L&#8288;P</a><br><sub>DecoderMLPForecaster / DecoderMLP_pkg / DecoderMLP_v2</sub></td>
<td align="left">使用解码区间可用的协变量构建前馈预测。</td>
<td align="left"><a href="models/linear_mlp/decodermlp/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp.py" title="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp.py :: DecoderMLP">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_forecaster_v2.py :: DecoderMLPForecaster">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_pkg.py" title="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_pkg.py :: DecoderMLP_pkg">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_v2.py" title="_sources/source-11/pytorch_forecasting/models/mlp/_decodermlp_v2.py :: DecoderMLP_v2">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/linear_mlp/decodermlp/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/linear_mlp/decodermlp/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/deepar/README.md">D&#8288;e&#8288;e&#8288;p&#8288;A&#8288;R</a><br><sub>DeepAR_pkg</sub></td>
<td align="left">用自回归循环网络学习未来值的概率分布。</td>
<td align="left"><a href="models/recurrent_convolution/deepar/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/deepar.py" title="_sources/source-10/neuralforecast/models/deepar.py :: DeepAR">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/deepar/_deepar.py" title="_sources/source-11/pytorch_forecasting/models/deepar/_deepar.py :: DeepAR">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/deepar/_deepar_pkg.py" title="_sources/source-11/pytorch_forecasting/models/deepar/_deepar_pkg.py :: DeepAR_pkg">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/recurrent_convolution/deepar/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/pii/S0169207019301888" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/deepar/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/deepnpts/README.md">D&#8288;e&#8288;e&#8288;p&#8288;N&#8288;P&#8288;T&#8288;S</a></td>
<td align="left">学习历史观测的权重，以非参数方式形成预测分布。</td>
<td align="left"><a href="models/linear_mlp/deepnpts/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/deepnpts.py" title="_sources/source-10/neuralforecast/models/deepnpts.py :: DeepNPTS">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/deepnpts/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2312.14657" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/deepnpts/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/dilatedrnn/README.md">D&#8288;i&#8288;l&#8288;a&#8288;t&#8288;e&#8288;d&#8288;R&#8288;N&#8288;N</a></td>
<td align="left">以不同时间跨度的循环连接捕捉长期依赖。</td>
<td align="left"><a href="models/recurrent_convolution/dilatedrnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/dilated_rnn.py" title="_sources/source-10/neuralforecast/models/dilated_rnn.py :: DilatedRNN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/dilatedrnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/1710.02224" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/dilatedrnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/dlinear/README.md">D&#8288;L&#8288;i&#8288;n&#8288;e&#8288;a&#8288;r</a><br><sub>DLinearForecaster / DLinearModel</sub></td>
<td align="left">先分解趋势与剩余变化，再分别做线性预测，是结构简单的对照模型。</td>
<td align="left"><a href="models/linear_mlp/dlinear/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/DLinear.py" title="_sources/source-07/models/DLinear.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/DLinear.py" title="_sources/source-08/models/DLinear.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/dlinear.py" title="_sources/source-10/neuralforecast/models/dlinear.py :: DLinear">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/dlinear/_dlinear_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/dlinear/_dlinear_forecaster_v2.py :: DLinearForecaster">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/dlinear/_dlinear_v2.py" title="_sources/source-11/pytorch_forecasting/models/dlinear/_dlinear_v2.py :: DLinear">实&#8288;现&#8288;5</a><br><a href="_sources/source-12/darts/models/forecasting/dlinear.py" title="_sources/source-12/darts/models/forecasting/dlinear.py :: DLinearModel">实&#8288;现&#8288;6</a></td>
<td align="left"><a href="models/linear_mlp/dlinear/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2205.13504.pdf" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/dlinear/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/emaformer/README.md">E&#8288;M&#8288;A&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">在变量 token 上叠加通道、相位和联合嵌入，再用 Transformer 预测。</td>
<td align="left"><a href="models/transformer_attention/emaformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-01/model/EMAformer.py" title="_sources/source-01/model/EMAformer.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/emaformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2511.08396" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/emaformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/etsformer/README.md">E&#8288;T&#8288;S&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">将水平、增长和季节项分开建模，结合可学习指数平滑、傅里叶外推与增长阻尼。</td>
<td align="left"><a href="models/decomposition_frequency/etsformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-05/models/etsformer/model.py" title="_sources/source-05/models/etsformer/model.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-07/models/ETSformer.py" title="_sources/source-07/models/ETSformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-08/models/ETSformer.py" title="_sources/source-08/models/ETSformer.py">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/decomposition_frequency/etsformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2202.01381" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/etsformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/exponentialsmoothing/README.md">E&#8288;x&#8288;p&#8288;o&#8288;n&#8288;e&#8288;n&#8288;t&#8288;i&#8288;a&#8288;l&#8288;S&#8288;m&#8288;o&#8288;o&#8288;t&#8288;h&#8288;i&#8288;n&#8288;g</a></td>
<td align="left">用递减权重估计水平、趋势和季节变化并外推。</td>
<td align="left"><a href="models/statistical/exponentialsmoothing/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/exponential_smoothing.py" title="_sources/source-12/darts/models/forecasting/exponential_smoothing.py :: ExponentialSmoothing">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/exponentialsmoothing/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/exponentialsmoothing/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/fcn/README.md">F&#8288;C&#8288;N</a></td>
<td align="left">用多层一维卷积和全局池化提取序列特征。</td>
<td align="left"><a href="models/recurrent_convolution/fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/FCN.py" title="_sources/source-09/tsai/models/FCN.py :: FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/fcnplus/README.md">F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">用多层一维卷积和全局池化提取序列特征。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/recurrent_convolution/fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/FCNPlus.py" title="_sources/source-09/tsai/models/FCNPlus.py :: FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/fedformer/README.md">F&#8288;E&#8288;D&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">在趋势季节分解的基础上，用傅里叶或小波模块处理长期依赖。</td>
<td align="left"><a href="models/decomposition_frequency/fedformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/FEDformer.py" title="_sources/source-07/models/FEDformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/FEDformer.py" title="_sources/source-08/models/FEDformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/fedformer.py" title="_sources/source-10/neuralforecast/models/fedformer.py :: FEDformer">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/decomposition_frequency/fedformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://proceedings.mlr.press/v162/zhou22g.html" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/fedformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/fft/README.md">F&#8288;F&#8288;T</a></td>
<td align="left">在去趋势等处理后选择傅里叶成分并外推周期变化。</td>
<td align="left"><a href="models/decomposition_frequency/fft/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/fft.py" title="_sources/source-12/darts/models/forecasting/fft.py :: FFT">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/decomposition_frequency/fft/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/decomposition_frequency/fft/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/state_space_dynamics/film/README.md">F&#8288;i&#8288;L&#8288;M</a></td>
<td align="left">用 Legendre/HiPPO 状态投影压缩历史，再以频域处理提取预测信息。</td>
<td align="left"><a href="models/state_space_dynamics/film/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/FiLM.py" title="_sources/source-07/models/FiLM.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/FiLM.py" title="_sources/source-08/models/FiLM.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/state_space_dynamics/film/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/forum?id=zTQdHSQUQWc" title="模型论文">论&#8288;文</a><br><a href="models/state_space_dynamics/film/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/fourtheta/README.md">F&#8288;o&#8288;u&#8288;r&#8288;T&#8288;h&#8288;e&#8288;t&#8288;a</a></td>
<td align="left">组合多条 Theta 变换线及其配置产生预测。</td>
<td align="left"><a href="models/statistical/fourtheta/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/theta.py" title="_sources/source-12/darts/models/forecasting/theta.py :: FourTheta">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/fourtheta/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/fourtheta/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/frets/README.md">F&#8288;r&#8288;e&#8288;T&#8288;S</a><br><sub>FreTSForecaster</sub></td>
<td align="left">把序列变到频域，用复数 MLP 混合时间和通道信息，再还原预测。</td>
<td align="left"><a href="models/decomposition_frequency/frets/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/FreTS.py" title="_sources/source-07/models/FreTS.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/FreTS.py" title="_sources/source-08/models/FreTS.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/frets/_frets_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/frets/_frets_forecaster_v2.py :: FreTSForecaster">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/frets/_frets_v2.py" title="_sources/source-11/pytorch_forecasting/models/frets/_frets_v2.py :: FreTS">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/decomposition_frequency/frets/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2311.06184.pdf" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/frets/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/gatedtabtransformer/README.md">G&#8288;a&#8288;t&#8288;e&#8288;d&#8288;T&#8288;a&#8288;b&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">以门控和注意力表示表格变量，可用于带静态属性任务。</td>
<td align="left"><a href="models/transformer_attention/gatedtabtransformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/GatedTabTransformer.py" title="_sources/source-09/tsai/models/GatedTabTransformer.py :: GatedTabTransformer">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/gatedtabtransformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2201.00199" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/gatedtabtransformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/globalnaiveaggregate/README.md">G&#8288;l&#8288;o&#8288;b&#8288;a&#8288;l&#8288;N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;A&#8288;g&#8288;g&#8288;r&#8288;e&#8288;g&#8288;a&#8288;t&#8288;e</a></td>
<td align="left">在全局模型接口中对输入窗口做指定聚合。</td>
<td align="left"><a href="models/statistical/globalnaiveaggregate/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/global_baseline_models.py" title="_sources/source-12/darts/models/forecasting/global_baseline_models.py :: GlobalNaiveAggregate">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/globalnaiveaggregate/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/globalnaiveaggregate/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/globalnaivedrift/README.md">G&#8288;l&#8288;o&#8288;b&#8288;a&#8288;l&#8288;N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;D&#8288;r&#8288;i&#8288;f&#8288;t</a></td>
<td align="left">在全局模型接口中延伸输入窗口的漂移趋势。</td>
<td align="left"><a href="models/statistical/globalnaivedrift/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/global_baseline_models.py" title="_sources/source-12/darts/models/forecasting/global_baseline_models.py :: GlobalNaiveDrift">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/globalnaivedrift/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/globalnaivedrift/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/globalnaiveseasonal/README.md">G&#8288;l&#8288;o&#8288;b&#8288;a&#8288;l&#8288;N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;S&#8288;e&#8288;a&#8288;s&#8288;o&#8288;n&#8288;a&#8288;l</a></td>
<td align="left">在全局模型接口中重复窗口中的季节观测。</td>
<td align="left"><a href="models/statistical/globalnaiveseasonal/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/global_baseline_models.py" title="_sources/source-12/darts/models/forecasting/global_baseline_models.py :: GlobalNaiveSeasonal">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/globalnaiveseasonal/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/globalnaiveseasonal/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/gmlp/README.md">g&#8288;M&#8288;L&#8288;P</a></td>
<td align="left">通过空间门控前馈模块混合序列位置，替代完整注意力。</td>
<td align="left"><a href="models/linear_mlp/gmlp/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/gMLP.py" title="_sources/source-09/tsai/models/gMLP.py :: gMLP">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/gmlp/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2105.08050" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/gmlp/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/gru/README.md">G&#8288;R&#8288;U</a></td>
<td align="left">以更新门和重置门递推隐藏状态，学习序列信息。</td>
<td align="left"><a href="models/recurrent_convolution/gru/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN.py" title="_sources/source-09/tsai/models/RNN.py :: GRU">实&#8288;现&#8288;1</a><br><a href="_sources/source-10/neuralforecast/models/gru.py" title="_sources/source-10/neuralforecast/models/gru.py :: GRU">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/gru/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1412.3555" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/gru/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/gru_fcn/README.md">G&#8288;R&#8288;U&#8288;_&#8288;F&#8288;C&#8288;N</a></td>
<td align="left">融合 GRU 循环分支与全卷积分支的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/gru_fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCN.py" title="_sources/source-09/tsai/models/RNN_FCN.py :: GRU_FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/gru_fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1812.07683" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/gru_fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/gru_fcnplus/README.md">G&#8288;R&#8288;U&#8288;_&#8288;F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">融合 GRU 循环分支与全卷积分支的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="models/recurrent_convolution/gru_fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCNPlus.py" title="_sources/source-09/tsai/models/RNN_FCNPlus.py :: GRU_FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/gru_fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1812.07683" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/gru_fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/gruattention/README.md">G&#8288;R&#8288;U&#8288;A&#8288;t&#8288;t&#8288;e&#8288;n&#8288;t&#8288;i&#8288;o&#8288;n</a></td>
<td align="left">结合 GRU 循环表示和注意力编码模块的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/gruattention/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNAttention.py" title="_sources/source-09/tsai/models/RNNAttention.py :: GRUAttention">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/gruattention/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/gruattention/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/gruattentionplus/README.md">G&#8288;R&#8288;U&#8288;A&#8288;t&#8288;t&#8288;e&#8288;n&#8288;t&#8288;i&#8288;o&#8288;n&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">结合 GRU 循环表示和注意力编码模块的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="models/recurrent_convolution/gruattentionplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNAttentionPlus.py" title="_sources/source-09/tsai/models/RNNAttentionPlus.py :: GRUAttentionPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/gruattentionplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/gruattentionplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/gruplus/README.md">G&#8288;R&#8288;U&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">GRU 的 可配置骨干与任务头变体。</td>
<td align="left"><a href="models/recurrent_convolution/gruplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNPlus.py" title="_sources/source-09/tsai/models/RNNPlus.py :: GRUPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/gruplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1412.3555" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/gruplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/hint/README.md">H&#8288;I&#8288;N&#8288;T</a></td>
<td align="left">结合基础预测与层级协调，使不同聚合层级的预测一致。</td>
<td align="left"><a href="models/ensemble_calibration/hint/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/hint.py" title="_sources/source-10/neuralforecast/models/hint.py :: HINT">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/hint/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2305.07089" title="模型论文">论&#8288;文</a><br><a href="models/ensemble_calibration/hint/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/hydramultirocketplus/README.md">H&#8288;y&#8288;d&#8288;r&#8288;a&#8288;M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">融合 Hydra 竞争卷积和 MultiRocket 统计特征。</td>
<td align="left"><a href="models/recurrent_convolution/hydramultirocketplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/HydraMultiRocketPlus.py" title="_sources/source-09/tsai/models/HydraMultiRocketPlus.py :: HydraMultiRocketPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/hydramultirocketplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/hydramultirocketplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/hydraplus/README.md">H&#8288;y&#8288;d&#8288;r&#8288;a&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">通过分组随机卷积的竞争响应生成特征，再接任务头。</td>
<td align="left"><a href="models/recurrent_convolution/hydraplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/HydraPlus.py" title="_sources/source-09/tsai/models/HydraPlus.py :: HydraPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/hydraplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/hydraplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/inceptionrocketplus/README.md">I&#8288;n&#8288;c&#8288;e&#8288;p&#8288;t&#8288;i&#8288;o&#8288;n&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">将多尺度卷积特征与 Rocket 风格任务头结合。</td>
<td align="left"><a href="models/recurrent_convolution/inceptionrocketplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MINIROCKETPlus_Pytorch.py" title="_sources/source-09/tsai/models/MINIROCKETPlus_Pytorch.py :: InceptionRocketPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/inceptionrocketplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/inceptionrocketplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/inceptiontime/README.md">I&#8288;n&#8288;c&#8288;e&#8288;p&#8288;t&#8288;i&#8288;o&#8288;n&#8288;T&#8288;i&#8288;m&#8288;e</a></td>
<td align="left">并行使用不同长度的一维卷积核提取多尺度模式。</td>
<td align="left"><a href="models/recurrent_convolution/inceptiontime/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/InceptionTime.py" title="_sources/source-09/tsai/models/InceptionTime.py :: InceptionTime">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/inceptiontime/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1909.04939" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/inceptiontime/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/inceptiontimeplus/README.md">I&#8288;n&#8288;c&#8288;e&#8288;p&#8288;t&#8288;i&#8288;o&#8288;n&#8288;T&#8288;i&#8288;m&#8288;e&#8288;P&#8288;l&#8288;u&#8288;s</a><br><sub>InceptionTimePlus17x17 / InceptionTimePlus32x32 / InceptionTimePlus47x47 / InceptionTimePlus62x62 / InceptionTimeXLPlus</sub></td>
<td align="left">并行使用不同长度的一维卷积核提取多尺度模式。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/recurrent_convolution/inceptiontimeplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InceptionTimePlus">实&#8288;现&#8288;1</a><br><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InceptionTimePlus17x17">实&#8288;现&#8288;2</a><br><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InceptionTimePlus32x32">实&#8288;现&#8288;3</a><br><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InceptionTimePlus47x47">实&#8288;现&#8288;4</a><br><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InceptionTimePlus62x62">实&#8288;现&#8288;5</a><br><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InceptionTimeXLPlus">实&#8288;现&#8288;6</a></td>
<td align="left"><a href="models/recurrent_convolution/inceptiontimeplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1909.04939" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/inceptiontimeplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/incoordtime/README.md">I&#8288;n&#8288;C&#8288;o&#8288;o&#8288;r&#8288;d&#8288;T&#8288;i&#8288;m&#8288;e</a></td>
<td align="left">在 InceptionTimePlus 中加入坐标卷积信息的变体。</td>
<td align="left"><a href="models/recurrent_convolution/incoordtime/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: InCoordTime">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/incoordtime/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/incoordtime/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/informer/README.md">I&#8288;n&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a><br><sub>Informer2020</sub></td>
<td align="left">用 ProbSparse 选择重要 query，并通过编码器蒸馏压缩长序列。</td>
<td align="left"><a href="models/transformer_attention/informer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-03/models/model.py" title="_sources/source-03/models/model.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-07/models/Informer.py" title="_sources/source-07/models/Informer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-08/models/Informer.py" title="_sources/source-08/models/Informer.py">实&#8288;现&#8288;3</a><br><a href="_sources/source-10/neuralforecast/models/informer.py" title="_sources/source-10/neuralforecast/models/informer.py :: Informer">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/transformer_attention/informer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2012.07436" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/informer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/itransformer/README.md">i&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">把每个变量的历史作为一个 token，让注意力直接学习变量之间的关系。</td>
<td align="left"><a href="models/transformer_attention/itransformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/iTransformer.py" title="_sources/source-07/models/iTransformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/iTransformer.py" title="_sources/source-08/models/iTransformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/itransformer.py" title="_sources/source-10/neuralforecast/models/itransformer.py :: iTransformer">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/transformer_attention/itransformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.06625" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/itransformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/state_space_dynamics/kalmanforecaster/README.md">K&#8288;a&#8288;l&#8288;m&#8288;a&#8288;n&#8288;F&#8288;o&#8288;r&#8288;e&#8288;c&#8288;a&#8288;s&#8288;t&#8288;e&#8288;r</a></td>
<td align="left">估计状态空间模型的隐状态，再以 Kalman 模型递推未来。</td>
<td align="left"><a href="models/state_space_dynamics/kalmanforecaster/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/kalman_forecaster.py" title="_sources/source-12/darts/models/forecasting/kalman_forecaster.py :: KalmanForecaster">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/state_space_dynamics/kalmanforecaster/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/state_space_dynamics/kalmanforecaster/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/kan/README.md">K&#8288;A&#8288;N</a></td>
<td align="left">用可学习的一元函数替代普通 MLP 边权拟合非线性关系。</td>
<td align="left"><a href="models/linear_mlp/kan/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/kan.py" title="_sources/source-10/neuralforecast/models/kan.py :: KAN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/kan/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2404.19756" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/kan/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/anomaly_specialized/kanad/README.md">K&#8288;A&#8288;N&#8288;A&#8288;D</a></td>
<td align="left">结合周期余弦特征和卷积重建序列，当前模型只实现异常检测。</td>
<td align="left"><a href="models/anomaly_specialized/kanad/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/KANAD.py" title="_sources/source-07/models/KANAD.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/anomaly_specialized/kanad/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2411.00278" title="模型论文">论&#8288;文</a><br><a href="models/anomaly_specialized/kanad/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/state_space_dynamics/koopa/README.md">K&#8288;o&#8288;o&#8288;p&#8288;a</a></td>
<td align="left">分离不同变化成分，用可学习和动态估计的 Koopman 算子推进隐状态。</td>
<td align="left"><a href="models/state_space_dynamics/koopa/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Koopa.py" title="_sources/source-07/models/Koopa.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/Koopa.py" title="_sources/source-08/models/Koopa.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/state_space_dynamics/koopa/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2305.18803.pdf" title="模型论文">论&#8288;文</a><br><a href="models/state_space_dynamics/koopa/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/lightgbmclassifiermodel/README.md">L&#8288;i&#8288;g&#8288;h&#8288;t&#8288;G&#8288;B&#8288;M&#8288;C&#8288;l&#8288;a&#8288;s&#8288;s&#8288;i&#8288;f&#8288;i&#8288;e&#8288;r&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">以 LightGBM 分类器预测离散目标。</td>
<td align="left"><a href="models/machine_learning/lightgbmclassifiermodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/lgbm.py" title="_sources/source-12/darts/models/forecasting/lgbm.py :: LightGBMClassifierModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/lightgbmclassifiermodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/lightgbmclassifiermodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/lightgbmmodel/README.md">L&#8288;i&#8288;g&#8288;h&#8288;t&#8288;G&#8288;B&#8288;M&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">以 LightGBM 梯度提升树对滞后窗口回归。</td>
<td align="left"><a href="models/machine_learning/lightgbmmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/lgbm.py" title="_sources/source-12/darts/models/forecasting/lgbm.py :: LightGBMModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/lightgbmmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/lightgbmmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/lightts/README.md">L&#8288;i&#8288;g&#8288;h&#8288;t&#8288;T&#8288;S</a></td>
<td align="left">通过连续与间隔采样提取序列片段，用 MLP 混合局部和跨片段信息。</td>
<td align="left"><a href="models/linear_mlp/lightts/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/LightTS.py" title="_sources/source-07/models/LightTS.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/LightTS.py" title="_sources/source-08/models/LightTS.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/linear_mlp/lightts/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2207.01186" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/lightts/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/linearregressionmodel/README.md">L&#8288;i&#8288;n&#8288;e&#8288;a&#8288;r&#8288;R&#8288;e&#8288;g&#8288;r&#8288;e&#8288;s&#8288;s&#8288;i&#8288;o&#8288;n&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">将滞后值与协变量展开为监督样本，用线性回归预测。</td>
<td align="left"><a href="models/machine_learning/linearregressionmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/linear_regression_model.py" title="_sources/source-12/darts/models/forecasting/linear_regression_model.py :: LinearRegressionModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/linearregressionmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/linearregressionmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/lstm/README.md">L&#8288;S&#8288;T&#8288;M</a></td>
<td align="left">用输入、遗忘和输出门维护长期记忆，学习序列映射。</td>
<td align="left"><a href="models/recurrent_convolution/lstm/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN.py" title="_sources/source-09/tsai/models/RNN.py :: LSTM">实&#8288;现&#8288;1</a><br><a href="_sources/source-10/neuralforecast/models/lstm.py" title="_sources/source-10/neuralforecast/models/lstm.py :: LSTM">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/lstm/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://ieeexplore.ieee.org/abstract/document/6795963/" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/lstm/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/lstm_fcn/README.md">L&#8288;S&#8288;T&#8288;M&#8288;_&#8288;F&#8288;C&#8288;N</a></td>
<td align="left">融合 LSTM 循环分支与全卷积分支的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/lstm_fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCN.py" title="_sources/source-09/tsai/models/RNN_FCN.py :: LSTM_FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/lstm_fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1709.05206" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/lstm_fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/lstm_fcnplus/README.md">L&#8288;S&#8288;T&#8288;M&#8288;_&#8288;F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">融合 LSTM 循环分支与全卷积分支的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="models/recurrent_convolution/lstm_fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCNPlus.py" title="_sources/source-09/tsai/models/RNN_FCNPlus.py :: LSTM_FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/lstm_fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1709.05206" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/lstm_fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/lstmattention/README.md">L&#8288;S&#8288;T&#8288;M&#8288;A&#8288;t&#8288;t&#8288;e&#8288;n&#8288;t&#8288;i&#8288;o&#8288;n</a></td>
<td align="left">结合 LSTM 循环表示和注意力编码模块的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/lstmattention/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNAttention.py" title="_sources/source-09/tsai/models/RNNAttention.py :: LSTMAttention">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/lstmattention/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/lstmattention/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/lstmattentionplus/README.md">L&#8288;S&#8288;T&#8288;M&#8288;A&#8288;t&#8288;t&#8288;e&#8288;n&#8288;t&#8288;i&#8288;o&#8288;n&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">结合 LSTM 循环表示和注意力编码模块的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="models/recurrent_convolution/lstmattentionplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNAttentionPlus.py" title="_sources/source-09/tsai/models/RNNAttentionPlus.py :: LSTMAttentionPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/lstmattentionplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/lstmattentionplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/lstmplus/README.md">L&#8288;S&#8288;T&#8288;M&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">LSTM 的 可配置骨干与任务头变体。</td>
<td align="left"><a href="models/recurrent_convolution/lstmplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNPlus.py" title="_sources/source-09/tsai/models/RNNPlus.py :: LSTMPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/lstmplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://ieeexplore.ieee.org/abstract/document/6795963/" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/lstmplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/state_space_dynamics/mamba/README.md">M&#8288;a&#8288;m&#8288;b&#8288;a</a></td>
<td align="left">用 Mamba 的选择性状态空间模块递推处理序列，减少对全量注意力的依赖。</td>
<td align="left"><a href="models/state_space_dynamics/mamba/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Mamba.py" title="_sources/source-07/models/Mamba.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/Mamba.py" title="_sources/source-08/models/Mamba.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/state_space_dynamics/mamba/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2312.00752" title="模型论文">论&#8288;文</a><br><a href="models/state_space_dynamics/mamba/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/state_space_dynamics/mambasimple/README.md">M&#8288;a&#8288;m&#8288;b&#8288;a&#8288;S&#8288;i&#8288;m&#8288;p&#8288;l&#8288;e</a></td>
<td align="left">在保留较简化的 Mamba 与扫描计算实现，便于阅读状态递推机制。</td>
<td align="left"><a href="models/state_space_dynamics/mambasimple/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/MambaSimple.py" title="_sources/source-07/models/MambaSimple.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/MambaSimple.py" title="_sources/source-08/models/MambaSimple.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/state_space_dynamics/mambasimple/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2312.00752" title="共用 Mamba 方法论文；当前文件是简化实现，参考 mamba-minimal，不宣称另有独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/state_space_dynamics/mambasimple/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/state_space_dynamics/mambasinglelayer/README.md">M&#8288;a&#8288;m&#8288;b&#8288;a&#8288;S&#8288;i&#8288;n&#8288;g&#8288;l&#8288;e&#8288;L&#8288;a&#8288;y&#8288;e&#8288;r</a><br><sub>MambaSL</sub></td>
<td align="left">用单层 Mamba 做序列分类，当前构造和前向路径限定分类任务。</td>
<td align="left"><a href="models/state_space_dynamics/mambasinglelayer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/MambaSingleLayer.py" title="_sources/source-07/models/MambaSingleLayer.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/state_space_dynamics/mambasinglelayer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/forum?id=YDl4vqQqGP" title="当前模块对应 MambaSL 分类论文；文件名 MambaSingleLayer 与论文模型名 MambaSL 分别保留。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/state_space_dynamics/mambasinglelayer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/mgru_fcn/README.md">M&#8288;G&#8288;R&#8288;U&#8288;_&#8288;F&#8288;C&#8288;N</a></td>
<td align="left">面向多变量序列的 GRU 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="models/recurrent_convolution/mgru_fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCN.py" title="_sources/source-09/tsai/models/RNN_FCN.py :: MGRU_FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/mgru_fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/mgru_fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/mgru_fcnplus/README.md">M&#8288;G&#8288;R&#8288;U&#8288;_&#8288;F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">面向多变量序列的 GRU 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="models/recurrent_convolution/mgru_fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCNPlus.py" title="_sources/source-09/tsai/models/RNN_FCNPlus.py :: MGRU_FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/mgru_fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/mgru_fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/micn/README.md">M&#8288;I&#8288;C&#8288;N</a></td>
<td align="left">用多尺度下采样、等距和上采样卷积提取局部与全局变化，并结合序列分解。</td>
<td align="left"><a href="models/recurrent_convolution/micn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/MICN.py" title="_sources/source-07/models/MICN.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/MICN.py" title="_sources/source-08/models/MICN.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/micn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=zt53IDUR1U" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/micn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/minirocket/README.md">M&#8288;i&#8288;n&#8288;i&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t</a><br><sub>MiniRocketClassifier / MiniRocketRegressor</sub></td>
<td align="left">用固定形式的卷积核和阈值统计快速生成分类或回归特征。</td>
<td align="left"><a href="models/recurrent_convolution/minirocket/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MINIROCKET.py" title="_sources/source-09/tsai/models/MINIROCKET.py :: MiniRocketClassifier">实&#8288;现&#8288;1</a><br><a href="_sources/source-09/tsai/models/MINIROCKET.py" title="_sources/source-09/tsai/models/MINIROCKET.py :: MiniRocketRegressor">实&#8288;现&#8288;2</a><br><a href="_sources/source-09/tsai/models/MINIROCKET_Pytorch.py" title="_sources/source-09/tsai/models/MINIROCKET_Pytorch.py :: MiniRocket">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/recurrent_convolution/minirocket/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2102.00457" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/minirocket/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/minirocketplus/README.md">M&#8288;i&#8288;n&#8288;i&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">用固定形式的卷积核和阈值统计快速生成分类或回归特征。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/recurrent_convolution/minirocketplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MINIROCKETPlus_Pytorch.py" title="_sources/source-09/tsai/models/MINIROCKETPlus_Pytorch.py :: MiniRocketPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/minirocketplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2102.00457" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/minirocketplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingclassifier/README.md">M&#8288;i&#8288;n&#8288;i&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t&#8288;V&#8288;o&#8288;t&#8288;i&#8288;n&#8288;g&#8288;C&#8288;l&#8288;a&#8288;s&#8288;s&#8288;i&#8288;f&#8288;i&#8288;e&#8288;r</a></td>
<td align="left">通过投票组合多个 MiniRocket 分类器。</td>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingclassifier/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MINIROCKET.py" title="_sources/source-09/tsai/models/MINIROCKET.py :: MiniRocketVotingClassifier">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingclassifier/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingclassifier/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingregressor/README.md">M&#8288;i&#8288;n&#8288;i&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t&#8288;V&#8288;o&#8288;t&#8288;i&#8288;n&#8288;g&#8288;R&#8288;e&#8288;g&#8288;r&#8288;e&#8288;s&#8288;s&#8288;o&#8288;r</a></td>
<td align="left">通过投票或平均组合多个 MiniRocket 回归器。</td>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingregressor/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MINIROCKET.py" title="_sources/source-09/tsai/models/MINIROCKET.py :: MiniRocketVotingRegressor">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingregressor/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/minirocketvotingregressor/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/mlp/README.md">M&#8288;L&#8288;P</a></td>
<td align="left">将历史窗口或表格变量交给多层前馈网络，作为非线性对照。</td>
<td align="left"><a href="models/linear_mlp/mlp/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MLP.py" title="_sources/source-09/tsai/models/MLP.py :: MLP">实&#8288;现&#8288;1</a><br><a href="_sources/source-10/neuralforecast/models/mlp.py" title="_sources/source-10/neuralforecast/models/mlp.py :: MLP">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/linear_mlp/mlp/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/mlp/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/mlpmultivariate/README.md">M&#8288;L&#8288;P&#8288;M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;v&#8288;a&#8288;r&#8288;i&#8288;a&#8288;t&#8288;e</a></td>
<td align="left">将多条序列的历史合并输入 MLP，联合产生多变量预测。</td>
<td align="left"><a href="models/linear_mlp/mlpmultivariate/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/mlpmultivariate.py" title="_sources/source-10/neuralforecast/models/mlpmultivariate.py :: MLPMultivariate">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/mlpmultivariate/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/linear_mlp/mlpmultivariate/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/mlstm_fcn/README.md">M&#8288;L&#8288;S&#8288;T&#8288;M&#8288;_&#8288;F&#8288;C&#8288;N</a></td>
<td align="left">面向多变量序列的 LSTM 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="models/recurrent_convolution/mlstm_fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCN.py" title="_sources/source-09/tsai/models/RNN_FCN.py :: MLSTM_FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/mlstm_fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0893608019301200" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/mlstm_fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/mlstm_fcnplus/README.md">M&#8288;L&#8288;S&#8288;T&#8288;M&#8288;_&#8288;F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">面向多变量序列的 LSTM 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="models/recurrent_convolution/mlstm_fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCNPlus.py" title="_sources/source-09/tsai/models/RNN_FCNPlus.py :: MLSTM_FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/mlstm_fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/abs/pii/S0893608019301200" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/mlstm_fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/moderntcn/README.md">M&#8288;o&#8288;d&#8288;e&#8288;r&#8288;n&#8288;T&#8288;C&#8288;N</a><br><sub>ModernTCNForecaster</sub></td>
<td align="left">用现代深度卷积分别组织时间、变量和特征维的信息。</td>
<td align="left"><a href="models/recurrent_convolution/moderntcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/modern_tcn/_modern_tcn_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/modern_tcn/_modern_tcn_forecaster_v2.py :: ModernTCNForecaster">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/modern_tcn/_modern_tcn_v2.py" title="_sources/source-11/pytorch_forecasting/models/modern_tcn/_modern_tcn_v2.py :: ModernTCN">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/moderntcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2401.17593" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/moderntcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/moirai/README.md">M&#8288;o&#8288;i&#8288;r&#8288;a&#8288;i</a></td>
<td align="left">调用 uni2ts 的预训练 Moirai 模型，接口用于零样本预测。</td>
<td align="left"><a href="models/pretrained_foundation/moirai/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Moirai.py" title="_sources/source-07/models/Moirai.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/moirai/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2402.02592" title="链接为上游 README 列出的 Moirai 系列论文；当前接口实际加载 moirai-2.0-R-small，具体版本以源码和权重标识为准。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/pretrained_foundation/moirai/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcn/README.md">M&#8288;R&#8288;N&#8288;N&#8288;_&#8288;F&#8288;C&#8288;N</a></td>
<td align="left">面向多变量序列的 RNN 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCN.py" title="_sources/source-09/tsai/models/RNN_FCN.py :: MRNN_FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcnplus/README.md">M&#8288;R&#8288;N&#8288;N&#8288;_&#8288;F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">面向多变量序列的 RNN 与全卷积混合网络，保留通道增强和对应配置。</td>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCNPlus.py" title="_sources/source-09/tsai/models/RNN_FCNPlus.py :: MRNN_FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/mrnn_fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/graph/msgnet/README.md">M&#8288;S&#8288;G&#8288;N&#8288;e&#8288;t</a></td>
<td align="left">先发现不同周期尺度，再通过图卷积和注意力学习多变量之间的关系。</td>
<td align="left"><a href="models/graph/msgnet/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/MSGNet.py" title="_sources/source-07/models/MSGNet.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/graph/msgnet/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://dl.acm.org/doi/10.1609/aaai.v38i10.28991" title="模型论文">论&#8288;文</a><br><a href="models/graph/msgnet/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/multiinceptiontimeplus/README.md">M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;I&#8288;n&#8288;c&#8288;e&#8288;p&#8288;t&#8288;i&#8288;o&#8288;n&#8288;T&#8288;i&#8288;m&#8288;e&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">以多个 InceptionTimePlus 分支处理输入组并融合输出。</td>
<td align="left"><a href="models/ensemble_calibration/multiinceptiontimeplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: MultiInceptionTimePlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/multiinceptiontimeplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/multiinceptiontimeplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/multiinputnet/README.md">M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;I&#8288;n&#8288;p&#8288;u&#8288;t&#8288;N&#8288;e&#8288;t</a></td>
<td align="left">将多个输入分支或骨干连接到统一输出头的封装。</td>
<td align="left"><a href="models/model_adapter/multiinputnet/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MultiInputNet.py" title="_sources/source-09/tsai/models/MultiInputNet.py :: MultiInputNet">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/multiinputnet/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/model_adapter/multiinputnet/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/multipatchformer/README.md">M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;P&#8288;a&#8288;t&#8288;c&#8288;h&#8288;F&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">用多种 patch 尺度表示序列，再结合注意力组织不同尺度与通道信息。</td>
<td align="left"><a href="models/transformer_attention/multipatchformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/MultiPatchFormer.py" title="_sources/source-07/models/MultiPatchFormer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/MultiPatchFormer.py" title="_sources/source-08/models/MultiPatchFormer.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/multipatchformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://www.nature.com/articles/s41598-024-82417-4" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/multipatchformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/multirocketplus/README.md">M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;R&#8288;o&#8288;c&#8288;k&#8288;e&#8288;t&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">联合原序列与差分序列的多种卷积池化统计特征。</td>
<td align="left"><a href="models/recurrent_convolution/multirocketplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/MultiRocketPlus.py" title="_sources/source-09/tsai/models/MultiRocketPlus.py :: MultiRocketPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/multirocketplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/multirocketplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/multitstplus/README.md">M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;T&#8288;S&#8288;T&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">对输入组分别应用 TSTPlus，再融合表示的封装。</td>
<td align="left"><a href="models/model_adapter/multitstplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TSTPlus.py" title="_sources/source-09/tsai/models/TSTPlus.py :: MultiTSTPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/multitstplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/model_adapter/multitstplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/multivariatemodel/README.md">M&#8288;u&#8288;l&#8288;t&#8288;i&#8288;v&#8288;a&#8288;r&#8288;i&#8288;a&#8288;t&#8288;e&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">将多个单变量预测器组合为统一多变量模型。</td>
<td align="left"><a href="models/model_adapter/multivariatemodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/multivariate_model.py" title="_sources/source-12/darts/models/forecasting/multivariate_model.py :: MultivariateModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/multivariatemodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/model_adapter/multivariatemodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/mwdn/README.md">m&#8288;W&#8288;D&#8288;N</a></td>
<td align="left">以可训练小波分解形成多分辨率表示，再接序列任务网络。</td>
<td align="left"><a href="models/decomposition_frequency/mwdn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/mWDN.py" title="_sources/source-09/tsai/models/mWDN.py :: mWDN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/decomposition_frequency/mwdn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3219819.3220060" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/mwdn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/mwdnplus/README.md">m&#8288;W&#8288;D&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">以可训练小波分解形成多分辨率表示，再接序列任务网络。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/decomposition_frequency/mwdnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/mWDN.py" title="_sources/source-09/tsai/models/mWDN.py :: mWDNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/decomposition_frequency/mwdnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3219819.3220060" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/decomposition_frequency/mwdnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/naivedrift/README.md">N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;D&#8288;r&#8288;i&#8288;f&#8288;t</a></td>
<td align="left">将首尾观测确定的平均变化速率延伸到未来。</td>
<td align="left"><a href="models/statistical/naivedrift/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/baselines.py" title="_sources/source-12/darts/models/forecasting/baselines.py :: NaiveDrift">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/naivedrift/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/naivedrift/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/naiveensemblemodel/README.md">N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;E&#8288;n&#8288;s&#8288;e&#8288;m&#8288;b&#8288;l&#8288;e&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">训练多个基础预测器，对预测结果做简单平均。</td>
<td align="left"><a href="models/ensemble_calibration/naiveensemblemodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/naive_ensemble_model.py" title="_sources/source-12/darts/models/forecasting/naive_ensemble_model.py :: NaiveEnsembleModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/naiveensemblemodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/naiveensemblemodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/naivemean/README.md">N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;M&#8288;e&#8288;a&#8288;n</a></td>
<td align="left">以历史平均值预测未来。</td>
<td align="left"><a href="models/statistical/naivemean/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/baselines.py" title="_sources/source-12/darts/models/forecasting/baselines.py :: NaiveMean">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/naivemean/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/naivemean/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/naivemovingaverage/README.md">N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;M&#8288;o&#8288;v&#8288;i&#8288;n&#8288;g&#8288;A&#8288;v&#8288;e&#8288;r&#8288;a&#8288;g&#8288;e</a></td>
<td align="left">利用末段窗口的移动平均递推预测。</td>
<td align="left"><a href="models/statistical/naivemovingaverage/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/baselines.py" title="_sources/source-12/darts/models/forecasting/baselines.py :: NaiveMovingAverage">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/naivemovingaverage/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/naivemovingaverage/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/naiveseasonal/README.md">N&#8288;a&#8288;i&#8288;v&#8288;e&#8288;S&#8288;e&#8288;a&#8288;s&#8288;o&#8288;n&#8288;a&#8288;l</a></td>
<td align="left">重复最后一个季节周期的观测。</td>
<td align="left"><a href="models/statistical/naiveseasonal/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/baselines.py" title="_sources/source-12/darts/models/forecasting/baselines.py :: NaiveSeasonal">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/naiveseasonal/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/naiveseasonal/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/nbeats/README.md">N&#8288;B&#8288;E&#8288;A&#8288;T&#8288;S</a><br><sub>NBEATSModel / NBeats / NBeats_pkg</sub></td>
<td align="left">堆叠残差前馈块，分别拟合历史与预测基函数并累加结果。</td>
<td align="left"><a href="models/linear_mlp/nbeats/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/nbeats.py" title="_sources/source-10/neuralforecast/models/nbeats.py :: NBEATS">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeats.py" title="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeats.py :: NBeats">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeats_pkg.py" title="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeats_pkg.py :: NBeats_pkg">实&#8288;现&#8288;3</a><br><a href="_sources/source-12/darts/models/forecasting/nbeats.py" title="_sources/source-12/darts/models/forecasting/nbeats.py :: NBEATSModel">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/linear_mlp/nbeats/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1905.10437" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/nbeats/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/nbeatskan/README.md">N&#8288;B&#8288;E&#8288;A&#8288;T&#8288;S&#8288;K&#8288;A&#8288;N</a><br><sub>NBeatsKAN / NBeatsKAN_pkg</sub></td>
<td align="left">在 N-BEATS 式残差结构中使用 KAN 层的变体。</td>
<td align="left"><a href="models/linear_mlp/nbeatskan/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeatskan.py" title="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeatskan.py :: NBeatsKAN">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeatskan_pkg.py" title="_sources/source-11/pytorch_forecasting/models/nbeats/_nbeatskan_pkg.py :: NBeatsKAN_pkg">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/linear_mlp/nbeatskan/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/linear_mlp/nbeatskan/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/nbeatsx/README.md">N&#8288;B&#8288;E&#8288;A&#8288;T&#8288;S&#8288;x</a></td>
<td align="left">在 N-BEATS 中加入历史和未来外生变量。</td>
<td align="left"><a href="models/linear_mlp/nbeatsx/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/nbeatsx.py" title="_sources/source-10/neuralforecast/models/nbeatsx.py :: NBEATSx">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/nbeatsx/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2104.05522" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/nbeatsx/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/neuralforecastmodel/README.md">N&#8288;e&#8288;u&#8288;r&#8288;a&#8288;l&#8288;F&#8288;o&#8288;r&#8288;e&#8288;c&#8288;a&#8288;s&#8288;t&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">把 模型接入 的训练和预测接口。</td>
<td align="left"><a href="models/model_adapter/neuralforecastmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/nf_model.py" title="_sources/source-12/darts/models/forecasting/nf_model.py :: NeuralForecastModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/neuralforecastmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/forum?id=cGDAkQo1C0p" title="此链接是源码列出的 TiDE 相关文献；本项是 NeuralForecast 接口适配器，不是该论文方法。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/model_adapter/neuralforecastmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/nhits/README.md">N&#8288;H&#8288;I&#8288;T&#8288;S</a><br><sub>NHiTS / NHiTSForecaster / NHiTSModel / NHiTS_pkg / NHiTS_v2</sub></td>
<td align="left">以多分辨率采样和分层插值组合短期细节与长期预测。</td>
<td align="left"><a href="models/linear_mlp/nhits/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/nhits.py" title="_sources/source-10/neuralforecast/models/nhits.py :: NHITS">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/nhits/_nhits.py" title="_sources/source-11/pytorch_forecasting/models/nhits/_nhits.py :: NHiTS">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/nhits/_nhits_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/nhits/_nhits_forecaster_v2.py :: NHiTSForecaster">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/nhits/_nhits_pkg.py" title="_sources/source-11/pytorch_forecasting/models/nhits/_nhits_pkg.py :: NHiTS_pkg">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/nhits/_nhits_v2.py" title="_sources/source-11/pytorch_forecasting/models/nhits/_nhits_v2.py :: NHiTS_v2">实&#8288;现&#8288;5</a><br><a href="_sources/source-12/darts/models/forecasting/nhits.py" title="_sources/source-12/darts/models/forecasting/nhits.py :: NHiTSModel">实&#8288;现&#8288;6</a></td>
<td align="left"><a href="models/linear_mlp/nhits/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2201.12886" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/nhits/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/nlinear/README.md">N&#8288;L&#8288;i&#8288;n&#8288;e&#8288;a&#8288;r</a><br><sub>NLinearModel</sub></td>
<td align="left">减去窗口最后一个值后线性预测变化，再加回该值。</td>
<td align="left"><a href="models/linear_mlp/nlinear/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/nlinear.py" title="_sources/source-10/neuralforecast/models/nlinear.py :: NLinear">实&#8288;现&#8288;1</a><br><a href="_sources/source-12/darts/models/forecasting/nlinear.py" title="_sources/source-12/darts/models/forecasting/nlinear.py :: NLinearModel">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/linear_mlp/nlinear/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/26317" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/nlinear/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/nonstationary_transformer/README.md">N&#8288;o&#8288;n&#8288;s&#8288;t&#8288;a&#8288;t&#8288;i&#8288;o&#8288;n&#8288;a&#8288;r&#8288;y&#8288;_&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a><br><sub>Non-stationary Transformer</sub></td>
<td align="left">在归一化输入之外学习去平稳注意力因子，补回序列的非平稳信息。</td>
<td align="left"><a href="models/transformer_attention/nonstationary_transformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Nonstationary_Transformer.py" title="_sources/source-07/models/Nonstationary_Transformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/Nonstationary_Transformer.py" title="_sources/source-08/models/Nonstationary_Transformer.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/nonstationary_transformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=ucNDIDRNjjv" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/nonstationary_transformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/omniscalecnn/README.md">O&#8288;m&#8288;n&#8288;i&#8288;S&#8288;c&#8288;a&#8288;l&#8288;e&#8288;C&#8288;N&#8288;N</a></td>
<td align="left">组合不同尺度的一维卷积核，减少手工选择尺度的依赖。</td>
<td align="left"><a href="models/recurrent_convolution/omniscalecnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/OmniScaleCNN.py" title="_sources/source-09/tsai/models/OmniScaleCNN.py :: OmniScaleCNN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/omniscalecnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2002.10061" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/omniscalecnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/patchtst/README.md">P&#8288;a&#8288;t&#8288;c&#8288;h&#8288;T&#8288;S&#8288;T</a><br><sub>PatchTSTForecaster / PatchTST_pkg / PatchTST_v2</sub></td>
<td align="left">把连续时间点切为 patch，并以通道独立的 Transformer 建模长历史。</td>
<td align="left"><a href="models/transformer_attention/patchtst/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/PatchTST.py" title="_sources/source-07/models/PatchTST.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/PatchTST.py" title="_sources/source-08/models/PatchTST.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-09/tsai/models/PatchTST.py" title="_sources/source-09/tsai/models/PatchTST.py :: PatchTST">实&#8288;现&#8288;3</a><br><a href="_sources/source-10/neuralforecast/models/patchtst.py" title="_sources/source-10/neuralforecast/models/patchtst.py :: PatchTST">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_forecaster_v2.py :: PatchTSTForecaster">实&#8288;现&#8288;5</a><br><a href="_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_pkg.py" title="_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_pkg.py :: PatchTST_pkg">实&#8288;现&#8288;6</a><br><a href="_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_v2.py" title="_sources/source-11/pytorch_forecasting/models/patch_tst/_patch_tst_v2.py :: PatchTST_v2">实&#8288;现&#8288;7</a><br><a href="_sources/source-11/pytorch_forecasting/models/patch_tst/patch_tst.py" title="_sources/source-11/pytorch_forecasting/models/patch_tst/patch_tst.py :: PatchTST">实&#8288;现&#8288;8</a></td>
<td align="left"><a href="models/transformer_attention/patchtst/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=Jbdc0vTOcol" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/patchtst/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/patchtstfmmodel/README.md">P&#8288;a&#8288;t&#8288;c&#8288;h&#8288;T&#8288;S&#8288;T&#8288;F&#8288;M&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">调用预训练 PatchTST foundation model，与从头训练版本区分。</td>
<td align="left"><a href="models/pretrained_foundation/patchtstfmmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/patchtst_fm_model.py" title="_sources/source-12/darts/models/forecasting/patchtst_fm_model.py :: PatchTSTFMModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/patchtstfmmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2602.06909" title="模型论文">论&#8288;文</a><br><a href="models/pretrained_foundation/patchtstfmmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/pattn/README.md">P&#8288;A&#8288;t&#8288;t&#8288;n</a></td>
<td align="left">用 patch 嵌入和单层注意力进行预测，提供无需调用语言模型的对照入口。</td>
<td align="left"><a href="models/transformer_attention/pattn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/PAttn.py" title="_sources/source-07/models/PAttn.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/PAttn.py" title="_sources/source-08/models/PAttn.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/pattn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2406.16964" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/pattn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/prophet/README.md">P&#8288;r&#8288;o&#8288;p&#8288;h&#8288;e&#8288;t</a></td>
<td align="left">组合可分解的趋势、季节与节假日成分预测。</td>
<td align="left"><a href="models/statistical/prophet/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/prophet_model.py" title="_sources/source-12/darts/models/forecasting/prophet_model.py :: Prophet">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/prophet/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/prophet/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/pyraformer/README.md">P&#8288;y&#8288;r&#8288;a&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">构建多尺度金字塔，在层内与层间设置稀疏连接以传递长期信息。</td>
<td align="left"><a href="models/transformer_attention/pyraformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-02/pyraformer/Pyraformer_LR.py" title="_sources/source-02/pyraformer/Pyraformer_LR.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-02/pyraformer/Pyraformer_SS.py" title="_sources/source-02/pyraformer/Pyraformer_SS.py">实&#8288;现&#8288;1&#8288;·&#8288;单&#8288;步</a><br><a href="_sources/source-07/models/Pyraformer.py" title="_sources/source-07/models/Pyraformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-08/models/Pyraformer.py" title="_sources/source-08/models/Pyraformer.py">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/transformer_attention/pyraformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/forum?id=0EXmFzUn5I" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/pyraformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/randomforestmodel/README.md">R&#8288;a&#8288;n&#8288;d&#8288;o&#8288;m&#8288;F&#8288;o&#8288;r&#8288;e&#8288;s&#8288;t&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">以随机森林学习滞后值和协变量到未来值的映射。</td>
<td align="left"><a href="models/machine_learning/randomforestmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/random_forest.py" title="_sources/source-12/darts/models/forecasting/random_forest.py :: RandomForestModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/randomforestmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/randomforestmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/recurrentnetwork/README.md">R&#8288;e&#8288;c&#8288;u&#8288;r&#8288;r&#8288;e&#8288;n&#8288;t&#8288;N&#8288;e&#8288;t&#8288;w&#8288;o&#8288;r&#8288;k</a><br><sub>RecurrentNetwork_pkg</sub></td>
<td align="left">以可配置的 LSTM 或 GRU 网络进行多步预测。</td>
<td align="left"><a href="models/recurrent_convolution/recurrentnetwork/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/rnn/_rnn.py" title="_sources/source-11/pytorch_forecasting/models/rnn/_rnn.py :: RecurrentNetwork">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/rnn/_rnn_pkg.py" title="_sources/source-11/pytorch_forecasting/models/rnn/_rnn_pkg.py :: RecurrentNetwork_pkg">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/recurrentnetwork/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/recurrentnetwork/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/reformer/README.md">R&#8288;e&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">使用 Reformer 的局部敏感哈希注意力处理长序列。</td>
<td align="left"><a href="models/transformer_attention/reformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Reformer.py" title="_sources/source-07/models/Reformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/Reformer.py" title="_sources/source-08/models/Reformer.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/reformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/forum?id=rkgNKkHtvB" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/reformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/ensemble_calibration/regressionensemblemodel/README.md">R&#8288;e&#8288;g&#8288;r&#8288;e&#8288;s&#8288;s&#8288;i&#8288;o&#8288;n&#8288;E&#8288;n&#8288;s&#8288;e&#8288;m&#8288;b&#8288;l&#8288;e&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">学习回归式组合器，融合多个基础预测结果。</td>
<td align="left"><a href="models/ensemble_calibration/regressionensemblemodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/regression_ensemble_model.py" title="_sources/source-12/darts/models/forecasting/regression_ensemble_model.py :: RegressionEnsembleModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/ensemble_calibration/regressionensemblemodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/ensemble_calibration/regressionensemblemodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rescnn/README.md">R&#8288;e&#8288;s&#8288;C&#8288;N&#8288;N</a></td>
<td align="left">结合一维卷积和残差连接的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/rescnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/ResCNN.py" title="_sources/source-09/tsai/models/ResCNN.py :: ResCNN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/rescnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://www.sciencedirect.com/science/article/pii/S0925231219311506" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/rescnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/resnet/README.md">R&#8288;e&#8288;s&#8288;N&#8288;e&#8288;t</a></td>
<td align="left">通过残差一维卷积堆叠提取时间序列特征。</td>
<td align="left"><a href="models/recurrent_convolution/resnet/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/ResNet.py" title="_sources/source-09/tsai/models/ResNet.py :: ResNet">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/resnet/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/resnet/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/resnetplus/README.md">R&#8288;e&#8288;s&#8288;N&#8288;e&#8288;t&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">通过残差一维卷积堆叠提取时间序列特征。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/recurrent_convolution/resnetplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/ResNetPlus.py" title="_sources/source-09/tsai/models/ResNetPlus.py :: ResNetPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/resnetplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1611.06455" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/resnetplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/rmok/README.md">R&#8288;M&#8288;o&#8288;K</a></td>
<td align="left">通过路由组合多种 KAN 专家，利用不同函数基预测。</td>
<td align="left"><a href="models/linear_mlp/rmok/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/rmok.py" title="_sources/source-10/neuralforecast/models/rmok.py :: RMoK">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/rmok/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2408.11306" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/rmok/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rnn/README.md">R&#8288;N&#8288;N</a><br><sub>RNNModel</sub></td>
<td align="left">通过循环隐藏状态编码历史，再预测未来或输出任务标签。</td>
<td align="left"><a href="models/recurrent_convolution/rnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN.py" title="_sources/source-09/tsai/models/RNN.py :: RNN">实&#8288;现&#8288;1</a><br><a href="_sources/source-10/neuralforecast/models/rnn.py" title="_sources/source-10/neuralforecast/models/rnn.py :: RNN">实&#8288;现&#8288;2</a><br><a href="_sources/source-12/darts/models/forecasting/rnn_model.py" title="_sources/source-12/darts/models/forecasting/rnn_model.py :: RNNModel">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/recurrent_convolution/rnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/rnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rnn_fcn/README.md">R&#8288;N&#8288;N&#8288;_&#8288;F&#8288;C&#8288;N</a></td>
<td align="left">融合 RNN 循环分支与全卷积分支的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/rnn_fcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCN.py" title="_sources/source-09/tsai/models/RNN_FCN.py :: RNN_FCN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/rnn_fcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/rnn_fcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rnn_fcnplus/README.md">R&#8288;N&#8288;N&#8288;_&#8288;F&#8288;C&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">融合 RNN 循环分支与全卷积分支的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="models/recurrent_convolution/rnn_fcnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNN_FCNPlus.py" title="_sources/source-09/tsai/models/RNN_FCNPlus.py :: RNN_FCNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/rnn_fcnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/rnn_fcnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rnnattention/README.md">R&#8288;N&#8288;N&#8288;A&#8288;t&#8288;t&#8288;e&#8288;n&#8288;t&#8288;i&#8288;o&#8288;n</a></td>
<td align="left">结合 RNN 循环表示和注意力编码模块的序列网络。</td>
<td align="left"><a href="models/recurrent_convolution/rnnattention/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNAttention.py" title="_sources/source-09/tsai/models/RNNAttention.py :: RNNAttention">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/rnnattention/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/rnnattention/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rnnattentionplus/README.md">R&#8288;N&#8288;N&#8288;A&#8288;t&#8288;t&#8288;e&#8288;n&#8288;t&#8288;i&#8288;o&#8288;n&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">结合 RNN 循环表示和注意力编码模块的序列网络。 此项保留 Plus 配置扩展。</td>
<td align="left"><a href="models/recurrent_convolution/rnnattentionplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNAttentionPlus.py" title="_sources/source-09/tsai/models/RNNAttentionPlus.py :: RNNAttentionPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/rnnattentionplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/rnnattentionplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rnnplus/README.md">R&#8288;N&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">RNN 的 可配置骨干与任务头变体。</td>
<td align="left"><a href="models/recurrent_convolution/rnnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/RNNPlus.py" title="_sources/source-09/tsai/models/RNNPlus.py :: RNNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/rnnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/rnnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/rocket/README.md">R&#8288;O&#8288;C&#8288;K&#8288;E&#8288;T</a><br><sub>RocketClassifier / RocketRegressor</sub></td>
<td align="left">用大量随机卷积核生成统计特征，再接线性分类或回归器。</td>
<td align="left"><a href="models/recurrent_convolution/rocket/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/ROCKET.py" title="_sources/source-09/tsai/models/ROCKET.py :: RocketClassifier">实&#8288;现&#8288;1</a><br><a href="_sources/source-09/tsai/models/ROCKET.py" title="_sources/source-09/tsai/models/ROCKET.py :: RocketRegressor">实&#8288;现&#8288;2</a><br><a href="_sources/source-09/tsai/models/ROCKET_Pytorch.py" title="_sources/source-09/tsai/models/ROCKET_Pytorch.py :: ROCKET">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/recurrent_convolution/rocket/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1910.13051" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/rocket/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/samformer/README.md">S&#8288;a&#8288;m&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a><br><sub>SamformerForecaster</sub></td>
<td align="left">以浅层注意力组织变量关系，结合对应训练策略预测。</td>
<td align="left"><a href="models/transformer_attention/samformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/samformer/_samformer_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/samformer/_samformer_forecaster_v2.py :: SamformerForecaster">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/samformer/_samformer_v2.py" title="_sources/source-11/pytorch_forecasting/models/samformer/_samformer_v2.py :: Samformer">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/samformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/samformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/scinet/README.md">S&#8288;C&#8288;I&#8288;N&#8288;e&#8288;t</a><br><sub>SCINetForecaster / SCINet_v2</sub></td>
<td align="left">递归拆分奇偶时间点，用交互卷积交换信息后重新合并序列。</td>
<td align="left"><a href="models/recurrent_convolution/scinet/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/SCINet.py" title="_sources/source-07/models/SCINet.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/SCINet.py" title="_sources/source-08/models/SCINet.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/scinet/_scinet_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/scinet/_scinet_forecaster_v2.py :: SCINetForecaster">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/scinet/_scinet_v2.py" title="_sources/source-11/pytorch_forecasting/models/scinet/_scinet_v2.py :: SCINet_v2">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/recurrent_convolution/scinet/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=AyajSjTAzmg" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/scinet/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/segrnn/README.md">S&#8288;e&#8288;g&#8288;R&#8288;N&#8288;N</a></td>
<td align="left">将序列分段后交给 GRU 编码，再按预测片段输出未来值。</td>
<td align="left"><a href="models/recurrent_convolution/segrnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/SegRNN.py" title="_sources/source-07/models/SegRNN.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/SegRNN.py" title="_sources/source-08/models/SegRNN.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/segrnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2308.11200.pdf" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/segrnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/sklearnclassifiermodel/README.md">S&#8288;K&#8288;L&#8288;e&#8288;a&#8288;r&#8288;n&#8288;C&#8288;l&#8288;a&#8288;s&#8288;s&#8288;i&#8288;f&#8288;i&#8288;e&#8288;r&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">将 scikit-learn 分类器接入序列预测。</td>
<td align="left"><a href="models/model_adapter/sklearnclassifiermodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sklearn_model.py" title="_sources/source-12/darts/models/forecasting/sklearn_model.py :: SKLearnClassifierModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/sklearnclassifiermodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/model_adapter/sklearnclassifiermodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/sklearnmodel/README.md">S&#8288;K&#8288;L&#8288;e&#8288;a&#8288;r&#8288;n&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">将 scikit-learn 回归器接入滞后特征预测。</td>
<td align="left"><a href="models/model_adapter/sklearnmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sklearn_model.py" title="_sources/source-12/darts/models/forecasting/sklearn_model.py :: SKLearnModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/sklearnmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/model_adapter/sklearnmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/softs/README.md">S&#8288;O&#8288;F&#8288;T&#8288;S</a><br><sub>SOFTSForecaster</sub></td>
<td align="left">将多变量聚合到共享核心，再融合回各变量，控制交互成本。</td>
<td align="left"><a href="models/linear_mlp/softs/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/softs.py" title="_sources/source-10/neuralforecast/models/softs.py :: SOFTS">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/softs/_softs_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/softs/_softs_forecaster_v2.py :: SOFTSForecaster">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/softs/_softs_v2.py" title="_sources/source-11/pytorch_forecasting/models/softs/_softs_v2.py :: SOFTS">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/linear_mlp/softs/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2404.14197" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/softs/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/softssharp/README.md">S&#8288;O&#8288;F&#8288;T&#8288;S&#8288;S&#8288;h&#8288;a&#8288;r&#8288;p</a></td>
<td align="left">在 SOFTS 类结构中加入随机变量位置编码。</td>
<td align="left"><a href="models/linear_mlp/softssharp/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/softssharp.py" title="_sources/source-10/neuralforecast/models/softssharp.py :: SOFTSSharp">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/softssharp/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/linear_mlp/softssharp/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/model_adapter/statsforecastmodel/README.md">S&#8288;t&#8288;a&#8288;t&#8288;s&#8288;F&#8288;o&#8288;r&#8288;e&#8288;c&#8288;a&#8288;s&#8288;t&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">把 StatsForecast 统计模型接入 接口。</td>
<td align="left"><a href="models/model_adapter/statsforecastmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_model.py" title="_sources/source-12/darts/models/forecasting/sf_model.py :: StatsForecastModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/model_adapter/statsforecastmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/model_adapter/statsforecastmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/graph/stemgnn/README.md">S&#8288;t&#8288;e&#8288;m&#8288;G&#8288;N&#8288;N</a></td>
<td align="left">结合图傅里叶与时间傅里叶变换，学习变量关系和时间依赖。</td>
<td align="left"><a href="models/graph/stemgnn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/stemgnn.py" title="_sources/source-10/neuralforecast/models/stemgnn.py :: StemGNN">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/graph/stemgnn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://proceedings.neurips.cc/paper/2020/hash/cdf6581cb7aca4b7e19ef136c6e601a5-Abstract.html" title="模型论文">论&#8288;文</a><br><a href="models/graph/stemgnn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/sundial/README.md">S&#8288;u&#8288;n&#8288;d&#8288;i&#8288;a&#8288;l</a></td>
<td align="left">调用外部预训练 Sundial 时序模型，保留其零样本预测适配接口。</td>
<td align="left"><a href="models/pretrained_foundation/sundial/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Sundial.py" title="_sources/source-07/models/Sundial.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/sundial/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2502.00816" title="模型论文">论&#8288;文</a><br><a href="models/pretrained_foundation/sundial/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/t0/README.md">T&#8288;0</a><br><sub>T0Model</sub></td>
<td align="left">调用 T0 预训练时序模型，支持多变量和协变量。</td>
<td align="left"><a href="models/pretrained_foundation/t0/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/t0_model.py" title="_sources/source-12/darts/models/forecasting/t0_model.py :: T0Model">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/t0/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/pretrained_foundation/t0/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tabfusiontransformer/README.md">T&#8288;a&#8288;b&#8288;F&#8288;u&#8288;s&#8288;i&#8288;o&#8288;n&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">将类别和连续特征编码为 token，再用注意力融合。</td>
<td align="left"><a href="models/transformer_attention/tabfusiontransformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TabFusionTransformer.py" title="_sources/source-09/tsai/models/TabFusionTransformer.py :: TabFusionTransformer">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tabfusiontransformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/tabfusiontransformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/tabmodel/README.md">T&#8288;a&#8288;b&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">对类别嵌入和连续表格变量进行前馈建模。</td>
<td align="left"><a href="models/linear_mlp/tabmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TabModel.py" title="_sources/source-09/tsai/models/TabModel.py :: TabModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/tabmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/linear_mlp/tabmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tabtransformer/README.md">T&#8288;a&#8288;b&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">以注意力上下文化类别变量，再结合连续变量输出。</td>
<td align="left"><a href="models/transformer_attention/tabtransformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TabTransformer.py" title="_sources/source-09/tsai/models/TabTransformer.py :: TabTransformer">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tabtransformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2012.06678" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/tabtransformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/tbats/README.md">T&#8288;B&#8288;A&#8288;T&#8288;S</a></td>
<td align="left">组合变换、趋势、ARMA 误差和三角季节项。</td>
<td align="left"><a href="models/statistical/tbats/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/sf_tbats.py" title="_sources/source-12/darts/models/forecasting/sf_tbats.py :: TBATS">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/tbats/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/tbats/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/tcn/README.md">T&#8288;C&#8288;N</a><br><sub>TCNModel</sub></td>
<td align="left">叠加因果与扩张卷积，扩展时间感受野。</td>
<td align="left"><a href="models/recurrent_convolution/tcn/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TCN.py" title="_sources/source-09/tsai/models/TCN.py :: TCN">实&#8288;现&#8288;1</a><br><a href="_sources/source-10/neuralforecast/models/tcn.py" title="_sources/source-10/neuralforecast/models/tcn.py :: TCN">实&#8288;现&#8288;2</a><br><a href="_sources/source-12/darts/models/forecasting/tcn_model.py" title="_sources/source-12/darts/models/forecasting/tcn_model.py :: TCNModel">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/recurrent_convolution/tcn/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1803.01271" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/tcn/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/temporalfusiontransformer/README.md">T&#8288;e&#8288;m&#8288;p&#8288;o&#8288;r&#8288;a&#8288;l&#8288;F&#8288;u&#8288;s&#8288;i&#8288;o&#8288;n&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a><br><sub>TFT / TFTForecaster / TFTModel / TemporalFusionTransformer_pkg</sub></td>
<td align="left">通过变量选择、门控循环层和注意力融合历史与时间协变量。</td>
<td align="left"><a href="models/transformer_attention/temporalfusiontransformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TemporalFusionTransformer.py" title="_sources/source-07/models/TemporalFusionTransformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/TemporalFusionTransformer.py" title="_sources/source-08/models/TemporalFusionTransformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/tft.py" title="_sources/source-10/neuralforecast/models/tft.py :: TFT">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft.py" title="_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft.py :: TemporalFusionTransformer">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft_forecaster_v2.py :: TFTForecaster">实&#8288;现&#8288;5</a><br><a href="_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft_pkg.py" title="_sources/source-11/pytorch_forecasting/models/temporal_fusion_transformer/_tft_pkg.py :: TemporalFusionTransformer_pkg">实&#8288;现&#8288;6</a><br><a href="_sources/source-12/darts/models/forecasting/tft_model.py" title="_sources/source-12/darts/models/forecasting/tft_model.py :: TFTModel">实&#8288;现&#8288;7</a></td>
<td align="left"><a href="models/transformer_attention/temporalfusiontransformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1912.09363" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/temporalfusiontransformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/theta/README.md">T&#8288;h&#8288;e&#8288;t&#8288;a</a></td>
<td align="left">组合趋势与平滑后的 Theta 线进行外推。</td>
<td align="left"><a href="models/statistical/theta/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/theta.py" title="_sources/source-12/darts/models/forecasting/theta.py :: Theta">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/theta/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/theta/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/tide/README.md">T&#8288;i&#8288;D&#8288;E</a><br><sub>TIDE / TIDEForecaster / TiDEModel / TiDEModel_pkg</sub></td>
<td align="left">用残差 MLP 编码历史和协变量，再通过稠密解码与时间投影得到预测。</td>
<td align="left"><a href="models/linear_mlp/tide/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TiDE.py" title="_sources/source-07/models/TiDE.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/TiDE.py" title="_sources/source-08/models/TiDE.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/tide.py" title="_sources/source-10/neuralforecast/models/tide.py :: TiDE">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/tide/_tide.py" title="_sources/source-11/pytorch_forecasting/models/tide/_tide.py :: TiDEModel">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/tide/_tide_dsipts/_tide_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/tide/_tide_dsipts/_tide_forecaster_v2.py :: TIDEForecaster">实&#8288;现&#8288;5</a><br><a href="_sources/source-11/pytorch_forecasting/models/tide/_tide_dsipts/_tide_v2.py" title="_sources/source-11/pytorch_forecasting/models/tide/_tide_dsipts/_tide_v2.py :: TIDE">实&#8288;现&#8288;6</a><br><a href="_sources/source-11/pytorch_forecasting/models/tide/_tide_pkg.py" title="_sources/source-11/pytorch_forecasting/models/tide/_tide_pkg.py :: TiDEModel_pkg">实&#8288;现&#8288;7</a><br><a href="_sources/source-12/darts/models/forecasting/tide_model.py" title="_sources/source-12/darts/models/forecasting/tide_model.py :: TiDEModel">实&#8288;现&#8288;8</a></td>
<td align="left"><a href="models/linear_mlp/tide/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2304.08424.pdf" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/tide/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/llm_reprogramming/time-llm/README.md">T&#8288;i&#8288;m&#8288;e&#8288;-&#8288;L&#8288;L&#8288;M</a><br><sub>TimeLLM</sub></td>
<td align="left">把时序 patch 对齐到文本原型，并用提示词与冻结语言模型生成预测表示。</td>
<td align="left"><a href="models/llm_reprogramming/time-llm/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-06/models/TimeLLM.py" title="_sources/source-06/models/TimeLLM.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-10/neuralforecast/models/timellm.py" title="_sources/source-10/neuralforecast/models/timellm.py :: TimeLLM">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/llm_reprogramming/time-llm/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.01728" title="模型论文">论&#8288;文</a><br><a href="models/llm_reprogramming/time-llm/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/graph/timefilter/README.md">T&#8288;i&#8288;m&#8288;e&#8288;F&#8288;i&#8288;l&#8288;t&#8288;e&#8288;r</a></td>
<td align="left">将时序 patch 组织成图，用邻接构造和路由过滤关系后预测。</td>
<td align="left"><a href="models/graph/timefilter/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TimeFilter.py" title="_sources/source-07/models/TimeFilter.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/graph/timefilter/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2501.13041" title="模型论文">论&#8288;文</a><br><a href="models/graph/timefilter/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/timemixer/README.md">T&#8288;i&#8288;m&#8288;e&#8288;M&#8288;i&#8288;x&#8288;e&#8288;r</a></td>
<td align="left">将序列分为多个尺度和趋势季节成分，通过 MLP 混合并汇总多尺度预测。</td>
<td align="left"><a href="models/decomposition_frequency/timemixer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TimeMixer.py" title="_sources/source-07/models/TimeMixer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/TimeMixer.py" title="_sources/source-08/models/TimeMixer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/timemixer.py" title="_sources/source-10/neuralforecast/models/timemixer.py :: TimeMixer">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/decomposition_frequency/timemixer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=7oLshfEIC2" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/timemixer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/timemoe/README.md">T&#8288;i&#8288;m&#8288;e&#8288;M&#8288;o&#8288;E</a><br><sub>Time-MoE</sub></td>
<td align="left">调用预训练 TimeMoE 混合专家时序模型，入口用于零样本预测。</td>
<td align="left"><a href="models/pretrained_foundation/timemoe/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TimeMoE.py" title="_sources/source-07/models/TimeMoE.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/timemoe/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2409.16040" title="模型论文">论&#8288;文</a><br><a href="models/pretrained_foundation/timemoe/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/timesfm/README.md">T&#8288;i&#8288;m&#8288;e&#8288;s&#8288;F&#8288;M</a></td>
<td align="left">调用预训练 TimesFM 预测接口，外部权重与运行依赖单独加载。</td>
<td align="left"><a href="models/pretrained_foundation/timesfm/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TimesFM.py" title="_sources/source-07/models/TimesFM.py">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/timesfm/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.10688" title="链接为上游 README 列出的 TimesFM 系列论文；当前接口实际调用 TimesFM 2.5，具体版本以源码和权重标识为准。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/pretrained_foundation/timesfm/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/timesfm2p5/README.md">T&#8288;i&#8288;m&#8288;e&#8288;s&#8288;F&#8288;M&#8288;2&#8288;p&#8288;5</a><br><sub>TimesFM2p5Model</sub></td>
<td align="left">调用 TimesFM 2.5 预训练模型，保留版本特定接口。</td>
<td align="left"><a href="models/pretrained_foundation/timesfm2p5/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/timesfm2p5_model.py" title="_sources/source-12/darts/models/forecasting/timesfm2p5_model.py :: TimesFM2p5Model">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/timesfm2p5/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.10688" title="TimesFM 系列基础论文，不将其标为 2.5 权重版本的专属论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/pretrained_foundation/timesfm2p5/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/timesfm3/README.md">T&#8288;i&#8288;m&#8288;e&#8288;s&#8288;F&#8288;M&#8288;3</a><br><sub>TimesFM3Model</sub></td>
<td align="left">调用 TimesFM 3.0 预训练模型，与早期版本分开索引。</td>
<td align="left"><a href="models/pretrained_foundation/timesfm3/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/timesfm3_model.py" title="_sources/source-12/darts/models/forecasting/timesfm3_model.py :: TimesFM3Model">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/timesfm3/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2310.10688" title="TimesFM 系列基础论文，不将其标为 3.0 权重版本的专属论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/pretrained_foundation/timesfm3/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/timesnet/README.md">T&#8288;i&#8288;m&#8288;e&#8288;s&#8288;N&#8288;e&#8288;t</a></td>
<td align="left">用 FFT 寻找周期，将序列按周期重排为二维，再用 Inception 卷积提取变化。</td>
<td align="left"><a href="models/recurrent_convolution/timesnet/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TimesNet.py" title="_sources/source-07/models/TimesNet.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/TimesNet.py" title="_sources/source-08/models/TimesNet.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/timesnet.py" title="_sources/source-10/neuralforecast/models/timesnet.py :: TimesNet">实&#8288;现&#8288;3</a></td>
<td align="left"><a href="models/recurrent_convolution/timesnet/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://openreview.net/pdf?id=ju_Uqw384Oq" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/timesnet/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/timexer/README.md">T&#8288;i&#8288;m&#8288;e&#8288;X&#8288;e&#8288;r</a><br><sub>TimeXerForecaster / TimeXer_pkg</sub></td>
<td align="left">结合目标序列的 patch 与外生变量表示，用注意力融合两类信息。</td>
<td align="left"><a href="models/transformer_attention/timexer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TimeXer.py" title="_sources/source-07/models/TimeXer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/TimeXer.py" title="_sources/source-08/models/TimeXer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/timexer.py" title="_sources/source-10/neuralforecast/models/timexer.py :: TimeXer">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/timexer/_timexer.py" title="_sources/source-11/pytorch_forecasting/models/timexer/_timexer.py :: TimeXer">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/timexer/_timexer_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/timexer/_timexer_forecaster_v2.py :: TimeXerForecaster">实&#8288;现&#8288;5</a><br><a href="_sources/source-11/pytorch_forecasting/models/timexer/_timexer_pkg.py" title="_sources/source-11/pytorch_forecasting/models/timexer/_timexer_pkg.py :: TimeXer_pkg">实&#8288;现&#8288;6</a></td>
<td align="left"><a href="models/transformer_attention/timexer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2402.19072" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/timexer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/tirex/README.md">T&#8288;i&#8288;R&#8288;e&#8288;x</a><br><sub>TiRexModel</sub></td>
<td align="left">调用 tirex-ts 的预训练模型，为零样本预测提供接口。</td>
<td align="left"><a href="models/pretrained_foundation/tirex/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TiRex.py" title="_sources/source-07/models/TiRex.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-12/darts/models/forecasting/tirex_model.py" title="_sources/source-12/darts/models/forecasting/tirex_model.py :: TiRexModel">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/pretrained_foundation/tirex/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2505.23719" title="模型论文">论&#8288;文</a><br><a href="models/pretrained_foundation/tirex/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/pretrained_foundation/tirex2/README.md">T&#8288;i&#8288;R&#8288;e&#8288;x&#8288;2</a><br><sub>TiRex2Model</sub></td>
<td align="left">调用 TiRex-2，支持多变量及过去、未来协变量预测。</td>
<td align="left"><a href="models/pretrained_foundation/tirex2/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/tirex2_model.py" title="_sources/source-12/darts/models/forecasting/tirex2_model.py :: TiRex2Model">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/pretrained_foundation/tirex2/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2607.01204" title="模型论文">论&#8288;文</a><br><a href="models/pretrained_foundation/tirex2/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/transformer/README.md">T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a><br><sub>TransformerModel / VanillaTransformer</sub></td>
<td align="left">使用标准编码器和解码器注意力结构，作为其他改造模型的对照。</td>
<td align="left"><a href="models/transformer_attention/transformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/Transformer.py" title="_sources/source-07/models/Transformer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/Transformer.py" title="_sources/source-08/models/Transformer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/vanillatransformer.py" title="_sources/source-10/neuralforecast/models/vanillatransformer.py :: VanillaTransformer">实&#8288;现&#8288;3</a><br><a href="_sources/source-12/darts/models/forecasting/transformer_model.py" title="_sources/source-12/darts/models/forecasting/transformer_model.py :: TransformerModel">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/transformer_attention/transformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/transformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/transformergruplus/README.md">T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r&#8288;G&#8288;R&#8288;U&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">将 Transformer 编码与 GRU 循环结构结合的时序网络。</td>
<td align="left"><a href="models/transformer_attention/transformergruplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TransformerRNNPlus.py" title="_sources/source-09/tsai/models/TransformerRNNPlus.py :: TransformerGRUPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/transformergruplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/transformergruplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/transformerlstmplus/README.md">T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r&#8288;L&#8288;S&#8288;T&#8288;M&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">将 Transformer 编码与 LSTM 循环结构结合的时序网络。</td>
<td align="left"><a href="models/transformer_attention/transformerlstmplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TransformerRNNPlus.py" title="_sources/source-09/tsai/models/TransformerRNNPlus.py :: TransformerLSTMPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/transformerlstmplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/transformerlstmplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/transformermodel/README.md">T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">的通用序列 Transformer 接口，与其他库实现分别保留。</td>
<td align="left"><a href="models/transformer_attention/transformermodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TransformerModel.py" title="_sources/source-09/tsai/models/TransformerModel.py :: TransformerModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/transformermodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/transformermodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/transformerrnnplus/README.md">T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r&#8288;R&#8288;N&#8288;N&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">将 Transformer 编码与 RNN 循环结构结合的时序网络。</td>
<td align="left"><a href="models/transformer_attention/transformerrnnplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TransformerRNNPlus.py" title="_sources/source-09/tsai/models/TransformerRNNPlus.py :: TransformerRNNPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/transformerrnnplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/transformerrnnplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tsitplus/README.md">T&#8288;S&#8288;i&#8288;T&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">将 ViT 式 token 和 Transformer 结构适配到时间序列。</td>
<td align="left"><a href="models/transformer_attention/tsitplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TSiTPlus.py" title="_sources/source-09/tsai/models/TSiTPlus.py :: TSiTPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tsitplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2010.11929" title="由所链接的方法适配而来，不宣称此时序变体有独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/transformer_attention/tsitplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/tsmixer/README.md">T&#8288;S&#8288;M&#8288;i&#8288;x&#8288;e&#8288;r</a><br><sub>TSMixerForecaster / TSMixerModel</sub></td>
<td align="left">交替沿时间轴和变量轴使用 MLP 混合信息，再映射到预测窗口。</td>
<td align="left"><a href="models/linear_mlp/tsmixer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/TSMixer.py" title="_sources/source-07/models/TSMixer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/TSMixer.py" title="_sources/source-08/models/TSMixer.py">实&#8288;现&#8288;2</a><br><a href="_sources/source-10/neuralforecast/models/tsmixer.py" title="_sources/source-10/neuralforecast/models/tsmixer.py :: TSMixer">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/tsmixer/_tsmixer_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/tsmixer/_tsmixer_forecaster_v2.py :: TSMixerForecaster">实&#8288;现&#8288;4</a><br><a href="_sources/source-11/pytorch_forecasting/models/tsmixer/_tsmixer_v2.py" title="_sources/source-11/pytorch_forecasting/models/tsmixer/_tsmixer_v2.py :: TSMixer">实&#8288;现&#8288;5</a><br><a href="_sources/source-12/darts/models/forecasting/tsmixer_model.py" title="_sources/source-12/darts/models/forecasting/tsmixer_model.py :: TSMixerModel">实&#8288;现&#8288;6</a></td>
<td align="left"><a href="models/linear_mlp/tsmixer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2303.06053.pdf" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/tsmixer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/tsmixerx/README.md">T&#8288;S&#8288;M&#8288;i&#8288;x&#8288;e&#8288;r&#8288;x</a></td>
<td align="left">在时间与变量混合 MLP 中接入外生变量和静态特征。</td>
<td align="left"><a href="models/linear_mlp/tsmixerx/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/tsmixerx.py" title="_sources/source-10/neuralforecast/models/tsmixerx.py :: TSMixerx">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/tsmixerx/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2303.06053" title="引用当前实现列出的基础方法或相关工作，不宣称变体另有专属论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/linear_mlp/tsmixerx/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tsperceiver/README.md">T&#8288;S&#8288;P&#8288;e&#8288;r&#8288;c&#8288;e&#8288;i&#8288;v&#8288;e&#8288;r</a></td>
<td align="left">以交叉注意力将长输入压缩到潜在表示，再在潜在空间建模。</td>
<td align="left"><a href="models/transformer_attention/tsperceiver/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TSPerceiver.py" title="_sources/source-09/tsai/models/TSPerceiver.py :: TSPerceiver">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tsperceiver/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2107.14795" title="由所链接的方法适配而来，不宣称此时序变体有独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/transformer_attention/tsperceiver/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/tssequencerplus/README.md">T&#8288;S&#8288;S&#8288;e&#8288;q&#8288;u&#8288;e&#8288;n&#8288;c&#8288;e&#8288;r&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">以双向 LSTM 混合序列位置，并结合前馈块。</td>
<td align="left"><a href="models/recurrent_convolution/tssequencerplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TSSequencerPlus.py" title="_sources/source-09/tsai/models/TSSequencerPlus.py :: TSSequencerPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/tssequencerplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2205.01972" title="由所链接的方法适配而来，不宣称此时序变体有独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/tssequencerplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tst/README.md">T&#8288;S&#8288;T</a></td>
<td align="left">使用时序嵌入和编码器注意力构建序列分类或回归。</td>
<td align="left"><a href="models/transformer_attention/tst/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TST.py" title="_sources/source-09/tsai/models/TST.py :: TST">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tst/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3447548.3467401" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/tst/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tstabfusiontransformer/README.md">T&#8288;S&#8288;T&#8288;a&#8288;b&#8288;F&#8288;u&#8288;s&#8288;i&#8288;o&#8288;n&#8288;T&#8288;r&#8288;a&#8288;n&#8288;s&#8288;f&#8288;o&#8288;r&#8288;m&#8288;e&#8288;r</a></td>
<td align="left">通过 Transformer 融合时间序列与表格特征。</td>
<td align="left"><a href="models/transformer_attention/tstabfusiontransformer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TabFusionTransformer.py" title="_sources/source-09/tsai/models/TabFusionTransformer.py :: TSTabFusionTransformer">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tstabfusiontransformer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/transformer_attention/tstabfusiontransformer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/tstplus/README.md">T&#8288;S&#8288;T&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">使用时序嵌入和编码器注意力构建序列分类或回归。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/transformer_attention/tstplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/TSTPlus.py" title="_sources/source-09/tsai/models/TSTPlus.py :: TSTPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/transformer_attention/tstplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://dl.acm.org/doi/abs/10.1145/3447548.3467401" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/transformer_attention/tstplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/transformer_attention/units/README.md">U&#8288;n&#8288;i&#8288;T&#8288;S</a><br><sub>UniTSForecaster</sub></td>
<td align="left">以统一时序表示和结构适配多种序列任务。</td>
<td align="left"><a href="models/transformer_attention/units/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/units/_units_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/units/_units_forecaster_v2.py :: UniTSForecaster">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/units/_units_v2.py" title="_sources/source-11/pytorch_forecasting/models/units/_units_v2.py :: UniTS">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/transformer_attention/units/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2403.00131" title="模型论文">论&#8288;文</a><br><a href="models/transformer_attention/units/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/statistical/varima/README.md">V&#8288;A&#8288;R&#8288;I&#8288;M&#8288;A</a></td>
<td align="left">把多个序列联合建模为向量自回归、差分和移动平均过程。</td>
<td align="left"><a href="models/statistical/varima/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/varima.py" title="_sources/source-12/darts/models/forecasting/varima.py :: VARIMA">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/statistical/varima/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/statistical/varima/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/decomposition_frequency/wpmixer/README.md">W&#8288;P&#8288;M&#8288;i&#8288;x&#8288;e&#8288;r</a></td>
<td align="left">先用离散小波拆分序列，再对不同分量做 patch 混合与预测重建。</td>
<td align="left"><a href="models/decomposition_frequency/wpmixer/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-07/models/WPMixer.py" title="_sources/source-07/models/WPMixer.py">实&#8288;现&#8288;1</a><br><a href="_sources/source-08/models/WPMixer.py" title="_sources/source-08/models/WPMixer.py">实&#8288;现&#8288;2</a></td>
<td align="left"><a href="models/decomposition_frequency/wpmixer/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2412.17176" title="模型论文">论&#8288;文</a><br><a href="models/decomposition_frequency/wpmixer/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xceptiontime/README.md">X&#8288;c&#8288;e&#8288;p&#8288;t&#8288;i&#8288;o&#8288;n&#8288;T&#8288;i&#8288;m&#8288;e</a></td>
<td align="left">将深度可分离卷积与多尺度时序模块结合。</td>
<td align="left"><a href="models/recurrent_convolution/xceptiontime/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/XceptionTime.py" title="_sources/source-09/tsai/models/XceptionTime.py :: XceptionTime">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xceptiontime/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1911.03803" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/xceptiontime/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xceptiontimeplus/README.md">X&#8288;c&#8288;e&#8288;p&#8288;t&#8288;i&#8288;o&#8288;n&#8288;T&#8288;i&#8288;m&#8288;e&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">将深度可分离卷积与多尺度时序模块结合。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/recurrent_convolution/xceptiontimeplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/XceptionTimePlus.py" title="_sources/source-09/tsai/models/XceptionTimePlus.py :: XceptionTimePlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xceptiontimeplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/1911.03803" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/xceptiontimeplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xcm/README.md">X&#8288;C&#8288;M</a></td>
<td align="left">同时提取时间与变量卷积特征，支持解释序列分类结果。</td>
<td align="left"><a href="models/recurrent_convolution/xcm/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/XCM.py" title="_sources/source-09/tsai/models/XCM.py :: XCM">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xcm/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://hal.inria.fr/hal-03469487/document" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/xcm/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xcmplus/README.md">X&#8288;C&#8288;M&#8288;P&#8288;l&#8288;u&#8288;s</a></td>
<td align="left">同时提取时间与变量卷积特征，支持解释序列分类结果。 此项为 的 Plus 可配置变体。</td>
<td align="left"><a href="models/recurrent_convolution/xcmplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/XCMPlus.py" title="_sources/source-09/tsai/models/XCMPlus.py :: XCMPlus">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xcmplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://hal.inria.fr/hal-03469487/document" title="引用基础方法论文；此项是库内 Plus 变体，未核实独立论文。">相&#8288;关&#8288;论&#8288;文</a><br><a href="models/recurrent_convolution/xcmplus/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xcoordtime/README.md">X&#8288;C&#8288;o&#8288;o&#8288;r&#8288;d&#8288;T&#8288;i&#8288;m&#8288;e</a></td>
<td align="left">结合坐标信息与可分离卷积的 InceptionTimePlus 变体。</td>
<td align="left"><a href="models/recurrent_convolution/xcoordtime/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/InceptionTimePlus.py" title="_sources/source-09/tsai/models/InceptionTimePlus.py :: XCoordTime">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xcoordtime/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/xcoordtime/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/xgbclassifiermodel/README.md">X&#8288;G&#8288;B&#8288;C&#8288;l&#8288;a&#8288;s&#8288;s&#8288;i&#8288;f&#8288;i&#8288;e&#8288;r&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">以 XGBoost 分类器处理离散目标预测。</td>
<td align="left"><a href="models/machine_learning/xgbclassifiermodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/xgboost.py" title="_sources/source-12/darts/models/forecasting/xgboost.py :: XGBClassifierModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/xgbclassifiermodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/xgbclassifiermodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/machine_learning/xgbmodel/README.md">X&#8288;G&#8288;B&#8288;M&#8288;o&#8288;d&#8288;e&#8288;l</a></td>
<td align="left">以 XGBoost 提升树对滞后特征和协变量回归。</td>
<td align="left"><a href="models/machine_learning/xgbmodel/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-12/darts/models/forecasting/xgboost.py" title="_sources/source-12/darts/models/forecasting/xgboost.py :: XGBModel">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/machine_learning/xgbmodel/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/machine_learning/xgbmodel/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/linear_mlp/xlinear/README.md">X&#8288;L&#8288;i&#8288;n&#8288;e&#8288;a&#8288;r</a></td>
<td align="left">以轻量 MLP 结合历史和外生输入，直接输出未来窗口。</td>
<td align="left"><a href="models/linear_mlp/xlinear/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/xlinear.py" title="_sources/source-10/neuralforecast/models/xlinear.py :: XLinear">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/linear_mlp/xlinear/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2601.09237" title="模型论文">论&#8288;文</a><br><a href="models/linear_mlp/xlinear/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xlstm/README.md">x&#8288;L&#8288;S&#8288;T&#8288;M</a></td>
<td align="left">使用扩展 LSTM 记忆结构处理历史，再接入预测头。</td>
<td align="left"><a href="models/recurrent_convolution/xlstm/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-10/neuralforecast/models/xlstm.py" title="_sources/source-10/neuralforecast/models/xlstm.py :: xLSTM">实&#8288;现&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xlstm/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/abs/2405.04517" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/xlstm/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xlstmtime/README.md">x&#8288;L&#8288;S&#8288;T&#8288;M&#8288;T&#8288;i&#8288;m&#8288;e</a><br><sub>xLSTMTimeForecaster / xLSTMTime_pkg / xLSTMTime_v2</sub></td>
<td align="left">面向时间序列预测的 xLSTM 适配结构，与通用 xLSTM 分开保留。</td>
<td align="left"><a href="models/recurrent_convolution/xlstmtime/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm.py" title="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm.py :: xLSTMTime">实&#8288;现&#8288;1</a><br><a href="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_forecaster_v2.py" title="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_forecaster_v2.py :: xLSTMTimeForecaster">实&#8288;现&#8288;2</a><br><a href="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_pkg.py" title="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_pkg.py :: xLSTMTime_pkg">实&#8288;现&#8288;3</a><br><a href="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_v2.py" title="_sources/source-11/pytorch_forecasting/models/xlstm/_xlstm_v2.py :: xLSTMTime_v2">实&#8288;现&#8288;4</a></td>
<td align="left"><a href="models/recurrent_convolution/xlstmtime/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="https://arxiv.org/pdf/2407.10240" title="模型论文">论&#8288;文</a><br><a href="models/recurrent_convolution/xlstmtime/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xresnet1d/README.md">X&#8288;R&#8288;e&#8288;s&#8288;N&#8288;e&#8288;t&#8288;1&#8288;d</a><br><sub>xresnet1d101 / xresnet1d152 / xresnet1d18 / xresnet1d18_deep / xresnet1d18_deeper / xresnet1d34 / xresnet1d34_deep / xresnet1d34_deeper / xresnet1d50 / xresnet1d50_deep / xresnet1d50_deeper</sub></td>
<td align="left">将 xresnet 架构适配为一维卷积，保留多种深度工厂。</td>
<td align="left"><a href="models/recurrent_convolution/xresnet1d/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d101">实&#8288;现&#8288;1</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d152">实&#8288;现&#8288;2</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d18">实&#8288;现&#8288;3</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d18_deep">实&#8288;现&#8288;4</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d18_deeper">实&#8288;现&#8288;5</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d34">实&#8288;现&#8288;6</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d34_deep">实&#8288;现&#8288;7</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d34_deeper">实&#8288;现&#8288;8</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d50">实&#8288;现&#8288;9</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d50_deep">实&#8288;现&#8288;1&#8288;0</a><br><a href="_sources/source-09/tsai/models/XResNet1d.py" title="_sources/source-09/tsai/models/XResNet1d.py :: xresnet1d50_deeper">实&#8288;现&#8288;1&#8288;1</a></td>
<td align="left"><a href="models/recurrent_convolution/xresnet1d/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/xresnet1d/README.md">项&#8288;目</a></td>
</tr>
<tr>
<td align="left"><a href="models/recurrent_convolution/xresnet1dplus/README.md">X&#8288;R&#8288;e&#8288;s&#8288;N&#8288;e&#8288;t&#8288;1&#8288;d&#8288;P&#8288;l&#8288;u&#8288;s</a><br><sub>xresnet1d101plus / xresnet1d152plus / xresnet1d18_deeperplus / xresnet1d18_deepplus / xresnet1d18plus / xresnet1d34_deeperplus / xresnet1d34_deepplus / xresnet1d34plus / xresnet1d50_deeperplus / xresnet1d50_deepplus / xresnet1d50plus</sub></td>
<td align="left">一维 xresnet 的增强版本，保留可配置头和深度工厂。</td>
<td align="left"><a href="models/recurrent_convolution/xresnet1dplus/README.md#%E5%AE%9E%E7%8E%B0">实&#8288;现&#8288;索&#8288;引</a></td>
<td align="left"><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: XResNet1dPlus">实&#8288;现&#8288;1</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d101plus">实&#8288;现&#8288;2</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d152plus">实&#8288;现&#8288;3</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d18_deeperplus">实&#8288;现&#8288;4</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d18_deepplus">实&#8288;现&#8288;5</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d18plus">实&#8288;现&#8288;6</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d34_deeperplus">实&#8288;现&#8288;7</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d34_deepplus">实&#8288;现&#8288;8</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d34plus">实&#8288;现&#8288;9</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d50_deeperplus">实&#8288;现&#8288;1&#8288;0</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d50_deepplus">实&#8288;现&#8288;1&#8288;1</a><br><a href="_sources/source-09/tsai/models/XResNet1dPlus.py" title="_sources/source-09/tsai/models/XResNet1dPlus.py :: xresnet1d50plus">实&#8288;现&#8288;1&#8288;2</a></td>
<td align="left"><a href="models/recurrent_convolution/xresnet1dplus/README.md#%E8%BF%90%E8%A1%8C%E6%96%B9%E5%BC%8F">运&#8288;行&#8288;方&#8288;式</a></td>
<td align="left"><a href="models/recurrent_convolution/xresnet1dplus/README.md">项&#8288;目</a></td>
</tr>
</tbody>
</table>

运行入口指向该实现的命令脚本或使用文档；支持任务与参数以对应源码为准。系列论文和加载变体的区别见论文链接的悬停说明。

<!-- MODEL_DETAILS_END -->

## 完整模型库与教程

| 模型库 | 主要内容 | 本仓库完整源码 | 项目出处 |
| --- | --- | --- | --- |
| Time-Series-Library | 多任务时序模型、预测、插补、异常检测、分类与预训练模型接口 | [完整源码](_sources/source-07/) | [原项目](https://github.com/thuml/Time-Series-Library) |
| TimeSeriesLibrary · ZJ | 模型、组件、任务脚本和教程 | [完整源码](_sources/source-08/) | [原项目](https://github.com/ZJ-LuoGuangQing/TimeSeriesLibrary) |
| tsai | 时间序列分类、回归、预测与网络变体 | [完整源码](_sources/source-09/) | [原项目](https://github.com/timeseriesAI/tsai) |
| NeuralForecast | 神经预测、训练与滚动评估接口 | [完整源码](_sources/source-10/) | [原项目](https://github.com/Nixtla/neuralforecast) |
| PyTorch Forecasting | 数据集、神经预测器、概率损失与训练接口 | [完整源码](_sources/source-11/) | [原项目](https://github.com/sktime/pytorch-forecasting) |
| Darts | 统计预测、机器学习、深度预测与集成 | [完整源码](_sources/source-12/) | [原项目](https://github.com/unit8co/darts) |

上述库的原始文件、教程、测试、示例与已有资源均完整保留。按项目查看教程和接口时使用[模型库指南](docs/library-guide.md)；按模型查找时使用上方统一目录。

## 目录结构

```text
zpb-time-series-research/
├── models/                    # 全部模型，按技术分类统一组织
│   ├── linear_mlp/
│   ├── recurrent_convolution/
│   ├── transformer_attention/
│   ├── decomposition_frequency/
│   ├── state_space_dynamics/
│   ├── graph/
│   ├── llm_reprogramming/
│   ├── pretrained_foundation/
│   ├── anomaly_specialized/
│   ├── statistical/
│   ├── machine_learning/
│   ├── ensemble_calibration/
│   └── model_adapter/
│       └── <模型名>/          # 每个模型都有 README.md 与 model.json
├── _sources/                  # 完整源码归档，统一编号保存
│   ├── source-01/
│   ├── ...
│   └── source-12/
├── docs/                      # 源码导航、运行指南、来源记录
├── research/
│   ├── models/                # 自己的模型和改动说明
│   └── notes/                 # 论文笔记、想法和代码阅读记录
├── experiments/
│   ├── templates/             # 可复制的实验记录模板
│   └── results/               # 小型指标汇总；大文件留在本地
├── data/                      # 数据来源与划分索引
├── zpbts/                     # 统一注册、数据协议、适配训练与指标
├── examples/                  # 可运行实验配置、数据和实测结果
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

阅读介绍与查找模型无需安装训练依赖。共用实验按[统一实验指南](docs/integration.md)运行；更多模型的完整入口见各模型页的“运行方式”。

已建立 **12 个来源、2503 个原始文件**的归档与逐文件校验，具体版本见[来源记录](docs/upstream-sources.md)。DLinear、TSMixer 已完成 CPU 训练与预测管道验证，记录见[合成示例](examples/forecasting/README.md)。外部研究数据和权重按模型要求准备；论文指标复现需在对应数据和设置上开展。

后续改进可先在 `research/` 下建立独立版本，通过实验记录保存基线提交、配置和结果。各上游论文的引用条目保留在对应原 README 中；许可证说明见 [LICENSES.md](LICENSES.md)。
