#!/usr/bin/python3

import sys

def inPipe(pipex, pipey, posx, posy):
	if pipex < 0 or pipex >= nRow or pipey < 0 or pipey >= nCol or posx < 0 or posx >= nRow or posy < 0 or posy >= nCol:
		return False
	if len(pipes[pipex][pipey]) < 2:
		return False
	if pipes[pipex][pipey][0][0] == posx and pipes[pipex][pipey][0][1] == posy:
		return True
	if pipes[pipex][pipey][1][0] == posx and pipes[pipex][pipey][1][1] == posy:
		return True
	return False

def nextPos(pipex, pipey, prevx, prevy):
	if pipex < 0 or pipex >= nRow or pipey < 0 or pipey >= nCol or prevx < 0 or prevx >= nRow or prevy < 0 or prevy >= nCol:
		return (-1. -1)
	if len(pipes[pipex][pipey]) < 2:
		return (-1. -1)
	if pipes[pipex][pipey][0][0] == prevx and pipes[pipex][pipey][0][1] == prevy:
		return pipes[pipex][pipey][1]
	if pipes[pipex][pipey][1][0] == prevx and pipes[pipex][pipey][1][1] == prevy:
		return pipes[pipex][pipey][0]
	return (-1. -1)

def flood_fill(x, y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= nRow or y < 0 or y >= nCol:
        return
    # secondly, check if the current position equals the old value
    if loopMap[y][x] != old:
        return
    # thirdly, set the current position to the new value
    loopMap[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)
    flood_fill(x+1, y+1, old, new)
    flood_fill(x+1, y-1, old, new)
    flood_fill(x-1, y+1, old, new)
    flood_fill(x-1, y-1, old, new)

inLoop = 0
pipes = []
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nRow = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	nRow += 1
nCol = len(fileLines[0])
sys.setrecursionlimit(nRow * nCol)
sx = -1
sy = -1
for i in range(0, nRow):
	pipes.append([])
	for j in range(0, nCol):
		pipes[i].append([])
		pipe = []
		pipeCh = fileLines[i][j]
		if pipeCh == '|':
			pipe = [(i-1, j), (i+1, j)]
		if pipeCh == '-':
			pipe = [(i, j-1), (i, j+1)]
		if pipeCh == 'L':
			pipe = [(i-1, j), (i, j+1)]
		if pipeCh == 'J':
			pipe = [(i-1, j), (i, j-1)]
		if pipeCh == '7':
			pipe = [(i+1, j), (i, j-1)]
		if pipeCh == 'F':
			pipe = [(i+1, j), (i, j+1)]
		if pipeCh == '.':
			pipe = []
		if pipeCh == 'S':
			sx = i
			sy = j
		pipes[i][j] = pipe
if inPipe(sx-1, sy, sx, sy):
	pipes[sx][sy].append((sx-1, sy))
if inPipe(sx+1, sy, sx, sy):
	pipes[sx][sy].append((sx+1, sy))
if inPipe(sx, sy-1, sx, sy):
	pipes[sx][sy].append((sx, sy-1))
if inPipe(sx, sy+1, sx, sy):
	pipes[sx][sy].append((sx, sy+1))
nSteps = 0
curPos = (sx, sy)
prevPos = (pipes[sx][sy][0][0], pipes[sx][sy][0][1])
loopMap = []
for i in range(0, nRow):
	loopMap.append([])
	for j in range(0, nCol):
		loopMap[i].append(0)
while curPos[0] != sx or curPos[1] != sy or nSteps == 0:
	temp = curPos
	curPos = nextPos(curPos[0], curPos[1], prevPos[0], prevPos[1])
	prevPos = temp
	nSteps += 1
	if curPos[0] == -1 or curPos[1] == -1:
		print("ERROR: out of pipes after " + str(nSteps) + " steps")
		exit(1)
	loopMap[curPos[0]][curPos[1]] = 1
flood_fill(0, 0, 0, 2)
flood_fill(0, nCol-1, 0, 2)
flood_fill(nRow-1, 0, 0, 2)
flood_fill(nRow-1, nCol-1, 0, 2)
loopsMap = []
for i in range(0, nRow):
	loops = ""
	for j in range(0, nCol):
		if loopMap[i][j] == 0:
			loops += "█"
			inLoop += 1
		if loopMap[i][j] == 1:
			#loops += fileLines[i][j]
			pipeCh = fileLines[i][j]
			if pipeCh == '|':
				loops += "│"
			if pipeCh == '-':
				loops += "─"
			if pipeCh == 'L':
				loops += "└"
			if pipeCh == 'J':
				loops += "┘"
			if pipeCh == '7':
				loops += "┐"
			if pipeCh == 'F':
				loops += "┌"
			if pipeCh == '.':
				loops += "▓" # should not exist
			if pipeCh == 'S':
				loops += "┐" # determined to be this one
		if loopMap[i][j] == 2:
			loops += " "
	loopsMap.append(loops)
	#print(loops)
#print("to be reviewed, <= " + str(inLoop))
inLoop = 0
for i in range(0, nRow):
	for j in range(0, nCol):
		if loopsMap[i][j] == '█':
			jleft = j - 1
			while loopsMap[i][jleft] != ' ' and jleft > 0:
				jleft -= 1
			jright = j + 1
			while loopsMap[i][jright] != ' ' and jright < nCol - 1:
				jright += 1
			wallLeft = 0
			state = 0 # 0 = not on horizontal wall, 1 = from up, 2 = from down
			for j1 in range(jleft, j):
				if loopsMap[i][j1] == '│':
					wallLeft += 1
				if loopsMap[i][j1] == '└' or loopsMap[i][j1] == '┘':
					if state == 0:
						state = 1
					elif state == 1:
						state = 0
					elif state == 2:
						state = 0
						wallLeft += 1
						#print(j1)
				if loopsMap[i][j1] == '┌' or loopsMap[i][j1] == '┐':
					if state == 0:
						state = 2
					elif state == 1:
						state = 0
						wallLeft += 1
						#print(j1)
					elif state == 2:
						state = 0
			#print(str(i) + ", " + str(j) + ": jleft = " + str(jleft) + ", jright = " + str(jright), "wallLeft = " + str(wallLeft))
			if wallLeft % 2 == 1:
				inLoop += 1
print(inLoop)
