#!/usr/bin/env python
# coding: utf-8



# Task 1: Printing the file contents
with open("/Users/ishantdhall/Desktop/BusRouteLA.txt",'r') as file: # File path (Please enter your file path)
        for line in file:                     
            for word in line.split(":"):      
                print(word) 



#Task 2: BusStop Class
class BusStop:
    def __init__(self,number,name,street,suburb):
        self.number = number
        self.name = name
        self.street = street
        self.suburb = suburb



# Task 3 : Combined Program for querying and loading the Bus Routes

BusStops = []
with open("/Users/ishantdhall/Desktop/BusRouteLA.txt",'r') as file: # File path (Please enter your file path)
        lines = file.readlines()

class BusStop:
    def __init__(self,number,name,street,suburb):
        self.number = number
        self.name = name
        self.street = street
        self.suburb = suburb

def loadData():
    for i in lines:
        words = i.split(":")
        if words[3][len(words[3])-1] == "\n":
            words[3] = words[3][:len(words[3])-1]
        temp = BusStop(words[0],words[1],words[2],words[3])
        BusStops.append(temp)

def listAllBusStopNames():
    x = []
    for i in BusStops:
        if i.name not in x:
            x.append(i.name)
    for i in x:
        print(i)

def listAllStreetsOnRoute():
    x = []
    for i in BusStops:
        if i.street not in x:
            x.append(i.street)
    for i in x:
        print(i)

def listAllSuburbsOnRoute():
    x = []
    for i in BusStops:
        if i.suburb not in x:
            x.append(i.suburb)
    for i in x:
        print(i)

def searchByNumber(start,end):
    if(start > end):
        print("The starting number cannot be greater than the ending number")
        return
    elif(start<1 ):
        print("The starting stop number should be at least 1")
        return
    elif(end > len(lines)):
        print("The end is out of bounds. The maximum ending stop number is "+str(len(lines)))
        return
    for i in range(start-1,end):
        print("Stop:"+lines[i])

def searchByName(namekey):
    index =0
    namekey = namekey.lower()
    c = 0
    for i in BusStops:
        if namekey in i.name.lower():
            c+=1
            print("Stop:"+lines[index])
        index+=1
    if(c==0):
        print("There are no matches!")

def searchByStreet(streetkey):
    index =0
    c=0
    streetkey = streetkey.lower()
    for i in BusStops:
        if streetkey in i.street.lower():
            print("Stop:"+lines[index])
            c+=1
        index+=1
    if(c==0):
        print("There are no matches!")

def searchBySuburb(suburbkey):
    index =0
    c =0
    suburbkey = suburbkey.lower()
    for i in BusStops:
        if suburbkey in i.suburb.lower():
            print("Stop:"+lines[index])
            c+=1
        index+=1
    if(c==0):
        print("There are no matches!")

def searchByAnyField(key):
    index =0
    c=0
    key = key.lower()
    for i in BusStops:
        if key in i.street.lower() or key in i.name.lower() or key in i.suburb.lower():
            print("Stop:"+lines[index])
            c+=1
        index+=1
    if(c==0):
        print("There are no matches!")
loadData()
# Please uncomment the following commands and test the functions. 
#listAllBusStopNames()
#listAllStreetsOnRoute()
#listAllSuburbsOnRoute()
#searchByNumber(5,10)
#searchByNumber(-1,67)
#searchByNumber(1,670)
#searchByName("de")
#searchByName("deasdf")
#searchByStreet("de")
#searchByStreet("sdde")
#searchBySuburb("Bundoora")
#searchBySuburb("kjjde")
#searchByAnyField("gar")
#searchByAnyField("jjkgar")





