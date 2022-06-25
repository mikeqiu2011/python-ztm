# set is unordered list of unique items

my_set = {1,2,3,4,5,5}
print(my_set) #{1, 2, 3, 4, 5} - only unique items return

my_set.add(100)
my_set.add(2)
print(my_set) #{1, 2, 3, 4, 5, 100}

# dedup
my_list = [1,2,3,4,5,5]
my_list = list(set(my_list))
print(my_list) # [1, 2, 3, 4, 5]

