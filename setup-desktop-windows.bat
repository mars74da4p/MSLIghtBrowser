@echo off
REM MSLightBrowser Auto-Setup for Windows
REM This script automatically creates a desktop shortcut and adds to Start menu

echo ========================================
echo MSLightBrowser - Windows Auto Setup
echo ========================================
echo.

REM Get the current directory (project directory)
set "PROJECT_DIR=%cd%"

echo Project directory: %PROJECT_DIR%
echo.

REM Check if .venv exists
if not exist ".venv" (
    echo Error: Virtual environment not found!
    echo Please run install.bat first to set up dependencies
    pause
    exit /b 1
)

echo Creating desktop shortcut...

REM Create VBScript to add desktop shortcut (since batch can't do this directly)
REM This creates a shortcut on the desktop
for /f %%%%A in ('cd') do set "CURRENT_DIR=%%%%A"

powershell -Command ^^
    "[System.IO.File]::WriteAllText('%TEMP%\create_shortcut.vbs', ^^ ^^
    'Set oWS = WScript.CreateObject("WScript.Shell")' + vbCrLf + ^^ ^^
    'sLinkFile = oWS.SpecialFolders("Desktop") + "\MSLightBrowser.lnk"' + vbCrLf + ^^ ^^
    'Set oLink = oWS.CreateShortCut(sLinkFile)' + vbCrLf + ^^ ^^
    'oLink.TargetPath = "%PROJECT_DIR%\run.bat"' + vbCrLf + ^^ ^^
    'oLink.WorkingDirectory = "%PROJECT_DIR%"' + vbCrLf + ^^ ^^
    'oLink.Description = "MSLightBrowser - Lightweight Web Browser"' + vbCrLf + ^^ ^^
    'oLink.WindowStyle = 1' + vbCrLf + ^^ ^^
    'oLink.Save' + vbCrLf); ^^ ^^
    cscript.exe "%TEMP%\create_shortcut.vbs"

echo.
echo ✓ Desktop shortcut created!
echo.

REM Try to add to Start Menu using registry (Windows 10/11)
echo Creating Start Menu shortcut...

REM Create folder in Start Menu
set "START_MENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs\MSLightBrowser"
mkdir "%START_MENU%" 2>nul

REM Create shortcut in Start Menu using PowerShell
powershell -Command ^^
    "[System.IO.File]::WriteAllText('%TEMP%\create_start_menu.vbs', ^^ ^^
    'Set oWS = WScript.CreateObject("WScript.Shell")' + vbCrLf + ^^ ^^
    'sLinkFile = "%START_MENU%\MSLightBrowser.lnk"' + vbCrLf + ^^ ^^
    'Set oLink = oWS.CreateShortCut(sLinkFile)' + vbCrLf + ^^ ^^
    'oLink.TargetPath = "%PROJECT_DIR%\run.bat"' + vbCrLf + ^^ ^^
    'oLink.WorkingDirectory = "%PROJECT_DIR%"' + vbCrLf + ^^ ^^
    'oLink.Description = "MSLightBrowser - Lightweight Web Browser"' + vbCrLf + ^^ ^^
    'oLink.WindowStyle = 1' + vbCrLf + ^^ ^^
    'oLink.Save' + vbCrLf); ^^ ^^
    cscript.exe "%TEMP%\create_start_menu.vbs"

echo.
echo ========================================
echo ✓ Setup Complete!
echo ========================================
echo.
echo How to launch MSLightBrowser:
echo.
echo   OPTION 1 - Desktop Icon:
echo   Double-click the "MSLightBrowser" icon on your desktop
echo.
echo   OPTION 2 - Start Menu:
echo   Press Win key, search "MSLightBrowser", and click
echo.
echo   OPTION 3 - Run from here:
echo   Double-click run.bat in the project folder
echo.
echo   OPTION 4 - Command Line:
echo   .venv\Scripts\python.exe main.py
echo.
pause
