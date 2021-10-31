# meta class
from termcolor import colored


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(colored(f'* execution: {name}\'s meta {meta}.__new__', 'green'))
        print(colored(f'base classes: {bases}', 'green'))
        print(colored(f'class_dict : {class_dict}', 'green'))
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass


class ValidatePolygon(type):
    def __new__(mcs, name, bases, class_dict):
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('Polygon needs More than 3 sides')
            return type.__new__(mcs, name, bases, class_dict)


class Polygon(metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


# class Triangle(Polygon):
#     sides = 3
#
#
# class Rectangle(Polygon):
#     sides = 4
#
#
# class Nonagon(Polygon):
#     sides = 9
#
#
# def assert_functions_about_polygon():
#     assert Rectangle.interior_angles() == 360
#     assert Triangle.interior_angles() == 180
#     assert Nonagon.interior_angles() == 1260


class BetterPolygon:
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('Polygon needs more than 3 sides')

    @classmethod
    def interior_angles(cls):
        return (cls.sides -2) * 180

class Hexagon(BetterPolygon):
    sides = 6

if __name__ == '__main__':
    print('hahah')
    # assert_functions_about_polygon()
    assert Hexagon.interior_angles() == 720
