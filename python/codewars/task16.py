def high_and_low(numbers):
    num_list = numbers.split()
    numlist = []
    for i in num_list:
        numlist.append(int(i))
    result = f'{max(numlist)}, {min(numlist)}'
    return result


print(high_and_low("1 2 3 4 2 3 2"))
