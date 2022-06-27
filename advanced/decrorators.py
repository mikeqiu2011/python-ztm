# decorator

def my_decorator(func):
    def wrap_func(*arg):
        print('wrapping')
        func(*arg)

    return wrap_func


@my_decorator
def hello(msg1, msg2):
    print(msg1, msg2)


hello('hi mike', 'how are you')
