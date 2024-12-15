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
		line = fileLine.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
		room.append(list(line))
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
	if room[x1][y1] == '[' or room[x1][y1] == ']':
		nBoxes = 0
		(xbox, ybox) = (x1, y1)
		if dirx == 0:
			nbox = 0
			while room[xbox][ybox] == '[' or room[xbox][ybox] == ']':
				nbox += 1
				ybox += diry
			if room[xbox][ybox] == '.':
				for j in range(nbox, 0, -1):
					room[x][y+((j+1)*diry)] = room[x][y+(j*diry)]
				room[x1][y1] = '@'
				room[x][y] = '.'
				(x, y) = (x1, y1)
		else:
			boxes = set()
			boxes.add((x1, y1))
			#dirx = -1 if up / 1 if down
			cols = set()
			cols.add(y1)
			if room[x1][y1] == '[':
				boxes.add((x1, y1 + 1))
				cols.add(y1 + 1)
			if room[x1][y1] == ']':
				boxes.add((x1, y1 - 1))
				cols.add(y1 - 1)
			curRow = x1
			lastRow = x1
			nbox = 2
			#gwa = True
			while nbox > 0:
				cols1 = set()
				for y2 in cols:
					if room[curRow+dirx][y2] == '[':
						boxes.add((curRow+dirx, y2))
						boxes.add((curRow+dirx, y2 + 1))
						cols1.add(y2)
						cols1.add(y2 + 1)
						lastRow = curRow+dirx
					if room[curRow+dirx][y2] == ']':
						boxes.add((curRow+dirx, y2))
						boxes.add((curRow+dirx, y2 - 1))
						cols1.add(y2)
						cols1.add(y2 - 1)
						lastRow = curRow+dirx
				curRow += dirx
				cols = cols1
				nbox = len(cols1)
			wall = False
			for box in boxes:
				if room[box[0]+dirx][box[1]] == '#':
					wall = True
					break
			if wall == False:
				for j in range(lastRow, x1 - dirx, -dirx):
					for box in boxes:
						if box[0] == j:
							room[box[0]+dirx][box[1]] = room[box[0]][box[1]]
							if (box[0]-dirx, box[1]) not in boxes:
								room[box[0]][box[1]] = '.'
				room[x1][y1] = '@'
				room[x][y] = '.'
				(x, y) = (x1, y1)
coord = 0
for i in range(0, row):
	for j in range(0, col):
		if room[i][j] == '[':
			coord += (100 * i) + j
print(coord)