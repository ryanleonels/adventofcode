#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = fileData.strip().split(',')
n = len(steps)

def getDist(x, y):
	dist = 0
	(x1, y1) = (abs(x), abs(y))
	if x1 >= y1:
		dist = x1
	else:
		dist = x1 + ((y1 - x1) // 2)
	return dist

(x, y) = (0, 0)
maxDist = 0
for i in range(0, n):
	step = steps[i]
	if step == "n":
		(x, y) = (x, y + 2)
	if step == "nw":
		(x, y) = (x - 1, y + 1)
	if step == "ne":
		(x, y) = (x + 1, y + 1)
	if step == "s":
		(x, y) = (x, y - 2)
	if step == "sw":
		(x, y) = (x - 1, y - 1)
	if step == "se":
		(x, y) = (x + 1, y - 1)
	curDist = getDist(x, y)
	maxDist = max(curDist, maxDist)

print(maxDist)