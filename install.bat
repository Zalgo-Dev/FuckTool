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

:: Name     :   FuckTool
:: Author   :   ZalgoDev
:: Date     :   16.02.2025

:: L’auteur n'est en aucun cas tenu responsable de tout dommage ou utilisation abusive du logiciel.

@echo off
chcp 65001 >nul
title FuckTool By ZalgoDev
cls

echo ========================================
echo =          FuckTool Installer          =
echo ========================================
echo.
echo Do you want to install FuckTool ?
echo.
echo [I] Install
echo [U] Uninstall
echo [X] Exit
echo.

choice /T 60 /C IUX /D X /N /M "Choose an option: "

if %errorlevel% EQU 3 (
    cls
    echo Installation cancelled.
    echo Exiting FuckTool Installer.
    exit /b
)

set "INSTALL_DIR=%USERPROFILE%\FuckTool"

if %errorlevel% EQU 2 (
    cls
    echo ========================================
    echo =          FuckTool Uninstaller       =
    echo ========================================
    echo.
    
    if not exist "%INSTALL_DIR%" (
        echo FuckTool is not installed.
        echo Exiting uninstaller.
        pause
        exit /b
    )
    
    echo Removing FuckTool...
    
    :: Supprimer le dossier d'installation
    rmdir /s /q "%INSTALL_DIR%" >nul 2>&1
    
    :: Supprimer le raccourci du bureau
    if exist "%USERPROFILE%\Desktop\FuckTool.lnk" (
        del "%USERPROFILE%\Desktop\FuckTool.lnk" >nul 2>&1
    )
    
    echo Uninstallation complete!
    pause
    exit /b
)

echo Installing FuckTool...

if exist "%INSTALL_DIR%" (
    echo Removing previous installation...
    rmdir /s /q "%INSTALL_DIR%" >nul 2>&1
)

:makeInstallDir
echo Creation of the main folder : %INSTALL_DIR%
mkdir "%INSTALL_DIR%" 2>nul
mkdir %INSTALL_DIR%\commands %INSTALL_DIR%\modules

if not exist %INSTALL_DIR% (
    goto makeInstallDir
)

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing Python...
    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe', '%INSTALL_DIR%\python-installer.exe')"
    
    if exist "%INSTALL_DIR%\python-installer.exe" (
        echo Installing Python...
        start /wait %INSTALL_DIR%\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
        del %INSTALL_DIR%\python-installer.exe
    ) else (
        echo Error: Python download failed.
        pause
        exit /b
    )
) else (
    echo Python is already installed.
)

python -m ensurepip >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip --default-pip
) else (
    echo Pip is already installed.
)

python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pip installation failed.
    pause
    exit /b
)

:: Main
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/main.py', '%INSTALL_DIR%\main.py')"

:: Requirements
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/requirements.txt', '%INSTALL_DIR%\requirements.txt')"

:: Commands
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/commands/__init__.py', '%INSTALL_DIR%\commands\__init__.py')"
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/commands/commands_handler.py', '%INSTALL_DIR%\commands\commands_handler.py')"
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/commands/detailsCommand.py', '%INSTALL_DIR%\commands\detailsCommand.py')"
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/commands/helpCommand.py', '%INSTALL_DIR%\commands\helpCommand.py')"
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/commands/infoCommand.py', '%INSTALL_DIR%\commands\infoCommand.py')"

:: Modules
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/modules/__init__.py', '%INSTALL_DIR%\modules\__init__.py')"
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/modules/colorsModule.py', '%INSTALL_DIR%\modules\colorsModule.py')"
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/modules/headerModule.py', '%INSTALL_DIR%\modules\headerModule.py')"

:: Ico
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/Zalgo-Dev/FuckTool/refs/heads/main/fucktool.ico', '%INSTALL_DIR%\fucktool.ico')"

timeout /T 3 /NOBREAK

if exist "%INSTALL_DIR%\requirements.txt" (
    echo Installing dependencies...
    python -m pip install -r "%INSTALL_DIR%\requirements.txt"
) else (
    echo Warning: No requirements.txt found. Skipping dependency installation.
)

set "SHORTCUT_PATH=%USERPROFILE%\Desktop\FuckTool.lnk"
set "PYTHON_SCRIPT=%INSTALL_DIR%\main.py"
set "ICON_PATH=%INSTALL_DIR%\fucktool.ico"

echo Creating desktop shortcut...
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT_PATH%'); $s.TargetPath = 'python'; $s.Arguments = '\"%PYTHON_SCRIPT%\"'; $s.WorkingDirectory = '%INSTALL_DIR%'; $s.IconLocation = '%ICON_PATH%'; $s.Save()"

echo Shortcut created on your desktop with custom icon!

echo Installation complete! You can now run FuckTool.
pause
exit