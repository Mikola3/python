'''
dates.log:
1st May 1992
2nd Dec 1994
11th Sep 2001
5th Oct 2005
3th Apr 2003
'''

import datetime
import re

def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1

file1 = open('dates.log', "r")
file2 = open('dates2.log', "a+")

for line in file1:
    number, month, year = line.split(' ')
    #print(number, month, year)
    number_new = re.findall('\d+', number)[0]
    #print(number_new, month, year)
    month_new = month_converter(month)
    data = datetime.datetime(int(year), int(month_new), int(number_new))
    infa = "{:0>4}-{:0>2}-{:0>2}".format(data.year, data.month, data.day)
    print(infa)
    file2.write(infa + '\n')
file1.close
file2.close

'''
dates2.log:
1992-05-01
1994-12-02
2001-09-11
2005-10-05
2003-04-03
'''
