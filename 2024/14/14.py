#!/usr/bin/python3

n = 0
pRobots = []
vRobots = []
(xSize, ySize) = (101, 103)
fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n += 1
	px = int(fileLine.split('p=')[1].split(' ')[0].split(',')[0])
	py = int(fileLine.split('p=')[1].split(' ')[0].split(',')[1])
	vx = int(fileLine.split('v=')[1].split(',')[0])
	vy = int(fileLine.split('v=')[1].split(',')[1])
	pRobots.append((px, py))
	vRobots.append((vx, vy))
quadrants = [0, 0, 0, 0]
for i in range(0, n):
	x = (pRobots[i][0] + (vRobots[i][0] * 100)) % xSize
	y = (pRobots[i][1] + (vRobots[i][1] * 100)) % ySize
	if x < xSize // 2 and y < ySize // 2:
		quadrants[0] += 1
	if x > xSize // 2 and y < ySize // 2:
		quadrants[1] += 1
	if x < xSize // 2 and y > ySize // 2:
		quadrants[2] += 1
	if x > xSize // 2 and y > ySize // 2:
		quadrants[3] += 1
safetyFactor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(safetyFactor)