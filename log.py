#!/usr/bin/env python3
import json
import sys
from datetime import date
from datetime import datetime, timedelta
import os.path

def add():
    # Get day
    today = date.today()
    now = datetime.now()

    hour = now.strftime("%H")
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    if int(hour) < 10:
        yesterday = datetime.now() - timedelta(1)
        day = yesterday.strftime("%d")
        month = yesterday.strftime("%m")
        year = yesterday.strftime("%y")

    # Filename
    fileName = "/home/ethan/Programs/log/" + year + month
    exists = os.path.isfile(fileName)

    if exists: 
        currentFile = open(fileName, "r")
        monthString = currentFile.read()
        monthJson = json.loads(monthString)
        currentFile.close()

    # Get info from user
    stuff = input("What Happened Today: ")
    trips = input("Where Were You Today: ")
    video = input("Favourite Video Today: ")
    song = input("Favourite Song Today: ")

    # Format into JSON
    todayJson = {
        "stuff": stuff,
        "trips": trips,
        "video": video,
        "song": song
    }

    # Add to monthJson
    if not exists:
        monthJson = {day:todayJson}
    else:
        monthJson.update({day: todayJson})

    # Save to file
    with open(fileName, "w") as write_file:
        newJson = json.dump(monthJson, write_file, indent=2)

def search(query, rangeA):
    # If the range is only one month, just search that month
    if len(rangeA) == 4:
        searchMonth(rangeA, query)
    # Else search all months in the specified year
    else:
        yearQuery = rangeA[0:2]
        for xy in range(12):
            if xy < 9:
                dateAA = rangeA + "0" + str(xy + 1)
            else:
                dateAA = rangeA + str(xy + 1)
            searchMonth(dateAA, query)

    
def searchMonth(yM, queryA):
    fileName = "/home/ethan/Programs/log/" + yM[0:2] + yM[2:4]
    exists = os.path.isfile(fileName)
    toReturn = []
    # Open file and get data
    if exists:
        currentFile = open(fileName, "r")
        monthString = currentFile.read()
        monthJson = json.loads(monthString)
        currentFile.close()
        # Extract day data from the dictionary of days
        for key in monthJson:
            #print(key)
            currentDay = monthJson[key]
            #print(currentDay)
            keys = ["stuff", "trips", "video", "song"]
            # Check for query and if found, add day to array toReturn
            for keyA in keys:
                if queryA in currentDay[keyA]:
                    toReturn.append(yM + key)
    # Only print array if it has values
    if len(toReturn) > 0:
        toReturn.sort()
        print("Present in month " + yM[2:4] + ":")
        for foundDate in toReturn:
            print(foundDate[4:6])



def findDay(dayQuery):
    yearFind = dayQuery[0:2]
    monthFind = dayQuery[2:4]
    dayFind = dayQuery[4:6]
    fileName = "/home/ethan/Programs/log/" + yearFind + monthFind
    exists = os.path.isfile(fileName)
    if exists: 
        try:
            currentFile = open(fileName, "r")
            monthString = currentFile.read()
            monthJson = json.loads(monthString)
            currentFile.close()
            print("What Happened: \t " + monthJson.get(dayFind).get("stuff"))
            print("Where Were You:  " + monthJson.get(dayFind).get("trips"))
            print("Favourite Video: " + monthJson.get(dayFind).get("video"))
            print("Favourite Song:  " + monthJson.get(dayFind).get("song"))
        except:
            print("Error, date not present")   
    else:
        print("Error, date not present")



# Run selected function
if len(sys.argv) == 1:
    add()
elif sys.argv[1] == "-s":
    if len(sys.argv) == 2:
        print("Usage: Type string to search after -s, optionally specify date with yy/yymm format")
    elif len(sys.argv) == 3:
        search(sys.argv[2], 0)
    else:
        search(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "-d":
    if len(sys.argv) == 2:
        print("Usage: type date in format yymmdd after -d")
    else:
        findDay(sys.argv[2])