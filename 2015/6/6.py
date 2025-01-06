#!/usr/bin/python3

grid = []
for i in range(0, 1000):
	grid.append([])
	for j in range(0, 1000):
		grid[i].append(False)
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
instructions = fileData.split('\n')
for instruction in instructions:
	if instruction.strip() == '':
		continue
	ins = ""
	(x1, y1) = (0, 0)
	(x2, y2) = (0, 0)
	if instruction[:7] == "turn on":
		ins = "on"
		xy1 = instruction[8:].split(' ')[0].split(',')
		(x1, y1) = (int(xy1[0]), int(xy1[1]))
		xy2 = instruction[8:].split(' ')[-1].split(',')
		(x2, y2) = (int(xy2[0]), int(xy2[1]))
		for i in range(x1, x2 + 1):
			for j in range(y1, y2 + 1):
				grid[i][j] = True
	if instruction[:8] == "turn off":
		ins = "off"
		xy1 = instruction[9:].split(' ')[0].split(',')
		(x1, y1) = (int(xy1[0]), int(xy1[1]))
		xy2 = instruction[9:].split(' ')[-1].split(',')
		(x2, y2) = (int(xy2[0]), int(xy2[1]))
		for i in range(x1, x2 + 1):
			for j in range(y1, y2 + 1):
				grid[i][j] = False
	if instruction[:6] == "toggle":
		ins = "toggle"
		xy1 = instruction[7:].split(' ')[0].split(',')
		(x1, y1) = (int(xy1[0]), int(xy1[1]))
		xy2 = instruction[7:].split(' ')[-1].split(',')
		(x2, y2) = (int(xy2[0]), int(xy2[1]))
		for i in range(x1, x2 + 1):
			for j in range(y1, y2 + 1):
				grid[i][j] = not grid[i][j]
n = 0
for i in range(0, 1000):
	for j in range(0, 1000):
		if grid[i][j] == True:
			n += 1
print(n)