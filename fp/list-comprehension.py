# list, set or dictionary comprehensions

# my_list = []
# for char in 'hello':
#     my_list.append(char)

my_list = [x+'i' for x in 'hello']
print(my_list)

my_list2 = [num*2 for num in range(100)]
print(my_list2)

my_list3 = [num**2 for num in range(100) if num % 2 == 0]
print(my_list3)
