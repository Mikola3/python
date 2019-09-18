import datetime

mass = str(datetime.datetime.now()).split()
day = mass[0]
hour = mass[1].split(':')[0]
minute = mass[1].split(':')[1]
sec = mass[1].split(':')[-1].split('.')[0]
date = day + "-" + hour + "-" + minute + "-" + sec

print(day)
print(hour)
print(minute)
print(sec)
print(date)
