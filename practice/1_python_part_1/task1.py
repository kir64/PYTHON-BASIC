"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
def delete_from_list(lst, x):
    i, n = 0, len(lst)
    while x in lst:
        i = lst.index(x, i, n)
        lst.pop(i)
    return lst


print(delete_from_list([1, 2, 3, 4, 3], 3))  # [1, 2, 4]
print(delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b'))  # ['a', 'c', 'd']
print(delete_from_list([1, 2, 3], 'b'))  # [1, 2, 3]
print(delete_from_list([], 'b'))  # []
