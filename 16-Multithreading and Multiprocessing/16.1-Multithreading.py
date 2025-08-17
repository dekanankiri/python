### Multithreading
## when to use multithreading
### I/O-bound task: Tasks  that spend more time waiting for I/O operations (e.g)., file operations, network requests).
### Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"number: {i}")

def print_letter():
  for letter in "abcde":
    time.sleep(1)
    print(f"Letter: {letter}")

## Create 2 Threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
## start the thread
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)