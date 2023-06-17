import keyboard
from PIL import ImageGrab
import pytesseract
import re
from datetime import datetime
import sys

#Keys used to trigger the process, change this if needed
HOTKEY = "ctrl+w"

#This should be change to your teseract folder
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

data = []

def process():
    screenshot = ImageGrab.grab()
    print("Hotkey captured")
    
    extracted_text = pytesseract.image_to_string(screenshot)

    m = re.search(r'(?<=niveau \d{2} : )\d+', extracted_text) 

    if not m:
        print("Any information match xp on the screenshot")
        return

    now = datetime.now()

    if not data:
        print(m.group(), " at ", now, "\n")
        data.append((int(m.group()), now))
    else:
        print(m.group(), " at ", now, "\n")

        time_diff = (now-data[0][1]).total_seconds()
        print("Time spent (secs) : \t", time_diff)

        xp_diff = int(m.group()) - data[0][0]
        print("Xp diff : \t\t", xp_diff)

        ratio = (xp_diff / time_diff) * 3600
        print("Farm speed (xp/h) : \t", ratio)

        data.clear()


keyboard.add_hotkey(HOTKEY, process)

try:
    keyboard.wait()
except:
    exit(0)
