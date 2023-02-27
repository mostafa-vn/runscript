import urllib.request
import re

mabda = input('Link : ')


if 'arvan' in mabda:
    mabda = 'https://www.arvancloud.ir/fa/ips.txt'
    sherkat = 'ArvanCloud'
elif 'derak' in mabda:
    mabda = 'https://api.derak.cloud/public/ipv4'
    sherkat = 'DerakCloud'
elif 'google' in mabda:
    mabda = 'https://developers.google.com/search/apis/ipranges/googlebot.json'
    sherkat = 'GoogleBot'
else:
    sherkat = input('Company : ')

urllib.request.urlretrieve(mabda, "ips.txt")

with open('ips.txt') as file:
    for line in file:
        with open('{}.txt'.format(sherkat), "a") as myfile:
            r1 = re.findall(r"\d+\.+\d+\.+\d+\.+\d+\/+\d+", line.rstrip())
            if bool(r1):
                myfile.write('csf -a {} {}\n'.format(r1[0], sherkat))
