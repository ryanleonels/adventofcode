#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
instructions = fileData.strip().split(', ')
(x, y) = (0, 0)
(dx, dy) = (1, 0)
l = {}
l[(1, 0)] = (0, -1)
l[(0, -1)] = (-1, 0)
l[(-1, 0)] = (0, 1)
l[(0, 1)] = (1, 0)
r = {}
r[(1, 0)] = (0, 1)
r[(0, 1)] = (-1, 0)
r[(-1, 0)] = (0, -1)
r[(0, -1)] = (1, 0)
n = len(instructions)
visited = set()
for i in range(0, n):
	direction = instructions[i][0]
	distance = int(instructions[i][1:])
	if direction == "L":
		(dx, dy) = l[(dx, dy)]
	if direction == "R":
		(dx, dy) = r[(dx, dy)]
	found = False
	for j in range(0, distance):
		(x, y) = (x + dx, y + dy)
		if (x, y) in visited:
			found = True
			print(abs(x)+abs(y))
			break
		visited.add((x, y))
	if found == True:
		break