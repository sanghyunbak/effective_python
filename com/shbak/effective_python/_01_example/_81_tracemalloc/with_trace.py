import tracemalloc

from termcolor import colored

from com.shbak.effective_python._01_example._81_tracemalloc import waste_memory

tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()

x = waste_memory.run()

time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print(colored(f'Top user: {top.traceback.format()}', 'green'))
