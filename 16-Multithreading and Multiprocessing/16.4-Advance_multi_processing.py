### Multiprocessinng with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
  time.sleep(1)
  return print(f"Square: {number*number}")

numbers = list(range(1,21))

if __name__=="__main__":
  with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(square_number,numbers)

  '''for result in results:
    print(result)'''