import numpy as np
import argparse

parser = argparse.ArgumentParser()
# Add an argument for the filename  
parser.add_argument("-f", "--filename", type=str, default="input", help="The filename to be parsed")  

# Parse the command-line arguments  
args = parser.parse_args()  

# Get the filename from the parsed arguments  
filename = args.filename  


with open(filename, "r") as f:
  dt = f.read()

  rows = dt.strip().split('\n')

  a = np.array([int(row.split()[0]) for row in rows])
  b = np.array([int(row.split()[1]) for row in rows])

  question1 = np.sum(abs(np.sort(a) - np.sort(b)))


  au, af = np.unique(a, return_counts=True)
  bu, bf = np.unique(b, return_counts=True)


fa = dict(zip(bu, bf))

question2 = 0

for i in a:
  if i in fa:
    question2 += fa[i]*i


print("\n== DAY 1 ==")
for i, answer in enumerate([question1, question2]):
  print(f"part {i+1}: {answer}")

