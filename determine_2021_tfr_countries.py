#determine for which countries 2021 tfr data is available
import csv

countries = []

with open("TFR.csv", "r") as f:
    reader = csv.reader(f)

    for i in reader:
        if i[0].strip() == "COUNTRY":
            num = 0
            for j in i[1:]:
                countries.append(j)
                num += 1

        if i[0].strip() == "2021":
            num = 0
            for j in i[1:]:
                if not (j.strip()=="0"):
                    print(f"{countries[num]}, {j}")
                num += 1