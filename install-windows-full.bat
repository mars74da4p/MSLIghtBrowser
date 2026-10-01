@echo off
REM MSLightBrowser Installation for Windows
REM This script installs Python, dependencies, and sets up desktop shortcuts

echo ========================================
echo MSLightBrowser Installation
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Attempting to install...
    powershell -Command "(New-Object System.Net.ServicePointManager).SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://www.python.org/ftp/python/3.10.13/python-3.10.13-amd64.exe'))"
) else (
    python --version
    echo Python found!
)

echo.
echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo.
echo ========================================
echo Creating desktop shortcuts...
echo ========================================
echo.

REM Call the setup script
call setup-desktop-windows.bat

echo.
echo Installation complete!
echo You can now run the browser:
echo   - Double-click the desktop shortcut
echo   - Or run: run.bat
echo.
pause
