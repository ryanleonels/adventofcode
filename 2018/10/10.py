#!/usr/bin/python3

fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(p, v) = ([], [])
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	px = int(fileLine.split('position=<')[1].split('>')[0].split(',')[0].strip())
	py = int(fileLine.split('position=<')[1].split('>')[0].split(',')[1].strip())
	vx = int(fileLine.split('velocity=<')[1].split('>')[0].split(',')[0].strip())
	vy = int(fileLine.split('velocity=<')[1].split('>')[0].split(',')[1].strip())
	p.append((px, py))
	v.append((vx, vy))
n = len(p)
(t, connected) = (-1, 0)
while connected < n * 0.9 and t < 11000:
	t += 1
	if t % 1000 == 0:
		print(t)
	pts = set()
	points = []
	(xmin, xmax, ymin, ymax) = (999999999, -999999999, 999999999, -999999999)
	for i in range(0, n):
		x = p[i][0] + (t * v[i][0])
		y = p[i][1] + (t * v[i][1])
		pts.add((x, y))
		points.append((x, y))
		xmin = min(xmin, x)
		xmax = max(xmax, x)
		ymin = min(ymin, y)
		ymax = max(ymax, y)
	connected = 0
	for i in range(0, n):
		(x, y) = points[i]
		if (x - 1, y) in pts or (x + 1, y) in pts or (x, y - 1) in pts or (x, y + 1) in pts:
			connected += 1
#print(n, t, connected, xmin, xmax, ymin, ymax)
#print("t=" + str(t))
for y in range(ymin, ymax + 1):
	row = ""
	for x in range(xmin, xmax + 1):
		if (x, y) in pts:
			row += "#"
		else:
			row += "."
	print(row)