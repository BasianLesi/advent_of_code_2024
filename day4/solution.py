import argparse
import numpy as np
from copy import deepcopy

def check_for_xmas(a):
    counter = 0
    for i in range(a.shape[0]):
            if "".join(a[i:i+4]) == "XMAS":
              counter += 1

    return counter

def check_for_mas(a):
    for i in range(a.shape[0]):
            if "".join(a[i:i+3]) == "MAS":
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
matrix = np.array([list(row) for row in rows])

counter = 0
b = deepcopy(matrix)
b_rev = matrix[:, ::-1]

b_col_rev = matrix[::-1, :]

for i in range(b.shape[0]-3):
    for j in range(b.shape[1] - 3):
        c = b[i:i+4, j:j+4]
        c_rev = c[:, ::-1]

        diag = np.array([c[i][i] for i in range(c.shape[0])])
        diag_rev = np.array([c_rev[i][i] for i in range(c_rev.shape[0])])

        counter += check_for_xmas(diag)
        counter += check_for_xmas(diag[::-1])
        counter += check_for_xmas(diag_rev)
        counter += check_for_xmas(diag_rev[::-1])


for i in range(b.shape[0]):
    counter += check_for_xmas(b[i])
    counter += check_for_xmas(b[i, ::-1])

for j in range(b.shape[1]):
    counter += check_for_xmas(b[:, j])
    counter += check_for_xmas(b[::-1, j])


# part 2
counter2 = 0

for i in range(b.shape[0]-2):
    for j in range(b.shape[1] - 2):
        c = b[i:i+3, j:j+3]
        c_rev = c[:, ::-1]

        diag = np.array([c[i][i] for i in range(c.shape[0])])
        diag_rev = np.array([c_rev[i][i] for i in range(c_rev.shape[0])])

        if (check_for_mas(diag) or check_for_mas(diag[::-1])) and (check_for_mas(diag_rev) or check_for_mas(diag_rev[::-1])):
            counter2 += 1

print("\n======== DAY 4 ========")
for i, answer in enumerate([counter, counter2]):
  print(f"part {i+1}: {answer}")
#diagonal
