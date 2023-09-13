@echo off
cd /d %~dp0

title Checking Python installation...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! (Go to https://www.python.org/downloads and install the python 3.11.0 or 3.10.0^)
    echo Very important click Add python exe to PATH.
    pause
)
python builder.py
