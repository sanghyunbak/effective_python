# object hook
from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


class LazyRecord:
    def __init__(self):
        self.exists = 5

    @trace_func
    def __getattr__(self, name):
        value = f'{name} value'  # set default value
        setattr(self, name, value)
        return value


class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(colored(f'call: __getattr__({name!r}),'
                      f'fill instance\'s dictionary'))
        result = super().__getattr__(name)
        print(colored(f'return: {result!r}', 'magenta'))
        return result


@trace_func
def do_logging_lazy():
    data = LoggingLazyRecord()
    print(colored(f'exists:{data.exists}', 'green'))
    print(colored(f'first foo: {data.foo}', 'green'))
    print(colored(f'first bar: {data.bar}', 'green'))


def do_lazy():
    data = LazyRecord()
    print(colored(f'[Before]: {data.__dict__}', 'green'))
    print(colored(f'foo: {data.foo}', 'green'))
    print(colored(f'[After]: {data.__dict__}', 'green'))


# logging when access attribute
class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(colored(f'* call: __getattr__({name!r})', 'green'))
        try:
            value = super().__getattribute__(name)
            print(colored(f'* {name!r} find, {value!r} return', 'green'))
            return value
        except AttributeError:
            value = f'for {name}'
            print(colored(f'* {name!r} set {value!r}', 'red'))
            setattr(self, name, value)
            return value


@trace_func
def test_validating_record():
    data = ValidatingRecord()
    print(colored(f'exists:{data.exists}', 'green'))
    print(colored(f'first foo:{data.foo}', 'green'))
    print(colored(f'second foo:{data.foo}', 'green'))


def get_attribute_called_when_has_attr_getattr():
    data = ValidatingRecord()
    print(colored(f'Has first foo: {hasattr(data, "foo")}'))
    print(colored(f'Has second foo: {hasattr(data, "foo")}'))


if __name__ == '__main__':
    do_lazy()
    do_logging_lazy()
    test_validating_record()
    get_attribute_called_when_has_attr_getattr()
