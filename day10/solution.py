import argparse
import numpy as np

def left_pos(pos):
    return (pos[0], pos[1] - 1)

def right_pos(pos):
    return (pos[0], pos[1] + 1)

def up_pos(pos):
    return (pos[0] - 1, pos[1])

def down_pos(pos):
    return (pos[0] + 1, pos[1])

def check_in_bounds(pos, map):
    return 0 <= pos[0] < map.shape[0] and 0 <= pos[1] < map.shape[1]

counter = 0

def find_path(start, end, map):
    start = tuple(start)
    end = tuple(end)
    sum = 0

    if start == end:
        return 1
    else:
        up = up_pos(start)
        down = down_pos(start)
        left = left_pos(start)
        right = right_pos(start)

        if check_in_bounds(up, map) and map[up] == map[start] + 1: 
            sum += find_path(up, end, map)
        if check_in_bounds(down, map) and map[down] == map[start] + 1:
            sum += find_path(down, end, map)
        if check_in_bounds(left, map) and map[left] == map[start] + 1:
            sum += find_path(left, end, map)
        if check_in_bounds(right, map) and map[right] == map[start] + 1 : 
            sum += find_path(right, end, map)
    
    return sum




parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="sample", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

sum1, sum2 = 0, 0

with open(filename, "r") as f:
  df = f.read()

dt = df
rows = dt.strip().split('\n')


matrix = np.array([[int(x) for x in row] for row in rows])
start = np.column_stack(np.where(matrix == 0))
end = np.column_stack(np.where(matrix == 9))

sum1 = 0

for s in start:
    for e in end:
        found = find_path(s, e, matrix)
        sum2 += found
        if found:
            sum1 += 1
        

print("\n================ DAY 10 ================")
for i, answer in enumerate([sum1, sum2]):
  print(f"part {i+1}: {answer}")
