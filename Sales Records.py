import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    read = csv.reader(csv_file_thing)
    