@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo Starting ErrorInsight...
"%~dp0python\python.exe" -m errorinsight
if errorlevel 1 (
    echo.
    echo ErrorInsight failed to start.
    echo Please check the package files.
    echo.
    pause
)