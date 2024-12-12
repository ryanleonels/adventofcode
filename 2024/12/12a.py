#!/usr/bin/python3

totalPrice = 0
row = 0
col = 0
grid = []
regionMap = []
regions = {}
fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row = len(grid)
col = len(grid[0])
for i in range(0, row):
	regionMap.append([])
	for j in range(0, col):
		regionMap[i].append(0)
curRegion = 0
for i in range(0, row):
	for j in range(0, col):
		if regionMap[i][j] == 0:
			curRegion += 1
			regions[curRegion] = set()
			regionStack = []
			regionStack.append((i, j))
			while len(regionStack) > 0:
				(x, y) = regionStack.pop()
				regionMap[x][y] = curRegion
				regions[curRegion].add((x, y))
				if x > 0 and grid[x - 1][y] == grid[x][y] and regionMap[x - 1][y] == 0:
					regionStack.append((x - 1, y))
				if x < row - 1 and grid[x + 1][y] == grid[x][y] and regionMap[x + 1][y] == 0:
					regionStack.append((x + 1, y))
				if y > 0 and grid[x][y - 1] == grid[x][y] and regionMap[x][y - 1] == 0:
					regionStack.append((x, y - 1))
				if y < col - 1 and grid[x][y + 1] == grid[x][y] and regionMap[x][y + 1] == 0:
					regionStack.append((x, y + 1))
for region in regions:
	area = len(regions[region])
	sides = 0
	for i in range(0, row + 1):
		fenceType = 0
		for j in range(0, col):
			onFence = False
			if ((i - 1, j) not in regions[region] and (i, j) in regions[region]):
				if fenceType != 1:
					sides += 1
				fenceType = 1
				onFence = True
			if ((i - 1, j) in regions[region] and (i, j) not in regions[region]):
				if fenceType != 2:
					sides += 1
				fenceType = 2
				onFence = True
			if onFence == False:
				fenceType = 0
	for i in range(0, col + 1):
		fenceType = 0
		for j in range(0, row):
			onFence = False
			if ((j, i - 1) not in regions[region] and (j, i) in regions[region]):
				if fenceType != 1:
					sides += 1
				fenceType = 1
				onFence = True
			if ((j, i - 1) in regions[region] and (j, i) not in regions[region]):
				if fenceType != 2:
					sides += 1
				fenceType = 2
				onFence = True
			if onFence == False:
				fenceType = 0
	price = area * sides
	#print((area, sides, price))
	totalPrice += price
print(totalPrice)