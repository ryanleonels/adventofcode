#!/usr/bin/python3

fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(xmin, xmax) = (999, 0)
(ymin, ymax) = (999, 0)
grid = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	path = fileLine.split(' -> ')
	n1 = len(path)
	for i in range(1, n1):
		(x0, y0) = [int(x) for x in path[i-1].split(',')]
		(x1, y1) = [int(x) for x in path[i].split(',')]
		xmin = min(xmin, x0, x1)
		xmax = max(xmax, x0, x1)
		ymin = min(ymin, y0, y1)
		ymax = max(ymax, y0, y1)
		if x0 > x1:
			for x in range(x1, x0 + 1):
				grid[(x, y0)] = '#'
		if x1 > x0:
			for x in range(x0, x1 + 1):
				grid[(x, y0)] = '#'
		if y0 > y1:
			for y in range(y1, y0 + 1):
				grid[(x0, y)] = '#'
		if y1 > y0:
			for y in range(y0, y1 + 1):
				grid[(x0, y)] = '#'
if ymin > 0:
	ymin = 0
"""for y in range(ymin, ymax + 1):
	line = ""
	for x in range(xmin, xmax + 1):
		if (x, y) in grid:
			line += grid[(x, y)]
		else:
			line += ' '
	print(line)"""
n = 0
abyss = False
while not abyss:
	(x, y) = (500, 0)
	rest = False
	while not rest:
		if y >= ymax:
			abyss = True
			break
		if (x, y + 1) not in grid:
			y += 1
			continue
		if (x - 1, y + 1) not in grid:
			x -= 1
			y += 1
			continue
		if (x + 1, y + 1) not in grid:
			x += 1
			y += 1
			continue
		rest = True
		grid[(x, y)] = 'o'
		#print(x, y)
	if not abyss:
		n += 1
"""for y in range(ymin, ymax + 1):
	line = ""
	for x in range(xmin, xmax + 1):
		if (x, y) in grid:
			line += grid[(x, y)]
		else:
			line += ' '
	print(line)"""
print(n)
