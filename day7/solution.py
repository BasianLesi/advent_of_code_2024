import argparse
import numpy as np
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}\t took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def concat(a, b):
  return int(str(a) + str(b))

def recursive_check(cur, values, goal):
  a = values[0]

  if len(values) == 1:
    if cur + a == goal or cur * a == goal or concat(cur, a) == goal:
      return True
    else:
      return False

  elif cur > goal:
    return False

  res1 = recursive_check(cur * a, values[1:], goal)
  res2 = recursive_check(cur + a, values[1:], goal)
  res3 = recursive_check(concat(cur, a), values[1:], goal)

  return res1 or res2 or res3

def check_equation(x, values):
  if x == np.sum(values) or x == np.prod(values):
    return True
  return recursive_check(values[0], values[1:], x)

@timeit
def get_sum(data):
  sum = 0
  for row in data:
    if check_equation(row[0], row[1:]):
      sum += row[0]
  return sum

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="input", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

with open(filename, "r") as f:
  df = f.read()

dt = df
rows = dt.strip().split('\n')
data = []

for line in rows:
  if line:
    parts = line.split(': ')
    numbers = [int(x) for x in parts[1].split()]
    data.append([int(parts[0])] + numbers)


print("\n============== DAY 7 ==============")
print(f"part 1: remove concat in the recursion")
print(f"part 2: {get_sum(data)}")
