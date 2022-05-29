import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    # Call csv.reader() and pass it the file object as an argument to create a reader object associated with that file.
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], [],
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot
    plt.title("Daily high temperatures, July 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # draw date label diagonally to prevent them from overlapping.
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()