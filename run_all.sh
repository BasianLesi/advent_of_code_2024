#!/bin/bash  

echo "Running Advent of Code solutions..."  
for dir in day*; do  
    if [ -d "$dir" ]; then  
        cd "$dir"
        python "solution.py"  
        cd ..
    fi  
done  
