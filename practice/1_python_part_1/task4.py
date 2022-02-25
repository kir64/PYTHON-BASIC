"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""

def calculate_power_with_difference(lst):
    ans, sub = [], 0
    for i in range(len(lst)):
        ans.append(lst[i] ** 2 - sub)
        sub = ans[i] - lst[i]
    return ans


print(calculate_power_with_difference([1, 2, 3]))  # [1, 4, 7]
