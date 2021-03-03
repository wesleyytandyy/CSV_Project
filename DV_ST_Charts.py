import csv
from datetime import datetime

Death_open = open("death_valley_2018_simple.csv", "r")
Sitka_open = open("sitka_weather_2018_simple.csv", "r")

Death_file = csv.reader(Death_open, delimiter=",")
Sitke_file = csv.reader(Sitka_open, delimiter=",")

header_row = next(Death_file)
header_row = next(Sitke_file)


for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


death_highs = []
death_lows = []
death_dates = []

Sitka_highs = []
Sitka_lows = []
Sitka_dates = []

# converted_date = datetime.strptime("2018-07-01", "%y-%m-%d")

for row in Death_file:
    try:
        dhigh = int(row[4])
        dlow = int(row[5])
        ddate = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {ddate}")
    else:
        death_highs.append(dhigh)
        death_lows.append(dlow)
        death_dates.append(ddate)


for row in Sitke_file:
    try:
        Shigh = int(row[5])
        Slow = int(row[6])
        Sdate = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {Sdate}")
    else:
        Sitka_highs.append(Shigh)
        Sitka_lows.append(Slow)
        Sitka_dates.append(Sdate)


import matplotlib.pyplot as plt

fig, a = plt.subplots(2)
a[0].plot(Sitka_dates, Sitka_highs, c="red")
a[0].plot(Sitka_dates, Sitka_lows, c="blue")
a[1].plot(death_dates, death_highs, c="red")
a[1].plot(death_dates, death_lows, c="blue")


a[0].set_title(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US \n SITKA AIRPORT, AK US ",
    fontsize=16,
)

a[1].set_title(
    "DEATH VALLEY, CA US",
    fontsize=16,
)

a[0].fill_between(Sitka_dates, Sitka_highs, Sitka_lows, facecolor="blue", alpha=0.1)
plt.tick_params(axis="both", labelsize=12)

a[1].fill_between(death_dates, death_highs, death_lows, facecolor="blue", alpha=0.1)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()
plt.show()