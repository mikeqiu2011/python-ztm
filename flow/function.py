# # def say_hello(name, emoji):
# #     print(f'hello {name} {emoji}')
# #
# # say_hello('mike', ':)') # position argument
# #
# # say_hello(':)', 'mike') # not working
# #
# # say_hello(emoji=':)', name='mike') # keyword argument, tell function explicitly
# #
# # say_hello(name='mike', emoji=':)') # good practice, follow the definition order
# #
# # # default parameter, increase the readbility and usability of your program
# # def say_hello2(name='kevin', emoji=':-|'):
# #     print(f'hello {name} {emoji}')
# #
# # say_hello2() # hello kevin :-|
# # say_hello2('mike') # hello mike :-|
# # say_hello2('mike', ':)') # hello mike :)
# # say_hello2(emoji=':)') # hello kevin :)
#
#
# # a function shall do one thing really well
# # should return something
#
# def sum(num1, num2):
#     return num1 + num2
#
# total = sum(10,5)
# print(total)
#
# def sum2(num1, num2):
#     '''
#     calculate the sum of the given two values
#     :param num1: first numer
#     :param num2: second number
#     :return: the sum of the two values
#     '''
#     def another_func(n1, n2):
#         print(f'calling from sub-func: {num1}') # sub-func can access parent's parameter
#         return n1 + n2
#
#     return another_func(num1, num2)
#
# print(sum2(10,10))
#
# help(sum2)
#
# print(sum2.__doc__)

# clean code
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(50))

# *agrs **kwargs
def super_func(*args):
    print(*args)  # 1 2 3
    print(args) # (1, 2, 3), this gives us a tuple we can iterate on
    return sum(args) # 6


print(super_func(1, 2, 3))