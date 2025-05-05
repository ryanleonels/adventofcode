#!/usr/bin/python3

fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
clays = set()

(xmin, xmax) = (9999, -9999)
(ymin, ymax) = (9999, -9999)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	x1 = fileLine.split('x=')[1].split(',')[0]
	y1 = fileLine.split('y=')[1].split(',')[0]
	if ".." in x1:
		x = (int(x1.split('..')[0]), int(x1.split('..')[1]))
		xmin = min(xmin, x[0])
		xmax = max(xmax, x[1])
		y = int(y1)
		ymin = min(ymin, y)
		ymax = max(ymax, y)
		for i in range(x[0], x[1] + 1):
			clays.add((i, y))
	if ".." in y1:
		x = int(x1)
		xmin = min(xmin, x)
		xmax = max(xmax, x)
		y = (int(y1.split('..')[0]), int(y1.split('..')[1]))
		ymin = min(ymin, y[0])
		ymax = max(ymax, y[1])
		for i in range(y[0], y[1] + 1):
			clays.add((x, i))
#print((xmin, xmax), (ymin, ymax))
#print(len(clays))
tiles = {}
for i in range(0, ymax + 1):
	line = ''
	for j in range(xmin - 1, xmax + 2):
		if (j, i) in clays:
			line += '#'
			tiles[(j, i)] = '#'
		else:
			if j == 500 and i == 0:
				line += '+'
				tiles[(j, i)] = '+'
			else:
				line += '.'
				tiles[(j, i)] = '.'
	#print(line)
turn = 0
(prev, cur) = (-1, 0)
while cur != prev:
	for i in range(0, ymax + 1):
		line = ''
		for j in range(xmin - 1, xmax + 2):
			if (j, i) in tiles:
				if tiles[(j, i)] == '|':
					tiles[(j, i)] = '.'
	stack = [(500, 0)]
	while len(stack) > 0:
		(x, y) = stack.pop()
		#print(x, y)
		if y < ymax and tiles[(x, y + 1)] == '.': # above void = flow down
			while y < ymax and tiles[(x, y + 1)] != '#':
				y += 1
				tiles[(x, y)] = '|'
				stack.append((x, y))
		else:
			if y < ymax and (tiles[(x, y + 1)] == '#' or tiles[(x, y + 1)] == '~'): # above clay / settled water = flow left+right
				settled = True
				x0 = x
				while (tiles[(x0, y + 1)] == '#' or tiles[(x0, y + 1)] == '~') and tiles[(x0 - 1, y)] != '#':
					x0 -= 1
				if tiles[(x0, y + 1)] != '#' and tiles[(x0, y + 1)] != '~':
					settled = False
					stack.append((x0, y))
				x1 = x
				while (tiles[(x1, y + 1)] == '#' or tiles[(x1, y + 1)] == '~') and tiles[(x1 + 1, y)] != '#':
					x1 += 1
				if tiles[(x1, y + 1)] != '#' and tiles[(x1, y + 1)] != '~':
					settled = False
					stack.append((x1, y))
				if settled == True:
					for i in range(x0, x1 + 1):
						tiles[(i, y)] = '~'
				if settled == False:
					for i in range(x0, x1 + 1):
						tiles[(i, y)] = '|'
			else:
				pass
	turn += 1
	prev = cur
	cur = 0
	for i in range(0, ymax + 1):
		line = ''
		for j in range(xmin - 1, xmax + 2):
			if (j, i) in tiles:
				line += tiles[(j, i)]
				if i >= ymin and tiles[(j, i)] == '|' or tiles[(j, i)] == '~':
					cur += 1
		#print(line)
	print("Turn " + str(turn) + ": " + str(cur) + " tiles")
n = 0
for i in range(0, ymax + 1):
	for j in range(xmin - 1, xmax + 2):
		if (j, i) in tiles:
			if tiles[(j, i)] == '~':
				n += 1
print(n)