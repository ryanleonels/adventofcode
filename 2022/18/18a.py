#!/usr/bin/python3

import sys

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
(xmin, xmax) = (999, -999)
(ymin, ymax) = (999, -999)
(zmin, zmax) = (999, -999)
for (x, y, z) in cubes:
	(xmin, xmax) = (min(xmin, x), max(xmax, x))
	(ymin, ymax) = (min(ymin, y), max(ymax, y))
	(zmin, zmax) = (min(zmin, z), max(zmax, z))

outside = set()

def floodFillOutside(x, y, z):
	if (x, y, z) not in cubes and (x, y, z) not in outside:
		outside.add((x, y, z))
		if x >= xmin:
			floodFillOutside(x - 1, y, z)
		if x <= xmax:
			floodFillOutside(x + 1, y, z)
		if y >= ymin:
			floodFillOutside(x, y - 1, z)
		if y <= ymax:
			floodFillOutside(x, y + 1, z)
		if z >= zmin:
			floodFillOutside(x, y, z - 1)
		if z <= zmax:
			floodFillOutside(x, y, z + 1)

sys.setrecursionlimit((xmax - xmin) * (ymax - ymin) * (zmax - zmin))
floodFillOutside(xmin - 1, ymin - 1, zmin - 1)

n = 0
for (x, y, z) in cubes:
	if (x - 1, y, z) not in cubes and (x - 1, y, z) in outside:
		n += 1
	if (x + 1, y, z) not in cubes and (x + 1, y, z) in outside:
		n += 1
	if (x, y - 1, z) not in cubes and (x, y - 1, z) in outside:
		n += 1
	if (x, y + 1, z) not in cubes and (x, y + 1, z) in outside:
		n += 1
	if (x, y, z - 1) not in cubes and (x, y, z - 1) in outside:
		n += 1
	if (x, y, z + 1) not in cubes and (x, y, z + 1) in outside:
		n += 1
print(n)
