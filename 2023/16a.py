#!/usr/bin/python3

import sys

row = 0
col = 0
grid = []
tiles = []
beams = []

def countTiles():
	energized = 0
	for i in range(0, row):
		for j in range(0, col):
			if tiles[i][j] == True:
				energized += 1
	return energized

def resetTiles():
	beams.clear()
	for i in range(0, row):
		for j in range(0, col):
			tiles[i][j] = False
	return

def runBeam(x, y, heading):
	if x < 0 or x >= row or y < 0 or y >= col:
		return
	if (x, y, heading) in beams:
		return
	beams.append((x, y, heading))
	tiles[x][y] = True
	if grid[x][y] == '.':
		if heading == 'U':
			runBeam(x-1, y, 'U')
		if heading == 'D':
			runBeam(x+1, y, 'D')
		if heading == 'L':
			runBeam(x, y-1, 'L')
		if heading == 'R':
			runBeam(x, y+1, 'R')
	if grid[x][y] == '/':
		if heading == 'U':
			runBeam(x, y+1, 'R')
		if heading == 'D':
			runBeam(x, y-1, 'L')
		if heading == 'L':
			runBeam(x+1, y, 'D')
		if heading == 'R':
			runBeam(x-1, y, 'U')
	if grid[x][y] == '\\':
		if heading == 'U':
			runBeam(x, y-1, 'L')
		if heading == 'D':
			runBeam(x, y+1, 'R')
		if heading == 'L':
			runBeam(x-1, y, 'U')
		if heading == 'R':
			runBeam(x+1, y, 'D')
	if grid[x][y] == '|':
		if heading == 'U':
			runBeam(x-1, y, 'U')
		if heading == 'D':
			runBeam(x+1, y, 'D')
		if heading == 'L' or heading == 'R':
			runBeam(x-1, y, 'U')
			runBeam(x+1, y, 'D')
	if grid[x][y] == '-':
		if heading == 'U' or heading == 'D':
			runBeam(x, y-1, 'L')
			runBeam(x, y+1, 'R')
		if heading == 'L':
			runBeam(x, y-1, 'L')
		if heading == 'R':
			runBeam(x, y+1, 'R')
	return

maxEnergized = 0
fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = [".|...\\....","|.-.\\.....",".....|-...","........|.","..........",".........\\","..../.\\\\..",".-.-/..|..",".|....-|.\\","..//.|...."]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	grid.append(fileLine)
row = len(grid)
col = len(grid[0])
#print(str(row)+'x'+str(col))
for i in range(0, row):
	tiles.append([])
	for j in range(0, col):
		tiles[i].append(False)
sys.setrecursionlimit(row * col)
# top row
for i in range(0, col):
	resetTiles()
	runBeam(0, i, 'D')
	cnt = countTiles()
	best = False
	strBest = ""
	if cnt >= maxEnergized:
		best = True
		strBest = " (current best)"
		if cnt == maxEnergized:
			strBest += " - tied"
		maxEnergized = cnt
	print("top row, column " + str(i) + ": " + str(cnt) + " tiles energized" + strBest)
# bottom row
for i in range(0, col):
	resetTiles()
	runBeam(row-1, i, 'U')
	cnt = countTiles()
	best = False
	strBest = ""
	if cnt >= maxEnergized:
		best = True
		strBest = " (current best)"
		if cnt == maxEnergized:
			strBest += " - tied"
		maxEnergized = cnt
	print("bottom row, column " + str(i) + ": " + str(cnt) + " tiles energized" + strBest)
# leftmost column
for i in range(0, col):
	resetTiles()
	runBeam(i, 0, 'R')
	cnt = countTiles()
	best = False
	strBest = ""
	if cnt >= maxEnergized:
		best = True
		strBest = " (current best)"
		if cnt == maxEnergized:
			strBest += " - tied"
		maxEnergized = cnt
	print("leftmost column, row " + str(i) + ": " + str(cnt) + " tiles energized" + strBest)
# rightmost column
for i in range(0, col):
	resetTiles()
	runBeam(i, col-1, 'L')
	cnt = countTiles()
	best = False
	strBest = ""
	if cnt >= maxEnergized:
		best = True
		strBest = " (current best)"
		if cnt == maxEnergized:
			strBest += " - tied"
		maxEnergized = cnt
	print("rightmost column, row " + str(i) + ": " + str(cnt) + " tiles energized" + strBest)
print(maxEnergized)
