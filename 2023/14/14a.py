#!/usr/bin/python3

import hashlib

totalLoad = 0
fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
row = 0
col = 0
platform = []
#fileLines = ["O....#....","O.OO#....#",".....##...","OO.#O....O",".O.....O#.","O.#..O.#.#","..O..#O..O",".......O..","#....###..","#OO..#...."]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	platform.append(fileLine)
row = len(platform)
col = len(platform[0])
#print(str(row)+'x'+str(col))
rocks = []
walls = []
for i in range(0, row):
	for j in range(0, col):
		if platform[i][j] == 'O':
			rocks.append((i,j))
		if platform[i][j] == '#':
			walls.append((i,j))
#print(rocks)
#print(walls)
nrocks = len(rocks)
platformStates = {}
#calculate load
totalLoads = []
totalLoad = 0
for i in range(0, nrocks):
	totalLoad += (row - rocks[i][0])
state = hashlib.md5(str(rocks).encode()).hexdigest()
platformStates[state] = 0
print("0 spins: total load = " + str(totalLoad) + ", platform hash = " + str(state))
totalLoads.append(totalLoad)
cycleStart = -1
cycleLength = -1
for n in range(0, 1000000000):
	#tilt north
	rocks.sort()
	for i in range(0, nrocks):
		rock = rocks[i]
		while rock[0] > 0 and (rock[0]-1,rock[1]) not in walls and (rock[0]-1,rock[1]) not in rocks:
			rock = (rock[0]-1,rock[1])
		rocks[i] = rock
	#tilt west
	rocks.sort(key=lambda a: a[1])
	for i in range(0, nrocks):
		rock = rocks[i]
		while rock[1] > 0 and (rock[0],rock[1]-1) not in walls and (rock[0],rock[1]-1) not in rocks:
			rock = (rock[0],rock[1]-1)
		rocks[i] = rock
	#tilt south
	rocks.sort(reverse = True)
	for i in range(0, nrocks):
		rock = rocks[i]
		while rock[0] < row-1 and (rock[0]+1,rock[1]) not in walls and (rock[0]+1,rock[1]) not in rocks:
			rock = (rock[0]+1,rock[1])
		rocks[i] = rock
	#tilt east
	rocks.sort(key=lambda a: a[1], reverse = True)
	for i in range(0, nrocks):
		rock = rocks[i]
		while rock[1] < col-1 and (rock[0],rock[1]+1) not in walls and (rock[0],rock[1]+1) not in rocks:
			rock = (rock[0],rock[1]+1)
		rocks[i] = rock
	#calculate load
	totalLoad = 0
	for i in range(0, nrocks):
		totalLoad += (row - rocks[i][0])
	state = hashlib.md5(str(rocks).encode()).hexdigest()
	print(str(n+1) + " spins: total load = " + str(totalLoad) + ", platform hash = " + str(state))
	totalLoads.append(totalLoad)
	if state in platformStates:
		cycleStart = platformStates[state]
		cycleLength = (n+1) - cycleStart
		print("cycle detected: " + str(cycleStart) + "-" + str(cycleStart + cycleLength))
		break
	platformStates[state] = n+1
print(totalLoads[cycleStart + ((1000000000 - cycleStart) % cycleLength)])
