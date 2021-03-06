import os
import subprocess
import time

from termcolor import colored

from com.shbak.effective_python._01_example._26_decorator.trace import trace_func

TEST_DURATION = '3'


def run_echo_subprocess():
    result = subprocess.run(['echo', 'hello to subprocess'],
                            capture_output=True,
                            encoding='utf-8')
    result.check_returncode()
    print(colored(f'result.output: {result.stdout}', 'green'))


def run_sleep_subprocess():
    result = subprocess.run(['sleep', TEST_DURATION])
    result.check_returncode()
    print(colored(f'[After] Sleeping 10 process', 'green'))
    print(colored(f'subprocess.run() is blocking method', 'cyan'))


def popen_subprocess_10_sleep():
    start = time.time()
    sleep_procs = []
    for _ in range(10):
        proc = subprocess.Popen(['sleep', '1'])
        sleep_procs.append(proc)

    for proc in sleep_procs:
        proc.communicate()
        print(colored(f'{dir(proc)}', 'green'))

    end = time.time()
    delta = end - start
    print(colored(f'{delta} sec duration end', 'green'))


def copy_system_env():
    env = os.environ.copy()
    print(colored(f'env: {env}', 'green'))
    return env


def encscrypt_with_system_env(data):
    """ openssl command need type information after command execution
    in stdin need "<ctrl> + d" when end of your typing

    :param data:
    :return:
    """
    env = copy_system_env()
    env['password'] = 'zfoiwjfa;owifj;oewifj/awe/fpja'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,  # stdin is pass to communicate method
        stdout=subprocess.PIPE
    )

    proc.stdin.write(
        data)  # if don't pass std argument to Popen method 'AttributeError' exception raised (NoneType object to write)
    proc.stdin.flush()
    return proc


def echo_with_stdin():
    proc = subprocess.Popen(
        ['echo'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )

    proc.stdin.write(bytes('1234123', 'utf-8'))
    proc.stdin.flush()
    output, _ = proc.communicate()
    print(colored(f'echo stdin: {output}', 'green'))


def run_encscrypt():
    procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = encscrypt_with_system_env(data)
        procs.append(proc)

    for proc in procs:
        out, _ = proc.communicate()
        print(colored(f'out[-10:]: {out[-10:]}', 'green'))


def run_hash(input_stdin):
    return subprocess.Popen(
        ['openssl', 'dgst', '-whirlpool', '-binary'],
        stdin=input_stdin,
        stdout=subprocess.PIPE)


@trace_func
def call_hash_with_pipe_chaining():
    encrypt_procs = []
    hash_procs = []
    for _ in range(3):
        data = os.urandom(100)
        encrypt_proc = encscrypt_with_system_env(data)
        encrypt_procs.append(encrypt_proc)

        hash_proc = run_hash(encrypt_proc.stdout)
        hash_procs.append(hash_proc)

        encrypt_proc.stdout.close()
        encrypt_proc.stdout = None

    for proc in encrypt_procs:
        proc.communicate()
        assert proc.returncode == 0

    for proc in hash_procs:
        out, _ = proc.communicate()
        print(colored(f'out[-10:]: {out[-10:]}', 'green'))
        assert proc.returncode == 0


if __name__ == '__main__':
    copy_system_env()
    run_echo_subprocess()
    run_sleep_subprocess()
    popen_subprocess_10_sleep()
    run_encscrypt()
    echo_with_stdin()
    call_hash_with_pipe_chaining()
