# Local C++ Practice Environment

## Scope

This repository tracks solution source files, problem metadata, the starter template, and portable helper scripts. Generated executables, downloaded samples, CPH metadata, the virtual environment, and machine-specific VS Code files remain local and are excluded from Git.

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
| `cph.language.cpp.Command` | `C:/msys64/ucrt64/bin/g++.exe` |
| `cph.language.cpp.Args` | `-std=c++20 -O2 -Wall -Wextra -Wshadow -static` |
| `cph.general.timeOut` | `3000` |

The installed CPH version launches C++ compilation directly, without a shell. The compiler command must contain only the executable path. A command such as `set "PATH=..." && g++.exe` causes `spawn ... ENOENT`, because CPH interprets the entire string as an executable name. The earlier shell-mode verification did not match the extension's C++ launch behavior and was insufficient.

CPH inherits the VS Code process environment. After adding UCRT64 to the Windows user `Path`, fully exit all VS Code windows and launch VS Code from a newly opened Windows PowerShell window. A window reload or opening an integrated terminal does not replace the main process's inherited environment.

For a deterministic launch, run the following in that external PowerShell window after exiting VS Code:

```powershell
$env:Path = 'C:\msys64\ucrt64\bin;' + $env:Path
code D:\CS\Code\atcoder-practice
```

Then open the source file, save it, and press `Ctrl+Alt+B`. IntelliSense also uses the plain executable path `C:/msys64/ucrt64/bin/g++.exe`.

## Daily workflow on this computer

1. Open the local `atcoder-practice.code-workspace` file in VS Code for browser imports.
2. Open and save the C++ file you are practicing with.
3. Press `Ctrl+Alt+B` to compile and run the CPH cases.
4. Use `F5` for the configured debugger. `Ctrl+Shift+B` uses the separate local sample runner and requires the per-problem `test/` layout created by `cp.cmd`; browser imports use CPH cases instead.
5. Record reasoning and results in `notes/progress.md`; commit the source, problem metadata, and learning record after review.

The portable `cp.cmd`, `tools/`, `templates/`, and `contests/` files are tracked. The `.venv/`, `.vscode/`, workspace file, binaries, downloaded tests, and CPH caches remain local.

## Browser imports and folder layout

In the installed CPH version, Competitive Companion imports create source files directly inside the first VS Code workspace folder. Opening the repository root as that folder therefore creates files such as `abc087b.cpp` in the repository root. The `cph.general.saveLocation` setting controls test metadata and compiled outputs, not imported source files.

The local `atcoder-practice.code-workspace` lists `contests/` first, followed by `docs/` and `notes/`. It includes the existing compiler settings and adapts the local build tasks to the named Practice folder. Open this workspace for the browser workflow. Companion imports will use a flat layout such as `contests/abc087b.cpp`; CPH does not automatically reproduce the helper's `contests/abc087/b/main.cpp` layout.

Browser imports may first appear as flat files such as `contests/abc087b.cpp`. Before committing, move them to the canonical `contests/<contest>/<task>/main.cpp` layout and add `problem.json`. The local helper already creates this canonical layout. Existing solutions were normalized to it on 2026-10-23.

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
```

Set the C++ compiler path and standard to the values above. Use the external PowerShell launch above if applications still inherit an old path. Enter sample input and expected output into CPH, and keep practice source files outside tracked documentation paths.

## Validation and limits

- The original direct compiler invocation reproduced exit code 1 with empty diagnostics.
- After the repository reorganization, the local sample runner compiled all six tracked C++ solutions with warnings enabled and passed all 18 saved official sample cases.
- The initial test incorrectly enabled shell mode, while CPH's C++ runner uses direct process spawning. That test did not establish compatibility with CPH.
- After restoring the plain compiler executable path, direct Node process spawning with shell mode disabled and UCRT64 prepended to `PATH` compiled successfully and passed all three ABC081B samples. The saved Windows user `Path` was also confirmed to include UCRT64.
- Official AtCoder acceptance is not claimed. See the practice log for submission status.
- The local runner's optional package update checks could not resolve PyPI in the restricted execution environment. These warnings did not prevent compilation or local sample tests.

The CPH panel itself must be checked in the user's running VS Code session; command-level verification does not establish the panel's displayed state.
