#!/usr/bin/python3

tiles = []
maxArea = 0
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y) = [int(x) for x in fileLine.strip().split(',')]
	tiles.append((x, y))
n = len(tiles)
for i in range(0, n - 1):
	for j in range(i + 1, n):
		x = abs(tiles[i][0] - tiles[j][0]) + 1
		y = abs(tiles[i][1] - tiles[j][1]) + 1
		area = x * y
		maxArea = max(area, maxArea)
print(maxArea)
