import matplotlib.pyplot as plt

import csv

from datetime import datetime

from matplotlib import style

filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'

with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs = [], []

    for row in reader:
        high = int(row[5])
        highs.append(high)

        c_d = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(c_d)

with open(filename2) as fa:
    reade = csv.reader(fa)
    header_ro = next(reade)

    highs1 = []

    for rw in reade:
        try:
            hig = int(rw[4])
        except ValueError:
            print(f"Missing data for {c_d}")
        else:
            highs1.append(hig)



fig, ax = plt.subplots()
plt.style.use('seaborn')
ax.plot(dates, highs, c='red',alpha=0.5)
ax.plot(dates, highs1, c='purple',alpha=0.5)
plt.fill_between(dates,highs,highs1,facecolor='blue',alpha=0.1)
ax.set_xlabel('DATES',fontsize=20)
ax.set_ylabel('TEMPERATUE(F)',fontsize=20)
plt.title('COMPARISON BETWEEN SITKA AND DEATH VALLEY',fontsize=24)
plt.show()
