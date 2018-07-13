# -*- coding: utf-8 -*-
# for run on python 2.7.5
# python simple_parse_xml.py storagee1 container1

from xml.dom import minidom
import requests
import sys

import urllib2

url = "https://storagee1.blob.core.windows.net/container1/?restype=container&comp=list"
artifact_list = []
dict1 = {}

def bring_xml(url):
    #artifact_list = []
    xmldoc = minidom.parse(urllib2.urlopen(url))
    item_name = xmldoc.getElementsByTagName('Name')
    item_length = xmldoc.getElementsByTagName('Content-Length')
    max_count = len(item_name)
    current_count = 0
    for current_count in range(max_count):
        file_name = str(item_name[current_count].childNodes[0].nodeValue)
        file_length = str(item_length[current_count].childNodes[0].nodeValue)
        item_path = 
        dict1[file_name] = file_length
        #print(file_length)
        #print(file)
        #artifact_list.append(file_name)
    #return artifact_list


bring_xml(url)

print(dict1)
#print(artifact_list)
