# tuple is immutable, you cannot reassign item, sort
# tuple is as list, which is immutable after creation, like const
# tuple is faster than list

my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z' # 'tuple' object does not support item assignment

print(my_tuple[1]) # 2

print(5 in my_tuple) # True