import time


def timeit(iteration):

    def inner(f):

        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret
        return wrapper

    return inner


@timeit(100000)
def double(x):
    return x * 2


"""
Exactly equivalent to:
inner = timeit(100000)
double = inner(double)
"""

double(2)
