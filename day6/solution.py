import argparse
import numpy as np

obstacle_counter = 0

def left_shift(lst):
    if len(lst) > 0:  
        first = lst.pop(0)  
        lst.append(first)

def is_out_of_bounds(lab, pos, dir):
  if pos[0] + dir[0] >= lab.shape[0] or pos[1] + dir[1] >= lab.shape[1]:
     return True

def is_move_legal(lab, pos, dir):
    if lab[pos[0] + dir[0]][pos[1] + dir[1]] != 2:
        lab[pos[0] + dir[0]][pos[1] + dir[1]] = 1
        return True

    return False

        

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="input", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

with open(filename, "r") as f:
  df = f.read()

dt = df
rows = dt.strip().split('\n')


direction = {
  "U": (-1, 0),
  "D": (1, 0),
  "L": (0, -1),
  "R": (0, 1),
}

move = ["U", "R", "D", "L"]
data = []
pos = None

for idx, string in enumerate(rows): 
  row = []
  for idy, char in enumerate(string):
    if char == ".":
      row.append(0)
    elif char == "#":
      row.append(2)
    else:
      row.append(1)
      pos = (idx, idy)

  data.append(row)

  
lab = np.array(data)
lab_dir = np.full(lab.shape, 'X').tolist()
lab_dir[pos[0]][pos[1]] += 'U'


guard = True

while guard:
  dir = direction[move[0]]
  if is_out_of_bounds(lab, pos, dir):
      guard = False

  else:
      if is_move_legal(lab, pos, dir):
          pos =  (pos[0] + dir[0], pos[1] + dir[1])
      else:
          left_shift(move)
          dir = direction[move[0]]

visited1 = len(lab[lab==1])


print("\n============ DAY 6 ============")
for i, answer in enumerate([visited1, obstacle_counter]):
  print(f"part {i+1}: {answer}")
