import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    # Profit For Items
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
    # Profit For Regions
    Profit_For_Sub_SaharanAfrica = []
    Profit_For_Middle_East_and_North_Africa = []
    Profit_For_Europe = []
    Profit_For_Asia = []
    Profit_For_Australia_and_Oceania = []
    Profit_For_Central_America_and_the_Caribbean = []
    Profit_For_North_America = []
    # Units sold
    Units_Sold_For_Fruit = []
    Units_Sold_For_Meat = []
    Units_Sold_For_Clothes = []
    Units_Sold_For_Beverages = []
    Units_Sold_For_OfficeSupplies = []
    Units_Sold_For_Cosmetics = []
    Units_Sold_For_Snacks = []
    Units_Sold_For_PersonalCare = []
    Units_Sold_For_Household = []
    Units_units_Sold_For_Vegetables = []
    Units_Sold_For_BabyFood = []
    Units_Sold_For_Cereal = []

    reader = csv.reader(csv_file_thing)
    for row in reader:
        Profit = row[13]
        Items = row[2]
        Region = row[0]
        Units_Sold = row[8]
        if Items == "Fruits":
            Profit_For_Fruit.append(float(Profit))
            Units_Sold_For_Fruit += int(Units_Sold)
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
        if Region == "Sub-Saharan Africa":
            Profit_For_Sub_SaharanAfrica.append(float(Profit))
        if Region == "Australia and Oceania":
            Profit_For_Australia_and_Oceania.append(float(Profit))
        if Region == "Middle East and North Africa":
            Profit_For_Middle_East_and_North_Africa.append(float(Profit))
        if Region == "Europe":
            Profit_For_Europe.append(float(Profit))
        if Region == "Asia":
            Profit_For_Asia.append(float(Profit))
        if Region == "Central America and the Caribbean":
            Profit_For_Central_America_and_the_Caribbean.append(float(Profit))
        if Region == "North America":
            Profit_For_North_America.append(float(Profit))
# Items
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
# Units Sold
Profit_Sold_For_Fruit_Average = Profit_For_Fruit
# Regions
Sub_SaharanAfrica_Total = sum(Profit_For_Sub_SaharanAfrica)
Middle_East_and_North_Africa_Total = sum(Profit_For_Middle_East_and_North_Africa)
Australia_and_Oceania_Total = sum(Profit_For_Australia_and_Oceania)
Europe_Total = sum(Profit_For_Europe)
Asia_Total = sum(Profit_For_Asia)
Central_America_and_the_Caribbean_Total = sum(Profit_For_Central_America_and_the_Caribbean)
North_America_Total = sum(Profit_For_North_America)
# Items
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
# regions
print()
print("Total profit for sub-saharan africa is %f" % Sub_SaharanAfrica_Total)
print("Total profit for middle east and north africa is %f" % Middle_East_and_North_Africa_Total)
print("Total profit for australia and oceania is %f" % Australia_and_Oceania_Total)
print("Total profit for europe is %f" % Europe_Total)
print("Total profit for asia is %f" % Asia_Total)
print("Total profit for central america and the caribbean is %f" % Central_America_and_the_Caribbean_Total)
print("Total profit for north america is %f" % North_America_Total)

item_sum = [Profit_For_Fruit, Profit_For_Meat, Profit_For_Clothes, Profit_For_Beverages, Profit_For_OfficeSupplies,
            Profit_For_Cosmetics, Profit_For_Snacks, Profit_For_PersonalCare, Profit_For_Household,
            Profit_For_Vegetables, Profit_For_BabyFood,  Profit_For_Cereal]

item_type = ["fruits", "meat", "clothes", "beverages", "office supplies", "cosmetics", "snacks", "personal care",
             "household", "vegetables", "baby food", "cereal"]

item_index = item_sum.index(max(item_sum))
print()
print("The item with the highest profit is %s" % item_type[item_index])

region_sum = [Sub_SaharanAfrica_Total, Middle_East_and_North_Africa_Total,
              Australia_and_Oceania_Total, Europe_Total, Asia_Total,
              Central_America_and_the_Caribbean_Total, North_America_Total]

region_type = ["sub-saharan africa", "middle east and north africa", "australia and oceania", "europe", "asia",
               "central america and the caribbean", "north america"]

region_index = region_sum.index(max(region_sum))
print()
print("The region with the highest profit is %s" % region_type[region_index])
