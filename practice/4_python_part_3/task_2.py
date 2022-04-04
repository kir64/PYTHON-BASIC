"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math


def math_calculate(function: str, *args):
    if len(args) > 2:
        raise AttributeError
    try:
        fun = getattr(math, function)
    except AttributeError:
        return 'OperationNotFoundException'
    return fun(*args)

"""
Write tests for math_calculate function
"""

def test_math_calculate_1():
    assert math_calculate('log', 1024, 2) == 10.0


def test_math_calculate_2():
    assert math_calculate('ceil', 10.7) == 11


def test_math_calculate_3(capfd):
    print(math_calculate('cel', 10, 7))
    out, err = capfd.readouterr()
    assert out == 'OperationNotFoundException\n'
