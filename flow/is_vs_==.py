# == checks equality of value, it will convert one to the same type as another
# for below 1st item, it will convert 1 to bool(1), which is True
# however, for better readbility, you shall never compare two different type of value and let
# python do the implicit type conversion for you
print(True == 1)  # True
print('' == 1)  # False
print('1' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True*
print([] == [])  # True*
print([1,2] == [1,2,3])
