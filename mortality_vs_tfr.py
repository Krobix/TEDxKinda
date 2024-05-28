import csv, json
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

countries_mortalities = ["United States", 'Sweden', 'Spain']
countries_tfr = ["USA", "Spain", "Sweden"]
country_ind = [0,0,0]
years = list(range(2015, 2022))

for i in range(0, 3):
    x_vals = [None] * len(years)
    y_vals = [None] * len(years)

    with open("world_mortality.json", "r") as f:
        countries = json.load(f)

        for y in years:
           x_vals[years.index(y)] = float(countries[countries_mortalities[i]][str(y)])

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
                            y_vals[ind] = float(z)

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

    plt.scatter(x_vals, y_vals, label=countries_tfr[i])
    for c in range(len(x_vals)):
        plt.annotate(str(years[c]), [x_vals[c], y_vals[c]])

plt.xlabel("Mortality Rate as Deaths per 100,000")
plt.ylabel("Total Fertility Rate as Children Per Woman")
plt.title("Mortality Rate VS. Total Fertility Rate (2015-2021)")
plt.legend()

plt.show()