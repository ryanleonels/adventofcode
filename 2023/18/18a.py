#!/usr/bin/python3

def inInterval(pos, intervals):
	for interval in intervals:
		if pos >= interval[0] and pos <= interval[1]:
			return True
	return False

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
	hexCode = fileLine.split('#')[1].split(')')[0]
	digPlan.append(("RDLU"[int(hexCode[5])], int(hexCode[:5], 16)))
	#digPlan.append((fileLine.split(' ')[0], int(fileLine.split(' ')[1]), fileLine.split(' ')[2]))
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
#print(str(row)+'x'+str(col))
#lagoon too big to implement in full, implementing the walls instead
wallH = {} #wallH[row] = list of wall cols interval tuples
wallV = {} #wallV[col] = list of wall rows interval tuples
#print(n)
x0 = -xmin
y0 = -ymin
#print((x0, y0))
x = x0
y = y0
for i in range(0, n):
	if digPlan[i][0] == 'U':
		x -= digPlan[i][1]
		if y not in wallV:
			wallV[y] = []
		wallV[y].append((x, x + digPlan[i][1]))
	if digPlan[i][0] == 'D':
		x += digPlan[i][1]
		if y not in wallV:
			wallV[y] = []
		wallV[y].append((x - digPlan[i][1], x))
	if digPlan[i][0] == 'L':
		y -= digPlan[i][1]
		if x not in wallH:
			wallH[x] = []
		wallH[x].append((y, y + digPlan[i][1]))
	if digPlan[i][0] == 'R':
		y += digPlan[i][1]
		if x not in wallH:
			wallH[x] = []
		wallH[x].append((y - digPlan[i][1], y))
for i in wallH:
	wallH[i].sort()
for i in wallV:
	wallV[i].sort()
wallH = dict(sorted(wallH.items()))
wallV = dict(sorted(wallV.items()))
"""print("Horizontal walls:")
for i in wallH:
	print("Row " + str(i) + ": " + str(wallH[i]))
print("Vertical walls:")
for i in wallV:
	print("Col " + str(i) + ": " + str(wallV[i]))"""
lavaVolume = 0
prevRow = -1
for i in wallH:
	#process rows between horizontal wall rows (row1-row2), determine where the walls are
	if i > 0:
		row1 = prevRow + 1
		row2 = i - 1
		nrow = (row2 - row1) + 1
		walls = []
		for j in wallV:
			if inInterval(row1, wallV[j]):
				walls.append(j)
		#print("Rows "+str(row1)+"-"+str(row2)+": "+str(walls))
		lavaPerRow = 0
		for j in range(0, len(walls), 2):
			lavaPerRow += (walls[j+1] - walls[j] + 1)
		lavaVolume += (nrow * lavaPerRow)
	#process row itself
	walls = []
	for j in wallV:
		if inInterval(i, wallV[j]):
			walls.append(j)
	#print("Row "+str(i)+": "+str(walls))
	lavaPerRow = 1
	inside = False
	for j in range(1, len(walls)):
		if (walls[j-1], walls[j]) in wallH[i]:
			lavaPerRow += (walls[j] - walls[j-1])
			#check if walls[j-1] and walls[j] share same direction
			wall = False
			if i == 0 and inInterval(i+1, wallV[walls[j-1]]) == inInterval(i+1, wallV[walls[j]]):
				wall = True
			if i > 0 and inInterval(i-1, wallV[walls[j-1]]) == inInterval(i-1, wallV[walls[j]]):
				wall = True
			if wall == True:
				inside = not inside
		else:
			inside = not inside
			if inside == True:
				lavaPerRow += (walls[j] - walls[j-1])
			else:
				lavaPerRow += 1
	#print(lavaPerRow)
	lavaVolume += lavaPerRow
	#go to next row
	prevRow = i
print(lavaVolume)
