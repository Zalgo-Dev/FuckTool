::  ███████╗    ██╗   ██╗     ██████╗    ██╗  ██╗    ████████╗     ██████╗      ██████╗     ██╗     
::  ██╔════╝    ██║   ██║    ██╔════╝    ██║ ██╔╝    ╚══██╔══╝    ██╔═══██╗    ██╔═══██╗    ██║     
::  █████╗      ██║   ██║    ██║         █████╔╝        ██║       ██║   ██║    ██║   ██║    ██║     
::  ██╔══╝      ██║   ██║    ██║         ██╔═██╗        ██║       ██║   ██║    ██║   ██║    ██║     
::  ██║         ╚██████╔╝    ╚██████╗    ██║  ██╗       ██║       ╚██████╔╝    ╚██████╔╝    ███████╗
::  ╚═╝          ╚═════╝      ╚═════╝    ╚═╝  ╚═╝       ╚═╝        ╚═════╝      ╚═════╝     ╚══════╝

::  ██╗    ███╗   ██╗    ███████╗    ████████╗     █████╗     ██╗         ██╗         ███████╗    ██████╗ 
::  ██║    ████╗  ██║    ██╔════╝    ╚══██╔══╝    ██╔══██╗    ██║         ██║         ██╔════╝    ██╔══██╗
::  ██║    ██╔██╗ ██║    ███████╗       ██║       ███████║    ██║         ██║         █████╗      ██████╔╝
::  ██║    ██║╚██╗██║    ╚════██║       ██║       ██╔══██║    ██║         ██║         ██╔══╝      ██╔══██╗
::  ██║    ██║ ╚████║    ███████║       ██║       ██║  ██║    ███████╗    ███████╗    ███████╗    ██║  ██║
::  ╚═╝    ╚═╝  ╚═══╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝    ╚══════╝    ╚══════╝    ╚══════╝    ╚═╝  ╚═╝

:: Name     :   FuckTool Ultimate Installer
:: Author   :   ZalgoDev
:: Version  :   2.0
:: Date     :   1.27
:: Note     :   L'auteur décline toute responsabilité concernant l'usage de ce logiciel

@echo off & setlocal enabledelayedexpansion
chcp 65001 >nul
title FuckTool Ultimate Installer v2.0 By ZalgoDev
color 0a
cls

:: ========================================
::          INITIALIZATION
:: ========================================
set "INSTALL_DIR=%USERPROFILE%\FuckTool"
set "REPO_URL=https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/main/"
set "PYTHON_URL=https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"

:: ========================================
::          MAIN MENU
:: ========================================
:main_menu
cls
echo ========================================
echo =       FUCKTOOL ULTIMATE INSTALLER    =
echo ========================================
echo.
echo [I] Install FuckTool
echo [U] Uninstall FuckTool
echo [G] Update FuckTool
echo [X] Exit
echo.

choice /C IUGX /N /M "Select option [I,U,X]: "

if %errorlevel% EQU 4 (
    cls
    echo Operation cancelled.
    timeout /t 2 >nul
    exit /b
)

if %errorlevel% EQU 3 (
    goto update
)

if %errorlevel% EQU 2 (
    goto uninstall
)

:: ========================================
::          INSTALLATION PROCESS
:: ========================================
:install
cls
echo ========================================
echo =          INSTALLATION IN PROGRESS    =
echo ========================================
echo.

:: Check and clean previous installation
if exist "%INSTALL_DIR%" (
    echo [!] Removing previous installation...
    rmdir /s /q "%INSTALL_DIR%" >nul 2>&1
)

:: Create directory structure
echo [+] Creating directory structure...
mkdir "%INSTALL_DIR%" >nul 2>&1
mkdir "%INSTALL_DIR%\commands" >nul 2>&1
mkdir "%INSTALL_DIR%\modules" >nul 2>&1

:: Get username
:get_username
set /p "USERNAME=Enter your hacker name: "
if "%USERNAME%"=="" (
    echo [!] Invalid input, try again
    goto get_username
)

:: Create config file
(
    echo [Settings]
    echo username=%USERNAME%
    echo install_date=%date% %time%
    echo.
    echo [System]
    echo version=2.0
    echo python_required=3.11+
) > "%INSTALL_DIR%\config.ini"

:: Check Python installation
:check_python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not detected
    call :install_python
    goto check_python
)

:: Verify Python version
python -c "import sys; exit(0 if sys.version_info >= (3,11) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python 3.11+ required
    call :install_python
)

:: Install pip if missing
python -m ensurepip --default-pip >nul 2>&1

:: Download all necessary files
echo [+] Downloading FuckTool components...

set "FILES=main.py requirements.txt"
set "COMMANDS=__init__.py commands_handler.py detailsCommand.py helpCommand.py infoCommand.py stressCommand.py dnsCommand.py"
set "MODULES=__init__.py colorsModule.py headerModule.py historyManager.py readlineSetup.py"
set "RESOURCES=fucktool.ico"

for %%f in (%FILES%) do (
    echo [.] Downloading %%f...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%%%f', '%INSTALL_DIR%\%%f')"
)

for %%c in (%COMMANDS%) do (
    echo [.] Downloading commands\%%c...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%commands/%%c', '%INSTALL_DIR%\commands\%%c')"
)

for %%m in (%MODULES%) do (
    echo [.] Downloading modules\%%m...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%modules/%%m', '%INSTALL_DIR%\modules\%%m')"
)

for %%r in (%RESOURCES%) do (
    echo [.] Downloading resources\%%r...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%fucktoolfiles/%%r', '%INSTALL_DIR%\%%r')"
)

:: Install dependencies
if exist "%INSTALL_DIR%\requirements.txt" (
    echo [+] Installing dependencies...
    python -m pip install --user --upgrade pip >nul
    python -m pip install --user -r "%INSTALL_DIR%\requirements.txt"
) else (
    echo [!] requirements.txt missing - skipping dependencies
)

:: Create desktop shortcut
echo [+] Creating desktop shortcut...
powershell -Command "$ws=New-Object -ComObject WScript.Shell; $s=$ws.CreateShortcut('%USERPROFILE%\Desktop\FuckTool.lnk'); $s.TargetPath='python'; $s.Arguments='\"%INSTALL_DIR%\main.py\"'; $s.WorkingDirectory='%INSTALL_DIR%'; $s.IconLocation='%INSTALL_DIR%\fucktool.ico'; $s.Description='FuckTool by ZalgoDev'; $s.Save()"

:: Final message
cls
echo ========================================
echo =       INSTALLATION COMPLETE!         =
echo ========================================
echo.
echo FuckTool has been successfully installed
echo.
echo Launch options:
echo 1. Double-click desktop shortcut
echo 2. Run: python "%INSTALL_DIR%\main.py"
echo 3. Navigate to %INSTALL_DIR% and run
echo.
pause
exit /b

:: ========================================
::          SUBROUTINES
:: ========================================
:install_python
echo [+] Installing Python 3.11...
echo [.] Downloading installer...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%PYTHON_URL%', '%TEMP%\python_installer.exe')"

echo [.] Running installer...
start /wait "" "%TEMP%\python_installer.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
del "%TEMP%\python_installer.exe" >nul 2>&1

echo [.] Verifying installation...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python installation failed
    pause
    exit /b 1
)
exit /b

:uninstall
cls
echo ========================================
echo =          UNINSTALLATION              =
echo ========================================
echo.

if not exist "%INSTALL_DIR%" (
    echo [!] FuckTool not found
    pause
    goto main_menu
)

echo [*] Removing FuckTool...
rmdir /s /q "%INSTALL_DIR%" >nul 2>&1

echo [*] Removing desktop shortcut...
if exist "%USERPROFILE%\Desktop\FuckTool.lnk" (
    del "%USERPROFILE%\Desktop\FuckTool.lnk" >nul 2>&1
)

echo [+] FuckTool has been completely removed
pause
goto main_menu

:update
cls
echo ========================================
echo =          UPDATE                      =
echo ========================================
echo.

if not exist "%INSTALL_DIR%" (
    echo [!] FuckTool not installed
    pause
    goto main_menu
)

echo [*] Updating FuckTool...
call :uninstall
call :install
goto :eof