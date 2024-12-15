#!/usr/bin/python3

room = []
moves = ""
(x, y) = (-1, -1)
fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
roomDone = False
for fileLine in fileLines:
	if fileLine.strip() == '':
		roomDone = True
		continue
	if roomDone == True:
		moves += fileLine.strip()
	else:
		room.append(list(fileLine))
row = len(room)
col = len(room[0])
for i in range(0, row):
	for j in range(0, col):
		if room[i][j] == '@':
			(x, y) = (i, j)
n = len(moves)
for i in range(0, n):
	(dirx, diry) = (0, 0)
	if moves[i] == '^':
		(dirx, diry) = (-1, 0)
	if moves[i] == 'v':
		(dirx, diry) = (1, 0)
	if moves[i] == '<':
		(dirx, diry) = (0, -1)
	if moves[i] == '>':
		(dirx, diry) = (0, 1)
	(x1, y1) = (x + dirx, y + diry)
	if room[x1][y1] == '.':
		room[x1][y1] = '@'
		room[x][y] = '.'
		(x, y) = (x1, y1)
	if room[x1][y1] == 'O':
		nBoxes = 0
		(xbox, ybox) = (x1, y1)
		while room[xbox][ybox] == 'O':
			(xbox, ybox) = (xbox + dirx, ybox + diry)
		if room[xbox][ybox] == '.':
			room[x1][y1] = '@'
			room[x][y] = '.'
			room[xbox][ybox] = 'O'
			(x, y) = (x1, y1)
coord = 0
for i in range(0, row):
	for j in range(0, col):
		if room[i][j] == 'O':
			coord += (100 * i) + j
print(coord)