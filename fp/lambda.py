# lambda expresion, anounomous function which run only onece

my_list = range(10)

new_list = list(map(lambda x: x*2, my_list))

print(new_list)

squared_list = list(map(lambda x: x**2, my_list))
print(squared_list)

li = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_li = sorted(li, key=lambda x: x[1])
print(sorted_li)  # [(10, -1), (0, 2), (4, 3), (9, 9)]
