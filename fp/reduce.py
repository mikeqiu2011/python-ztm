from functools import reduce

my_list = [1, 2, 3]


def accumulator(num1, num2):
    return num1 + num2


result = reduce(accumulator, my_list, 5)
print(result)  # 11 now, as the initial now is 5
