```markdown
# Python Scripts

This repository contains two Python scripts for various purposes.

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

Feel free to explore and use these scripts as needed.

```

You can copy and paste the above content into a file named `README.md` in your GitHub repository. Make sure to adjust the installation instructions and code sections based on your specific requirements.
