@echo off
cls
rmdir /S /Q .\commands\__pycache__
rmdir /S /Q .\modules\__pycache__
set "HISTORY_FILE=%CD%\.mcpfucktool_history"
if exist "%HISTORY_FILE%" (
    erase /Q "%HISTORY_FILE%" >nul 2>&1
    echo Previous history file removed.
)