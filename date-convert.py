'''
dates.log:

11th Sep 2001
5th Oct 2005
3th Apr 2003
'''

import datetime

def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

file1 = open('dates.log', "r")
file2 = open('dates2.log', "a+")

for line in file1:
    number = line.split(' ')[0].split('th')[0]
    month = line.split(' ')[1]
    month_num = month_converter(month)
    year = line.split(' ')[-1]
    data = datetime.datetime(int(year), int(month_num), int(number))
    infa = "{:0>4}-{:0>2}-{:0>2}".format(data.year, data.month, data.day)
    print(infa)
    file2.write(infa + '\n')
file1.close
file2.close

'''
dates2.log:

2001-09-11
2005-10-05
2003-04-03
'''
