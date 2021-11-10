from typing import TypeVar, Callable, List

Value =TypeVar('Value')
Func = Callable[[Value, Value], Value]


def combine(func: Func[Value], values: List[Value]) -> Value:
    assert len(values) > 0

    result = values[0]
    for next_value in values[1:]:
        result = func(result, next_value)

    return result

Real = TypeVar('Real', int , float)

def add(x: Real, y: Real) -> Real:
    return x + y

inputs = [1, 2, 3, 4j]  #oops!
result = combine(add, inputs)
assert result == 10