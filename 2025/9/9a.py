#!/usr/bin/python3

import sys

tiles = []
maxArea = 0
(xSet, ySet) = (set(), set())
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y) = [int(x) for x in fileLine.strip().split(',')]
	tiles.append((x, y))
	xSet.add(x)
	ySet.add(y)
(xList, yList) = (list(sorted(xSet)), list(sorted(ySet)))
(nx, ny) = (len(xList), len(yList))
(xMap, yMap) = ({}, {})
for i in range(0, nx):
	xMap[xList[i]] = i
for i in range(0, ny):
	yMap[yList[i]] = i
n = len(tiles)
grid = []
for i in range(0, ny):
	grid.append([])
	for j in range(0, nx):
		grid[i].append('.')
for i in range(0, n):
	(x1, y1) = (xMap[tiles[i][0]], yMap[tiles[i][1]])
	(x2, y2) = (xMap[tiles[(i+1)%n][0]], yMap[tiles[(i+1)%n][1]])
	if x2 > x1 and y2 == y1:
		grid[y1][x1] = '#'
		for j in range(x1 + 1, x2):
			grid[y1][j] = 'X'
		grid[y2][x2] = '#'
	if x2 < x1 and y2 == y1:
		grid[y2][x2] = '#'
		for j in range(x2 + 1, x1):
			grid[y2][j] = 'X'
		grid[y1][x1] = '#'
	if y2 > y1 and x2 == x1:
		grid[y1][x1] = '#'
		for j in range(y1 + 1, y2):
			grid[j][x1] = 'X'
		grid[y2][x2] = '#'
	if y2 < y1 and x2 == x1:
		grid[y2][x2] = '#'
		for j in range(y2 + 1, y1):
			grid[j][x2] = 'X'
		grid[y1][x1] = '#'
"""for i in range(0, ny):
	print(''.join(grid[i]))"""
y0 = -1
for y in range(0, ny):
	prev = '.'
	nChange = 0
	if y0 == -1:
		x0 = -1
	for x in range(0, nx):
		if prev == '.' and grid[y][x] != '.':
			nChange += 1
		prev = grid[y][x]
		if grid[y][x] == '.' and y0 == -1 and x0 == -1 and nChange == 1:
			x0 = x
	if nChange == 2 and y0 == -1:
		y0 = y

sys.setrecursionlimit(nx * ny * 4)

def floodFill(y, x):
	if y < 0 or y >= ny or x < 0 or x >= nx or grid[y][x] != '.':
		return
	grid[y][x] = 'X'
	floodFill(y + 1, x)
	floodFill(y - 1, x)
	floodFill(y, x + 1)
	floodFill(y, x - 1)

floodFill(y0, x0)

"""for i in range(0, ny):
	print(''.join(grid[i]))"""

(countRow, countTotal) = ([], [])
for i in range(0, ny):
	countRow.append([])
	countTotal.append([])
	for j in range(0, nx):
		countRow[i].append(0)
		countTotal[i].append(0)
for i in range(0, ny):
	rowTotal = 0
	for j in range(0, nx):
		if grid[i][j] != '.':
			rowTotal += 1
		countRow[i][j] = rowTotal
for i in range(0, ny):
	for j in range(0, nx):
		if i == 0:
			countTotal[i][j] = countRow[i][j]
		else:
			countTotal[i][j] = countTotal[i - 1][j] + countRow[i][j]

for i in range(0, n - 1):
	for j in range(i + 1, n):
		(x1, y1) = (xMap[tiles[i][0]], yMap[tiles[i][1]])
		(x2, y2) = (xMap[tiles[j][0]], yMap[tiles[j][1]])
		(xmin, ymin) = (min(x1, x2) - 1, min(y1, y2) - 1)
		(xmax, ymax) = (max(x1, x2), max(y1, y2))
		area1 = (xmax - xmin) * (ymax - ymin)
		if ymin < 0 or xmin < 0:
			count00 = 0
		else:
			count00 = countTotal[ymin][xmin]
		if ymin < 0:
			count01 = 0
		else:
			count01 = countTotal[ymin][xmax] - count00
		if xmin < 0:
			count10 = 0
		else:
			count10 = countTotal[ymax][xmin] - count00
		count11 = countTotal[ymax][xmax] - count00 - count01 - count10
		if count11 == area1:
			x = abs(tiles[i][0] - tiles[j][0]) + 1
			y = abs(tiles[i][1] - tiles[j][1]) + 1
			area = x * y
			maxArea = max(area, maxArea)
print(maxArea)
