"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import *


def calculate_days(custom_date='2021-12-24'):
    try:
        custom_date = datetime.strptime(custom_date, '%Y-%m-%d').date()
        cur_date = date.today()
        return cur_date.toordinal() - custom_date.toordinal()
    except ValueError:
        return 'WrongFormatExpression'


print(calculate_days('2021-10-07'))  # for this example today is 6 october 2021
# -1
print(calculate_days('2021-10-05'))
# 1
print(calculate_days('10-07-2021'))
# WrongFormatException
print(calculate_days())
# 77
print(calculate_days('2022-04-01'))
# -21



"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
