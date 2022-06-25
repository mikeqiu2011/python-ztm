# Scope - what variables do i have access to

total = 100 # global scope

print(total)

def some_func():
    total2 = 10
    print(total) # function can access global variable

#print(total2) # cannot access function scope

some_func()


# block scope

if True:
    x = 10

print(x) # 10, can access block scope