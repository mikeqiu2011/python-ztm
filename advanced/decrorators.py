# decorator

def my_decorator(func):
    def wrap_func(msg):
        print('wrapping')
        func(msg)

    return wrap_func


@my_decorator
def hello(msg):
    print(msg)


hello('hi mike')
