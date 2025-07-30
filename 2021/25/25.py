#!/usr/bin/python3

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))
row = len(grid)
col = len(grid[0])
eastHerd = []
southHerd = []
#print(row, col)
for i in range(0, row):
	#print(''.join(grid[i]))
	for j in range(0, col):
		if grid[i][j] == '>':
			eastHerd.append((i, j))
		if grid[i][j] == 'v':
			southHerd.append((i, j))
(nEast, nSouth) = (len(eastHerd), len(southHerd))

step = 0
moved = True
while moved:
	step += 1
	moved = False
	for i in range(0, nEast):
		(x, y) = eastHerd[i]
		y1 = (y + 1) % col
		if grid[x][y1] == '.':
			eastHerd[i] = (x, y1)
			moved = True
	for i in range(0, row):
		for j in range(0, col):
			grid[i][j] = '.'
	for i in range(0, nEast):
		grid[eastHerd[i][0]][eastHerd[i][1]] = '>'
	for i in range(0, nSouth):
		grid[southHerd[i][0]][southHerd[i][1]] = 'v'
	"""print(step)
	for i in range(0, row):
		print(''.join(grid[i]))"""
	for i in range(0, nSouth):
		(x, y) = southHerd[i]
		x1 = (x + 1) % row
		if grid[x1][y] == '.':
			southHerd[i] = (x1, y)
			moved = True
	for i in range(0, row):
		for j in range(0, col):
			grid[i][j] = '.'
	for i in range(0, nEast):
		grid[eastHerd[i][0]][eastHerd[i][1]] = '>'
	for i in range(0, nSouth):
		grid[southHerd[i][0]][southHerd[i][1]] = 'v'
	"""print(step)
	for i in range(0, row):
		print(''.join(grid[i]))"""
print(step)
