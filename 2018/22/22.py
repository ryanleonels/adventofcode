#!/usr/bin/python3

fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

(depth, targetX, targetY) = (0, 0, 0)

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:5] == "depth":
		depth = int(fileLine.split(': ')[1])
	if fileLine[:6] == "target":
		targetX = int(fileLine.split(': ')[1].split(',')[0])
		targetY = int(fileLine.split(': ')[1].split(',')[1])

geo1 = {}
geo1[(0, 0)] = 0
geo1[(targetX, targetY)] = 0

def ero(x):
	return (x + depth) % 20183

def geo(x, y):
	if (x, y) in geo1:
		return geo1[(x, y)]
	if y == 0:
		geoi = x * 16807
	if x == 0:
		geoi = y * 48271
	if x != 0 and y != 0:
		geoi = ero(geo(x - 1, y)) * ero(geo(x, y - 1))
	geo1[(x, y)] = geoi
	return geoi

riskLevel = 0
for i in range(0, targetX + 1):
	for j in range(0, targetY + 1):
		riskLevel += (ero(geo(i, j)) % 3)
print(riskLevel)