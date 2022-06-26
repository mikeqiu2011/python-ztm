list1 = range(10)


def is_even(num):
    return num % 2 == 0


# map always return the same number of item of original one, while filter normally return less than the origin
list2 = list(filter(lambda x: x % 2 == 0, list1))

print(list2)  # [0, 2, 4, 6, 8]
