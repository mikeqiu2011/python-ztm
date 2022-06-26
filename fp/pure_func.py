new_list = []


def multiply_by2(li):
    for item in li:
        new_list.append(item)

    return new_list


my_list = [1, 2, 3]
print(multiply_by2(my_list))  # [1, 2, 3]
print(multiply_by2(my_list))  # [1, 2, 3, 1, 2, 3]
