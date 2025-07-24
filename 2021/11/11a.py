#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append([int(x) for x in list(fileLine)])
row = len(grid)
col = len(grid[0])
#flashes = 0
"""print(row, col)
for i in range(0, row):
	print(grid[i])"""
flashed = []
t = 0
while len(flashed) < row * col:
	flash = []
	flashed = []
	for i in range(0, row):
		for j in range(0, col):
			grid[i][j] += 1
			if grid[i][j] > 9:
				flash.append((i, j))
				flashed.append((i, j))
	while len(flash) > 0:
		for (x, y) in flash:
			for i in range(-1, 2):
				for j in range(-1, 2):
					if (i != 0 or j != 0) and (x + i) >= 0 and (x + i) < row and (y + j) >= 0 and (y + j) < col and (x + i, y + j) not in flashed:
						grid[x + i][y + j] += 1
		flash = []
		for i in range(0, row):
			for j in range(0, col):
				if grid[i][j] > 9 and (i, j) not in flashed:
					flash.append((i, j))
					flashed.append((i, j))
	for i in range(0, row):
		for j in range(0, col):
			if (i, j) in flashed:
				grid[i][j] = 0
	#flashes += len(flashed)
	t += 1
	"""if t % 10 == 0:
		print(t)
		for i in range(0, row):
			print(grid[i])"""
print(t)
