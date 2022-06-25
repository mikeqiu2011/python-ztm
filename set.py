# # set is unordered list of unique items
#
# my_set = {1,2,3,4,5,5}
# print(my_set) #{1, 2, 3, 4, 5} - only unique items return
#
# my_set.add(100)
# my_set.add(2)
# print(my_set) #{1, 2, 3, 4, 5, 100}
#
# # dedup
# my_list = [1,2,3,4,5,5]
# my_list = list(set(my_list))
# print(my_list) # [1, 2, 3, 4, 5]
#
# # access set item
# # print(my_set[0]) # 'set' object is not subscriptable
#
# print(1 in my_set) # True
# print(len(my_set)) # 6
#
# new_set = my_set.copy()
# my_set.clear()
# print(my_set) # set()
# print(new_set) # {1, 2, 3, 4, 5, 100}

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set)) # {1, 2, 3} - duplicates get ignored
# print(my_set) # {1, 2, 3, 4, 5} - original one not updated
# my_set.discard(5)
# print(my_set) # {1, 2, 3, 4}

# my_set.difference_update(your_set)
# print(my_set) # {1, 2, 3} - original one get updated

# print(my_set.intersection(your_set)) # {4, 5}
# print(my_set.isdisjoint(your_set)) # False, return true if nothing in common

print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, union together but remove duplicates
print(my_set | your_set) # same result

