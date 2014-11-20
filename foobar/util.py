import functools


def factorial(k):
    """Returns the factorial of a number.
    """
    return functools.reduce(int.__mul__, xrange(1, k + 1), 1)


def foo(x):
    "This is supposed to be untested to show our coverage testing works."
    return x+1

