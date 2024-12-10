import argparse
import numpy as np
import itertools


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, default="sample", help="The filename to be parsed")  
parser.add_argument("-d", "--debug", action="store_true", default=False, help="The filename to be parsed")  
args = parser.parse_args()  
filename = args.filename  

counter = 0

class File:
    def __init__(self, id):
        self.id = id

class Dots:
    def __init__(self, len, id=None):
        self.len = len
        self.id = id

def expand(string):
    id_counter = 0
    expanded = ""
    files = []
    id_files = []
    dot_files = []
    i = 0
    id = 0
    while i < len(string):
        
        num = int(string[i])
        for k in range(num):
            files.append(File(id_counter))
        id_counter += 1
        id_files.append(Dots(num, id_counter))
        id +=1

        i += 1
        
        num = int(string[i])
        dots = '.' * num
        files += list(dots)
        dot_files.append(Dots(num))
        i += 1
    
    return files, dot_files, id_files
        
        
def compress(files, dot_files):
    ids = []
    j = len(files)


    files_only = [f for f in files if f != '.']
    end = len(files_only) - 1
    
    for i, char in enumerate(files):
        if char == '.' and end > -1:
            files[i] = files_only[end]
            end -= 1
            j -= 1
        if i == end:
            break
    
    return files[:j], ids[:j]
        
def find_file_of_size(id_files, ln):
    fid = None
    for i in range(0, len(id_files), -1):
        if id_files[i].len <= ln:
            fid = id_files.pop(i)
    
    return fid

def compress2(files, dot_files, id_files):
    import pdb; pdb.set_trace()
    com_files = []
    ifile = 0

    for i in range(len(files)):
        if files[i] == '.':


            
            
    pass
        
def checksum(files_id):
    sum = 0

    for idx, i in enumerate(files_id):
        sum += idx*int(i.id)
        
    return sum


sum1, sum2 = 0, 0

with open(filename, "r") as f:
  df = f.read()


df += "0"

def files_to_str(files):
    dt = ''
    for f in files:
        if f == '.':
            dt += f
        else:
            dt += str(f.id)
    return dt

files, dot_files, id_files = expand(df)
dt = files_to_str(files)
files_id, ids = compress(files, dot_files)
files_id, ids = compress2(files, dot_files, id_files)
sum1 = checksum(files_id)


print("\n================ DAY 8 ================")
for i, answer in enumerate([sum1, sum2]):
  print(f"part {i+1}: {answer}")

import pdb; pdb.set_trace()