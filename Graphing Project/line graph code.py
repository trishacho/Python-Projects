import csv
from matplotlib import pyplot as plt

filename = 'MPAs.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    yr2000, yr2005, yr2010, yr2015, yr2017 = [], [], [], [], []
    for row in reader:
        try:
            mpa2000 = float(row[2])
            mpa2005 = float(row[3])
            mpa2010 = float(row[4])
            mpa2015 = float(row[5])
            mpa2017 = float(row[6])
        except ValueError:
            print('Missing data')
        else:
            yr2000.append(mpa2000)
            yr2005.append(mpa2005)
            yr2010.append(mpa2010)
            yr2015.append(mpa2015)
            yr2017.append(mpa2017)

africa2000 = yr2000[:30]
africa2005 = yr2005[:30]
africa2010 = yr2010[:30]
africa2015 = yr2015[:30]
africa2017 = yr2017[:30]

total = 0
for x in africa2000:
    total = total + x
africa = []
africa.append(total)

total = 0
for x in africa2005:
    total = total + x
africa.append(total)

total = 0
for x in africa2010:
    total = total + x
africa.append(total)

total = 0
for x in africa2015:
    total = total + x
africa.append(total)

total = 0
for x in africa2017:
    total = total + x
africa.append(total)
###################################
asia2000 = yr2000[30:64]
asia2005 = yr2005[30:64]
asia2010 = yr2010[30:64]
asia2015 = yr2015[30:64]
asia2017 = yr2017[30:64]

total = 0
for x in asia2000:
    total = total + x
asia = []
asia.append(total)

total = 0
for x in asia2005:
    total = total + x
asia.append(total)

total = 0
for x in asia2010:
    total = total + x
asia.append(total)

total = 0
for x in asia2015:
    total = total + x
asia.append(total)

total = 0
for x in asia2017:
    total = total + x
asia.append(total)
##################################
europe2000 = yr2000[64:95]
europe2005 = yr2005[64:95]
europe2010 = yr2010[64:95]
europe2015 = yr2015[64:95]
europe2017 = yr2017[64:95]

total = 0
for x in europe2000:
    total = total + x
europe = []
europe.append(total)

total = 0
for x in europe2005:
    total = total + x
europe.append(total)

total = 0
for x in europe2010:
    total = total + x
europe.append(total)

total = 0
for x in europe2015:
    total = total + x
europe.append(total)

total = 0
for x in europe2017:
    total = total + x
europe.append(total)
###############################
nAmerica2000 = yr2000[95:126]
nAmerica2005 = yr2005[95:126]
nAmerica2010 = yr2010[95:126]
nAmerica2015 = yr2015[95:126]
nAmerica2017 = yr2017[95:126]

total = 0
for x in nAmerica2000:
    total = total + x
nAmerica = []
nAmerica.append(total)

total = 0
for x in nAmerica2005:
    total = total + x
nAmerica.append(total)

total = 0
for x in nAmerica2010:
    total = total + x
nAmerica.append(total)

total = 0
for x in nAmerica2015:
    total = total + x
nAmerica.append(total)

total = 0
for x in nAmerica2017:
    total = total + x
nAmerica.append(total)
###############################
oceania2000 = yr2000[126:148]
oceania2005 = yr2005[126:148]
oceania2010 = yr2010[126:148]
oceania2015 = yr2015[126:148]
oceania2017 = yr2017[126:148]

total = 0
for x in oceania2000:
    total = total + x
oceania = []
oceania.append(total)

total = 0
for x in oceania2005:
    total = total + x
oceania.append(total)

total = 0
for x in oceania2010:
    total = total + x
oceania.append(total)

total = 0
for x in oceania2015:
    total = total + x
oceania.append(total)

total = 0
for x in oceania2017:
    total = total + x
oceania.append(total)
######################################
sAmerica2000 = yr2000[148:162]
sAmerica2005 = yr2005[148:162]
sAmerica2010 = yr2010[148:162]
sAmerica2015 = yr2015[148:162]
sAmerica2017 = yr2017[148:162]

total = 0
for x in sAmerica2000:
    total = total + x
sAmerica = []
sAmerica.append(total)

total = 0
for x in sAmerica2005:
    total = total + x
sAmerica.append(total)

total = 0
for x in sAmerica2010:
    total = total + x
sAmerica.append(total)

total = 0
for x in sAmerica2015:
    total = total + x
sAmerica.append(total)

total = 0
for x in sAmerica2017:
    total = total + x
sAmerica.append(total)
#############################
years = ["2000", "2005", "2010", "2015", "2017"]

plt.plot(years, africa, color = '#003f5c', marker = 'o', linestyle = 'solid', label = 'Africa', linewidth = 2.5)
plt.plot(years, asia, color = '#ffa600', marker = 'o', linestyle = 'solid', label = 'Asia', linewidth = 2.5)
plt.plot(years, europe, color = '#444e86', marker = 'o', linestyle = 'solid', label = 'Europe', linewidth = 2.5)
plt.plot(years, nAmerica, color = '#955196', marker = 'o', linestyle = 'solid', label = 'North America', linewidth = 2.5)
plt.plot(years, oceania, color = '#ff6e54', marker = 'o', linestyle = 'solid', label = 'Oceania', linewidth = 2.5)
plt.plot(years, sAmerica, color = '#dd5182', marker = 'o', linestyle = 'solid', label = 'South America', linewidth = 2.5)

plt.title("Ecosystem vitality in marine protected areas among continents of the world")

plt.xlabel("Years")
plt.ylabel("MPA values")

plt.xticks()

plt.legend()

plt.show()
