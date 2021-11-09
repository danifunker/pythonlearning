#!/usr/bin/env python3
import sys

#sys.argv = list of all args 
#sys.argv[#] = array of positional character

#dir(sys)
print(f"USAGE: {sys.base_prefix}: arg1 arg2")
print(f"You entered {len(sys.argv) -1 } args")
if len(sys.argv) > 1: 
    #for loop to provide index number and value (idx, val) and using enumerate function in python. This time it is starting from 1 as specified by [1:]
    for idx, val in enumerate(sys.argv[1:]):
        print(f"for arg number {idx}, you entered {val}")