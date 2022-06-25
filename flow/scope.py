# # Scope - what variables do i have access to
#
# total = 100 # global scope
#
# print(total)
#
# def some_func():
#     total2 = 10
#     print(total) # function can access global variable
#
# #print(total2) # cannot access function scope
#
# some_func()
#
#
# # block scope
#
# if True:
#     x = 10
#
# print(x) # 10, can access block scope

# Scope rule:
#1 start with local(e.g. create a same name variable if has assignment)
#2 - Parent local?
#3 - global
#4 - built-in python functions


a = 1
def confusion():
    a = 5   # the function creates a new local variable a
    return a

print(a) # 1
print(confusion()) # 5
print(a) # 1