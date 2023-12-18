#!/usr/bin/python3

import sys

row = 0
col = 0
digPlan = []
lagoon = []
lavaVolume = 0
fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = "R 6 (#70c710)","D 5 (#0dc571)","L 2 (#5713f0)","D 2 (#d2c081)","R 2 (#59c680)","D 2 (#411b91)","L 5 (#8ceee2)","U 2 (#caa173)","L 1 (#1b58a2)","U 2 (#caa171)","R 2 (#7807d2)","U 3 (#a77fa3)","L 2 (#015232)","U 2 (#7a21e3)"
n = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	digPlan.append((fileLine.split(' ')[0], int(fileLine.split(' ')[1]), fileLine.split(' ')[2]))
	n += 1
#print(n)
#print(digPlan)
x = 0
y = 0
xmin = 0
xmax = 0
ymin = 0
ymax = 0
for i in range(0, n):
	if digPlan[i][0] == 'U':
		x -= digPlan[i][1]
		if x < xmin:
			xmin = x
	if digPlan[i][0] == 'D':
		x += digPlan[i][1]
		if x > xmax:
			xmax = x
	if digPlan[i][0] == 'L':
		y -= digPlan[i][1]
		if y < ymin:
			ymin = y
	if digPlan[i][0] == 'R':
		y += digPlan[i][1]
		if y > ymax:
			ymax = y
#print("x = " + str(xmin) + " - " + str(xmax) + ", y = " + str(ymin) + " - " + str(ymax))
row = xmax - xmin + 1
col = ymax - ymin + 1
for i in range(0, row):
	lagoonRow = ""
	for j in range(0, col):
		lagoonRow += '.'
	lagoon.append(lagoonRow)
x0 = -xmin
y0 = -ymin
x = x0
y = y0
lagoonRow = list(lagoon[x0])
lagoonRow[y0] = '#'
lagoon[x0] = ''.join(lagoonRow)
for i in range(0, n):
	if digPlan[i][0] == 'U':
		x -= digPlan[i][1]
		for j in range(x, x + digPlan[i][1]):
			lagoonRow = list(lagoon[j])
			lagoonRow[y] = '#'
			lagoon[j] = ''.join(lagoonRow)
	if digPlan[i][0] == 'D':
		x += digPlan[i][1]
		for j in range(x, x - digPlan[i][1], -1):
			lagoonRow = list(lagoon[j])
			lagoonRow[y] = '#'
			lagoon[j] = ''.join(lagoonRow)
	if digPlan[i][0] == 'L':
		y -= digPlan[i][1]
		lagoonRow = list(lagoon[x])
		for j in range(y, y + digPlan[i][1]):
			lagoonRow[j] = '#'
		lagoon[x] = ''.join(lagoonRow)
	if digPlan[i][0] == 'R':
		y += digPlan[i][1]
		lagoonRow = list(lagoon[x])
		for j in range(y, y - digPlan[i][1], -1):
			lagoonRow[j] = '#'
		lagoon[x] = ''.join(lagoonRow)
#print(str(row)+'x'+str(col))
#for i in range(0, row):
	#print(lagoon[i])
for i in range(0, row):
	debug = ""
	inside = False
	for j in range(0, col):
		if lagoon[i][j] == '#':
			lavaVolume += 1
			debug += '#'
		if lagoon[i][j] == '.':
			#inside = False
			if j > 0 and lagoon[i][j-1] == '#':
				if j < 2 or lagoon[i][j-2] == '.': # vertical wall
					inside = not inside
				else: # horizontal wall
					wallEnd = j-1
					wallStart = wallEnd - 1
					while wallStart > 0 and lagoon[i][wallStart-1] == '#':
						wallStart -= 1
					wall = False
					if i == 0 and lagoon[i+1][wallStart] != lagoon[i+1][wallEnd]:
						wall = True
					if i > 0 and lagoon[i-1][wallStart] != lagoon[i-1][wallEnd]:
						wall = True
					if wall == True:
						inside = not inside
			if inside == True:
				lavaVolume += 1
				debug += '#'
			if inside == False:
				debug += '.'
	#print(debug)
print(lavaVolume)
