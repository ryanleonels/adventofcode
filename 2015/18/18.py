#!/usr/bin/python3

grid = []
fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
row = 0
col = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append([])
	col = len(fileLine)
	for i in range(0, col):
		if fileLine[i] == '#':
			grid[row].append(True)
		else:
			grid[row].append(False)
	row += 1
grid1 = []
for i in range(0, row):
	grid1.append([])
	for j in range(0, col):
		grid1[i].append(grid[i][j])
nStep = 100
for step in range(0, nStep):
	for i in range(0, row):
		for j in range(0, col):
			grid1[i][j] = grid[i][j]
	for i in range(0, row):
		for j in range(0, col):
			neighbor = 0
			if i > 0 and j > 0 and grid[i-1][j-1] == True:
				neighbor += 1
			if i > 0 and grid[i-1][j] == True:
				neighbor += 1
			if i > 0 and j < col - 1 and grid[i-1][j+1] == True:
				neighbor += 1
			if j > 0 and grid[i][j-1] == True:
				neighbor += 1
			if j < col - 1 and grid[i][j+1] == True:
				neighbor += 1
			if i < row - 1 and j > 0 and grid[i+1][j-1] == True:
				neighbor += 1
			if i < row - 1 and grid[i+1][j] == True:
				neighbor += 1
			if i < row - 1 and j < col - 1 and grid[i+1][j+1] == True:
				neighbor += 1
			if grid[i][j] == True and (neighbor < 2 or neighbor > 3):
				grid1[i][j] = False
			if grid[i][j] == False and neighbor == 3:
				grid1[i][j] = True
	for i in range(0, row):
		for j in range(0, col):
			grid[i][j] = grid1[i][j]
n = 0
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] == True:
			n += 1
print(n)