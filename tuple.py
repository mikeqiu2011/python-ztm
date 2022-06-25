# tuple is immutable, you cannot reassign item, sort
# tuple is as list, which is immutable after creation, like const
# tuple is faster than list

my_tuple = (1,2,3,4,5,5)
# my_tuple[1] = 'z' # 'tuple' object does not support item assignment

print(my_tuple[1]) # 2
print(5 in my_tuple) # True

new_tuple = my_tuple[1:4]
print(new_tuple) # just like list slicing, (2, 3, 4)

x,y, *other = my_tuple
print(x,y, other) # 1 2 [3, 4, 5]

print(my_tuple.count(5)) # 2

print(my_tuple.index(5)) # 4

print(len(my_tuple)) # 6