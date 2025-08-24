## Multiprocessing in Python is a technique to run multiple processes simultaneously, allowing you to take advantage of multiple CPU cores. Each process runs independently and has its own memory space, which avoids the Global Interpreter Lock (GIL) limitation present in Python threads. This makes multiprocessing suitable for CPU-bound tasks, such as data processing, computations, and simulations. The `multiprocessing` module provides tools to create and manage processes, share data between them, and synchronize their execution. Common components include `Process`, `Queue`, `Pool`, and `Manager`. Multiprocessing can improve performance for tasks that require significant computation, but it introduces complexity in communication and data sharing between processes.

import multiprocessing
import time

def square_number():
    for n in range(5):
        time.sleep(1)
        print(f"Square of {n}: {n*n}")

def cube_number():
    for n in range(5):
        time.sleep(1.5)
        print(f"Cube of {n}: {n*n*n}")

if __name__ == "__main__":
    # numbers = [1, 2, 3, 4, 5]

    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print("Time taken:", end - start)
