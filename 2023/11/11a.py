#!/usr/bin/python3

sumLengths = 0
galaxies = []
emptyX = []
emptyY = []
fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["...#......",".......#..","#.........","..........","......#...",".#........",".........#","..........",".......#..","#...#....."]
nRow = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	nRow += 1
nCol = len(fileLines[0])
for i in range(0, nRow):
	empty = True
	for j in range(0, nCol):
		if fileLines[i][j] == '#':
			empty = False
			galaxies.append((i, j))
	if empty == True:
		emptyX.append(i)
for i in range(0, nCol):
	empty = True
	for j in range(0, nRow):
		if fileLines[j][i] == '#':
			empty = False
	if empty == True:
		emptyY.append(i)
n = len(galaxies)
expansionRate = 1000000
for i in range(0, n-1):
	for j in range(i+1, n):
		if galaxies[i][0] < galaxies[j][0]:
			xmin = galaxies[i][0]
			xmax = galaxies[j][0]
		else:
			xmin = galaxies[j][0]
			xmax = galaxies[i][0]
		if galaxies[i][1] < galaxies[j][1]:
			ymin = galaxies[i][1]
			ymax = galaxies[j][1]
		else:
			ymin = galaxies[j][1]
			ymax = galaxies[i][1]
		length = (xmax - xmin) + (ymax - ymin)
		for k in range(xmin, xmax):
			if k in emptyX:
				length += (expansionRate - 1)
		for k in range(ymin, ymax):
			if k in emptyY:
				length += (expansionRate - 1)
		sumLengths += length
print(sumLengths)
