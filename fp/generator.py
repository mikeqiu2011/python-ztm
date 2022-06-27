# list is in memory, it takes the whole space

def make_list(num):
    result = []

    for i in range(num):
        result.append(i*2)

    return result


my_list = make_list(100)
print(my_list)


# range() is a generator, which gives you one by one
# if you need a huge list, the list must be first created in memory as a whole before you can use it, which is not efficient
