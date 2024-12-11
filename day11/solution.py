import argparse
from functools import cache

@cache
def split(stone, depth=0):
    if depth == 0:
        return 1

    if stone == 0:
        stone = 1
        return split(stone, depth-1)

    elif len(str(stone))%2 == 0:
        mid = len(str(stone))//2
        stone1 = int(str(stone)[:mid])
        stone2 = int(str(stone)[mid:])
        return split(stone1, depth-1) + split(stone2, depth-1)

    else:
        return split(stone*2024, depth-1)
     

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="sample", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

sum1, sum2 = 0, 0

with open(filename, "r") as f:
  df = f.read()

rows = df.strip().split(' ')

for row in rows:
    stone = int(row)
    sum1 += split(stone, 25)
    sum2 += split(stone, 75)

print("\n================ DAY 10 ================")
for i, answer in enumerate([sum1, sum2]):
  print(f"part {i+1}: {answer}")

import pdb; pdb.set_trace()
