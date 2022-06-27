# decorator pattern
from time import time


def performance(fn):
    def wrap_func(*args, **kvargs):
        start = time()
        result = fn(*args, **kvargs)
        print(f'it takes {time()-start} to run the code')

        return result

    return wrap_func


@performance
def long_job():
    for i in range(10000000):
        i*5


long_job()
