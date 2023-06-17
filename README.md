# DiabloIV_xp_stats

This program is used to get some stats of xp speed. You have to place your mouse on the xp bar before using the hotkey. This should be trigger twice, at the beginning and end of the period you wish to get stats.

## Prerequisites

- Python 3 installed on your system
- Required Python packages:
  - keyboard
  - Pillow
  - pytesseract
- Tesseract OCR installed on your system and its executable path set in the program

## Installation

1. Clone or download the project files to your local machine.

2. Install the necessary Python packages by running the following command in a terminal or command prompt:

   ```shell
   pip install keyboard Pillow pytesseract
   ```

3. Install Tesseract OCR:

Download the appropriate installer for your system from the following link: https://github.com/UB-Mannheim/tesseract/wiki
Follow the installation instructions specific to your operating system.
Make a note of the installation path of the Tesseract OCR executable.

4. Set the path to the Tesseract OCR executable by updating the following line of code with the correct path:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

5. Change the hotkey if needed (ctrl+w by default)

6. The regex used to extract xp is set to work with french text. If your game is not in french, just change the word "niveau" which means level in french.