def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

def my_res(x, y):
    """A function that multiply. """
    return x-y
    
def numeros_fibonacci(n):
    fibs = []
    a, b = 0, 1
    while a < n:
        fibs.append(a)
        a, b = b, a+b
    return fibs
