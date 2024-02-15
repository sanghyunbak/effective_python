import asyncio
import time

from termcolor import colored


async def main():
    print(colored(f"start at: {time.strftime('%X')}", 'green'))
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(colored(f"end at  : {time.strftime('%X')}", 'green'))

    # print(colored(f'hello', 'green'))
    # await asyncio.sleep(1)
    # print(colored(f'world', 'green'))


async def main2():
    task1 = asyncio.create_task(say_after(1, 'this'))
    task2 = asyncio.create_task(say_after(2, 'is what'))
    print(colored(f"[main2] start at  : {time.strftime('%X')}", 'green'))
    await task1
    await task2
    print(colored(f"[main2] end at    : {time.strftime('%X')}", 'green'))


async def say_after(delay, what):
    print(colored(f"say_after delay: ({delay}), what: ({what}) is called", 'yellow'))
    await asyncio.sleep(delay)
    print(colored(f'{what}', 'green'))


async def single_traffic_process():
    print(colored(f"single traffic process is called sleep 3 seconds", 'green'))
    await asyncio.sleep(3)
    print(colored(f"single traffic process is end", 'green'))
    print(colored(f"callback is called {callback()}", 'green'))


def callback():
    print(colored(f"callback is callled", 'magenta'))


def simulator():
    """ simulate massive traffic

    """


async def run_listening_server_emulator():
    """ listening traffic server emulator to test coroutine

    """
    cnt = 0
    while cnt < 10:
        cnt += 1
        print(colored(f"start sleep", 'magenta'))
        time.sleep(0.01)
        print(colored(f"start task", 'magenta'))
        # await asyncio.create_task(single_traffic_process())
        await asyncio.gather(asyncio.create_task(single_traffic_process()),
                             asyncio.create_task(single_traffic_process()),
                             asyncio.create_task(single_traffic_process()),
                             asyncio.create_task(single_traffic_process()),
                             asyncio.create_task(single_traffic_process()))

        print(colored(f"after task\n", 'magenta'))

    time.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
    time.sleep(4)
    asyncio.run(run_listening_server_emulator())
