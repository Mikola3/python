'''
sites.log:
google.com - 1 - http
onliner.by - 2 - https
google.com - 3 - http
tut.by - 4 - https
onliner.by - 5 - https
google.com - 6 - http
tut.by - 7 - http
'''
sites = []

file1 = open('sites.log', "r")
file2 = open('sites2.log', "a+")
for line in file1:
    site = line.split(' - ')[0]
    sites.append(site)

d = {}
for i in sites:
    d[i]=sites.count(i)
#print(d)
#{'google.com': 3, 'onliner.by': 2, 'tut.by': 2}

for i in d:
    infa = "{} - {}".format(i, d[i])
    file2.write(infa + '\n')

file1.close
file2.close

'''
google.com - 3
onliner.by - 2
tut.by - 2
'''
