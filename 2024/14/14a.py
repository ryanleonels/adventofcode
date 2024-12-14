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
t = 0
grid = []
for i in range(0, ySize):
	grid.append([])
	for j in range(0, xSize):
		grid[i].append(0)
maxn = 0
for t in range(0, xSize * ySize):
	if t % 100 == 0:
		print(t)
	for i in range(0, ySize):
		for j in range(0, xSize):
			grid[i][j] = 0
	for i in range(0, n):
		x = (pRobots[i][0] + (vRobots[i][0] * t)) % xSize
		y = (pRobots[i][1] + (vRobots[i][1] * t)) % ySize
		grid[y][x] += 1
	xmas = False
	for i in range(0, ySize):
		for j in range(0, xSize - 10):
			xmas = True
			for k in range(0, 10):
				if grid[i][j+k] != 1:
					xmas = False
					break
			if xmas == True:
				break
		if xmas == True:
			break
	if xmas == True:
		break
print(t)
for i in range(0, ySize):
	line = ""
	for j in range(0, xSize):
		line += chr(grid[i][j]+48)
	print(line)