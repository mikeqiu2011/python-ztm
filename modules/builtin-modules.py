import random
print(random)

# help(random)
# print(dir(random))

print(random.random()) # random float between 0 t0 1

print(random.randint(1, 10)) # random int between 1 to 10

print(random.choice([3,5,8]))

my_list = list(range(10))
random.shuffle(my_list)
print(my_list)
