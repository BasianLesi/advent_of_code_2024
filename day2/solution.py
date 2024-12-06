import numpy as np
import argparse

parser = argparse.ArgumentParser()
# Add an argument for the filename  
parser.add_argument("-f", "--filename", type=str, default="input", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  

# Parse the command-line arguments  
args = parser.parse_args()  

# Get the filename from the parsed arguments  
filename = args.filename  

def check_diff_with_removed_element(data):
  for i in range(len(data)):
    if level_safe(np.delete(data, i)):
      return True
  return False

def level_safe(data):
  df = np.diff(data)
  if (np.all(df > 0) or np.all(df < 0)):
    if max(abs(df)) <=3:
      return True
  return False


with open(filename, "r") as f:
  dt = f.read()
rows = dt.strip().split('\n')
a = [np.array([int(i) for i in row.split(" ") if i.isnumeric()]) for row in rows]

question1 = 0
question2 = 0


for i in a:
  if level_safe(i):
      question1 += 1
  elif check_diff_with_removed_element(i):
    question2 += 1


print("\n==== DAY 2 ====")
for i, answer in enumerate([question1, question1 + question2]):
  print(f"part {i+1}: {answer}")






