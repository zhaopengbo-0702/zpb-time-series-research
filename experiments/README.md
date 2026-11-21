# 实验管理

统一入口：`python -m zpbts run CONFIG --output DIR`。一次运行保存可再次执行的 `config.json`、包含数据协议和来源版本的 `metrics.json`、逐预测点的 `predictions.csv`。本地实验放在 `experiments/local/`，已加入忽略规则。

`python -m zpbts compare DIR1 DIR2` 按 MAE 排序，展示 MSE、RMSE、sMAPE 与 MASE。只有数据哈希、列、时间划分、输入窗、预测窗、步长和评价协议完全相同的结果才能比较。

| 内容 | 位置 |
| --- | --- |
| 统一配置、指标和数学定义 | [整合实验指南](../docs/integration.md) |
| 最小可运行示例与验证结果 | [forecasting](../examples/forecasting/README.md) |
| 研究假设、消融和完整命令 | [实验记录模板](templates/experiment.md) |
| 自己的模型与改进 | [研究工作区](../research/README.md) |

合成示例检查训练、数据流和指标管道。正式研究应固定预算、运行多个种子，并在自己的数据上比较。
