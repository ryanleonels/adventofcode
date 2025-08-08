#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	row1 = [int(x) for x in list(fileLine.strip())]
	grid.append(row1)
row = len(grid)
col = len(grid[0])
n = 0
for i in range(0, row):
	for j in range(0, col):
		#check up
		visible = True
		for k in range(i - 1, -1, -1):
			if grid[k][j] >= grid[i][j]:
				visible = False
				break
		if visible:
			n += 1
			continue
		#check down
		visible = True
		for k in range(i + 1, row):
			if grid[k][j] >= grid[i][j]:
				visible = False
				break
		if visible:
			n += 1
			continue
		#check left
		visible = True
		for k in range(j - 1, -1, -1):
			if grid[i][k] >= grid[i][j]:
				visible = False
				break
		if visible:
			n += 1
			continue
		#check right
		visible = True
		for k in range(j + 1, col):
			if grid[i][k] >= grid[i][j]:
				visible = False
				break
		if visible:
			n += 1
			continue
print(n)
