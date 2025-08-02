#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
curCalories = 0
elves = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		elves.append(curCalories)
		curCalories = 0
		continue
	curCalories += int(fileLine)
if curCalories > 0:
	elves.append(curCalories) # just in case
elves = sorted(elves)
print(elves[-1] + elves[-2] + elves[-3])
