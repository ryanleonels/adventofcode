#!/usr/bin/python3

import math

trees = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))

(row, col) = (len(grid), len(grid[0]))
for i in range(0, row):
	if grid[i][(i * 3) % col] == '#':
		trees += 1
print(trees)