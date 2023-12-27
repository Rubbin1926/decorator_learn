# Decorator itself is a callable
# Decorator is a function whose input and output are often both functions (Input must be func, output not)
def dec(f):
    pass


@dec
def double(x):
    return x * 2


"""
Exactly equivalent to:
double = dec(double)
"""