import time


def timeit(f):

    def wrapper(x):
        start = time.time()
        ret = f(x)
        print(time.time() - start)
        return ret

    return wrapper


@timeit
def my_func(x):
    time.sleep(x)


@timeit
def other_func(x):
    return x * 2

my_func(1)
print(other_func(2))
