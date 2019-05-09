import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    total = 0

    for row in reader:
        Profit = row[13]
        Items = row[2]
        Revenue = row[11]
        Total_Cost = row[12]
        Unit_Cost = row[10]
        Unit_Price = row[9]
        Unit_Sold = row[8]
        if Items == "Fruits":
            # print(Profit, Items, Revenue)
            total += float(Profit)
    print(total)
