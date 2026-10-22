@echo off
setlocal
if not exist "%~dp0.venv\Scripts\python.exe" (
    echo Missing .venv. Follow the setup steps in README.md.
    exit /b 1
)
"%~dp0.venv\Scripts\python.exe" "%~dp0tools\practice.py" %*
exit /b %errorlevel%
