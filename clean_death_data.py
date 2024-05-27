#Mortality dataset has monthly but not yearly data - We can clean it up into a bin file and average into years
import json, csv

countries = {}

with open("world_mortality.csv", "r") as f:
    reader = csv.DictReader(f)

    for i in reader:
        if i["country_name"] not in countries:
            countries[i["country_name"]] = {}
        if i["year"] not in countries[i["country_name"]]:
            countries[i["country_name"]][i["year"]] = []
        countries[i["country_name"]][i["year"]].append(i["deaths"])

    for i in countries:
        for j in countries[i]:
            total = 0
            for k in countries[i][j]:
                total += float(k)
            countries[i][j].append(total)

with open("population.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        #print(r)
        for i in countries:
            if r["country"] == i:
                for j in countries[i]:
                    if (str(j) in r) and (not r[str(j)] == ""):
                        countries[i][j] = (countries[i][j][-1]/float(r[str(j)]))*100000


with open("world_mortality.json", "w") as f:
    json.dump(countries, f)