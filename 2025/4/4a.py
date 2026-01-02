#!/usr/bin/python3

n = 0
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
grid = fileData.split('\n')
row = len(grid) - 1
col = len(grid[0])
for i in range(0, row):
	grid[i] = list(grid[i])
done = False
while not done:
	n1 = 0
	removals = set()
	for i in range(0, row):
		for j in range(0, col):
			if grid[i][j] == '@':
				adj = 0
				for i1 in [-1, 0, 1]:
					for j1 in [-1, 0, 1]:
						if (i1 != 0 or j1 != 0) and i + i1 >= 0 and i + i1 < row and j + j1 >= 0 and j + j1 < col:
							if grid[i + i1][j + j1] == '@':
								adj += 1
				if adj < 4:
					n1 += 1
					removals.add((i, j))
	n += n1
	if n1 == 0:
		done = True
	else:
		for (i, j) in removals:
			grid[i][j] = '.'
print(n)
