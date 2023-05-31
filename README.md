```
# Python-Scripts

This repository contains various Python scripts for different purposes.

## Screenshot.py

The `screenshot.py` script allows you to capture screenshots using Python. It utilizes the `pyscreenshot` and `PIL` (Python Imaging Library) packages to capture and manipulate the screenshots.

### Prerequisites

Before running the script, make sure you have the following dependencies installed:

- `pyscreenshot`: A Python library to capture screenshots.
- `PIL` (Python Imaging Library): A library for opening, manipulating, and saving many different image file formats.

You can install the dependencies by running the following command:

```shell
pip install pyscreenshot Pillow
```

### Usage

To capture a screenshot, run the `screenshot.py` script. The script performs the following actions:

1. Imports the necessary packages:
   ```python
   import pyscreenshot
   import PIL
   ```

2. Captures the screen:
   ```python
   capture = pyscreenshot.grab()
   ```

3. Displays the captured screen:
   ```python
   capture.show()
   ```

4. Saves the screenshot as "capturedthroughscript.jpg":
   ```python
   capture.save("capturedthroughscript.jpg")
   ```

Make sure to adjust the filename and path when saving the screenshot according to your requirements.

Feel free to explore and modify the script as needed for your specific use case.

## License

This repository is licensed under the [MIT License](LICENSE).
```
