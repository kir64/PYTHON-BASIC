"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""

def get_min_max(filename):
    with open(filename) as opened_file:
        num_lst = [int(line) for line in opened_file]
    return min(num_lst), max(num_lst)


print(get_min_max('input.txt'))  #(-2, 34)
