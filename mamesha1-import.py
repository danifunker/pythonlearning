#!/usr/bin/env python3

#Load new sha1s from text file
#1. load file
#2. parse look for this
#chdman - MAME Compressed Hunks of Data (CHD) manager 0.237 (mame0237)
# means a new entry
# grab the filename, and sha1
# put into a dict
# update XML
#
import sys
import os

if len(sys.argv) < 3: 
   print(f"USAGE: {os.path.basename(__file__)} <chdmanoutputfile.txt> <mamesoftwarelist>.xml")
   exit(1)

#open the first file, first check it exists
chdfile = open(sys.argv[1], "r")
def getchds():
    #done
    return 0
i=0
chdDict = {}
filename = ""
sha = ""
for line in chdfile.readlines():
    if line.startswith("chdman - MAME Compressed Hunks of Data (CHD) manager"):
        item=i+1
    if line.startswith("Input file:   "):
        fullpath = str.lower(line[14:])
        #for Windows Paths
        if fullpath != None and "\\" in fullpath:
            splitPath=fullpath.split('\\')
        #for *nix and compatible paths
        if fullpath != None and "/" in fullpath:
            splitPath=fullpath.split('/')
        lastItem = len(splitPath) -1
        filename = splitPath[lastItem].rstrip().replace("[!]","")
        #print(f"{filename}")

    if line.startswith("SHA1:         "):
        sha = line[14:].rstrip()
    if ((len(filename) > 1) and (len(sha) == 40) ):
        #print(f"Currently filename is {filename} and sha is {sha}. Going to add to dict")
        chdDict.update({filename:sha})
        #Now there is a match, unset the variables so that we ensure it goes in order
        filename = ""
        sha = ""

print("List looks like:")

for items in chdDict.items():
    print(f"{items}")

chdlist = list()
print(chdfile.read())