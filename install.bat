@echo off
echo Setting up Bulk MozJPEG Compressor...

:: Check for Python installation
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python 3.x and ensure it is added to PATH.
    pause
    exit /b
)

:: Install required Python packages
echo Installing required Python packages...
pip install -r requirements.txt

echo.
echo Installation complete!
echo To use the Bulk MozJPEG Compressor, double-click bulk_mozjpeg_compressor.py
echo Make sure you have the MozJPEG "cjpeg.exe" file downloaded and ready.
echo Visit https://github.com/mozilla/mozjpeg/releases for the latest version.
pause
