from foobar.util import factorial


def test_factorial0():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2


def test_factorial1():
    assert factorial(3) == 6


def test_factorial2():
    assert factorial(4) == 24
    # get one wrong on purpose
    assert factorial(5) == 121
    assert factorial(6) == 720


