import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    Profit_For_Fruit = []
    Profit_For_Meat = []
    Profit_For_Clothes = []
    Profit_For_Beverages = []
    Profit_For_OfficeSupplies = []
    Profit_For_Cosmetics = []
    Profit_For_Snacks = []
    Profit_For_PersonalCare = []
    Profit_For_Household = []
    Profit_For_Vegetables = []
    Profit_For_BabyFood = []
    Profit_For_Cereal = []
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
        if Items == "Office Supplies":
            Profit_For_OfficeSupplies.append(float(Profit))
        if Items == "Cosmetics":
            Profit_For_Cosmetics.append(float(Profit))
        if Items == "Snacks":
            Profit_For_Snacks.append(float(Profit))
        if Items == "Personal Care":
            Profit_For_PersonalCare.append(float(Profit))
        if Items == "Household":
            Profit_For_Household.append(float(Profit))
        if Items == "Vegetables":
            Profit_For_Vegetables.append(float(Profit))
        if Items == "Baby Food":
            Profit_For_BabyFood.append(float(Profit))
        if Items == "Cereal":
            Profit_For_Cereal.append(float(Profit))

Fruits_Total = sum(Profit_For_Fruit)
Meat_Total = sum(Profit_For_Meat)
Clothes_Total = sum(Profit_For_Clothes)
Beverages_Total = sum(Profit_For_Beverages)
OfficeSupplies_Total = sum(Profit_For_OfficeSupplies)
Cosmetics_Total = sum(Profit_For_Cosmetics)
Snacks_Total = sum(Profit_For_Snacks)
PersonalCare_Total = sum(Profit_For_PersonalCare)
Household_Total = sum(Profit_For_Household)
Vegetables_Total = sum(Profit_For_Vegetables)
BabyFood_Total = sum(Profit_For_BabyFood)
Cereal_Total = sum(Profit_For_Cereal)

print("Total profit for fruits is %f" % Fruits_Total)
print("Total profit for meat is %f" % Meat_Total)
print("Total profit for clothes is %f" % Clothes_Total)
print("Total profit for beverages is %f" % Beverages_Total)
print("Total profit for office supplies is %f" % OfficeSupplies_Total)
print("Total profit for cosmetics is %f" % Cosmetics_Total)
print("Total profit for snacks is %f" % Snacks_Total)
print("Total profit for personal care is %f" % PersonalCare_Total)
print("Total profit for household is %f" % Household_Total)
print("Total profit for vegetables is %f" % Vegetables_Total)
print("Total profit for baby food is %f" % BabyFood_Total)
print("Total profit for cereal is %f" % Cereal_Total)

list_sum = [Profit_For_Fruit, Profit_For_Meat, Profit_For_Clothes, Profit_For_Beverages, Profit_For_OfficeSupplies,
            Profit_For_Cosmetics, Profit_For_Snacks, Profit_For_PersonalCare, Profit_For_Household,
            Profit_For_Vegetables, Profit_For_BabyFood,  Profit_For_Cereal]

list_type = ["fruits", "meat", "clothes", "beverages", "office supplies", "cosmetics", "snacks", "persmoal care", ]
