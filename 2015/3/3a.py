#!/usr/bin/python3

nHouse = 0
houses = set()
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
directions = fileData.strip()
n = len(directions)
(x, y) = (0, 0)
(x1, y1) = (0, 0)
houses.add((x, y))
for i in range(0, n):
	if i % 2 == 0:
		if directions[i] == '^':
			x += 1
		if directions[i] == 'v':
			x -= 1
		if directions[i] == '>':
			y += 1
		if directions[i] == '<':
			y -= 1
		houses.add((x, y))
	if i % 2 == 1:
		if directions[i] == '^':
			x1 += 1
		if directions[i] == 'v':
			x1 -= 1
		if directions[i] == '>':
			y1 += 1
		if directions[i] == '<':
			y1 -= 1
		houses.add((x1, y1))
nHouse = len(houses)
print(nHouse)