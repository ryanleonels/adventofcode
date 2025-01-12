#!/usr/bin/python3

def getTotal(obj):
	if type(obj) is list:
		curTotal = 0
		for obj1 in obj:
			curTotal += getTotal(obj1)
		return curTotal
	if type(obj) is dict:
		curTotal = 0
		for obj1 in obj:
			if obj[obj1] == "red":
				return 0
			curTotal += getTotal(obj[obj1])
		return curTotal
	if type(obj) is str:
		return 0
	if type(obj) is int:
		return obj
	if type(obj) is float:
		return obj
	return 0

total = 0
fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
json = fileData.strip()
obj = eval(json)
total = getTotal(obj)
print(total)