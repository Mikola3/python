#!/usr/bin/env python
from xml.dom.minidom import parseString
import requests
import json

url = "https://storagee1.blob.core.windows.net/container1/?restype=container&comp=list"

final_array = []
xmlDoc = parseString(requests.get(url, allow_redirects=True).content)
itemlist = xmlDoc.getElementsByTagName('Name')
for current_count in range(len(itemlist)):
  current_json = {}
  additional_json = {}
  current_path = ''
  current_artefact = str(itemlist[current_count].childNodes[0].nodeValue).split('/')
  for e in current_artefact:
    current_path += e + '/'
    if 'folder' in e and current_json == {}:
      current_json = {'type':'folder', 'name':e, "path": current_path}
    elif 'folder' not in e and current_json != {}: 
      current_json['data'] = [{'type':'file', 'name':e, "path": current_path[:-1]}]
    if 'folder' in e and current_json != {} and (len(current_path.split('/'))-1) > 1:
      additional_json = {'type':'folder', 'name':e, "path": current_path}
      current_json['data'] = additional_json
    if additional_json != {} and current_json != {}:
      additional_json['data'] = [{'type':'file', 'name':e, "path": current_path[:-1]}]
      current_json['data'] = additional_json 
    if current_json == {}:
      current_json = {'type':'file', 'name':e, "path": current_path[:-1]}
  final_array.append(current_json)
print('---FINAL----')
json_dict = {'data':final_array}
print json.dumps(json_dict, indent=4, sort_keys=False)
