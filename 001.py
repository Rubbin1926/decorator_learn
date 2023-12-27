def get_multiple_func(n):

    def multiple(x):
        return n * x

    return multiple  # The function is output as the result


double = get_multiple_func(2)
triple = get_multiple_func(3)

print(double(3))
print(triple(3))
