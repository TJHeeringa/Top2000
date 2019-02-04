import csv
import matplotlib.pyplot as plt
from colour import Color
import numpy as np

song_time_span = range(1920, 2020)
top2000_time_span = range(1999, 2017)
interesting_top = 2000

top2000 = {str(year): {str(y): 0 for y in song_time_span} for year in top2000_time_span}
red = Color("red")
top2000_colours = list(red.range_to(Color("green"), 17))
with open('Top2000.csv', newline='', encoding='ANSI') as csvfile:
    next(csvfile, None)
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        top2000_year = row[0]
        publishing_year = row[4]
        if int(row[1]) <= interesting_top:
            top2000[top2000_year][publishing_year] += 1

count = 0
fig_line = plt.figure("Top2000")
for year, color in zip(top2000.keys(), top2000_colours):
    x, y = zip(*sorted(top2000[year].items()))
    plt.plot(x, y, label=year, color=color.rgb)
    count += 1
    print(count)
plt.title("Top2000 over de jaren")
plt.xlabel("Jaar van uitgifte")
plt.ylabel("Aantal nummers")
plt.legend()

top2000_mesh = np.transpose(np.array([list(top2000[year].values()) for year in list(top2000.keys())]))
fig_mesh = plt.figure("Top2000 mesh")
plt.pcolormesh(top2000_time_span, song_time_span, top2000_mesh)
plt.title("Top2000 over de jaren")
plt.xlabel("Top2000 editie")
plt.ylabel("Jaar van uitgifte")
cbar = plt.colorbar()
cbar.set_label("Aantal nummers")
plt.show()
