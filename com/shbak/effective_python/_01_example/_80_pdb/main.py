import math

from termcolor import colored


def compute_rmse(observed, ideal):
    total_err_2 = 0
    count = 0

    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        breakpoint()  # start debugger
        total_err_2 += err_2
        count += 1

    mean_err = total_err_2 / count
    rmse = math.sqrt(mean_err)
    return rmse


def compute_rmse_with_conditional_breakpoint(observed, ideal):
    total_err_2 = 0
    count = 0

    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        if err_2 >= 1:
            breakpoint()  # start debugger
        total_err_2 += err_2
        count += 1

    mean_err = total_err_2 / count
    rmse = math.sqrt(mean_err)
    return rmse

def call_compute_rmse():
    result = compute_rmse(
        [1.8, 1.7, 3.2, 6],
        [2, 1.5, 3, 5]
    )
    print(colored(f'result: {result}', 'green'))


def call_compute_rmse_with_conditional_breakpoint():
    result = compute_rmse_with_conditional_breakpoint(
        [1.8, 1.7, 3.2, 6],
        [2, 1.5, 3, 5]
    )
    print(colored(f'result: {result}', 'green'))

def call_compute_rmse_postmortem():
    result = compute_rmse_with_conditional_breakpoint(
        [1.8, 1.7, 3.2, 7j],
        [2, 1.5, 3, 5]
    )
    print(colored(f'result: {result}', 'green'))

if __name__ == '__main__':
    # call_compute_rmse()
    # call_compute_rmse_with_conditional_breakpoint()
    call_compute_rmse_postmortem()