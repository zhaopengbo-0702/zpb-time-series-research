# 自动同步上游源码

[返回首页](../README.md) · [来源记录](upstream-sources.md) · [版本锁定清单](../sources.lock.json) · [同步状态](upstream-status.md) · [同步历史](upstream-sync-history.md)

本研究仓库通过 GitHub Actions 定期检查七个来源的默认分支，并将新版本同步到对应目录。六个独立模型仍放在 `baselines/`，完整 Time-Series-Library 仍放在 `libraries/`；自己的模型、笔记和实验记录继续放在 `research/`、`experiments/`。

## 同步哪些内容

| 上游 | 本仓库目录 |
| --- | --- |
| [PlanckChang/EMAformer](https://github.com/PlanckChang/EMAformer) | `baselines/EMAformer/` |
| [ant-research/Pyraformer](https://github.com/ant-research/Pyraformer) | `baselines/Pyraformer/` |
| [zhouhaoyi/Informer2020](https://github.com/zhouhaoyi/Informer2020) | `baselines/Informer2020/` |
| [thuml/Autoformer](https://github.com/thuml/Autoformer) | `baselines/Autoformer/` |
| [azkanaon/etsformer](https://github.com/azkanaon/etsformer) | `baselines/ETSformer/` |
| [KimMeen/Time-LLM](https://github.com/KimMeen/Time-LLM) | `baselines/Time-LLM/` |
| [thuml/Time-Series-Library](https://github.com/thuml/Time-Series-Library) | `libraries/Time-Series-Library/` |

每次同步读取上游当时的默认分支，锁定其提交，再获取该提交的完整受 Git 跟踪文件。下载文件按 Git blob SHA-1 逐个核验，成功后更新源目录、`sources.lock.json`、[统一分类模型目录](model-catalog.md)、[同步状态](upstream-status.md)和[同步历史](upstream-sync-history.md)，并由工作流提交到本仓库主分支。上游没有变化时无需产生新的源码提交。

统一模型目录将独立项目和库内模型逐个并列分类，同名模型共用条目并保留两类实现入口。分类信息维护在 `tools/model_categories.json`；上游新增的模型会自动收录，尚未分类时进入“待分类”分组。

同步更新的是源码及随源码跟踪的文件。外部数据集、预训练语言模型和时序大模型权重仍按各项目要求另行准备；Git 子模块引用也不会自动变成已下载的依赖内容。具体范围见[来源记录](upstream-sources.md)。

## 定时运行与手动运行

工作流为 [sync-upstreams.yml](../.github/workflows/sync-upstreams.yml)，计划每天 **UTC 02:20，即北京时间约 10:20** 运行。GitHub 的定时任务可能排队，实际开始时间以 Actions 记录为准。

在 [GitHub Actions 的上游同步页面](https://github.com/zhaopengbo-0702/zpb-time-series-research/actions/workflows/sync-upstreams.yml)可以查看每次运行。拥有仓库写入权限且已登录的用户，可点击 **Run workflow**，选择 `main`，再点击运行按钮手动触发，无需等到下一个定时时间。

进入某次运行后，可展开步骤日志查看哪些来源有更新、版本校验是否通过，以及提交结果。页面的运行摘要展示来源与文件变更数量；JSON 报告以 **upstream-sync-report** artifact 保存 30 天，可在该次运行页面底部的 **Artifacts** 区域下载。报告给出该次检查的版本和处理状态，不表示模型训练或论文指标复现已经完成。

修改同步脚本、行为测试或工作流文件也会触发一次检查。自动生成的源码提交不匹配这组路径，因此不会反复触发自身。

公开仓库连续约 60 天没有活动时，GitHub 可能停用定时工作流，可到 Actions 页面重新启用。工作流还依赖 GitHub 的运行服务、上游网络和主分支写入权限；分支保护、权限不足或网络失败会显示为失败运行，应根据该次日志处理后重试。

## 保护自己的改动

同步前会按旧版锁定清单核对源目录。如果原文件被本地修改、删除，或目录内出现额外文件，同步会报冲突并停止，不会直接用上游覆盖这些内容。上游许可证文件有变化时也会暂停更新，保留当前版本以便先核查变化。`research/` 和 `experiments/` 不在上游覆盖范围内。

建议将个人改进放在 `research/` 的独立版本或自己的开发分支，并在实验记录中写明基线提交。若已经直接修改了原版目录，先保存改动和新增文件，再明确迁移到自己的工作区；不要仅为消除冲突而删除尚未保存的研究代码。训练生成的数据、检查点或缓存也可能成为额外文件，应在实验工作副本中运行和整理。

## 在本地检查或同步

从本研究仓库根目录执行。以下命令使用单行形式，适用于 Windows PowerShell；脚本使用 **Python 3.11 或更新版本**的标准库，无需安装模型训练环境。

只检查当前上游版本：

```powershell
python tools/sync_upstreams.py --check
```

检查模式不改写工作区；如需机器可读输出，使用 `python tools/sync_upstreams.py --check --output-json -` 输出到标准输出。此模式不接受报告文件路径。

同步到本地工作区并暂存变更，同时输出 JSON 报告：

```powershell
python tools/sync_upstreams.py --stage --output-json upstream-sync-report.json
```

检查变更后再自行提交：

```powershell
git diff --cached --stat
python tools/verify_sources.py --strict
git commit -m "Sync upstream source snapshots"
```

GitHub Actions 在远端运行，不会自动改动电脑上的克隆目录。只想取回 GitHub 上已经同步的版本时，先确认本地工作已保存，再执行：

```powershell
git status
git pull --ff-only
python tools/verify_sources.py --strict
```

`git pull --ff-only` 只接受快进更新；本地与远端历史分叉时会停止，保留当前提交，需先处理分支关系。无需为了获取远端更新重复执行本地上游同步脚本。

## 保持旧实验可追溯

`sources.lock.json` 记录每个上游的准确提交、文件哈希和目录。每次自动同步还保留本研究仓库的 Git 提交历史，因此“现在的最新版”和“某次实验用的版本”可以分别查到。

开始实验时，在记录中保存本研究仓库提交 SHA，以及所用来源的锁定提交。查看锁定清单的历史可执行：

```powershell
git log --oneline -- sources.lock.json
```

重做旧实验时，从对应的本研究仓库提交创建独立复现分支或 worktree，再按该版本锁定清单校验源码。这样可以取回当时的源码组合；该实验所用的数据、权重、依赖环境和结果文件仍应按[实验管理](../experiments/README.md)另行保存。
