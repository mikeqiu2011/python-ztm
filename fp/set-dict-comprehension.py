# set comprehension

# my_list = {char for char in 'hello'}
# print(my_list)

# my_list2 = {num for num in range(10)}
# print(my_list2)

# dictionary comprehension

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k+'i': v**2 for k,
           v in simple_dict.items() if v % 2 == 0}
print(my_dict)  # {'bi': 4}

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)
