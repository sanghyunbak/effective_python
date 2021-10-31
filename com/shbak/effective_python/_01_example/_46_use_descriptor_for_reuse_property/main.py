# property's cons is non-reusable
from weakref import WeakKeyDictionary

from termcolor import colored


class CheckClassMethod:
    # self is current instance, not class
    value = 'initial'

    def __init__(self):
        self._message = 'initial'
        # self.value = 'initial2'

    @classmethod
    def change_value(cls, value):
        cls._message = value
        cls.value = value

    @classmethod
    def get_value(cls):
        return cls.value

    @property
    def message(self):
        return self._message


def debug_check_class_method():
    obj1 = CheckClassMethod()
    obj2 = CheckClassMethod()
    obj3 = CheckClassMethod()

    print(colored(f'obj1.message : {obj1.message}', 'green'))
    print(colored(f'obj2.message : {obj2.message}', 'green'))
    print(colored(f'obj3.message : {obj3.message}', 'green'))

    print(colored(f'obj1.value : {obj1.get_value()}', 'green'))
    print(colored(f'obj2.value : {obj2.get_value()}', 'green'))
    print(colored(f'obj3.value : {obj3.get_value()}', 'green'))

    print(colored(f'===========================', 'yellow'))
    print(colored(f'change value to "final" use classmethod', 'yellow'))
    CheckClassMethod.change_value('final')
    obj1.change_value('changed in obj1')
    # change_value method change both value, message variables

    print(colored(f'obj1.message : {obj1.message}', 'green'))
    print(colored(f'obj2.message : {obj2.message}', 'green'))
    print(colored(f'obj3.message : {obj3.message}', 'green'))
    print(colored(f'CheckClassMethod.message : {CheckClassMethod._message}', 'green'))

    print(colored(f'obj1.value : {obj1.get_value()}', 'green'))
    print(colored(f'obj2.value : {obj2.get_value()}', 'green'))
    print(colored(f'obj3.value : {obj3.get_value()}', 'green'))
    print(colored(f'CheckClassMethod.value : {CheckClassMethod.get_value()}', 'green'))


class Exam:
    # all attribut needed to call _check_grade function to validate
    def __init__(self):
        self._writting_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Your score is 0 ~ 100')

    @property
    def writting_grade(self):
        return self._writting_grade

    @writting_grade.setter
    def writting_grade(self, value):
        self._check_grade(value)
        self._writting_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


class Grade:
    def __init__(self):
        # self._values = {}
        self._values = WeakKeyDictionary() # it protect memory leak

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Score must be between 0 to 100')

        self._values[instance] = value


class ExamNew:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


def run_exam_new():
    first_exam = ExamNew()
    first_exam.writing_grade = 92
    first_exam.science_grade = 99
    print(colored(f'writing: {first_exam.writing_grade}', 'green'))
    print(colored(f'science: {first_exam.science_grade}', 'green'))

    second_exam = ExamNew()
    second_exam.writing_grade = 75
    print(colored(f'[first] wring: {first_exam.writing_grade}', 'green'))
    print(colored(f'[second] wring: {second_exam.writing_grade}', 'green'))

if __name__ == '__main__':
    debug_check_class_method()
    run_exam_new()