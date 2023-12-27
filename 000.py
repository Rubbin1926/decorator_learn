def double(x):
    return x * 2


def triple(x):
    return x * 3


def calc_number(func, x):  # The function is passed as parameter
    print(func(x))


calc_number(double, 3)
calc_number(triple, 3)
