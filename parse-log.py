'''
sites.log:

google - 1 - http
onliner - 2 - https
google - 3 - http
google - 4 - http
onliner - 5 - https
google - 6 - http
google - 7 - http
'''

a = 0
b = 0

f = open('sites.log', "r")
for line in f:
    if line.split(' - ')[0] == "google":
        a +=1
    elif line.split(' - ')[0] == "onliner":
        b +=1
f.close

print("Google:", a)
print("Onliner:", b)

'''
Google: 5
Onliner: 2
'''
