# Local C++ Practice Environment

## Scope

This repository tracks solution source files, problem metadata, the starter template, helper scripts, and the project workspace. Generated executables, downloaded samples, CPH metadata, the virtual environment, and `.vscode/` folder settings remain local and are excluded from Git.

## Installed tools

Verified on 2026-10-20:

| Component | Local installation |
| --- | --- |
| Compiler | MSYS2 UCRT64 GCC 16.1.0, `C:\msys64\ucrt64\bin\g++.exe` |
| Debugger | GDB 17.2, `C:\msys64\ucrt64\bin\gdb.exe` |
| VS Code C++ extension | `ms-vscode.cpptools` 1.34.4 |
| Sample panel | Competitive Programming Helper (CPH) 2026.10.1792170155 |
| Local sample runner | online-judge-tools 11.5.1 in `.venv` |

## Compilation failure and fix

The observed CPH error was `Exit code: 1 Errors while compiling:` with no following diagnostics. The source itself compiled through `cp.cmd`, proving that the failure was in CPH's process environment rather than C++ syntax. A shell-free Node reproduction matching CPH also exited with code 1 and empty diagnostics.

The local workspace now uses these CPH settings:

| Setting | Value |
| --- | --- |
| `cph.language.cpp.Command` | `D:/CS/Code/atcoder-practice/tools/cph-gpp-wrapper.exe` |
| `cph.language.cpp.Args` | `-std=c++20 -O2 -Wall -Wextra -Wshadow -static` |
| `cph.general.timeOut` | `3000` |

The installed CPH version launches C++ compilation directly, without a shell. The compiler command must contain only an executable path. A command such as `set "PATH=..." && g++.exe` causes `spawn ... ENOENT`, because CPH interprets the entire string as an executable name.

On this computer, Anaconda's MinGW directory precedes MSYS2 UCRT64 in the combined process `PATH`. Directly spawning the absolute `g++.exe` still lets GCC find incompatible child tools first, producing exit code 1 with empty diagnostics. The tracked `tools/cph-gpp-wrapper.cpp` builds a small native launcher that prepends UCRT64 before forwarding CPH's arguments to GCC. Rebuild it with `cp.cmd build tools/cph-gpp-wrapper.cpp` after a fresh clone or after deleting generated executables.

Build the wrapper once with `cp.cmd build tools/cph-gpp-wrapper.cpp`. Then open the project with `open-workspace.cmd`, open the source file, save it, and press `Ctrl+Alt+B`. IntelliSense continues to use the plain compiler path `C:/msys64/ucrt64/bin/g++.exe`.

## Daily workflow on this computer

1. Run `open-workspace.cmd` to open the tracked `atcoder-practice.code-workspace` file. Do not open the repository folder directly for browser imports.
2. Open and save the C++ file you are practicing with.
3. Press `Ctrl+Alt+B` to compile and run the CPH cases.
4. Use `F5` for the configured debugger. `Ctrl+Shift+B` uses the separate local sample runner and requires the per-problem `test/` layout created by `cp.cmd`; browser imports use CPH cases instead.
5. Record reasoning and results in `notes/progress.md`; commit the source, problem metadata, and learning record after review.

The `cp.cmd`, `open-workspace.cmd`, `atcoder-practice.code-workspace`, `tools/`, `templates/`, and `contests/` files are tracked. The `.venv/`, `.vscode/`, binaries, downloaded tests, and CPH caches remain local.

## Browser imports and folder layout

In the installed CPH version, Competitive Companion imports create source files directly inside the first VS Code workspace folder. Opening the repository root as that folder therefore creates files such as `abc087b.cpp` in the repository root. The `cph.general.saveLocation` setting controls test metadata and compiled outputs, not imported source files.

The local `atcoder-practice.code-workspace` lists `contests/` first, followed by `docs/` and `notes/`. It includes the existing compiler settings and adapts the local build tasks to the named Practice folder. Open this workspace for the browser workflow. Companion imports will use a flat layout such as `contests/abc087b.cpp`; CPH does not automatically reproduce the helper's `contests/abc087/b/main.cpp` layout.

Browser imports appear as flat files such as `contests/dpb.cpp` because CPH writes sources into the first workspace folder and does not offer a source-subdirectory setting. Before committing, move them to the canonical `contests/<contest>/<task>/main.cpp` layout and add `problem.json`. Opening the repository folder instead of the workspace incorrectly places imports in the repository root. The local helper creates the canonical layout directly.

### C++ starter template

Both the local workspace and the repository folder settings set `cph.general.defaultLanguage` to `cpp` and `cph.general.defaultLanguageTemplateFileLocation` to `D:/CS/Code/atcoder-practice/templates/main.cpp`. CPH reads this literal filesystem path, so update it if the practice folder moves. The existing template contains the include, namespace, `main`, fast I/O settings, and an English reminder to describe the approach and complexity.

CPH copies the template only when creating a new source file. Reimporting a problem whose file already exists does not insert the template. Existing nonempty source files are preserved. Continue using the browser's green plus button for new tasks, or use `cp.cmd new <AtCoder task URL>` to create the canonical layout directly.

## Setup on another Windows computer

Install VS Code, MSYS2 UCRT64 GCC and GDB, and the C/C++ and CPH extensions. Add `C:\msys64\ucrt64\bin` to the Windows user `Path`, adjusting it if MSYS2 is installed elsewhere. Fully exit and reopen VS Code after changing the path; signing out and back in also refreshes inherited environments.

From the repository root, create the Python environment and install the pinned sample-runner dependencies:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
cp.cmd doctor
cp.cmd build tools/cph-gpp-wrapper.cpp
open-workspace.cmd
```

If the repository is cloned to another path or MSYS2 is installed elsewhere, update the literal template, wrapper, compiler, and debugger paths in the workspace and wrapper source, then rebuild the wrapper. Enter sample input and expected output into CPH when browser import is unavailable.

## Validation and limits

- The original direct compiler invocation reproduced exit code 1 with empty diagnostics.
- After the repository reorganization, the local sample runner compiled all seven tracked C++ solutions with warnings enabled and passed all 22 saved official sample cases.
- Direct Node process spawning reproduced CPH's exit code 1 with empty diagnostics when Anaconda's MinGW preceded UCRT64. Spawning the native wrapper with shell mode disabled compiled successfully because the wrapper prepends the correct toolchain directory.
- Official AtCoder acceptance is not claimed. See the practice log for submission status.
- The local runner's optional package update checks could not resolve PyPI in the restricted execution environment. These warnings did not prevent compilation or local sample tests.

The CPH panel itself must be checked in the user's running VS Code session; command-level verification does not establish the panel's displayed state.
