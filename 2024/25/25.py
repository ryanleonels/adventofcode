#!/usr/local/bin/python3

nLock = 0
nKey = 0
locks = set()
keys = set()
locksRaw = []
keysRaw = []
lineType = "empty"

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		lineType = "empty"
		continue
	if lineType == "empty":
		if fileLine == "#####":
			lineType = "lock"
			locksRaw.append([])
			nLock += 1
		if fileLine == ".....":
			lineType = "key"
			keysRaw.append([])
			nKey += 1
	if lineType == "lock":
		locksRaw[nLock - 1].append(fileLine)
	if lineType == "key":
		keysRaw[nKey - 1].append(fileLine)

for i in range(0, nLock):
	height = len(locksRaw[i])
	pins = [-1, -1, -1, -1, -1]
	for j in range(1, height):
		for k in range(0, 5):
			if locksRaw[i][j][k] == '.' and pins[k] == -1:
				pins[k] = j - 1
	for j in range(0, 5):
		if pins[j] == -1:
			pins[j] = height - 1
	locks.add(tuple(pins))

for i in range(0, nKey):
	height = len(keysRaw[i])
	pins = [-1, -1, -1, -1, -1]
	for j in range(height - 2, -1, -1):
		for k in range(0, 5):
			if keysRaw[i][j][k] == '.' and pins[k] == -1:
				pins[k] = (height - 2) - j
	for j in range(0, 5):
		if pins[j] == -1:
			pins[j] = height - 1
	keys.add(tuple(pins))

n = 0
for lock in locks:
	for key in keys:
		overlap = False
		for i in range(0, 5):
			if lock[i] + key[i] > 5:
				overlap = True
				break
		if overlap == False:
			n += 1
print(n)