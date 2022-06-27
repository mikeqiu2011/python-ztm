# decorator

def my_decorator(func):
    def wrap_func():
        print('wrapping')
        func()

    return wrap_func


@my_decorator
def hello():
    print('hello')


hello()
