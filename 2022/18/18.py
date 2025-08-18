#!/usr/bin/python3

fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
cubes = set()
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y, z) = [int(x) for x in fileLine.split(',')]
	cubes.add((x, y, z))
n = 0
for (x, y, z) in cubes:
	if (x - 1, y, z) not in cubes:
		n += 1
	if (x + 1, y, z) not in cubes:
		n += 1
	if (x, y - 1, z) not in cubes:
		n += 1
	if (x, y + 1, z) not in cubes:
		n += 1
	if (x, y, z - 1) not in cubes:
		n += 1
	if (x, y, z + 1) not in cubes:
		n += 1
print(n)
