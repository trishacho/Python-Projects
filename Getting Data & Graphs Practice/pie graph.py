#Trisha Choudhary
#pie graph

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

diff = []
for i in range(len(highs)):
    diff.append(highs[i] - lows[i])

newDiff = []
numOfTemps = []
for i in range(max(diff)):
    numOfTemps.append(diff.count(i))
    if i not in newDiff:
        newDiff.append(i)
    
fig1, ax1 = plt.subplots()
ax1.pie(numOfTemps, labels = newDiff, autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')

plt.show()
