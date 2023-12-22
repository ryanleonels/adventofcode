#!/usr/bin/python3

bricks = []
grid = []
fall = []
fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["1,0,1~1,2,1","0,0,2~2,0,2","0,2,3~2,2,3","0,0,4~0,2,4","2,0,5~2,2,5","0,1,6~2,1,6","1,1,8~1,1,9"]
# parse brick coordinates
n = 0
xmin = 999
xmax = -999
ymin = 999
ymax = -999
zmin = 999
zmax = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	x0 = int(fileLine.split('~')[0].split(',')[0])
	if x0 < xmin:
		xmin = x0
	y0 = int(fileLine.split('~')[0].split(',')[1])
	if y0 < ymin:
		ymin = y0
	z0 = int(fileLine.split('~')[0].split(',')[2])
	if z0 < zmin:
		zmin = z0
	x1 = int(fileLine.split('~')[1].split(',')[0])
	if x1 > xmax:
		xmax = x1
	y1 = int(fileLine.split('~')[1].split(',')[1])
	if y1 > ymax:
		ymax = y1
	z1 = int(fileLine.split('~')[1].split(',')[2])
	if z1 > zmax:
		zmax = z1
	bricks.append([(x0,y0,z0),(x1,y1,z1)])
	n += 1
#print([(xmin,ymin,zmin),(xmax,ymax,zmax)])
n = len(bricks)
#print(bricks)
# setup grid
for i in range(0, xmax + 1):
	grid.append([])
	for j in range(0, ymax + 1):
		grid[i].append([])
		for k in range(0, zmax + 1):
			grid[i][j].append(-1)
# put bricks to grid
x = 0
for brick in bricks:
	for i in range(brick[0][0], brick[1][0] + 1):
		for j in range(brick[0][1], brick[1][1] + 1):
			for k in range(brick[0][2], brick[1][2] + 1):
				grid[i][j][k] = x
	x += 1
	fall.append(0)
# sort bricks by z for fall simulations
bricksOrder = []
for i in range(1, zmax + 1):
	for j in range(0, n):
		if bricks[j][0][2] == i:
			bricksOrder.append(j)
#print(bricksOrder)
# simulate bricks falling
settled = False
while settled == False:
	settled = True
	#check if bricks can fall down one step
	for i in range(0, n):
		brick = bricks[bricksOrder[i]]
		brickCanFall = True
		for j in range(brick[0][0], brick[1][0] + 1):
			for k in range(brick[0][1], brick[1][1] + 1):
				newZ = brick[0][2] - (fall[bricksOrder[i]] + 1)
				if newZ < 1 or grid[j][k][newZ] != -1:
					brickCanFall = False
		#if they can, do push them down
		if brickCanFall == True:
			settled = False
			for j in range(brick[0][0], brick[1][0] + 1):
				for k in range(brick[0][1], brick[1][1] + 1):
					newZ = brick[0][2] - (fall[bricksOrder[i]] + 1)
					oldZ = brick[1][2] - fall[bricksOrder[i]]
					grid[j][k][newZ] = bricksOrder[i]
					grid[j][k][oldZ] = -1
			fall[bricksOrder[i]] += 1
			#print("brick " + str(bricksOrder[i]) + " falls down one step")
# debug: show final state
"""for i in range(0, zmax + 1):
	print(i)
	grid1 = []
	for j in range(0, xmax + 1):
		grid1.append([])
		for k in range(0, ymax + 1):
			grid1[j].append(grid[j][k][i])
		print(grid1[j])"""
# check which bricks support which bricks
supportList = []
for i in range(0, n):
	supportList.append([])
	brick = bricks[i]
	finalZ = bricks[i][0][2] - fall[i]
	#print(finalZ)
	for j in range(brick[0][0], brick[1][0] + 1):
		for k in range(brick[0][1], brick[1][1] + 1):
			belowZ = brick[0][2] - (fall[i] + 1)
			if grid[j][k][belowZ] != -1 and grid[j][k][belowZ] not in supportList[i]:
				supportList[i].append(grid[j][k][belowZ])
#print(supportList)
nBricks = n
for i in range(0, n):
	if [i] in supportList: # if a block is sole support of another block
		#print(i)
		nBricks -= 1
print(nBricks)
