list1 = range(10)


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item)
    return new_list


list2 = list(map(multiply_by2, list1))
print(list2)
