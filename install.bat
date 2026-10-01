@echo off
echo ========================================
echo MSLightBrowser Installation
echo ========================================

echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Installing Python...
    powershell -Command "(New-Object System.Net.ServicePointManager).SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://www.python.org/ftp/python/3.10.13/python-3.10.13-amd64.exe'))"
) else (
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
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Installation complete!
echo Run 'run.bat' to start the browser.
pause
