import csv 
import os
import numpy as np
import sys
sys.stdout = open(r'C:\Users\13106\python-challenge\PyBank\analysis\python_analysis', 'a')
date = []
income = []
with open(r'..\resources\budget_data.csv', newline='') as csvfile:   
        item = list(csv.reader(csvfile, delimiter=','))
        item.pop(0)
        for x in item:
                date.append(x[0])
                income.append(x[1])
print("Total Months:", (len(date)))
totalincome = 0
totaldiff = []
for x in income: 
        previoustotal = totalincome
        totalincome = int(x)+ previoustotal
        diff = totalincome - previoustotal
        totaldiff.append(diff)
total = 0
a = np.array(totaldiff)
b = np.diff(a)
c = np.diff(a)/(len(b))
dtotal = np.sum(c)
print("Average Change: $", (round(dtotal, 2)))
for x in totaldiff:
        total = x + total
print("Total: $", (total))
arrb = np.array([b])
blist = arrb.tolist()
minval = arrb.tolist()
date.pop(0)
zfile = zip(b, date)
zfile1 = zip(b, date)
blist, date = max(zfile)
print("The highest increase in profits was $%r in %s" % (blist, date))
blist, date = min(zfile1)
print("The greatest decrease in profits was $%r in %s" % (blist, date))
sys.stdout.close()