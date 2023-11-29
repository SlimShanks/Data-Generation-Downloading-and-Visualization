import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows= [], [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        c_d = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(c_d)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, highs,c='purple',alpha=0.5)
ax.plot(dates, lows,c='red',alpha=0.5)
plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)
ax.set_title('Daily high temperatures 2018')
fig.autofmt_xdate()
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('TEMPERATURE(F)')
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
