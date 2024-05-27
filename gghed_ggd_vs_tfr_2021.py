#test comparison between the US, Spain, and Sweden

import csv
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

countries_spending = ["United States of America", 'Sweden', 'Spain']
countries_tfr = ["USA", "Spain", "Sweden"]
country_ind = [0,0,0]
years = list(range(2000, 2022))

for i in range(0, 3):
    x_vals = [None] * len(years)
    y_vals = [None] * len(years)

    with open("GHED_data.csv", "r") as f:
        reader = csv.DictReader(f)

        for x in reader:
            if x["country"]==countries_spending[i] and int(x["year"]) in years:
                x_vals[years.index(int(x["year"]))] = x["gghed_gge"]

    with open("TFR.csv", "r") as f:
        reader = csv.reader(f)

        for x in reader:
            for y in years:
                ind = years.index(y)
                if x[0]=="COUNTRY":
                    for a in x:
                        for b in countries_tfr:
                            if a==b:
                                country_ind[countries_tfr.index(b)] = x.index(a)
                    #print(country_ind)

                elif x[0]==str(y):
                    for z in x:
                        if x.index(z)==country_ind[i]:
                            y_vals[ind] = z

    print(x_vals)
    print(y_vals)

    to_remove = []
    offset = 0

    for y in y_vals:
        if y is None:
            to_remove.append(y_vals.index(y)-offset)
            offset  += 1

    for r in to_remove:
        y_vals.pop(r)
        x_vals.pop(r)

    plt.scatter(x_vals, y_vals)

plt.show()
