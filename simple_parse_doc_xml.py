# -*- coding: utf-8 -*-
# for run on python 2.7.5
# python simple_parse_xml.py storagee1 container1

from xml.dom import minidom
import requests

import sys

#for arg in sys.argv:
#    print(arg)

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
current_count = 0
for current_count in range(max_count):
   print(itemlist[current_count].childNodes[0].nodeValue)
