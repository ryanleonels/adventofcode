#!/usr/bin/python3

fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
clays = set()

area = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	area.append(list(fileLine))
(row, col) = (len(area), len(area[0]))
states = {}
curState = ""
for i in range(0, row):
	curState += ''.join(area[i])
states[curState] = 0
values = {}
(cycleStart, cycleLength) = (-1, 0)
for t in range(1, 1000000001):
	area1 = []
	for i in range(0, row):
		area1row = []
		for j in range(0, col):
			area1row.append(' ')
		area1.append(area1row)
	for i in range(0, row):
		for j in range(0, col):
			(nTree, nLumberyard) = (0, 0)
			for i1 in range(-1, 2):
				for j1 in range(-1, 2):
					if (i1 != 0 or j1 != 0) and i + i1 >= 0 and i + i1 < row and j + j1 >= 0 and j + j1 < col:
						if area[i + i1][j + j1] == '|':
							nTree += 1
						if area[i + i1][j + j1] == '#':
							nLumberyard += 1
			if area[i][j] == '.':
				if nTree >= 3:
					area1[i][j] = '|'
				else:
					area1[i][j] = '.'
			if area[i][j] == '|':
				if nLumberyard >= 3:
					area1[i][j] = '#'
				else:
					area1[i][j] = '|'
			if area[i][j] == '#':
				if nTree >= 1 and nLumberyard >= 1:
					area1[i][j] = '#'
				else:
					area1[i][j] = '.'
	area = area1
	(nTree, nLumberyard) = (0, 0)
	for i in range(0, row):
		for j in range(0, col):
			if area[i][j] == '|':
				nTree += 1
			if area[i][j] == '#':
				nLumberyard += 1
	#print(nTree, nLumberyard)
	print(t, nTree * nLumberyard)
	values[t] = nTree * nLumberyard
	curState = ""
	for i in range(0, row):
		curState += ''.join(area[i])
	if curState in states:
		(cycleStart, cycleLength) = (states[curState], t - states[curState])
		print("cycle detected: start=" + str(cycleStart) + " length=" + str(cycleLength))
		break
	else:
		states[curState] = t
t1 = (1000000000 - cycleStart) % cycleLength
print("1000000000 is in position " + str(t1) + " of the cycle")
print(values[cycleStart + t1])