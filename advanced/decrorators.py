# decorator pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('before func call')
        func(*args, **kwargs)
        print('after func call')

    return wrap_func


@my_decorator
def hello(msg, emoji=':)'):
    print(msg, emoji)


hello('hi mike')
