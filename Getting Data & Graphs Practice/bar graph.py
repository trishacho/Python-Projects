#Trisha Choudhary
#bar graph

import csv
from matplotlib import pyplot as plt

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    max_temps = []
    dates = []
    for row in reader:
        max_temps.append(int(row[1]))
        dates.append(row[0])

labelDates =[]
print("Enter how many dates you want to see.")
dateRange = int(input())

for x in range(1, dateRange+1):
    labelDates.append(x)

plt.bar(dates[: dateRange], max_temps[: dateRange], color = 'teal')

plt.title("Max Temps")

plt.xticks(range(len(labelDates)), labelDates, fontsize = 8)

plt.xlabel("Date in September 2014")
plt.ylabel("Temperatures (F)")

plt.show()
