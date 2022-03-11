#!/usr/bin/env python3
#requirements: bs4, lxml
#Load new sha1s from text file
#1. load file
#2. parse look for this
#chdman - MAME Compressed Hunks of Data (CHD) manager 0.237 (mame0237)
# means a new entry
# grab the filename, and sha1
# put into a dict
# update XML
#
from bs4 import BeautifulSoup as bs
import sys
import os
import lxml

#chdListfilename = sys.argv[1]
#softwarelistFileName = sys.argv[2]

chdListfilename="mamechds.txt"
softwarelistFileName="cdi.xml"

#if len(sys.argv) < 3: 
#   print(f"USAGE: {os.path.basename(__file__)} <chdmanoutputfile.txt> <mamesoftwarelist>.xml")
#   exit(1)

#open the first file, first check it exists
chdfile = open(chdListfilename, "r")
chdDict = {}
filename = ""
sha = ""
for line in chdfile.readlines():
    if line.startswith("Input file:   "):
        fullpath = str.lower(line[14:])
        #for Windows Paths
        if fullpath != None and "\\" in fullpath:
            splitPath=fullpath.split('\\')
        #for *nix and compatible paths
        if fullpath != None and "/" in fullpath:
            splitPath=fullpath.split('/')
        lastItem = len(splitPath) -1
        filename = splitPath[lastItem].rstrip().replace("[!]","").replace(".chd","")
        #print(f"{filename}")
    if line.startswith("SHA1:         "):
        sha = line[14:].rstrip()
    if ((len(filename) > 1) and (len(sha) == 40) ):
        #print(f"Currently filename is {filename} and sha is {sha}. Going to add to dict")
        chdDict.update({filename:sha})
        #Now there is a match, unset the variables so that we ensure it goes in order
        filename = ""
        sha = ""
#Close hooks
chdfile.close()
#print("chdDict looks like:")
#for items in chdDict.items():
#    print(f"{items}")

xmlContent= []

 # Read the XML file
with open(softwarelistFileName, "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    xmlContent = "".join(content)
    bs_content = bs(xmlContent, "lxml")

disks = bs_content.find_all('disk')
mamedisks = {}
for disk in disks:
    mamedisks.update({disk.get('name'):disk.get('sha1')})


matches = []
nonmatches = []
for chds in chdDict.keys():
    try: 
        #print(f"Trying {chds}")
        matches.append(list(mamedisks.keys()).index(chds))
    except ValueError:
        nonmatches.append({chds})
    else: 
        #print(f"Couldn't match {chds}")
        pass

for chds in chdDict.keys(): 
    print(f"Trying {chds}")
    if mamedisks.get({chds}): 
        print(f"found it")
        matches.append({chds})
    else: 
        nonmatches.append({chds})
        pass