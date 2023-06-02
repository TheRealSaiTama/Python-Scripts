Here's an updated version of the `README.md` file that includes the information about the newly added `webcrawler.py` script:

```markdown
# Python Scripts

This repository contains various Python scripts for different purposes.

## screenshot.py

This script allows you to capture the screen, display the captured screen, and save it as an image file.

### Usage

1. Install the required dependencies by running the following command:
   ```
   pip install pyscreenshot Pillow
   ```

2. Run the script using the following command:
   ```
   python screenshot.py
   ```

### Code

```python
import pyscreenshot
import PIL

capture = pyscreenshot.grab()  # to capture the screen

# to display captured screen
capture.show()

# to save screenshot
capture.save("capturedthroughscript.jpg")
```

## funfact.py

This script generates and prints random fun facts.

### Usage

1. Install the required dependencies by running the following command:
   ```
   pip install randfacts
   ```

2. Run the script using the following command:
   ```
   python funfact.py
   ```

### Code

```python
from randfacts import get_fact

print("Fact of the moment:", get_fact(filter_enabled=False))
print("Stay Silent with these facts:", get_fact(only_unsafe=True))
```

## webcrawler.py

This script implements a web crawler to find all links on a web page.

### Usage

1. Install the required dependencies by running the following command:
   ```
   pip install requests beautifulsoup4
   ```

2. Run the script using the following command:
   ```
   python webcrawler.py
   ```

The script will crawl the web page specified in the `url` variable and print out all the links found.

Feel free to explore and use these scripts as needed.

```

I will continue updating the `README.md` file as i keep adding new scripts
