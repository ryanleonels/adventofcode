#!/usr/bin/python3

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

maxDist = 0
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
while curPos[0] != sx or curPos[1] != sy or nSteps == 0:
	temp = curPos
	curPos = nextPos(curPos[0], curPos[1], prevPos[0], prevPos[1])
	prevPos = temp
	nSteps += 1
	if curPos[0] == -1 or curPos[1] == -1:
		print("ERROR: out of pipes after " + str(nSteps) + " steps")
		exit(1)
maxDist = int(nSteps / 2)
print(maxDist)
