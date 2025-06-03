#!/usr/bin/python3

import math

(trees1, trees2, trees3, trees4, trees5) = (0, 0, 0, 0, 0)
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
	if grid[i][i % col] == '#':
		trees1 += 1
	if grid[i][(i * 3) % col] == '#':
		trees2 += 1
	if grid[i][(i * 5) % col] == '#':
		trees3 += 1
	if grid[i][(i * 7) % col] == '#':
		trees4 += 1
for i in range(0, row, 2):
	if grid[i][(i // 2) % col] == '#':
		trees5 += 1
print(trees1 * trees2 * trees3 * trees4 * trees5)
