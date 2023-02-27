#!/usr/bin/python3
import datetime, os, urllib.request
if datetime.datetime.now().hour == 23:
    urllib.request.urlopen('https://mtrx.ir')
print(urllib.request.urlopen('https://mtrx.ir/').content())
# if datetime.datetime.now() == '':
# if a != '':
#     os.system('{}'.format(b))