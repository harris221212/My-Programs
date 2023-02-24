#!/usr/bin/env python3
import sys
from datetime import date
from datetime import datetime, timedelta
import os.path

today = date.today()
now = datetime.now()

hour = now.strftime("%H")
minute = now.strftime("%M")
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

fileName = "/home/ethan/Programs/log/" + "angery" + ".txt"

f = open(fileName, "a")

toAdd = input("Go off: ")
toWrite = year + month + day + " " + hour + minute + " " + toAdd + "\n"
f.write(toWrite)
f.close()