# Bulk MozJPEG Compressor

## Overview

Bulk MozJPEG Compressor is a Python-based tool with a graphical user interface (GUI) for batch compressing JPEG and PNG images using the [MozJPEG](https://github.com/mozilla/mozjpeg) encoder. It allows users to set compression quality, append prefixes or suffixes to filenames, and replace original files if desired.

## Features

- **Bulk Compression**: Quickly compress multiple JPEG and PNG files at once.
- **Adjustable Compression Quality**: Set a custom quality level (0-100) to balance file size and image quality.
- **Filename Customization**: Optionally add prefixes and/or suffixes to output filenames.
- **Replace Original Files**: Enable the option to overwrite original images with compressed versions.
- **Preserves Directory Structure**: Maintains the input folder structure within the output folder.
- **User-Friendly GUI**: Built with Tkinter, providing a simple and intuitive interface.

## Requirements

- **Python 3.x**
- **Pillow** library for image processing
- **MozJPEG** (`cjpeg.exe`) installed on your system

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/bulk-mozjpeg-compressor.git
   cd bulk-mozjpeg-compressor
