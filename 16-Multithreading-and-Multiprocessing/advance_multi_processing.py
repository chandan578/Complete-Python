#  Multiprocessing with ProcessPoolExecutor

# This code demonstrates how to use Python's `concurrent.futures.ProcessPoolExecutor` for parallel processing. The `ProcessPoolExecutor` runs tasks in separate processes, allowing CPU-bound operations to execute concurrently and utilize multiple CPU cores. The `executor.map()` method distributes the `task` function across the provided `numbers` list, running each call in a separate process. This approach is useful for improving performance in programs that perform heavy computations.


from concurrent.futures import ProcessPoolExecutor
import time

def print_num(number):
    time.sleep(3)  ## only first time it sleep for 3 sec otherwise it do not sleep....
    return f"Number : {number}"

numbers = [1,2,3,4,5,6,7,8]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_num, numbers)

    for result in results:
        print(result)
