#!/usr/local/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
wire1 = fileLines[0].strip().split(',')
wire2 = fileLines[1].strip().split(',')
#print(wire1)
#print(wire2)
wire1path = set()
wire2path = set()
(x, y) = (0, 0)
for step in wire1:
	(dir1, n) = (step[0], int(step[1:]))
	for i in range(0, n):
		match dir1:
			case 'L':
				x -= 1
			case 'R':
				x += 1
			case 'D':
				y -= 1
			case 'U':
				y += 1
		wire1path.add((x, y))
(x, y) = (0, 0)
for step in wire2:
	(dir1, n) = (step[0], int(step[1:]))
	for i in range(0, n):
		match dir1:
			case 'L':
				x -= 1
			case 'R':
				x += 1
			case 'D':
				y -= 1
			case 'U':
				y += 1
		wire2path.add((x, y))
mindist = 999999999
for (x, y) in wire1path:
	if (x, y) in wire2path:
		dist = abs(x) + abs(y)
		if dist < mindist:
			mindist = dist
print(mindist)
