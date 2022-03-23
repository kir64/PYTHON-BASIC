"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import random
import string
import tempfile


def task_read_write_2(file1_name, file2_name):
    def generate_words(n=20):
        words = list()
        for _ in range(n):
            word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
            words.append(word)

        return words

    lst = generate_words()
    with open(file1_name, 'w', encoding='UTF-8') as f1:
        print(*lst, sep='\n', file=f1)
    with open(file2_name, 'w', encoding='CP1252') as f2:
        print(*reversed(lst), sep=',', file=f2)


def test_task_read_write_2():
    tmp_file = tempfile.NamedTemporaryFile()
    task_read_write_2(tmp_file.name, 'file2.txt')

    with open(tmp_file.name, 'r') as rf:
        txt_to_check = rf.read()
    with open('file2.txt', 'r') as rf:
        res_txt = rf.read()

    txt_to_check = ','.join(txt_to_check.strip().split('\n')[::-1])
    assert res_txt.strip() == txt_to_check


test_task_read_write_2()
