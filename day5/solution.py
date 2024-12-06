import argparse
import numpy as np

def check_valid_order(dr, pre_list, candidate):
  for i in pre_list:
    if i not in dr:
      return False
    elif candidate not in dr[i]:
      return False
  return True

def check_order(candidate, pre_list, dr):
  for i, num in enumerate(pre_list):
    if num in dr[candidate]:
      return i

  
  return i+1


def fixed_order(order, dr):
  pre_list = []
  for i in range(len(order)):
    if pre_list == []:
      pre_list.append(order[i])
    else:
      candidate = order[i]
      if candidate not in dr:
        pre_list.append(candidate)
      else:
        index = check_order(candidate, pre_list, dr) 
        pre_list.insert(index, candidate)
    

  median = pre_list[int(len(pre_list)/2)] 

  return median





parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="input", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

with open(filename, "r") as f:
  df = f.read()

dt = df
rows = dt.strip().split('\n')
rules = [row for row in rows if "|" in row]
rules = np.array([[int(i) for i in row.split("|")] for row in rules if "|" in row ])

order = [row for row in rows if "|" not in row]
data = []

for row in order:
  if row:
    numbers = [int(x) for x in row.split(',')]
    data.append(numbers)

order = data

is_valid = [True]*len(order)

dr = {}
for row in rules:
  key = row[0]
  value = row[1]
  if key in dr:
    dr[key].append(value)
  else:
    dr[key] = [value]

for index, row in enumerate(order):
  pre_list = []
  for i in row:
    if pre_list == []:
      pre_list.append(i)
    else:
      if check_valid_order(dr, pre_list, i):
        pre_list.append(i)
      else:
        is_valid[index] = False


sum = 0
sum2 = 0
for valid, row in zip(is_valid, order):
  if valid:
    sum += row[int(len(row)/2)]
  else:
    sum2 += fixed_order(row, dr) 

print("\n========== DAY 5 ==========")
for i, answer in enumerate([sum, sum2]):
  print(f"part {i+1}: {answer}")
