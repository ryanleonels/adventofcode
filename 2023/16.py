#!/usr/bin/python3

import sys

row = 0
col = 0
grid = []
tiles = []
beams = []

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
runBeam(0, 0, 'R')
energized = 0
for i in range(0, row):
	for j in range(0, col):
		if tiles[i][j] == True:
			energized += 1
print(energized)
