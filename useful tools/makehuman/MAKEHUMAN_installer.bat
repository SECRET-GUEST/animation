@echo off
title Full Installation of MakeHuman and Its Plugins

REM Clear the screen
cls

echo ===============================================
echo       Full Installation of MakeHuman
echo ===============================================
echo.

REM Ask the user to specify the installation path
set /p installPath="Enter the installation path for MakeHuman (e.g., C:\\...\MakeHuman): "

REM Check if the specified directory exists, otherwise create it
if not exist "%installPath%" (
    echo The path does not exist; it will be created.
    mkdir "%installPath%"
)

REM Move to the installation directory
cd /d "%installPath%"

REM Clone the MakeHuman repository
echo Downloading MakeHuman from GitHub...
git clone https://github.com/makehumancommunity/makehuman.git

REM Verify if the clone was successful
if not exist "%installPath%\makehuman" (
    echo Error downloading MakeHuman.
    pause
    exit /b
)

REM Create a Python virtual environment
echo Creating Python virtual environment...
cd /d "%installPath%\makehuman"
python -m venv venv

REM Activate the virtual environment
call "%installPath%\makehuman\venv\Scripts\activate.bat"

REM Upgrade pip to the latest version
python -m pip install --upgrade pip

REM Install Python dependencies from the requirements.txt file
echo Installing Python dependencies...
pip install -r requirements.txt

REM Verify if the dependencies installation was successful
if %errorlevel% neq 0 (
    echo Error installing Python dependencies. Ensure pip is installed and compatible.
    pause
    exit /b
)

REM Create the plugins directory if necessary
if not exist "%installPath%\makehuman\makehuman\plugins" (
    mkdir "%installPath%\makehuman\makehuman\plugins"
)

REM Download necessary plugins from GitHub
echo Downloading MHAPI and Asset Downloader plugins...

REM Remove existing plugin directories if they exist
if exist "%installPath%\makehuman\makehuman\plugins\1_MHAPI" (
    echo Removing existing 1_MHAPI plugin directory...
    rmdir /s /q "%installPath%\makehuman\makehuman\plugins\1_MHAPI"
)

if exist "%installPath%\makehuman\makehuman\plugins\8_assetdownload" (
    echo Removing existing 8_assetdownload plugin directory...
    rmdir /s /q "%installPath%\makehuman\makehuman\plugins\8_assetdownload"
)

REM Clone the plugins from GitHub
git clone https://github.com/makehumancommunity/community-plugins-mhapi.git "%installPath%\makehuman\makehuman\plugins\1_MHAPI"
git clone https://github.com/makehumancommunity/community-plugins-assetdownload.git "%installPath%\makehuman\makehuman\plugins\8_assetdownload"

REM Compile models, proxies, and targets
cd /d "%installPath%\makehuman\makehuman"

echo Compiling models...
python compile_models.py
if %errorlevel% neq 0 (
    echo Error compiling models.
    pause
    exit /b
)

echo Compiling proxies...
python compile_proxies.py
if %errorlevel% neq 0 (
    echo Error compiling proxies.
    pause
    exit /b
)

echo Compiling targets...
python compile_targets.py
if %errorlevel% neq 0 (
    echo Error compiling targets.
    pause
    exit /b
)

REM Deactivate the virtual environment
call "%installPath%\makehuman\venv\Scripts\deactivate.bat"

cd /d "%installPath%"

REM Create a batch file to launch MakeHuman
echo Creating a batch file to launch MakeHuman...
(
    echo @echo off
    echo REM Activate the virtual environment
    echo call "%installPath%\makehuman\venv\Scripts\activate.bat"
    echo cd /d "%installPath%\makehuman\makehuman"
    echo python makehuman.py
    echo REM Deactivate the virtual environment
    echo call "%installPath%\makehuman\venv\Scripts\deactivate.bat"
    echo exit
) > "%installPath%\makehuman\makehuman.bat"

REM Download the icon from GitHub
echo Downloading icon...
curl -L -o "%installPath%\makehuman\makehuman.ico" "https://github.com/SECRET-GUEST/animation/raw/blender/useful%%20tools/makehuman/makehuman.ico"

REM Verify if the icon was downloaded successfully
if not exist "%installPath%\makehuman\makehuman.ico" (
    echo Icon download failed.
    pause
    exit /b
)

REM Create a VBScript to create the shortcut with the icon
echo Creating shortcut on the desktop...
(
echo Set oWS = WScript.CreateObject^("WScript.Shell"^)
echo sLinkFile = oWS.SpecialFolders^("Desktop"^) ^& "\MakeHuman.lnk"
echo Set oLink = oWS.CreateShortcut^(sLinkFile^)
echo oLink.TargetPath = "%installPath%\makehuman\makehuman.bat"
echo oLink.WindowStyle = 1
echo oLink.IconLocation ="%installPath%\makehuman\makehuman.ico"
echo oLink.Description = "MakeHuman"
echo oLink.WorkingDirectory ="%installPath%\makehuman"
echo oLink.Save
) > createShortcut.vbs

REM Run the VBScript to create the shortcut
cscript //nologo createShortcut.vbs

REM Delete the temporary VBScript file
del createShortcut.vbs

echo Shortcut created successfully on your desktop.
echo Installation complete.
pause
exit
