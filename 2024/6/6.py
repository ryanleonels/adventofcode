#!/usr/bin/python3

grid = []
visited = []
positions = 0
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row = len(grid)
col = len(grid[0])
x = -1
y = -1
dirx = -1
diry = 0
for i in range(0, row):
	visited.append([])
	for j in range(0, col):
		visited[i].append(False)
		if grid[i][j] == '^':
			visited[i][j] = True
			x = i
			y = j
done = False
while done == False:
	x1 = x + dirx
	y1 = y + diry
	if x1 < 0 or x1 >= row or y1 < 0 or y1 >= col:
		done = True
		break
	if grid[x1][y1] == '#':
		dirx1 = dirx
		diry1 = diry
		if dirx == -1 and diry == 0:
			dirx1 = 0
			diry1 = 1
		if dirx == 0 and diry == 1:
			dirx1 = 1
			diry1 = 0
		if dirx == 1 and diry == 0:
			dirx1 = 0
			diry1 = -1
		if dirx == 0 and diry == -1:
			dirx1 = -1
			diry1 = 0
		dirx = dirx1
		diry = diry1
	else:
		x = x1
		y = y1
		visited[x][y] = True
for i in range(0, row):
	for j in range(0, col):
		if visited[i][j] == True:
			positions += 1
print(positions)