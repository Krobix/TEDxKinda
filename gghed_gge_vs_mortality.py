import csv, json
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

countries_mortalities = ["United States", 'Sweden', 'Spain']
countries_spending = ["United States of America", 'Sweden', 'Spain']
country_ind = [0,0,0]
years = list(range(2015, 2022))

for i in range(0, 3):
    x_vals = [None] * len(years)
    y_vals = [None] * len(years)

    with open("GHED_data.csv", "r") as f:
        reader = csv.DictReader(f)

        for x in reader:
            if x["country"] == countries_spending[i] and int(x["year"]) in years:
                x_vals[years.index(int(x["year"]))] = float(x["gghed_gge"])

    with open("world_mortality.json", "r") as f:
        countries = json.load(f)

        for y in years:
            y_vals[years.index(y)] = float(countries[countries_mortalities[i]][str(y)])

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

    plt.scatter(x_vals, y_vals, label=countries_mortalities[i])
    for c in range(len(x_vals)):
        plt.annotate(str(years[c]), [x_vals[c], y_vals[c]])

plt.xlabel("Domestic General Government Health Expenditure (GGHE-D) as % General Government Expenditure (GGE)")
plt.ylabel("Mortality Rate as Deaths per 100,000")
plt.title("Government Health Expenditures VS. Mortality Rate (2015-2021)")
plt.legend()

plt.show()