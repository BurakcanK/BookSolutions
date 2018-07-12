import csv

from datetime import datetime
from matplotlib import pyplot as plt

FILENAME = "sitka_weather_2014.csv"
FILENAME = "death_valley_2014.csv"

# get dates, high and low temps from the file
dates, highs, lows = [], [], []
with open(FILENAME) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            currentDate = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(currentDate, 'missing data')
        else:
            dates.append(currentDate)
            highs.append(high)
            lows.append(low)

# plot the data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

# format plot
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.title("Daily high and low temperatures - 2014\nDeath Valley", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature {F}", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
