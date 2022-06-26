# ok if one of the iterable is a tuple,as long as it is iterable
my_list = (1, 2, 3, 4)
your_list = {10, 20, 30}  # set is also fine
his_list = ['a', 'b', ]  # result will be based on the shortest one

# zip will zip different items together as individual tuple
zipped_list = list(zip(my_list, your_list, his_list))
print(zipped_list)  # [(1, 10, 'a'), (2, 20, 'b')]
