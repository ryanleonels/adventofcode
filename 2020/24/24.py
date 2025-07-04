#!/usr/bin/python3

sum1 = 0
fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

tiles = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y) = (0, 0)
	n = len(fileLine)
	(i, i1) = (0, 0)
	while i < n:
		if fileLine[i] == 'e':
			x += 2
			i1 = 1
		if fileLine[i:i+2] == 'se':
			x += 1
			y -= 1
			i1 = 2
		if fileLine[i:i+2] == 'sw':
			x -= 1
			y -= 1
			i1 = 2
		if fileLine[i] == 'w':
			x -= 2
			i1 = 1
		if fileLine[i:i+2] == 'nw':
			x -= 1
			y += 1
			i1 = 2
		if fileLine[i:i+2] == 'ne':
			x += 1
			y += 1
			i1 = 2
		i += i1
	#print(x, y)
	if (x, y) not in tiles:
		tiles[(x, y)] = 1
	else:
		tiles[(x, y)] = 1 - tiles[(x, y)]

nTiles = 0
for tile in tiles:
	if tiles[tile] == 1:
		nTiles += 1
print(nTiles)
