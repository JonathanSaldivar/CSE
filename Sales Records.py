import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    Profit_For_Fruit = []
    Profit_For_Meat = []
    Profit_For_Clothes = []
    Profit_For_Beverages =[]
    reader = csv.reader(csv_file_thing)
    for row in reader:
        Profit = row[13]
        Items = row[2]
        if Items == "Fruits":
            Profit_For_Fruit.append(float(Profit))
        if Items == "Meat":
            Profit_For_Meat.append(float(Profit))
        if Items == "Clothes":
            Profit_For_Clothes.append(float(Profit))
        if Items == "Beverages":
            Profit_For_Beverages.append(float(Profit))
Fruits_Total = sum(Profit_For_Fruit)
Meat_Total = sum(Profit_For_Meat)
Clothes_Total = sum(Profit_For_Clothes)
Beverages_Total = sum(Profit_For_Beverages)
print("Total profit for fruits is %f" % Fruits_Total)
print("Total profit for meat is %f" % Meat_Total)
print("Total profit for clothes is %f" % Clothes_Total)
print("Total profit for beverages is %f" % Beverages_Total)
