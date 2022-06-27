# decorator

def my_decorator(func):
    def wrap_func():
        print('wrapping')
        func()

    return wrap_func


# @my_decorator
def hello():
    print('hello')


# hello()

# underneth the hood:
a = my_decorator(hello)
a()
