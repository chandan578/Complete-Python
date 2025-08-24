import time

## Multithreading with thread pool
# Multithreading with thread pool allows you to execute multiple tasks concurrently using a pool of threads.
# The ThreadPoolExecutor from the concurrent.futures module manages a pool of threads and schedules tasks to run in those threads.
# You submit tasks to the pool, and each task is executed in a separate thread.
# This approach is useful for I/O-bound operations, such as network requests or file I/O, where threads can run in parallel and improve performance.
# The thread pool automatically handles thread creation and destruction, making it easier to manage resources.
# Results from tasks can be retrieved using Future objects, which represent the outcome of asynchronous operations.


from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"

numbers = [1,2,3,4,5,6, 7, 8]
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)
    