import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    for row in reader:
        Profit = row[13]
        Fruit = row[2]
        if Fruit == "":

            print(Profit, Fruit)
