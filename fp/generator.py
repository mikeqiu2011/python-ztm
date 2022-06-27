# range() is a generator, which gives you one by one
# if you need a huge list, the list must be first created in memory as a whole before you can use it, which is not efficient

def generator_function(num):
    for i in range(num):
        yield i * 2  # the yield pause the function


g = generator_function(3)
print(g)  # generator object
print(next(g))  # 2
print(next(g))  # 4
print(next(g))  # 6
print(next(g))  # 8
