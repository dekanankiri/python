### Multithreading With thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
  time.sleep(1)
  return print(f"Number : {number}\n")

numbers = list(range(20))

t=time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
  results=executor.map(print_number,numbers)

print(f"executed time: {time.time() - t}")


#for result in results:
#  print(result)