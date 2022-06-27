# generator real demo
# it is especially useful for large ammound of data
from time import time


def performance(fn):
    def wrap_func(*args, **kvargs):
        start = time()
        result = fn(*args, **kvargs)
        print(f'it takes {time()-start} to run the code')

        return result

    return wrap_func


@performance
def long_job(num):
    for i in range(num):
        i*5


@performance
def long_job2(num):
    for i in list(range(num)):
        i*5


num = 100000000
long_job(num)  # 9 seconds
long_job2(num)  # 40 seconds!!
