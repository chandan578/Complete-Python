## Multithreading :
# Multithreading allows concurrent execution of two or more parts of a program for maximum utilization of CPU.
# In Python, the 'threading' module is used to create and manage threads.
# Threads run in the same memory space, making communication between them easier but requiring synchronization for shared resources.
## Basically two types :
## I/O execution : 
## Concurrent Execution : 

import threading
import time

def print_number() :
    for i in range(5) :
        time.sleep(2)
        print(f"Number : {i}")


def print_letter():
    for i in "abcde" :
        time.sleep(2)
        print(f"Letter : {i}")
# t = time.time()
# print_number()
# print_letter()
# finished_time = time.time()-t
# print(finished_time)


## Create two thread 
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

t = time.time()
## start the thread..
t1.start()
t2.start()

## wait for both thread completed
t1.join()
t2.join()

## after compleation
finished_time = time.time()-t
print(finished_time)
