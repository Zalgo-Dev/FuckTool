@echo off & setlocal enabledelayedexpansion
chcp 65001 >nul
title FuckTool Installer v1.2 By ZalgoDev
cls

:: ========================================
::          INITIALIZATION
:: ========================================
set "INSTALL_DIR=%USERPROFILE%\FuckTool"
set "REPO_URL=https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/main"
set "PYTHON_URL=https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe"

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

choice /C IUGX /N /M "Select option [I,U,G,X]: "

if %errorlevel% EQU 4 exit /b
if %errorlevel% EQU 3 goto update
if %errorlevel% EQU 2 goto uninstall

:: ========================================
::          INSTALLATION PROCESS
:: ========================================
:install
cls
echo ========================================
echo =          INSTALLATION IN PROGRESS    =
echo ========================================
echo.

:: Clean previous install
if exist "%INSTALL_DIR%" (
    echo [!] Removing previous installation...
    rmdir /s /q "%INSTALL_DIR%" >nul 2>&1
)

:: Create directories
echo [+] Creating directory structure...
mkdir "%INSTALL_DIR%" >nul
mkdir "%INSTALL_DIR%\fucktool" >nul
mkdir "%INSTALL_DIR%\fucktool\commands" >nul
mkdir "%INSTALL_DIR%\fucktool\core" >nul
mkdir "%INSTALL_DIR%\fucktool\FakeProxy" >nul
mkdir "%INSTALL_DIR%\fucktool\FakeProxy\plugins" >nul
mkdir "%INSTALL_DIR%\fucktool\FakeProxy\plugins\bStats" >nul
mkdir "%INSTALL_DIR%\fucktool\resources" >nul

:: Python check
:check_python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found
    call :install_python
    goto check_python
)

:: Check Python version
python -c "import sys; exit(0 if sys.version_info >= (3,11) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python 3.12+ required
    call :install_python
)

python -m ensurepip --default-pip >nul 2>&1

:: Download main and resources
echo [+] Downloading files...

:: Main files
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/main.py', '%INSTALL_DIR%\fucktool\main.py')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/__init__.py', '%INSTALL_DIR%\fucktool\__init__.py')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/config.py', '%INSTALL_DIR%\fucktool\config.py')"

:: Commands
for %%f in (__init__.py clear.py details.py dns.py fakeproxy.py help.py info.py stress.py) do (
    echo [.] commands/%%f
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/commands/%%f', '%INSTALL_DIR%\fucktool\commands\%%f')"
)

:: Core
for %%f in (__init__.py colors.py command_manager.py debug.py header.py input_manager.py) do (
    echo [.] core/%%f
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/core/%%f', '%INSTALL_DIR%\fucktool\core\%%f')"
)

:: FakeProxy files
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/FakeProxy/forwarding.secret', '%INSTALL_DIR%\fucktool\FakeProxy\forwarding.secret')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/FakeProxy/velocity.jar', '%INSTALL_DIR%\fucktool\FakeProxy\velocity.jar')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/FakeProxy/velocity.toml', '%INSTALL_DIR%\fucktool\FakeProxy\velocity.toml')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/FakeProxy/plugins/FakeProxyAdmin-1.2.1.jar', '%INSTALL_DIR%\fucktool\FakeProxy\plugins\FakeProxyAdmin-1.2.1.jar')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/FakeProxy/plugins/bStats/config.txt', '%INSTALL_DIR%\fucktool\FakeProxy\plugins\bStats\config.txt')"

:: Resources
for %%f in (fucktool.ico) do (
    echo [.] resources/%%f
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/fucktool/resources/%%f', '%INSTALL_DIR%\fucktool\resources\%%f')"
)

:: Install requirements
echo [+] Installing dependencies...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%REPO_URL%/requirements.txt', '%INSTALL_DIR%\requirements.txt')"
python -m pip install --user -r "%INSTALL_DIR%\requirements.txt"

:: Desktop Shortcut
echo [+] Creating desktop shortcut...
powershell -Command ^
  "$python = (Get-Command python).Source; " ^
  "$ws = New-Object -ComObject WScript.Shell; " ^
  "$s = $ws.CreateShortcut('%USERPROFILE%\Desktop\FuckTool.lnk'); " ^
  "$s.TargetPath = $python; " ^
  "$s.Arguments = '\"%INSTALL_DIR%\fucktool\main.py\"'; " ^
  "$s.WorkingDirectory = '%INSTALL_DIR%\fucktool'; " ^
  "$s.IconLocation = '%INSTALL_DIR%\fucktool\resources\fucktool.ico'; " ^
  "$s.Description = 'FuckTool by ZalgoDev'; " ^
  "$s.Save()"

cls
echo ========================================
echo =       INSTALLATION COMPLETE!         =
echo ========================================
echo.
echo FuckTool has been installed to:
echo %INSTALL_DIR%
echo.
pause
exit /b

:: ========================================
::         PYTHON INSTALL
:: ========================================
:install_python
echo [+] Installing Python...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%PYTHON_URL%', '%TEMP%\python_installer.exe')"
start /wait "" "%TEMP%\python_installer.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
del "%TEMP%\python_installer.exe" >nul 2>&1
exit /b

:: ========================================
::         UNINSTALL
:: ========================================
:uninstall
cls
echo ========================================
echo =          UNINSTALLATION              =
echo ========================================
echo.
if not exist "%INSTALL_DIR%" (
    echo [!] FuckTool is not installed.
    pause
    goto main_menu
)

echo [*] Removing files...
rmdir /s /q "%INSTALL_DIR%" >nul 2>&1
if exist "%USERPROFILE%\Desktop\FuckTool.lnk" (
    del "%USERPROFILE%\Desktop\FuckTool.lnk"
)
echo [+] FuckTool has been removed.
pause
goto main_menu

:: ========================================
::         UPDATE
:: ========================================
:update
cls
echo ========================================
echo =             UPDATE                   =
echo ========================================
echo.
if not exist "%INSTALL_DIR%" (
    echo [!] FuckTool not installed
    pause
    goto main_menu
)
echo [*] Updating...
call :uninstall
call :install
goto :eof