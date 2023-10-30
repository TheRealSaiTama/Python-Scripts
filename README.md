```markdown
# Python Scripts

## 1. screenshot.py

Captures the screen, displays the captured screen, and saves it as an image file.

### Usage

1. Install the required dependencies by running the following command:

```shell
pip install pyscreenshot Pillow
```

2. Run the script using the following command:

```shell
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

## 2. funfact.py

Generates and prints random fun facts.

### Usage

1. Install the required dependencies by running the following command:

```shell
pip install randfacts
```

2. Run the script using the following command:

```shell
python funfact.py
```

### Code

```python
from randfacts import get_fact

print("Fact of the moment:", get_fact(filter_enabled=False))
print("Stay Silent with these facts:", get_fact(only_unsafe=True))
```

## 3. webcrawler.py

Implements a web crawler to find all links on a web page.

### Usage

1. Install the required dependencies by running the following command:

```shell
pip install requests beautifulsoup4
```

2. Run the script using the following command:

```shell
python webcrawler.py
```

The script will crawl the web page specified in the `url` variable and print out all the links found.

## 4. whatsappautomation.py

Automates sending WhatsApp messages using the `pywhatkit` library.

### Usage

1. Install the required dependencies by running the following command:

```shell
pip install pywhatkit
```

2. Update the `phone_number`, `message`, `hour`, and `minute` variables in the script with your desired values.

3. Run the script using the following command:

```shell
python whatsappautomation.py
```

The script will send the specified message to the provided phone number at the specified time.

## 5. camimg.py

Captures an image from the default camera and saves it as a JPEG file.

### Usage

1. Install the required dependencies by running the following command:

```shell
pip install cv2
```

2. Run the script using the following command:

```shell
python camimg.py
```

### Code

```python
import cv2

imgcapture = cv2.VideoCapture(0)
result = True
while(result):
    ret, frame = imgcapture.read()
    cv2.imwrite("test.jpg", frame)
    result = False
    print("Image Captured...")

imgcapture.release()
```

## 6. ServerScript.py

Implements a TCP chat server that allows clients to connect and send messages.

### Usage

1. Install the required dependencies by running the following command:

```shell
pip install socket
```

2. Run the script using the following command:

```shell
python ServerScript.py
```

The script will start a TCP server on port 3000 and listen for incoming connections. When a client connects, the script will print the client's address and receive messages from the client. The script will also send messages to the client.

## 7. findthegold.py

A game where you try to find the hidden gold on a 3x3 grid.

### Usage

1. Run the script using the following command:

```shell
python findthegold.py
```

## 8. fizzbuzz.py

Generates a random number and applies the FizzBuzz rules.

### Usage

1. Run the script using the following command:

```shell
python fizzbuzz.py
```

## 9. twodicerolling.py

Simulates rolling two dice and displays the results.

### Usage

1. Run the script using the following command:

```shell
python twodicerolling.py
```

## 10. billroulette.py

Randomly selects a person to pay the bill.

### Usage

1. Run the script using the following command:

```shell
python billroulette.py
```

# Python Scripts

| Script | Description | Usage |
| --- | --- | --- |
| **screenshot.py** | Captures the screen, displays the captured screen, and saves it as an image file. | 1. Install pyscreenshot and Pillow<br>2. Run the script using `python screenshot.py` |
| **funfact.py** | Generates and prints random fun facts. | 1. Install randfacts<br>2. Run the script using `python funfact.py` |
| **webcrawler.py** | Implements a web crawler to find all links on a web page. | 1. Install requests and beautifulsoup4<br>2. Run the script using `python webcrawler.py` |
| **whatsappautomation.py** | Automates sending WhatsApp messages using the pywhatkit library. | 1. Install pywhatkit<br>2. Update the variables with your desired values<br>3. Run the script using `python whatsappautomation.py` |
| **camimg.py** | Captures an image from the default camera and saves it as a JPEG file. | 1. Install cv2<br>2. Run the script using `python camimg.py` |
| **ServerScript.py** | Implements a TCP chat server that allows clients to connect and send messages. | 1. Install socket<br>2. Run the script using `python ServerScript.py` |
| **findthegold.py** | A game where you try to find the hidden gold on a 3x3 grid. | 1. Run the script using `python findthegold.py` |
| **fizzbuzz.py** | Generates a random number and applies the FizzBuzz rules. | 1. Run the script using `python fizzbuzz.py` |
| **twodicerolling.py** | Simulates rolling two dice and displays the results. | 1. Run the script using `python twodicerolling.py` |
| **billroulette.py** | Randomly selects a person to pay the bill. | 1. Run the script using `python billroulette.py` |

Feel free to explore and use these scripts as needed. If you have any questions or suggestions, don't hesitate to reach out!
