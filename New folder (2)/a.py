from pyautogui import click, position, moveTo
from PIL import ImageGrab
from pytesseract import pytesseract
from time import sleep
from playsound import playsound

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# time = input('Enter time:  ')

def check(left, top, right, bottom):
    return pytesseract.image_to_string(
        ImageGrab.grab().crop((left, top, right, bottom)))

# while True:
#     if check(1658, 347, 1842, 392) != '':
#         lastReply = int((check(230, 350, 450, 390)[0:2]).replace('h', ''))
#         if lastReply > int(time):
#             playsound('a.mp3')
#         if lastReply == 55:
#             moveTo(1542, 369, interval=10)

#             for i in ['Reply', 'Open']:
#                 if i in check(300, 205, 460, 233):
#                     moveTo(387, 220, interval=1)
#                 elif i in check(430, 205, 610, 233):
#                     moveTo(528, 220, interval=1)
#                 elif i in check(542, 205, 700, 233):
#                     moveTo(647, 220, interval=1)
#                 elif i in check(626, 205, 780, 233):
#                     moveTo(700, 220, interval=1)
#                 else:
#                     moveTo(885, 220, interval=1)

#             moveTo(575, 389, interval=1)

#             moveTo(56, 81, interval=1)

#     sleep(10)



# import zstandard , sys
# zst = zstandard.ZstdDecompressor()
# with open('test.tar.zst', 'rb') as f1, open('test.tar', 'wb') as f2:
#     zst.copy_stream(f1, f2, write_size=65536)
