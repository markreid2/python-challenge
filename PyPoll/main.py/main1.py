import csv 
import os
import numpy as np
import statistics
import sys
sys.stdout = open(r'C:\Users\13106\python-challenge\PyPoll\analysis\pypoll_analysis', 'a')
from collections import Counter
voter_ID = []
county = []
candidate = []
with open(r'C:\Users\13106\python-challenge\PyPoll\resources\election_data.csv', newline='') as csvfile1:
        item1 = list(csv.reader(csvfile1, delimiter=','))
        item1.pop(0)
        for x in item1:
            voter_ID.append(x[0])
            county.append(x[1])
            candidate.append(x[2])
print("Total Votes:", (len(voter_ID)))  
count = Counter(candidate).items()
percents = {x: int(float(y) / len(candidate) * 100) for x, y in count}
for name, pct in percents.items():
    print('%s - %s%s' % (name, pct, '%'))
names_to_count = (word for word in candidate if word[:1].isupper())
c = Counter(candidate)
print (c.most_common(4))
def winner(candidate):
    return(statistics.mode(candidate))
print(r'The Winner is:', winner(candidate))
sys.stdout.close()