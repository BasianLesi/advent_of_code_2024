import argparse
import numpy as np
import time
from functools import wraps


def check_in_bounds_shape(pos, shape):
    if -1 < pos[0] < shape[0] and -1 < pos[1] < shape[1]:
        return True
    else:
        return False

class Node:
    def __init__(self, _id, _x, _y):
        self.x = _x
        self.y = _y
        self.pos = np.array([_x,_y])
        self.dist = None
        self.antinodes = None

    def create_dist(self, ant_pos, map_shape):
        dist = []
        for i in ant_pos:
            distance = self.pos - i
            dist.append(distance)
        self.dist = np.array(dist)
        self.create_antinodes(map_shape)

    def create_antinodes(self, map_shape):
        antinode = []
        for i in self.dist:
            if (i != np.array([0,0])).any():
                if map_shape is None:
                    anti_pos1 = self.pos + i
                    anti_pos2 = self.pos - 2*i
                    antinode.append(anti_pos1)
                    antinode.append(anti_pos2)
                else:
                    for h in range(map_shape[0]):
                        anti_pos1 = self.pos + h*i
                        anti_pos2 = self.pos - h*i
                        if check_in_bounds_shape(anti_pos1, map_shape):
                            antinode.append(anti_pos1)
                        if check_in_bounds_shape(anti_pos2, map_shape):
                            antinode.append(anti_pos2)

        self.antinodes = np.array(antinode)


class Fz:
    """Store frequencies data"""
    def __init__(self, _id, _x, _y, _map_shape=None):
        self.id = _id
        self.x = _x
        self.y = _y
        self.map_shape = _map_shape
        self.pos = np.column_stack((_x, _y))
        self.dist = np.diff(self.pos, axis=0)
        self.nodes = self.create_nodes()
        self.antinodes = self.calc_dist()
        
    
    def create_nodes(self):
        nodes = []
        for i in self.pos:
            node = Node(self.id, i[0], i[1])
            nodes.append(node)

        return nodes

    def calc_dist(self):
        for i in self.nodes:
            i.create_dist(self.pos, self.map_shape)


def check_in_bounds(pos, matrix):
    if -1 < pos[0] < matrix.shape[0] and -1 < pos[1] < matrix.shape[1]:
        return True
    else:
        return False


def add_antinodes(fz, matrix):
    for node in fz.nodes:
        for pos in node.antinodes:
            if check_in_bounds(pos, matrix): 
                 matrix[pos[0], pos[1]] = '#'


    


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
data = np.array([[cell for cell in row] for row in rows])

antinodes_matrix = np.full(data.shape, '.', dtype=str)
ant_dict = {}
antennas = []

uc = np.unique(data)
unique_chars = uc[uc != '.']
map_shape = data.shape

for i in unique_chars:
    pos = np.where(data == i)
    x = pos[0]
    y = pos[1]
    ant_dict[i] = Fz(i, x, y, map_shape)
    antennas.append(Fz(i, x, y, map_shape))

for fz in antennas:
    add_antinodes(fz, antinodes_matrix)

sum1 = antinodes_matrix[antinodes_matrix == "#"].shape[0]


print("\n============== DAY 8 ==============")
for i, answer in enumerate([sum1, sum2]):
  print(f"part {i+1}: {answer}")
