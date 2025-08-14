#!/usr/bin/python3

fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
algorithm = ""
image = []

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if algorithm != '':
		image.append(list(fileLine.strip()))
	if algorithm == '':
		algorithm = fileLine.strip()

row = len(image)
col = len(image[0])
grid = {}
for x in range(0, row):
	for y in range(0, col):
		if image[x][y] == '#':
			grid[(x, y)] = 1
		else:
			grid[(x, y)] = 0

step = 1
nstep = 50
while step <= nstep:
	print("step " + str(step))
	if algorithm[0] == '#':
		(xmin, xmax) = (-(nstep * 2), row + (nstep * 2) - 1)
		(ymin, ymax) = (-(nstep * 2), col + (nstep * 2) - 1)
	else:
		(xmin, xmax) = (-step, row + step - 1)
		(ymin, ymax) = (-step, col + step - 1)
	n = 0
	grid1 = {}
	for x in range(xmin, xmax + 1):
		for y in range(ymin, ymax + 1):
			pos = 0
			for x1 in [-1, 0, 1]:
				for y1 in [-1, 0, 1]:
					curbit = 0
					if (x + x1, y + y1) in grid:
						curbit = grid[(x + x1, y + y1)]
					pos = (pos * 2) + curbit
			if algorithm[pos] == '#':
				if x >= -step and x <= row + step - 1 and y >= -step and y <= col + step - 1:
					n += 1
				grid1[(x, y)] = 1
			else:
				grid1[(x, y)] = 0
	grid = grid1
	step += 1
print(n)
