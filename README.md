# Bulk MozJPEG Compressor

## Overview

Bulk MozJPEG Compressor is a simple-to-use, Windows-friendly Python tool with a graphical interface that makes it easy to compress multiple JPEG and PNG images at once. Built to feel as familiar as a traditional `.exe` program, this tool allows users to adjust image compression quality, customize filenames, and choose whether to overwrite original files—all without needing to run complex commands.

## Features

- **Easy GUI**: No need to use the command line; everything can be done through a user-friendly interface.
- **Adjustable Compression Quality**: Set the quality level to balance file size and image clarity.
- **Filename Customization**: Easily add prefixes and/or suffixes to distinguish compressed images.
- **Replace Original Files**: Optionally overwrite original images with compressed versions.
- **Preserves Folder Structure**: Maintains the input folder structure in the output folder.
- **Windows-Compatible**: Designed to work seamlessly on Windows.

## Requirements

- **Python 3.x** (Download [here](https://www.python.org/downloads/))
- **Pillow** library for image processing
- **MozJPEG** (`cjpeg.exe`) installed on your system

## Installation on Windows

1. **Download or Clone the Repository**

   - To download, click on the **Code** button above and select **Download ZIP**.
   - Extract the contents to a convenient folder.

2. **Run the Installer**

   - Double-click `install.bat`.
   - This script will:
     - Check if Python is installed.
     - Install required packages automatically.

3. **Download MozJPEG**

   - Visit the [MozJPEG Releases](https://github.com/mozilla/mozjpeg/releases) page and download the latest release for Windows.
   - Unzip the downloaded file and locate `cjpeg.exe` (usually in a folder like `D:\mozjpeg\mozjpeg-v4.0.3-win-x64\shared\Release`).

## Running the Program on Windows

Once you’ve completed the installation, using this program is as simple as double-clicking an `.exe` file.

1. **Open the Program**: Double-click the `bulk_mozjpeg_compressor.py` file.
2. **Using the GUI**: All tasks can be completed through the graphical interface.

### Using the GUI

- **Input Folder**: Select the folder with images you want to compress.
- **Output Folder**: Choose a folder where the compressed images will be saved.
- **Compression Quality**: Adjust the slider between `0` and `100` for desired quality.
- **Path to `cjpeg.exe`**: Use **Browse** to locate `cjpeg.exe`.
- **Filename Prefix/Suffix**: Customize the names of your output files.
- **Replace Original Files**: Check this option if you want the compressed files to overwrite the originals.
- **Start Compression**: Click **Start Compression** and let the program handle the rest.

> **Note**: This program is designed to feel like a standard Windows app and does not require any command-line work beyond setup.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [MozJPEG](https://github.com/mozilla/mozjpeg) for providing powerful JPEG compression tools.
- [Pillow](https://python-pillow.org/) for image processing in Python.
