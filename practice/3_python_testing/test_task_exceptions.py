"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

class DivisionByOneException(ArithmeticError):
    pass


def division(x, y):
    try:
        if y == 1:
            raise DivisionByOneException('Deletion on 1 get the same result')  
            # "Division", not "Deletion" task should be fixed. 
        return x // y
    except ZeroDivisionError:
        print('Division by 0')
        return None
    except DivisionByOneException as err:
        print(f'DivisionByOneException("{err}")')
        return None
    finally:
        print('Division finished')


def test_division_ok(capfd):
    ans = division(32, 4)
    out, err = capfd.readouterr()
    assert out == 'Division finished\n'
    assert ans == 8


def test_division_by_zero(capfd):
    division(32, 0)
    out, err = capfd.readouterr()
    assert out == 'Division by 0\nDivision finished\n'


def test_division_by_one(capfd):
    division(32, 1)
    out, err = capfd.readouterr()
    assert out == 'DivisionByOneException("Deletion on 1 get the same result")\nDivision finished\n'
