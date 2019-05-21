import csv
test_num = "2617471728477380"
print(test_num)


def validate(num: str):
    cut_nums = remove_num(test_num[:15])
    # print(cut_nums)
    reversed_nums = reverse_it(cut_nums)
    # print(reversed_nums)
    list_nums = list(reversed_nums)
    print(list_nums)
    for index in range(len(list_nums)):
         list_nums[index] = int(list_nums[index])
    print(list_nums)


def multiply_odd_digits(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9

    print(validate(test_num))
