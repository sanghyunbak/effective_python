import gc

from termcolor import colored

from com.shbak.effective_python._01_example._81_tracemalloc import waste_memory

found_objects = gc.get_objects()
print(colored(f'[Before] memory size: {len(found_objects)}', 'green'))

hold_reference = waste_memory.run()

found_objects = gc.get_objects()
print(colored(f'[After] memory size: {len(found_objects)}', 'green'))

for obj in found_objects[:3]:
    print(colored(f'{repr(obj)[:100]}', 'green'))

print(colored(f'hold_reference: {hold_reference}', 'green'))
