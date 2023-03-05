from pyautogui import click, position
from PIL import ImageGrab
from pytesseract import pytesseract
from time import sleep

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def check(left, top, right, bottom):
    return pytesseract.image_to_string((ImageGrab.grab().crop((left, top, right, bottom)).convert('L')))


a = check(20, 925, 600, 980)
print(a)

while True:
    if a == check(20, 925, 600, 980):
        pass
    else:
        a = check(20, 925, 600, 980)
        click(270, 960)

    sleep(5)