#!/usr/local/bin/python3

fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))

(nrow, ncol) = (len(grid), len(grid[0]))
"""print(nrow, ncol)
for i in range(0, nrow):
	print(''.join(grid[i]))"""

infGrid = {}
for i in range(0, nrow):
	for j in range(0, ncol):
		if grid[i][j] == '#':
			infGrid[(i, j)] = True
		else:
			infGrid[(i, j)] = False

(rowmin, rowmax, colmin, colmax) = (0, nrow - 1, 0, ncol - 1)
carrierPos = (nrow // 2, ncol // 2)
carrierDir = (-1, 0)

n = 10000
bursts = 0
infected = 0
while bursts < n:
	if carrierPos not in infGrid:
		infGrid[carrierPos] = False
		rowmin = min(rowmin, carrierPos[0])
		rowmax = max(rowmax, carrierPos[0])
		colmin = min(colmin, carrierPos[1])
		colmax = max(colmax, carrierPos[1])
	turn = 'L'
	if infGrid[carrierPos] == True:
		turn = 'R'
	if (turn, carrierDir) == ('L', (-1, 0)):
		(turn, carrierDir) = ('', (0, -1))
	if (turn, carrierDir) == ('R', (-1, 0)):
		(turn, carrierDir) = ('', (0, 1))
	if (turn, carrierDir) == ('L', (0, 1)):
		(turn, carrierDir) = ('', (-1, 0))
	if (turn, carrierDir) == ('R', (0, 1)):
		(turn, carrierDir) = ('', (1, 0))
	if (turn, carrierDir) == ('L', (1, 0)):
		(turn, carrierDir) = ('', (0, 1))
	if (turn, carrierDir) == ('R', (1, 0)):
		(turn, carrierDir) = ('', (0, -1))
	if (turn, carrierDir) == ('L', (0, -1)):
		(turn, carrierDir) = ('', (1, 0))
	if (turn, carrierDir) == ('R', (0, -1)):
		(turn, carrierDir) = ('', (-1, 0))
	infGrid[carrierPos] = not infGrid[carrierPos]
	if infGrid[carrierPos]:
		infected += 1
	carrierPos = (carrierPos[0] + carrierDir[0], carrierPos[1] + carrierDir[1])
	bursts += 1

print(infected)
