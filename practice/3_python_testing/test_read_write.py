"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import os
import tempfile
import random


def task_read_write(folder_path):
    folder = sorted(os.listdir(folder_path))
    ans_lst = []
    for file in folder:
        file_path = folder_path + '/' + file
        with open(file_path, 'r') as rf:
            value = rf.read()
            ans_lst.append(value)
    with open('result.txt', 'w') as wf:
        print(', '.join(ans_lst), file=wf)


def test_task_read_write():
    test_files_num = 5
    num_rand_lim = 100
    tmp_dir = tempfile.TemporaryDirectory()
    dir_path = os.path.abspath(tmp_dir.name)
    lst = [None] * test_files_num
    content_lst = [random.randrange(num_rand_lim) for i in range(test_files_num)]

    with tmp_dir:
        for i in range(test_files_num):
            lst[i] = tempfile.NamedTemporaryFile(dir=tmp_dir.name, mode='w+t')
        lst.sort(key=lambda x: x.name)

        for i in range(test_files_num):
            lst[i].write(str(content_lst[i]))
            lst[i].seek(0)
            lst[i].read()

        task_read_write(dir_path)
        [lst[i].close() for i in range(test_files_num)]

    with open('result.txt', 'r') as rf:
        res_content = rf.read()

    assert ', '.join(map(str, content_lst)) == res_content


test_task_read_write()
