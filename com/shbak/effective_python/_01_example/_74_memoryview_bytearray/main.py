import timeit
from socket import socket

from termcolor import colored


def print_memoryview():
    data = b'shave and a haircut, two bits'
    view = memoryview(data)
    chunk = view[12:19]
    print(colored(f'chunk: {chunk}', 'green'))
    print(colored(f'size: {chunk.nbytes}', 'green'))
    print(colored(f'view data: {chunk.tobytes()}', 'green'))
    print(colored(f'inside data: {chunk.obj}', 'green'))


def bytes_and_bytearray_test():
    my_bytes = b'hello'
    try:
        my_bytes[0] = '\x79'
    except Exception as e:
        print(colored(f'Exception occur: {e}', 'red'))

    my_array = bytearray('hello '.encode('utf8'))
    my_array[0] = 0x79
    print(colored(f'my_array: {my_array}', 'green'))

    my_array = bytearray('row, row, row your boat'.encode('utf8'))
    my_view = memoryview(my_array)
    write_view = my_view[3:13]
    write_view[:] = b'-10 bytes-'
    print(my_array)


def run_test():
    my_array = bytearray('row, row, row your boat'.encode('utf8'))
    my_view = memoryview(my_array)
    write_view = my_view[3:13]
    write_view[:] = b'-10 bytes-'
    byte_offset = 10
    size = len(write_view)
    chunk = write_view[byte_offset:byte_offset + size]
    # socket.recv_info(chunk)


def benchmark():
    result = timeit.timeit(
        stmt='run_test()',
        globals=globals(),
        number=100
    ) / 100

    print(colored(f'{result:0.9f} sec', 'magenta'))


if __name__ == '__main__':
    print_memoryview()
    bytes_and_bytearray_test()
    benchmark()
