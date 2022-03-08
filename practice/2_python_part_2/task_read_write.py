"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""

import os

folder_path = '/Users/klatanov/PYTHON-BASIC/practice/2_python_part_2/files'
folder = sorted(os.listdir(folder_path))
ans_lst = []
for file in folder:
    file_path = folder_path + '/' + file
    with open(file_path, 'r') as rf:
        value = rf.read()
        ans_lst.append(value)
with open('result.txt', 'w') as wf:
    print(', '.join(ans_lst), file=wf)
