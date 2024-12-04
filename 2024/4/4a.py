#!/usr/bin/python3

n = 0
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
grid = fileData.split('\n')
row = len(grid) - 1
col = len(grid[0])
for i in range(1, row - 1):
	for j in range(0, col - 1):
		if grid[i][j] == 'A':
			if grid[i - 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S':
				n += 1
			if grid[i - 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M':
				n += 1
			if grid[i - 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'S':
				n += 1
			if grid[i - 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'M':
				n += 1
print(n)