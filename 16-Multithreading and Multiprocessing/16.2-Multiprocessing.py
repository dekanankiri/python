## Process that run in parallel
### CPU-Bound Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)
## Parallel execution - Multiple cores of the CPU

import multiprocessing

import time

def square_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"Square: {i*i}")

def cube_numbers():
  for i in range(5):
    time.sleep(1.5)
    print(f"Cube: {i * i * i}")

if __name__ == "__main__":
  ## create 2 processes
  p1 = multiprocessing.Process(target=square_numbers)
  p2 = multiprocessing.Process(target=cube_numbers)
  t = time.time()
  ## start the process
  p1.start()
  p2.start()

  ## Wait
  p1.join()
  p2.join()

  finished_time = time.time() - t
  print(f"Total time for execute: {finished_time}")