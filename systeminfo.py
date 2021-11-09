#!/usr/bin/env python3
import sys
import os
import requests
import socket #used to get IP address stuff

mysock = socket
externalIP=requests.get(https://api.my-ip.io/ip)
internalIP=mysock.gethostbyname(mysock.gethostname())
myLogin=os.getlogin()

print(f"My External IP is: {externalIP}")
print(f"My Hostname is {mysock.gethostname}")
print(f"Logged in User: {myLogin}")
