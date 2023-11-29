import matplotlib.pyplot as plt
import csv
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    yo = next(reader)
    print(yo)

    prcps, dates = [], []
    for row in reader:
        prcp = float(row[3])
        prcps.append(prcp)
        c_d = datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(c_d)

fig, ax = plt.subplots()

ax.plot(dates,prcps, c='purple')
ax.set_ylabel('Dates')
fig.autofmt_xdate()
ax.set_ylabel('Rainfall amount')
plt.show()
