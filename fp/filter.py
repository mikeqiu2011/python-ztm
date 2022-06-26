list1 = range(10)


def is_even(num):
    return num % 2 == 0


list2 = list(filter(is_even, list1))

print(list2)  # [0, 2, 4, 6, 8]
