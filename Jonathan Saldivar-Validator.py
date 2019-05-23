import csv
test_num = "2617471728477380"


def validate(num: str):
    if len(num) is not 16:
        print("Doesn't Work")
        return False
    last_num = int(num[15])
    list_nums = list(num)[:15][::-1]
    print(list_nums)
    for index in range(len(list_nums)):
        list_nums[index] = int(list_nums[index])
        if index % 2 == 0:
            list_nums[index] *= 2
            if list_nums[index] > 9:
                list_nums[index] -= 9
    total = sum(list_nums)
    return total % 10 == last_num


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile,csv", 'w', newline='') as new_csv:
        print("Writing File...")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)

print(validate(test_num))
