#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
coordinates = []
(xmax, ymax) = (0, 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	coordinate = tuple([int(x) for x in fileLine.split(', ')])
	coordinates.append(coordinate)
	(xmax, ymax) = (max(xmax, coordinate[0]), max(ymax, coordinate[1]))
n = len(coordinates)
areas = [0] * n
isInfinite = [False] * n
maxArea = 0
for x in range(-xmax, (xmax * 2) + 1):
	print(x)
	for y in range(-ymax, (ymax * 2) + 1):
		(coord, minDist, tied) = (-1, 9999, False)
		for i in range(0, n):
			dist = abs(x - coordinates[i][0]) + abs(y - coordinates[i][1])
			if dist == minDist:
				(coord, tied) = (i, True)
			if dist < minDist:
				(coord, minDist, tied) = (i, dist, False)
		if not tied:
			areas[coord] += 1
			if x == -xmax or x == (xmax * 2) or y == -ymax or y == (ymax * 2):
				isInfinite[coord] = True
for i in range(0, n):
	print(i, areas[i], isInfinite[i])
	if not isInfinite[i]:
		maxArea = max(maxArea, areas[i])
print(maxArea)