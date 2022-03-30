"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

from datetime import *
import pytest


class Homework:
    def __init__(self, text,  days_left):
        self.text = text
        self.days_left = days_left
        self.created = datetime.now()
        self.deadline = timedelta(days=days_left)

    def is_active(self):
        return datetime.now() < self.created + self.deadline


class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Teacher(Human):
    @staticmethod
    def create_homework(task, days_to_complete):
        return Homework(task, days_to_complete)


class Student(Human):
    @staticmethod
    def do_homework(homework):
        if homework.is_active():
            return homework
        print('You are late')
        return None


@pytest.fixture()
def homework_test1():
    return Homework('Learn functions', 0)


@pytest.fixture()
def homework_test2():
    return Homework('OOP', 5)


@pytest.fixture()
def teacher():
    return Teacher('Dmitry', 'Orlyakov')


@pytest.fixture()
def student():
    return Student('Vladislav', 'Popov')


def test_teacher_name(teacher):
    assert teacher.first_name == 'Dmitry' and teacher.last_name == 'Orlyakov'


def test_teacher_create_homework_test1(homework_test1):
    assert homework_test1.text == 'Learn functions' and homework_test1.days_left == 0


def test_teacher_create_homework_test2(homework_test2):
    assert homework_test2.text == 'OOP' and homework_test2.days_left == 5


def test_student_name(student):
    assert student.first_name == 'Vladislav' and student.last_name == 'Popov'


def test_student_do_homework_test1(capfd, homework_test1, student):
    student.do_homework(homework_test1)
    out, err = capfd.readouterr()
    assert out == "You are late\n"


def test_student_do_homework_test2(homework_test2, student):
    student.do_homework(homework_test2)


def test_homework_is_active_test1(homework_test1):
    assert homework_test1.is_active() == False


def test_homework_is_active_test2(homework_test2):
    assert homework_test2.is_active() == True
