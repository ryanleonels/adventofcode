#!/usr/bin/python3

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
for i in range(0, col):
	rocks = []
	walls = []
	for j in range(0, row):
		if platform[j][i] == 'O':
			rocks.append(j)
		if platform[j][i] == '#':
			walls.append(j)
	#print(rocks)
	#print(walls)
	n = len(rocks)
	rocks1 = []
	for j in range(0, n):
		x = rocks[j]
		while x > 0 and (x-1) not in walls and (x-1) not in rocks1:
			x -= 1
		rocks1.append(x)
		totalLoad += (row - x)
	#print(rocks1)
print(totalLoad)
