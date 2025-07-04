#!/usr/bin/python3

sum1 = 0
fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

(xmin, xmax, ymin, ymax) = (999, -999, 999, -999)
tiles = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y) = (0, 0)
	n = len(fileLine)
	(i, i1) = (0, 0)
	while i < n:
		if fileLine[i] == 'e':
			x += 2
			i1 = 1
		if fileLine[i:i+2] == 'se':
			x += 1
			y -= 1
			i1 = 2
		if fileLine[i:i+2] == 'sw':
			x -= 1
			y -= 1
			i1 = 2
		if fileLine[i] == 'w':
			x -= 2
			i1 = 1
		if fileLine[i:i+2] == 'nw':
			x -= 1
			y += 1
			i1 = 2
		if fileLine[i:i+2] == 'ne':
			x += 1
			y += 1
			i1 = 2
		i += i1
	#print(x, y)
	if (x, y) not in tiles:
		tiles[(x, y)] = 1
	else:
		tiles[(x, y)] = 1 - tiles[(x, y)]
	xmin = min(xmin, x)
	xmax = max(xmax, x)
	ymin = min(ymin, y)
	ymax = max(ymax, y)

for x in range(xmin, xmax):
	for y in range(ymin, ymax):
		if x % 2 == y % 2 and (x, y) not in tiles:
			tiles[(x, y)] = 0

# valid values of (x, y): (x even, y even) / (x odd, y odd)
# neighbors of (x, y): (x + 2, y), (x + 1, y - 1), (x - 1, y - 1), (x - 2, y), (x - 1, y + 1), (x + 1, y + 1)

for day in range(1, 101):
	xmin -= 2
	xmax += 2
	ymin -= 1
	ymax += 1
	tiles1 = {}
	n = 0
	for x in range(xmin, xmax + 1):
		for y in range(ymin, ymax + 1):
			if x % 2 == y % 2:
				adj = 0
				if x + 2 <= xmax and (x + 2, y) in tiles and tiles[(x + 2, y)] == 1:
					adj += 1
				if x + 1 <= xmax and y - 1 >= ymin and (x + 1, y - 1) in tiles and tiles[(x + 1, y - 1)] == 1:
					adj += 1
				if x - 1 >= xmin and y - 1 >= ymin and (x - 1, y - 1) in tiles and tiles[(x - 1, y - 1)] == 1:
					adj += 1
				if x - 2 >= xmin and (x - 2, y) in tiles and tiles[(x - 2, y)] == 1:
					adj += 1
				if x - 1 >= xmin and y + 1 <= ymax and (x - 1, y + 1) in tiles and tiles[(x - 1, y + 1)] == 1:
					adj += 1
				if x + 1 <= xmax and y + 1 <= ymax and (x + 1, y + 1) in tiles and tiles[(x + 1, y + 1)] == 1:
					adj += 1
				tiles1[(x, y)] = 0
				if (x, y) in tiles:
					tiles1[(x, y)] = tiles[(x, y)]
					if tiles[(x, y)] == 1 and (adj == 0 or adj > 2):
						tiles1[(x, y)] = 0
				if tiles1[(x, y)] == 0 and adj == 2:
					tiles1[(x, y)] = 1
				if tiles1[(x, y)] == 1:
					n += 1
	print("Day " + str(day) + ": " + str(n))
	tiles = tiles1

print(n)
