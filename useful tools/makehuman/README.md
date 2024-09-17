![Batch Script](https://img.shields.io/badge/script-batch-DDFF00)
![VINDWOS](https://img.shields.io/badge/vVINDWOS-blue)

```
███╗   ███╗ █████╗ ██╗  ██╗███████╗██╗  ██╗██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗    ██╗   ██╗██╗███╗   ██╗██████╗  ██████╗ ███████╗    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║    ██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗██╔════╝    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██╔████╔██║███████║█████╔╝ █████╗  ███████║██║   ██║██╔████╔██║███████║██╔██╗ ██║    ██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║███████╗    ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║╚════██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║     ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝███████║    ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                              
```

# MakeHuman Automated Installer for Windows

## Introduction

This script automates the installation of [MakeHuman](http://www.makehumancommunity.org/) and its essential plugins on Windows systems. It performs the following tasks:

- Clones the MakeHuman repository from GitHub.
- Installs required Python dependencies.
- Downloads and installs necessary plugins (MHAPI and Asset Downloader).
- Compiles models, proxies, and targets.
- Creates a batch file to launch MakeHuman.
- Downloads a custom icon for MakeHuman.
- Creates a desktop shortcut to launch MakeHuman, complete with the custom icon.

## Prerequisites

Before running this script, ensure you have the following installed and configured:

- **Git**: Required to clone repositories from GitHub. [Download Git](https://git-scm.com/downloads)
- **Python 3.x**: MakeHuman requires Python 3.x. Ensure Python is installed and added to your system's PATH. [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer, required to install dependencies. pip is usually included with Python 3.x installations.
- **curl**: Used to download the icon file. [Download curl](https://curl.se/windows/)
- **Administrator Privileges**: The script may need elevated permissions to write to certain directories and create desktop shortcuts.
- **Internet Connection**: Required to download repositories and files from GitHub.

## Instructions

### 1. Download the Script

Save or download the following script as `install_makehuman.bat` on your Windows machine:

```batch
@echo off
title Full Installation of MakeHuman and Its Plugins

REM Clear the screen
cls

echo ===============================================
echo       Full Installation of MakeHuman
echo ===============================================
echo.

REM Ask the user to specify the installation path
set /p installPath="Enter the installation path for MakeHuman (e.g., C:\\Program Files\\MakeHuman): "

REM Check if the specified directory exists, otherwise create it
if not exist "%installPath%" (
    echo The path does not exist, it will be created.
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

REM Install Python dependencies from the requirements.txt file
echo Installing Python dependencies...
cd /d "%installPath%\makehuman"
pip install -r requirements.txt

REM Verify if the dependencies installation was successful
if %errorlevel% neq 0 (
    echo Error installing Python dependencies. Make sure pip is installed and compatible.
    pause
    exit /b
)

REM Create the plugins directory if necessary
if not exist "%installPath%\makehuman\makehuman\plugins" (
    mkdir "%installPath%\makehuman\makehuman\plugins"
)

REM Download necessary plugins from GitHub
echo Downloading MHAPI and Asset Downloader plugins...
git clone https://github.com/makehumancommunity/community-plugins-mhapi.git "%installPath%\makehuman\makehuman\plugins\1_MHAPI"
git clone https://github.com/makehumancommunity/community-plugins-assetdownload.git "%installPath%\makehuman\makehuman\plugins\8_assetdownload"

REM Compile models, proxies, and targets
python makehuman/makehuman/compile_models.py
python makehuman/makehuman/compile_proxies.py
python makehuman/makehuman/compile_targets.py

REM Create a batch file to launch MakeHuman
echo Creating a batch file to launch MakeHuman...
(
    echo @echo off
    echo cd /d "%installPath%\makehuman\makehuman"
    echo python makehuman.py
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

cscript //nologo createShortcut.vbs
del createShortcut.vbs
goto end

:end
echo Shortcut created successfully on your desktop.
echo Installation complete.
pause
exit
```

### 2. Run the Script

1. **Open Command Prompt as Administrator**:

   - Click on the Start menu.
   - Type `cmd`.
   - Right-click on **Command Prompt** and select **Run as administrator**.

2. **Navigate to the Script's Directory**:

   Use the `cd` command to navigate to the directory where you saved `install_makehuman.bat`. For example:

   ```batch
   cd C:\Users\YourUsername\Downloads
   ```

3. **Execute the Script**:

   ```batch
   install_makehuman.bat
   ```

### 3. Follow the Prompts

- **Installation Path**: When prompted, enter the installation path where you want MakeHuman to be installed. For example:

  ```
  Enter the installation path for MakeHuman (e.g., C:\Program Files\MakeHuman):
  ```

- **Wait for the Installation to Complete**: The script will perform all the necessary steps automatically. This may take several minutes depending on your internet connection and system performance.

### 4. Launch MakeHuman

- After the installation is complete, a shortcut named **MakeHuman.lnk** will be created on your desktop.
- Double-click the shortcut to launch MakeHuman.

## Notes

- **Permissions**: Ensure you run the script as an administrator to allow it to create directories and shortcuts.
- **Python Version**: MakeHuman requires Python 3.x. Ensure that Python is correctly installed and accessible from the command line.
- **Environment Variables**: Python and Git should be added to your system's PATH environment variable.
- **Internet Connectivity**: A stable internet connection is required to download repositories and files.
- **Antivirus Software**: Some antivirus programs may interfere with the script's operations. If you encounter issues, consider temporarily disabling your antivirus software during the installation.

## Troubleshooting

### Error: 'git' is not recognized as an internal or external command

- **Cause**: Git is not installed or not added to your system's PATH.
- **Solution**: Install Git from [https://git-scm.com/downloads](https://git-scm.com/downloads) and ensure you select the option to add Git to your PATH during installation.

### Error: 'python' is not recognized as an internal or external command

- **Cause**: Python is not installed or not added to your system's PATH.
- **Solution**: Install Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/) and check the option to add Python to PATH during installation.

### Error installing Python dependencies

- **Cause**: pip may not be installed or properly configured.
- **Solution**: Ensure pip is installed by running `python -m ensurepip --default-pip` in the Command Prompt.

### Icon download failed

- **Cause**: curl is not installed or there is a network issue.
- **Solution**: Install curl from [https://curl.se/windows/](https://curl.se/windows/) and ensure it's added to your PATH. Also, verify your internet connection.

### Shortcut not created

- **Cause**: The script may not have sufficient privileges to create a desktop shortcut.
- **Solution**: Ensure you are running the script as an administrator.

## Uninstallation

To uninstall MakeHuman and its components:

1. **Delete the Installation Directory**:

   Remove the directory you specified during installation. For example:

   ```batch
   rmdir /s /q "C:\Program Files\MakeHuman"
   ```

2. **Remove the Desktop Shortcut**:

   Delete the **MakeHuman.lnk** shortcut from your desktop.

3. **Optional**: Uninstall Python, Git, and curl if they are no longer needed.

## License

This script is provided "as is" without any warranty. Use it at your own risk.

## Acknowledgements

- **MakeHuman Community**: [https://github.com/makehumancommunity/makehuman](https://github.com/makehumancommunity/makehuman)
- **MHAPI Plugin**: [https://github.com/makehumancommunity/community-plugins-mhapi](https://github.com/makehumancommunity/community-plugins-mhapi)
- **Asset Downloader Plugin**: [https://github.com/makehumancommunity/community-plugins-assetdownload](https://github.com/makehumancommunity/community-plugins-assetdownload)

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Disclaimer

- This script is intended for educational and personal use.
- Ensure you comply with all licenses and terms of use for MakeHuman and its plugins.

---

**Enjoy creating 3D human models with MakeHuman!**
