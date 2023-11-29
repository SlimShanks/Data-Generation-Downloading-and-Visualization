import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, highs, lows = [], [], []
    for row in reader:
        c_d = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {c_d}")
        else:
            lows.append(low)
            highs.append(high)
            dates.append(c_d)

plt.style.use('seaborn')

fig, ax = plt.subplots()


ax.plot(dates, highs, c='purple', alpha=0.5)
ax.plot(dates, lows, c='red', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('Daily high temperatures 2018')

fig.autofmt_xdate()

title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title,fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('TEMPERATURE(F)')

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()