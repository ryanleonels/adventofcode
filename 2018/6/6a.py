#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
coordinates = []
(xmin, xmax, ymin, ymax) = (999, 0, 999, 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	coordinate = tuple([int(x) for x in fileLine.split(', ')])
	coordinates.append(coordinate)
	(xmin, ymin) = (min(xmin, coordinate[0]), min(ymin, coordinate[1]))
	(xmax, ymax) = (max(xmax, coordinate[0]), max(ymax, coordinate[1]))
n = len(coordinates)
area = 0
for x in range(xmin, xmax + 1):
	print(x)
	for y in range(ymin, ymax + 1):
		dist = 0
		for i in range(0, n):
			dist += (abs(x - coordinates[i][0]) + abs(y - coordinates[i][1]))
		if dist < 10000:
			area += 1
print(area)