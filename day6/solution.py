import argparse
import numpy as np
from copy import deepcopy

obstacle_counter = 0
cnt = 0

direction = {
  "U": (-1, 0),
  "D": (1, 0),
  "L": (0, -1),
  "R": (0, 1),
}

move = ["U", "R", "D", "L"]


def left_shift(lst):
    if len(lst) > 0:  
        first = lst.pop(0)  
        lst.append(first)

def get_map_value(map, pos, dir=(0,0)):
  return map[pos[0] + dir[0]][pos[1] + dir[1]]

def get_pos(pos, dir):
  return (pos[0] + dir[0], pos[1] + dir[1])

def is_out_of_bounds(lab, pos, dir=(0,0)):
  if pos[0] + dir[0] >= lab.shape[0] or pos[1] + dir[1] >= lab.shape[1] or pos[0] + dir[0] < 0 or pos[1] + dir[1] < 0:
     return True

def check_if_loop(lab, pos, dir, move):
  state = set()

  new_lab = deepcopy(lab)
  global o_map

  if is_out_of_bounds(new_lab, pos, dir):
      return 0
  elif o_map[get_pos(pos, dir)] == 5 or new_lab[get_pos(pos, dir)] == 2:
    return 0
  else:
    new_lab[get_pos(pos, dir)] = 2

  # placed obstacle so change dir
  new_move = deepcopy(move)
  left_shift(new_move)

  new_dir = direction[new_move[0]]
  new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
  #new_pos = pos

  
  while True:
    if is_out_of_bounds(new_lab, new_pos) or is_out_of_bounds(new_lab, new_pos, new_dir):
      return 0

    else:
      if get_map_value(new_lab, new_pos) != 2:
          new_lab[new_pos[0]][new_pos[1]] = 1
          new_state = (new_pos, new_dir) 
          new_pos =  get_pos(new_pos, new_dir)
          if new_state in state:
              o_map[get_pos(pos,dir)] = 5
              return 0
          else:
            state.add(new_state)
      else:
          # obtacle found change dir
          left_shift(new_move)
          new_dir = direction[new_move[0]]



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
o_map = deepcopy(lab)


guard = True

while guard:
  dir = direction[move[0]]
  check_if_loop(lab, pos, dir, move)

  if is_out_of_bounds(lab, pos, dir):
      guard = False

  else:
      if is_move_legal(lab, pos, dir):
          pos =  (pos[0] + dir[0], pos[1] + dir[1])
      else:
          left_shift(move)
          dir = direction[move[0]]

visited1 = len(lab[lab==1])
visited2 = len(o_map[o_map==5])

print(cnt)


print("\n============ DAY 6 ============")
for i, answer in enumerate([visited1, visited2]):
  print(f"part {i+1}: {answer}")
