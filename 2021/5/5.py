#!/usr/bin/python3

fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
diagram = {}
vents = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	x1 = int(fileLine.split(' -> ')[0].split(',')[0])
	y1 = int(fileLine.split(' -> ')[0].split(',')[1])
	x2 = int(fileLine.split(' -> ')[1].split(',')[0])
	y2 = int(fileLine.split(' -> ')[1].split(',')[1])
	vents.append((x1, y1, x2, y2))
	if x1 == x2:
		if y2 > y1:
			for i in range(y1, y2 + 1):
				if (x1, i) in diagram:
					diagram[(x1, i)] += 1
				else:
					diagram[(x1, i)] = 1
		else:
			for i in range(y2, y1 + 1):
				if (x1, i) in diagram:
					diagram[(x1, i)] += 1
				else:
					diagram[(x1, i)] = 1
	if y1 == y2:
		if x2 > x1:
			for i in range(x1, x2 + 1):
				if (i, y1) in diagram:
					diagram[(i, y1)] += 1
				else:
					diagram[(i, y1)] = 1
		else:
			for i in range(x2, x1 + 1):
				if (i, y1) in diagram:
					diagram[(i, y1)] += 1
				else:
					diagram[(i, y1)] = 1

n = 0
for point in diagram:
	if diagram[point] > 1:
		n += 1
print(n)
