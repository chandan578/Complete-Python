'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import sys
import multiprocessing
import math
import time

## set max digit...
sys.set_int_max_str_digits(100000000)


def computer_factorial(number):
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)

    end_time = time.time()
    print(f"Results : {results}")
    print(f"Time taken : {end_time-start_time} seconds")