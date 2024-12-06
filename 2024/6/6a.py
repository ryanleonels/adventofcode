#!/usr/bin/python3

n = 0
grid = []
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
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] == '^':
			x0 = i
			y0 = j
for i in range(0, row):
	print("Processing row " + str(i) + "...")
	for j in range(0, col):
		if grid[i][j] == '.':
			done = False
			loop = False
			x = x0
			y = y0
			dirx = -1
			diry = 0
			dir1 = 0
			visited = {(x0, y0, 0)}
			while done == False:
				x1 = x + dirx
				y1 = y + diry
				if x1 < 0 or x1 >= row or y1 < 0 or y1 >= col:
					done = True
					break
				if grid[x1][y1] == '#' or (x1 == i and y1 == j):
					dirx1 = dirx
					diry1 = diry
					if dirx == -1 and diry == 0:
						dirx1 = 0
						diry1 = 1
						dir1 = 1
					if dirx == 0 and diry == 1:
						dirx1 = 1
						diry1 = 0
						dir1 = 2
					if dirx == 1 and diry == 0:
						dirx1 = 0
						diry1 = -1
						dir1 = 3
					if dirx == 0 and diry == -1:
						dirx1 = -1
						diry1 = 0
						dir1 = 0
					dirx = dirx1
					diry = diry1
				else:
					x = x1
					y = y1
				if (x, y, dir1) in visited:
					done = True
					loop = True
					break
				visited.add((x, y, dir1))
			if loop == True:
				n += 1
				print([i, j])
print(n)