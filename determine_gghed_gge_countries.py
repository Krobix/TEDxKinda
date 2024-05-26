#Determine which countries in GHED_data.csv have gghed_gge data
import csv

with open("GHED_data.csv", "r") as f:
    reader = csv.DictReader(f)

    for i in reader:
        gghed_gge = i["gghed_gge"]
        gghed_gge = gghed_gge.strip()

        if not (gghed_gge==""):
            print(f"{i["country"]}, {i["year"]}, {i["gghed_gge"]}")