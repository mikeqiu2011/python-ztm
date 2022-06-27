def hello():
    print('hellooo')


greet = hello
del hello
# hello() not working

greet()  # still works
