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



def left_shift(lst):
    if len(lst) > 0:  
        first = lst.pop(0)  
        lst.append(first)

def get_guard_pos(lab_map):
    g_pos = np.where(lab_map == '^')
    g_pos = g_pos[0][0], g_pos[1][0]
    return g_pos

def check_new_pos_in_bounds(shape, pos, dir):
    if 0 <= pos[0] + dir[0] < shape[0] and 0 <= pos[1] + dir[1] < shape[1]:
        return True
    else:
        return False

def check_if_obstacle(lab_map, g_pos, dir):
    new_pos = g_pos[0] + dir[0], g_pos[1] + dir[1]
    if lab_map[new_pos] == '#' or lab_map[new_pos] == 'O':
        return True
    else:
        return False

def get_new_dir(move):
    left_shift(move)
    return direction[move[0]]

def get_new_pos(lab_map, g_pos, dir, move):
    obstacle = True
    if check_new_pos_in_bounds(lab_map.shape, g_pos, dir):
        
        while obstacle:
            obstacle = check_if_obstacle(lab_map, g_pos, dir)
            if obstacle:
                dir = get_new_dir(move)
                obstacle = check_if_obstacle(lab_map, g_pos, dir)

        new_pos = g_pos[0] + dir[0], g_pos[1] + dir[1]
        return new_pos
    else:
        return None


def move_guard(lab_map, g_pos, new_pos):
    lab_map[g_pos] = 'X'
    lab_map[new_pos] = '^'

def play_moves(lab_map, move):
    states = set()

    while True:
        g_pos = get_guard_pos(lab_map)
        dir = direction[move[0]]
        new_pos = get_new_pos(lab_map, g_pos, dir, move)


        if new_pos is None:
            return lab_map, 0
        else:
            state = (g_pos, dir)
            if state in states:

                global obstacle_counter
                return None, 1
            else:
                states.add(state)

            move_guard(lab_map, g_pos, new_pos)
            g_pos = get_guard_pos(lab_map)






parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="sample", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

with open(filename, "r") as f:
  df = f.read()

dt = df
rows = dt.strip().split('\n')


data = []
pos = None
answer1, answer2 = 0, 0

lab_map = np.array([[i for i in row] for row in rows], dtype="str")
guard_pos = np.where(lab_map == '^')[0][0], np.where(lab_map == '^')[1][0]
available_moves = ["U", "R", "D", "L"]

new_map ,_ = play_moves(deepcopy(lab_map), deepcopy(available_moves))
guard_pos = np.where(new_map == '^')[0][0], np.where(new_map == '^')[1][0]
new_map[guard_pos] = 'X'
answer1 = new_map[new_map == "X"].shape[0]

for i in range(new_map.shape[0]):
    for j in range(new_map.shape[0]):
        if new_map[i, j] == "X" and lab_map[i, j] != "^":
            loop_map = deepcopy(lab_map)
            loop_map[i, j] = "O"
            answer2 += play_moves(loop_map, deepcopy(available_moves))[1]



print("\n============ DAY 6 ============")
for i, answer in enumerate([answer1, answer2]):
  print(f"part {i+1}: {answer}")
