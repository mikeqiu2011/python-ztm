# == checks equality of value, it will convert one to the same type as another
# for below 1st item, it will convert 1 to bool(1), which is True
# however, for better readbility, you shall never compare two different type of value and let
# python do the implicit type conversion for you
# print(True == 1)  # True
# print('' == 1)  # False
# print('1' == 1)  # False
# print([] == 1)  # False
# print(10 == 10.0)  # True*
# print([] == [])  # True*
# print([1,2] == [1,2,3])


# 'is' not check value, instead it checks the reference, whether the memory location is
# the same
print(True is 1)  # False
print('' is 1)  # False
print('1' is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([] is [])  # False,
print([1,2,3] is [1,2,3]) # False


print(True is True)
print('1' is '1')

a = [1,2]
b = [1,2]
print(a is b) # False
print(a == b) # True
b = a
print(a is b) # True
