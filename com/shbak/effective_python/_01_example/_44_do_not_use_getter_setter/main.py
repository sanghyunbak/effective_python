from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func


class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        """ when voltage setting setter is called (getter)

        :return:
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """when voltage property setting, current will update (setter)
        just update if you use dot operator
        :param voltage:
        """
        self._voltage = voltage
        self.current = self._voltage / self.ohms


def use_voltage_resistance():
    r2 = VoltageResistance(1e3)
    print(colored(f'Before: {r2.current: .2f} Amphere', 'green'))
    r2.voltage = 10
    print(colored(f'After: {r2.current: .2f} Amphere', 'green'))


class OldResistor:
    # not python style use getter, setter
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'resistance > 0, actual value: {ohms}')
        self._ohms = ohms


@trace_func
def use_bounded_resistance():
    r3 = BoundedResistance(1e3)
    r3.ohms = 1


def use_getter_setter():
    r0 = OldResistor(05e3)
    print(colored(f'Before: {r0.get_ohms()}', 'green'))
    r0.set_ohms(10e3)
    print(colored(f'After: {r0.get_ohms()}', 'green'))


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms is immutable object")
        self._ohms = ohms


def run_fixed_resistance():
    try:
        r4 = FixedResistance(1e3)
        r4.ohms = 2e3
    except AttributeError as ae:
        print(colored('{ae}', 'red'))


class MysteriousResister(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


@trace_func
def run_mysterious_resistor():
    r7 = MysteriousResister(10)
    r7.current = 0.01
    print(colored(f'Before: {r7.voltage:.2f}'))
    r7.ohms
    print(colored(f'After: {r7.voltage:.2f}'))


if __name__ == '__main__':
    use_getter_setter()
    use_voltage_resistance()
    use_bounded_resistance()
    run_fixed_resistance()
    run_mysterious_resistor()