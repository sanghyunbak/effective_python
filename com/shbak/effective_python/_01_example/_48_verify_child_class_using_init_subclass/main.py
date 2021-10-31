# meta class
import json

from termcolor import colored

# class Meta(type):
#     def __new__(meta, name, bases, class_dict):
#         print(colored(f'* execution: {name}\'s meta {meta}.__new__', 'green'))
#         print(colored(f'base classes: {bases}', 'green'))
#         print(colored(f'class_dict : {class_dict}', 'green'))
#         return type.__new__(meta, name, bases, class_dict)
#
#
# class MyClass(metaclass=Meta):
#     stuff = 123
#
#     def foo(self):
#         pass
#
#
# class MySubclass(MyClass):
#     other = 567
#
#     def bar(self):
#         pass
from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


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


class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9


def assert_functions_about_polygon():
    assert Rectangle.interior_angles() == 360
    assert Triangle.interior_angles() == 180
    assert Nonagon.interior_angles() == 1260


class BetterPolygon:
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('Polygon needs more than 3 sides')

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Hexagon(BetterPolygon):
    sides = 6


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class BetterSerializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        # dump and dumps are different
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self):
        name = self.__class__.__name__
        args_str = ', '.join(str(x) for x in self.args)
        return f'{name}({args_str})'


class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


@trace_func
def run_serialize():
    before = Vector3D(10, -7, 3)
    data = before.serialize()
    print(colored(f'serialized value : {data}', 'green'))
    print(colored(f'deserialize: {deserialize(data)}', 'green'))


class BetterRegisteredSerializable(BetterSerializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)


class Vector1D(BetterRegisteredSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude


def run_vector_1d():
    before = Vector1D(6)
    print(colored(f'[Before]: {before}', 'green'))
    data = before.serialize()
    print(colored(f'[serialized]: {data}', 'green'))
    print(colored(f'[After]: {deserialize(data)}', 'green'))


if __name__ == '__main__':
    print('hahah')
    assert_functions_about_polygon()
    assert Hexagon.interior_angles() == 720
    run_serialize()
    run_vector_1d()
