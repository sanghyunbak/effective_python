import contextlib
import io
import logging
import warnings

# Example 3
from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func

CONVERSIONS = {
    'mph': 1.60934 / 3600 * 1000,  # m/s
    'hours': 3600,  # seconds
    'miles': 1.60934 * 1000,  # m
    'meters': 1,  # m
    'm/s': 1,  # m
    'seconds': 1,  # s
}


def convert(value, units):
    rate = CONVERSIONS[units]
    return rate * value


def localize(value, units):
    rate = CONVERSIONS[units]
    return value / rate


def print_distance(speed, duration, *,
                   speed_units=None,
                   time_units=None,
                   distance_units=None):
    if speed_units is None:
        warnings.warn('speed_unit required', DeprecationWarning)
        speed_units = 'mph'

    if time_units is None:
        warnings.warn('time_units required', DeprecationWarning)
        time_units = 'hours'

    if distance_units is None:
        warnings.warn('distance_units required', DeprecationWarning)
        distance_units = 'miles'

    norm_speed = convert(speed, speed_units)
    norm_duration = convert(duration, time_units)
    norm_distance = norm_speed * norm_duration
    distance = localize(norm_distance, distance_units)
    print(colored(f'{distance} {distance_units}', 'green'))


def contextlib_stderr():
    fake_stderr = io.StringIO()
    with contextlib.redirect_stderr(fake_stderr):
        print_distance(1000, 3,
                       speed_units='meters',
                       time_units='seconds')
    print(colored(f'{fake_stderr.getvalue()}', 'green'))


def require(name, value, default):
    """return value, if not exist return default value

    :param name:
    :param value:
    :param default:
    :return:
    """
    if value is not None:
        return value
    warnings.warn(
        f'{name} will be required, change your code',
        DeprecationWarning,
        stacklevel=3
    )
    return default


def print_distance_with_help(speed, duration, *,
                             speed_units=None,
                             time_units=None,
                             distance_units=None):
    speed_units = require('speed_units', speed_units, 'mph')
    time_units = require('time_units', time_units, 'hours')
    distance_units = require('distance_units', distance_units, 'miles')

    norm_speed = convert(speed, speed_units)
    norm_duration = convert(duration, time_units)
    norm_distance = norm_speed * norm_duration
    distance = localize(norm_distance, distance_units)
    print(colored(f'{distance} {distance_units}', 'green'))


@trace_func
def call_print_distance_with_help():
    fake_stderr = io.StringIO()
    with contextlib.redirect_stdout(fake_stderr):
        print_distance_with_help(1000, 3,
                                 speed_units='meters',
                                 time_units='seconds')
    print(colored(f'{fake_stderr.getvalue()}', 'green'))


def call_warnning_to_except():
    warnings.simplefilter('error')
    try:
        warnings.warn('This method will be blocked', DeprecationWarning)
    except DeprecationWarning:
        print(colored(f'Deprecate Warning to be except', 'red'))
        pass


def wrap_warning_to_logger():
    fake_stderr = io.StringIO()
    handler = logging.StreamHandler(fake_stderr)
    formatter = logging.Formatter(
        '%(asctime)-15s WARNING] %(message)s'
    )
    handler.setFormatter(formatter)

    logging.captureWarnings(True)
    logger = logging.getLogger('py.warnings')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    warnings.resetwarnings()
    warnings.simplefilter('default')
    warnings.warn('This will go to the logs output')

    print(colored(f'{fake_stderr.getvalue()}', 'green'))


if __name__ == '__main__':
    # print_distance(1000, 3,
    #                speed_units='meters',
    #                time_units='seconds')
    # contextlib_stderr()
    # call_print_distance_with_help()
    call_warnning_to_except()
    wrap_warning_to_logger()
