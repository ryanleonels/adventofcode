#!/usr/bin/python3

import sys

row = 0
col = 0
cityBlocks = []
minLoss = [] #row, col, dir (last dir: [UDLR](1-3))
maxHeatLoss = 1600 #needed to limit recursion, arbitrary as it's known that the first solution less than this value is quickly discovered
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
		if y < col - 10:
			sendCrucible(x, y+10, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4] + cityBlocks[x][y+5] + cityBlocks[x][y+6] + cityBlocks[x][y+7] + cityBlocks[x][y+8] + cityBlocks[x][y+9] + cityBlocks[x][y+10])
		if y < col - 9:
			sendCrucible(x, y+9, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4] + cityBlocks[x][y+5] + cityBlocks[x][y+6] + cityBlocks[x][y+7] + cityBlocks[x][y+8] + cityBlocks[x][y+9])
		if y < col - 8:
			sendCrucible(x, y+8, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4] + cityBlocks[x][y+5] + cityBlocks[x][y+6] + cityBlocks[x][y+7] + cityBlocks[x][y+8])
		if y < col - 7:
			sendCrucible(x, y+7, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4] + cityBlocks[x][y+5] + cityBlocks[x][y+6] + cityBlocks[x][y+7])
		if y < col - 6:
			sendCrucible(x, y+6, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4] + cityBlocks[x][y+5] + cityBlocks[x][y+6])
		if y < col - 5:
			sendCrucible(x, y+5, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4] + cityBlocks[x][y+5])
		if y < col - 4:
			sendCrucible(x, y+4, 'R', heatLoss + cityBlocks[x][y+1] + cityBlocks[x][y+2] + cityBlocks[x][y+3] + cityBlocks[x][y+4])
		if y >= 4:
			sendCrucible(x, y-4, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4])
		if y >= 5:
			sendCrucible(x, y-5, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4] + cityBlocks[x][y-5])
		if y >= 6:
			sendCrucible(x, y-6, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4] + cityBlocks[x][y-5] + cityBlocks[x][y-6])
		if y >= 7:
			sendCrucible(x, y-7, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4] + cityBlocks[x][y-5] + cityBlocks[x][y-6] + cityBlocks[x][y-7])
		if y >= 8:
			sendCrucible(x, y-8, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4] + cityBlocks[x][y-5] + cityBlocks[x][y-6] + cityBlocks[x][y-7] + cityBlocks[x][y-8])
		if y >= 9:
			sendCrucible(x, y-9, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4] + cityBlocks[x][y-5] + cityBlocks[x][y-6] + cityBlocks[x][y-7] + cityBlocks[x][y-8] + cityBlocks[x][y-9])
		if y >= 10:
			sendCrucible(x, y-10, 'L', heatLoss + cityBlocks[x][y-1] + cityBlocks[x][y-2] + cityBlocks[x][y-3] + cityBlocks[x][y-4] + cityBlocks[x][y-5] + cityBlocks[x][y-6] + cityBlocks[x][y-7] + cityBlocks[x][y-8] + cityBlocks[x][y-9] + cityBlocks[x][y-10])
	if dir1 == 'L' or dir1 == 'R':
		if x < row - 10:
			sendCrucible(x+10, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y] + cityBlocks[x+5][y] + cityBlocks[x+6][y] + cityBlocks[x+7][y] + cityBlocks[x+8][y] + cityBlocks[x+9][y] + cityBlocks[x+10][y])
		if x < row - 9:
			sendCrucible(x+9, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y] + cityBlocks[x+5][y] + cityBlocks[x+6][y] + cityBlocks[x+7][y] + cityBlocks[x+8][y] + cityBlocks[x+9][y])
		if x < row - 8:
			sendCrucible(x+8, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y] + cityBlocks[x+5][y] + cityBlocks[x+6][y] + cityBlocks[x+7][y] + cityBlocks[x+8][y])
		if x < row - 7:
			sendCrucible(x+7, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y] + cityBlocks[x+5][y] + cityBlocks[x+6][y] + cityBlocks[x+7][y])
		if x < row - 6:
			sendCrucible(x+6, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y] + cityBlocks[x+5][y] + cityBlocks[x+6][y])
		if x < row - 5:
			sendCrucible(x+5, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y] + cityBlocks[x+5][y])
		if x < row - 4:
			sendCrucible(x+4, y, 'D', heatLoss + cityBlocks[x+1][y] + cityBlocks[x+2][y] + cityBlocks[x+3][y] + cityBlocks[x+4][y])
		if x >= 4:
			sendCrucible(x-4, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y])
		if x >= 5:
			sendCrucible(x-5, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y] + cityBlocks[x-5][y])
		if x >= 6:
			sendCrucible(x-6, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y] + cityBlocks[x-5][y] + cityBlocks[x-6][y])
		if x >= 7:
			sendCrucible(x-7, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y] + cityBlocks[x-5][y] + cityBlocks[x-6][y] + cityBlocks[x-7][y])
		if x >= 8:
			sendCrucible(x-8, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y] + cityBlocks[x-5][y] + cityBlocks[x-6][y] + cityBlocks[x-7][y] + cityBlocks[x-8][y])
		if x >= 9:
			sendCrucible(x-9, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y] + cityBlocks[x-5][y] + cityBlocks[x-6][y] + cityBlocks[x-7][y] + cityBlocks[x-8][y] + cityBlocks[x-9][y])
		if x >= 10:
			sendCrucible(x-10, y, 'U', heatLoss + cityBlocks[x-1][y] + cityBlocks[x-2][y] + cityBlocks[x-3][y] + cityBlocks[x-4][y] + cityBlocks[x-5][y] + cityBlocks[x-6][y] + cityBlocks[x-7][y] + cityBlocks[x-8][y] + cityBlocks[x-9][y] + cityBlocks[x-10][y])

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
sendCrucible(0, 10, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4] + cityBlocks[0][5] + cityBlocks[0][6] + cityBlocks[0][7] + cityBlocks[0][8] + cityBlocks[0][9] + cityBlocks[0][10])
sendCrucible(0, 9, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4] + cityBlocks[0][5] + cityBlocks[0][6] + cityBlocks[0][7] + cityBlocks[0][8] + cityBlocks[0][9])
sendCrucible(0, 8, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4] + cityBlocks[0][5] + cityBlocks[0][6] + cityBlocks[0][7] + cityBlocks[0][8])
sendCrucible(0, 7, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4] + cityBlocks[0][5] + cityBlocks[0][6] + cityBlocks[0][7])
sendCrucible(0, 6, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4] + cityBlocks[0][5] + cityBlocks[0][6])
sendCrucible(0, 5, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4] + cityBlocks[0][5])
sendCrucible(0, 4, "R", cityBlocks[0][1] + cityBlocks[0][2] + cityBlocks[0][3] + cityBlocks[0][4])
sendCrucible(10, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0] + cityBlocks[5][0] + cityBlocks[6][0] + cityBlocks[7][0] + cityBlocks[8][0] + cityBlocks[9][0] + cityBlocks[10][0])
sendCrucible(9, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0] + cityBlocks[5][0] + cityBlocks[6][0] + cityBlocks[7][0] + cityBlocks[8][0] + cityBlocks[9][0])
sendCrucible(8, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0] + cityBlocks[5][0] + cityBlocks[6][0] + cityBlocks[7][0] + cityBlocks[8][0])
sendCrucible(7, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0] + cityBlocks[5][0] + cityBlocks[6][0] + cityBlocks[7][0])
sendCrucible(6, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0] + cityBlocks[5][0] + cityBlocks[6][0])
sendCrucible(5, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0] + cityBlocks[5][0])
sendCrucible(4, 0, "D", cityBlocks[1][0] + cityBlocks[2][0] + cityBlocks[3][0] + cityBlocks[4][0])
minHeatLoss = maxHeatLoss
for dir1 in minLoss[i][j]:
	if minLoss[i][j][dir1] < minHeatLoss:
		minHeatLoss = minLoss[i][j][dir1]
print(minHeatLoss)
