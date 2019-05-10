import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    total = 0

    for row in reader:
        Profit = row[13]
        Revenue = row[11]
        Total_Cost = row[12]
        Unit_Cost = row[10]
        Unit_Price = row[9]
        Unit_Sold = row[8]
        Items = row[2]
        if Items == "Fruits":
            total += float(Profit)
        if Items == "Clothes":
            total += float(Profit)
        if Items == "Meat":
            total += float(Profit)
    print(total)
