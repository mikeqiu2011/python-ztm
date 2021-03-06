from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pets_cap = list(map(lambda x: x.capitalize(), my_pets))
print(my_pets_cap)


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
zip_list = list(zip(my_numbers, my_strings))
zip_list_sorted = sorted(zip_list, key=lambda x: x[0])
print(zip_list_sorted)


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
scores_filtered = list(filter(lambda x: x > 50, scores))
print(scores_filtered)


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

li = my_numbers + scores
result = reduce(lambda acc, num: acc+num, li)
print(result)
