list1 = list(range(10))


def multiply_by2(x):
    return x*2


# map will take each item in the iterable to be processed by the func and return
list2 = list(map(multiply_by2, list1))
print(list2)
print(list1)  # no change to original list
