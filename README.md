# AtCoder Blue Project

A reproducible C++ practice repository for [Lorendw](https://atcoder.jp/users/Lorendw). The current goal is to reach and retain AtCoder blue: algorithm rating **1600-1999**. Progress is measured by independent contest performance, not by accepted submissions alone.

## Start here

- [Blue-rating training plan](docs/training-plan.md): phase gates, weekly routine, topic order, and the next two weeks.
- [Practice log](notes/progress.md): verified submissions, assistance level, review queue, and current metrics.
- [Local environment](docs/local-environment.md): Windows, VS Code, GCC, CPH, and the sample runner.

## Repository layout

```text
contests/<contest>/<task>/
  main.cpp       # submitted or practice solution
  problem.json   # problem identity and URL
docs/            # plan and environment documentation
notes/           # progress and review records
templates/       # C++ starter template
tools/           # local build, download, and test helper
cp.cmd           # Windows entry point for tools/practice.py
```

Generated executables, downloaded samples, CPH metadata, virtual environments, and machine-specific editor settings are intentionally ignored. Source code, portable tooling, and learning records are tracked.

## Quick workflow

On a fresh Windows clone, create the local Python environment and verify the toolchain:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
cp.cmd doctor
```

Create a problem folder and download its public samples:

```powershell
cp.cmd new https://atcoder.jp/contests/abc153/tasks/abc153_e
```

Build and test an existing solution:

```powershell
cp.cmd test contests/abc153/e/main.cpp
```

After each session:

1. Record the result and assistance level in `notes/progress.md`.
2. If help was used, schedule an independent reimplementation in 2-3 days.
3. Record the approach, correctness argument, complexity, and the official submission URL when available.
4. Review the staged files before committing. Never commit binaries, credentials, or generated caches.

Passing samples is not the same as an AtCoder AC. Classify work honestly as **independent**, **hint**, or **editorial/guided**.
