# Local C++ Practice Environment

## Scope

This repository publishes documentation only. Solution files, samples, helper scripts, and VS Code settings are local working files and are excluded from Git. Existing local files were preserved during the documentation-only conversion. A fresh clone does not include those tools or solutions.

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

The observed CPH error was `Exit code: 1 Errors while compiling:` with no following diagnostics. Running the configured GCC executable directly reproduced that failure when `C:\msys64\ucrt64\bin` was absent from the process `PATH`. Running the same compiler with that directory prepended succeeded.

An absolute path to `g++.exe` identifies the compiler driver but does not provide the runtime search path needed by its child tools. The saved Windows user `Path` already included UCRT64, while the current process environment did not. This is consistent with applications that were open before the path was updated. VS Code's terminal environment setting affects terminals, not the CPH extension host.

The local workspace now uses these CPH settings:

| Setting | Value |
| --- | --- |
| `cph.language.cpp.Command` | `set "PATH=C:\msys64\ucrt64\bin;%PATH%" && C:/msys64/ucrt64/bin/g++.exe` |
| `cph.language.cpp.Args` | `-std=c++20 -O2 -Wall -Wextra -Wshadow -static` |
| `cph.general.timeOut` | `3000` |

The installed CPH version launches C++ compilation through the Windows command shell. The command therefore supplies the required path for each compilation, including from a stale extension-host environment. It is a Windows-specific configuration. IntelliSense continues to use the plain executable path `C:/msys64/ucrt64/bin/g++.exe`.

## Daily workflow on this computer

1. Open the local practice folder in VS Code.
2. Open and save the C++ file you are practicing with.
3. Press `Ctrl+Alt+B` to compile and run the CPH cases.
4. Use `Ctrl+Shift+B` for the existing local sample-runner task, or `F5` for the configured debugger.
5. Record reasoning and results in `notes/progress.md`; publish documents only.

The existing `cp.cmd`, `tools/`, `templates/`, `.venv/`, `.vscode/`, and `contests/` files remain local. Their availability should not be assumed on another computer.

## Setup on another Windows computer

Install VS Code, MSYS2 UCRT64 GCC and GDB, and the C/C++ and CPH extensions. Add `C:\msys64\ucrt64\bin` to the Windows user `Path`, adjusting it if MSYS2 is installed elsewhere. Fully exit and reopen VS Code after changing the path; signing out and back in also refreshes inherited environments.

Set the C++ compiler path and standard to the values above. For this CPH version, the shell-prefixed compiler command also works when the parent process has an old path. Enter sample input and expected output into CPH, and keep practice source files outside tracked documentation paths.

## Validation and limits

- The original direct compiler invocation reproduced exit code 1 with empty diagnostics.
- The existing local sample runner compiled ABC081B and passed all three saved official samples after supplying the compiler path.
- The updated CPH command was also tested with Node's `spawnSync` using the installed extension's shell mode and compiler arguments: compilation succeeded and all three ABC081B samples passed.
- Official AtCoder acceptance is not claimed. See the practice log for submission status.
- The local runner's optional package update checks could not resolve PyPI in the restricted execution environment. These warnings did not prevent compilation or local sample tests.

The CPH panel itself must be checked in the user's running VS Code session; command-level verification does not establish the panel's displayed state.
