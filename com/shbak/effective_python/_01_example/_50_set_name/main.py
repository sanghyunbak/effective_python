#
from termcolor import colored


class NewField:
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        # when class created, this method is called
        self.name = name
        self.internal_name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Field:
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class FixedCustomer:
    first_name = NewField()
    last_name = NewField()
    prefix = NewField()
    suffix = NewField()


def run_fixed_customer():
    cust = FixedCustomer()
    print(colored(f'[Before]: {cust.first_name!r} {cust.__dict__}'))
    cust.first_name = 'Mersen'
    print(colored(f'[After]: {cust.first_name!r} {cust.__dict__}'))


class Customer:
    first_name = Field('first_name')
    second_name = 3
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

    def __init__(self, first_name):
        self.first_name = first_name




def use_customer():
    cust = Customer('12')
    print(colored(f'[Before]: cust.first_name: {cust.first_name!r} cust.__dict__: {cust.__dict__}'
                  f',\n     Customer.first_name: {Customer.first_name}, Customer.second_name: {Customer.second_name!r}', 'green'))
    cust.first_name = 'euclid'
    print(colored(f'[After]: {cust.first_name!r} {cust.__dict__}', 'green'))


if __name__ == '__main__':
    use_customer()
    run_fixed_customer()
