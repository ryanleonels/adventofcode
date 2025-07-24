#!/usr/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
heightMap = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	heightMap.append([int(x) for x in list(fileLine)])
row = len(heightMap)
col = len(heightMap[0])
lowPoints = []
for i in range(0, row):
	for j in range(0, col):
		lowPoint = True
		if i > 0 and heightMap[i - 1][j] <= heightMap[i][j]:
			lowPoint = False
		if i < row - 1 and heightMap[i + 1][j] <= heightMap[i][j]:
			lowPoint = False
		if j > 0 and heightMap[i][j - 1] <= heightMap[i][j]:
			lowPoint = False
		if j < col - 1 and heightMap[i][j + 1] <= heightMap[i][j]:
			lowPoint = False
		if lowPoint == True:
			lowPoints.append((i, j))
n = len(lowPoints)
basin = {}
basins = []
for i in range(0, n):
	basin[lowPoints[i]] = i
	basins.append(0)

def getBasin(x, y):
	if (x, y) in basin:
		return basin[(x, y)]
	if heightMap[x][y] == 9:
		basin[(x, y)] = -1
		return -1
	min1 = heightMap[x][y]
	nextPoint = (x, y)
	if x > 0 and heightMap[x - 1][y] < min1:
		min1 = heightMap[x - 1][y]
		nextPoint = (x - 1, y)
	if x < row - 1 and heightMap[x + 1][y] < min1:
		min1 = heightMap[x + 1][y]
		nextPoint = (x + 1, y)
	if y > 0 and heightMap[x][y - 1] < min1:
		min1 = heightMap[x][y - 1]
		nextPoint = (x, y - 1)
	if y < col - 1 and heightMap[x][y + 1] < min1:
		min1 = heightMap[x][y + 1]
		nextPoint = (x, y + 1)
	basin1 = getBasin(nextPoint[0], nextPoint[1])
	basin[(x, y)] = basin1
	return basin1

for i in range(0, row):
	for j in range(0, col):
		curBasin = getBasin(i, j)
		if curBasin != -1:
			basins[curBasin] += 1

basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])
