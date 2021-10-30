from collections import namedtuple, defaultdict

from termcolor import colored

Grade = namedtuple('Grade', ('score', 'weight'))


class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

    def print_grades(self, name):
        for _, grade in enumerate(self._grades[name]):
            print(colored(f'grade : {grade}', 'green'))


def print_simpleGradeBook():
    book = SimpleGradebook()
    book.add_student('Issac Newton')
    book.report_grade('Issac Newton', 90)
    book.report_grade('Issac Newton', 95)
    book.report_grade('Issac Newton', 85)
    book.print_grades('Issac Newton')


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


def use_classes():
    book = Gradebook()
    albert = book.get_student('albert einstein')
    math = albert.get_subject('math')
    math.report_grade(75, 0.05)
    math.report_grade(65, 0.15)
    math.report_grade(70, 0.80)
    gym = albert.get_subject('Gym')
    gym.report_grade(100, 0.40)
    gym.report_grade(85, 0.60)
    print(albert.average_grade())


if __name__ == '__main__':
    print_simpleGradeBook()
    use_classes()
