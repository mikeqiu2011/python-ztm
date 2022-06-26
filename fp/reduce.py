from functools import reduce

my_list = [1, 2, 3]


def accumulator(num1, num2):
    return num1 + num2


result = reduce(accumulator, my_list)
print(result)  # 6
