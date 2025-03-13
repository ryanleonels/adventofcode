#!/usr/bin/python3

fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

ranges = {}
maxDepth = 0
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	(depth, range1) = [int(x) for x in fileLine.split(': ')]
	ranges[depth] = range1
	maxDepth = max(depth, maxDepth)

def isCaught(delay):
	for depth in range(0, maxDepth + 1):
		if depth in ranges:
			range1 = ranges[depth]
			if range1 == 1 or (depth + delay) % ((range1 - 1) * 2) == 0:
				return True
	return False

delay = 0
caught = True
while caught:
	delay += 1
	if isCaught(delay) == False:
		caught = False
print(delay)