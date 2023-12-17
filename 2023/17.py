#!/usr/bin/python3

import sys

row = 0
col = 0
cityBlocks = []
minLoss = [] #row, col, dir (last dir: [UDLR](1-3))
maxHeatLoss = 1500 #needed to limit recursion, arbitrary as it's known that the first solution less than this value is quickly discovered
curBest = maxHeatLoss

def sendCrucible(x, y, dir1, heatLoss):
	if heatLoss >= minLoss[x][y][dir1]:
		return
	minLoss[x][y][dir1] = heatLoss
	global curBest
	if x == row - 1 and y == col - 1 and heatLoss < curBest:
		curBest = heatLoss
		print("goal reached at " + str(heatLoss))
	if dir1 == 'U' or dir1 == 'D':
		if y < col - 3:
			sendCrucible(x, y+3, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3])
		if y < col - 2:
			sendCrucible(x, y+2, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2])
		if y < col - 1:
			sendCrucible(x, y+1, 'R', heatLoss + cityBlocks[x][y+1])
		if y >= 1:
			sendCrucible(x, y-1, 'L', heatLoss + cityBlocks[x][y-1])
		if y >= 2:
			sendCrucible(x, y-2, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2])
		if y >= 3:
			sendCrucible(x, y-3, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3])
	if dir1 == 'L' or dir1 == 'R':
		if x < row - 3:
			sendCrucible(x+3, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y])
		if x < row - 2:
			sendCrucible(x+2, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y])
		if x < row - 1:
			sendCrucible(x+1, y, 'D', heatLoss + cityBlocks[x+1][y])
		if x >= 1:
			sendCrucible(x-1, y, 'U', heatLoss + cityBlocks[x-1][y])
		if x >= 2:
			sendCrucible(x-2, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y])
		if x >= 3:
			sendCrucible(x-3, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y])

minHeatLoss = 0
fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["2413432311323","3215453535623","3255245654254","3446585845452","4546657867536","1438598798454","4457876987766","3637877979653","4654967986887","4564679986453","1224686865563","2546548887735","4322674655533"]
row = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	cityBlocks.append([])
	for i in range(0, len(fileLine)):
		cityBlocks[row].append(0)
		if fileLine[i] >= '1' and fileLine[i] <= '9':
			cityBlocks[row][i] = int(fileLine[i])
	row += 1
row = len(cityBlocks)
col = len(cityBlocks[0])
#print(str(row)+'x'+str(col))
#for i in range(0, row):
	#print(cityBlocks[i])
sys.setrecursionlimit(row * col * 4)
for i in range(0, row):
	minLoss.append([])
	for j in range(0, col):
		minLoss[i].append({})
		minLoss[i][j]['U'] = maxHeatLoss
		minLoss[i][j]['D'] = maxHeatLoss
		minLoss[i][j]['L'] = maxHeatLoss
		minLoss[i][j]['R'] = maxHeatLoss
minLoss[0][0]['U'] = 0
minLoss[0][0]['D'] = 0
minLoss[0][0]['L'] = 0
minLoss[0][0]['R'] = 0
sendCrucible(0, 3, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3])
sendCrucible(0, 2, "R", cityBlocks[0][1] + cityBlocks[0][2])
sendCrucible(0, 1, "R", cityBlocks[0][1])
sendCrucible(3, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0])
sendCrucible(2, 0, "D", cityBlocks[1][0] + cityBlocks[2][0])
sendCrucible(1, 0, "D", cityBlocks[1][0])
minHeatLoss = maxHeatLoss
for dir1 in minLoss[i][j]:
	if minLoss[i][j][dir1] < minHeatLoss:
		minHeatLoss = minLoss[i][j][dir1]
print(minHeatLoss)
