from xml.dom.minidom import parseString
from xml.dom import minidom
import requests
import sys


artifact_list = []

dict = {}
childArray = []
dict["data"] = childArray
url = "https://storagee1.blob.core.windows.net/container1/?restype=container&comp=list"
xmldoc = parseString(requests.get(url, allow_redirects=True).content)

itemlist = xmldoc.getElementsByTagName('Name')
max_count = len(itemlist)
current_count = 0
for current_count in range(max_count):
    file = str(itemlist[current_count].childNodes[0].nodeValue)
    #print(file)
    artifact_list.append(file)

global_dictionary = []
unique_count = 0

def recurse_function(current_massive, current_dictionary, unique_count):

	local_dict = {}
	current_count = 0
	sizeMassive = len(current_massive)
	# print "size_massive = " + str(sizeMassive)
	isWas = False   
	new_massive = []
	# print "current_massive = " + str(current_massive)
	mini_global_count = 0
	for item in current_massive:
		if not current_massive:
			break
		if not '/' in item:
			current_dictionary["data"].append({})		
			current_dictionary["data"][current_count]["type"] = "file"
			current_dictionary["data"][current_count]["name"] = item
			current_dictionary["data"][current_count]["path"] = item
			current_count += 1  
			# current_massive.remove(item)
		else:			
			array_folder = []
			local_counter = 0
			array_folder = []
			array_folder.append(current_massive[0].split('/')[0])
			# print "current_massive here: !" + str(current_massive)
			for super_item in current_massive:				
				if '.' in array_folder[0]:
					array_folder[0] = super_item.split('/')[0]
				if array_folder[local_counter] != super_item.split('/')[0] and '/' in super_item:					
					array_folder.append(super_item.split('/')[0])
					local_counter += 1
			print array_folder
			'''
			for item in array_folder:
					if not array_folder:
						break
					if not '/' in item: 
						array_folder.remove(item)
						'''
			# print "array_folder = " + str(array_folder)
			
			for mini_item in array_folder:
				for super_item in current_massive:			    
				    current_folder = mini_item
				    new_massive.append(super_item.replace(current_folder + str('/'),""))					
				# if mini_global_count == sizeMassive - 1:
				if isWas == False:			
					current_folder = item.split('/')[0]
					current_dictionary["data"].append({})		
					current_dictionary["data"][current_count]["type"] = "folder"
					current_dictionary["data"][current_count]["name"] = mini_item
					current_dictionary["data"][current_count]["path"] = mini_item
					current_dictionary["data"][current_count]["data"] = []
					#current_dictionary["data"][current_count]["data"] = global_array
					# recurse
					global_dictionary = current_dictionary["data"][current_count]	
					# print new_massive		
					# before start recurse it should remove all cllean files (without path with directories)
					for item in current_massive:
						if not current_massive:
							break
						if not '/' in item: 
							new_massive.remove(item)
					recurse_function(new_massive, global_dictionary, unique_count)
					unique_count += 1
					print "Hello"				
					isWas = True			
					current_count += 1
		# mini_global_count += 1
	print current_dictionary
	# print new_massive



recurse_function(artifact_list, dict, unique_count)
# print unique_count
#print artifact_list
# print artifact_list
'''
local_dict = {}
current_count = 0
isWas = False
new_massive = []
for item in artifact_list:
	if not artifact_list:
		break
	if not '/' in item:
		dict["data"].append({})		
		dict["data"][current_count]["type"] = "file"
		dict["data"][current_count]["name"] = item
		dict["data"][current_count]["path"] =  item
		current_count += 1  
		# artifact_list.remove(item)
	else:
		current_folder = item.split('/')[0]
		new_massive.append(item.replace(current_folder + str('/'),""))
		if isWas == False:
			dict["data"].append({})		
			dict["data"][current_count]["type"] = "folder"
			dict["data"][current_count]["name"] = current_folder
			dict["data"][current_count]["path"] = current_folder
			dict["data"][current_count]["data"] =  []
			isWas = True			
			current_count += 1
		# isWas = True
		# print new_dict 	       
#print(artifact_list)
print(new_massive)
#print dict
'''
