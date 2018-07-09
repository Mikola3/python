# -*- coding: utf-8 -*-
from xml.dom import minidom
import requests

import sys
# first item in parameters is script's name
storage = str(sys.argv[1])
container = str(sys.argv[2])
url = "https://" + storage + ".blob.core.windows.net/" + container + "/?restype=container&comp=list"
print(url)

#url = 'https://storagee1.blob.core.windows.net/container1/?restype=container&comp=list'
r = requests.get(url, allow_redirects=True)
open('test.xml', 'wb').write(r.content)

xmldoc = minidom.parse('test.xml')
itemlist = xmldoc.getElementsByTagName('Name')
max_count = len(itemlist)
itemlist2 = xmldoc.getElementsByTagName('Last-Modified')
max_count2 = len(itemlist2)
current_count = 0
dict = {}

for current_count in range(max_count):
    for current_count in range(max_count2):
        a = str(itemlist[current_count].childNodes[0].nodeValue)
        b = str(itemlist2[current_count].childNodes[0].nodeValue)
        dict[a] = b

print(dict)
