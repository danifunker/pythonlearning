#!/usr/bin/env python3
import os

#get help 
help("if")

dir(os)

#or

import inspect
inspect.getmembers(os)

# get type
type(os)

#change types
strtoint="1"
print(type(strtoint)) #will return str
strtoint=int(strtoint)
print(type(strtoint)) #will now return int

#set hexnumber
hexnum=hex(15)
intnum=int(hexnum, 16) # second thing is base whatever

#binary
t=int("101", 2)