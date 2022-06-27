# range() is a generator, which gives you one by one
# if you need a huge list, the list must be first created in memory as a whole before you can use it, which is not efficient

def generator_function(num):
    for i in range(num):
        yield i  # instead returning, generator yield


for item in generator_function(1000):
    print(item)
