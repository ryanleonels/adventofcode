#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(curCalories, maxCalories) = (0, 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		maxCalories = max(maxCalories, curCalories)
		curCalories = 0
		continue
	curCalories += int(fileLine)
maxCalories = max(maxCalories, curCalories) # just in case
print(maxCalories)
