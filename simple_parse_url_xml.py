# -*- coding: utf-8 -*-
# for run on python 2.7.5
# python simple_parse_xml.py storagee1 container1

from xml.dom import minidom
import requests
import sys

import urllib2

artifact_list = []

url = "https://storagee1.blob.core.windows.net/container1/?restype=container&comp=list"

xmldoc = minidom.parse(urllib2.urlopen(url))
itemlist = xmldoc.getElementsByTagName('Name')

max_count = len(itemlist)
current_count = 0
for current_count in range(max_count):
    file = str(itemlist[current_count].childNodes[0].nodeValue)
    print(file)
    artifact_list.append(file)
