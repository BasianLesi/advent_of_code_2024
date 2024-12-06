import argparse

parser = argparse.ArgumentParser()
# Add an argument for the filename  
parser.add_argument("-f", "--filename", type=str, default="input", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  

# Parse the command-line arguments  
args = parser.parse_args()  

# Get the filename from the parsed arguments  
filename = args.filename  

with open(filename, "r") as f:
  df = f.read()

dt = df


def get_X(data):
  for i in range(3):
      if data[3-i] == "," and data[:3-i].isnumeric():
        return int(data[:3-i]), i
  return False, False

def get_Y(data):
  for i in range(3):
      if data[3-i] == ")" and data[:3-i].isnumeric():
        return int(data[:3-i]), i
  return False, False

action = True

dont = "don't()"
do = "do()"

print("\n====== DAY 3 ======")

for part in range(2):
    X = []
    Y = []
    x,y = 0,0

    for i in range(len(dt)):
        if part == 0:
          action = True
        elif dt[i:i+len(dont)] == dont:
            action = False
        elif dt[i:i+len(do)] == do:
            action = True

    
        if dt[i:i+4] == "mul(" and action: 
            x, idx = get_X(dt[i+4: i+8])
            if x != False:
                y, idx = get_Y(dt[i+8-idx: i+12-idx])
                if y != False:
                    X.append(x)
                    Y.append(y)
    
    sum = 0 
    for i in range(len(X)):
        sum += X[i] * Y[i]
    
    print (f"Part {part+1}: {sum}")




