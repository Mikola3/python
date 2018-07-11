# -*- coding: utf-8 -*-
# for run on python 2.7.5
# python simple_parse_xml.py storagee1 container1

from xml.dom import minidom
import requests
import sys

artifact_list = []

url = "https://storagee1.blob.core.windows.net/container1/?restype=container&comp=list"

r = requests.get(url, allow_redirects=True)
open('test.xml', 'wb').write(r.content)

xmldoc = minidom.parse('test.xml')
itemlist = xmldoc.getElementsByTagName('Name')
max_count = len(itemlist)
current_count = 0
for current_count in range(max_count):
    file = str(itemlist[current_count].childNodes[0].nodeValue)
    #print(file)
    artifact_list.append(file)


#string = 'folder1/folder2/test2.tar.gz'
d = {}

def dictizeString(string, dictionary):
    #while string.startswith('/'): # returns True if a string starts with the specified prefix
    #    string = string[1:]
    parts = string.split('/', 1)
    if len(parts) > 1:
        branch = dictionary.setdefault(parts[0], {})
        dictizeString(parts[1], branch)
    else:
        if dictionary.has_key(parts[0]):
             # If there's an addition error here, it's because invalid data was added
             dictionary[parts[0]] += 1
        else:
             #dictionary[parts[0]] = 1
             dictionary[parts[0]] = 'file'

for item in artifact_list:
    dictizeString(item, d)

print(d)
# output
# {'folder1': {'child1.md': 'file', 'child2.md': 'file', 'folder2': {'folder3': {'test3.tar.gz': 'file'}, 'test2.tar.gz': 'file'}}, 'folder5': {'test5.tar.gz': 'file'}, 'test1.tar.gz': 'file'}
