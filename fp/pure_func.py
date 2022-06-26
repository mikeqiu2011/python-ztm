def multiply_by2(li):
    new_list = []  # will not affect the outside world
    for item in li:
        new_list.append(item)

    return new_list


my_list = [1, 2, 3]

# same result no matter how many times you run
print(multiply_by2(my_list))  # [1, 2, 3]
print(multiply_by2(my_list))  # [1, 2, 3]
