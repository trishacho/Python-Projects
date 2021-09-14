"""
import csv

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print (header_row)

#sometimes headers are not formatted consistently-so what do we do?

import csv

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
for index,column_header in enumerate(header_row):
    print(index, column_header)

#now that we can see the columns lets look at the MAX temp column only
import csv

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs=[]
    for row in reader:
        highs.append(int (row[1]))
        #change high = highs.append(int row[1])
    print (highs)
#can use try-and-catch to remove "incorrect" values in a dataset
"""
import csv
from matplotlib import pyplot as plt
filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs=[]
    for row in reader:
        highs.append(int(row[1]))
#plot the data
fig = plt.figure(dpi =128, figsize=(10,6))
plt.plot(highs, c='red')

#format plot
plt.title("Daily High Temps", fontsize = 24)
plt.xlabel(' ', fontsize=16)
plt.ylabel("Temp(F)", fontsize = 16)
plt.tick_params(axis='both', which = 'major', labelsize = 16)
plt.show()
