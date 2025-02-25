#!/usr/local/bin/python3

fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nodes = {}

(xmax, ymax) = (0, 0)
(xhole, yhole) = (0, 0)
(xwall, ywall) = (0, 0)

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:10] == "/dev/grid/":
		name = fileLine[10:22].strip()
		(x, y) = (int(name.split('-x')[1].split('-')[0]), int(name.split('-y')[1]))
		(xmax, ymax) = (max(x, xmax), max(y, ymax))
		size = int(fileLine[23:27].strip())
		used = int(fileLine[29:33].strip())
		avail = int(fileLine[35:40].strip())
		use = int(fileLine[42:46].strip())
		nodes[(x, y)] = (size, used, avail, use)
		if used == 0:
			(xhole, yhole) = (x, y)
		if used > 100 and xwall == 0:
			(xwall, ywall) = (x, y)

step = xhole - (xwall - 1)
step += yhole
step += xmax - (xwall - 1)
step += (5 * (xmax - 1))
print(step)

"""
the general case is very difficult to solve, this is a special case where there is just 1 hole and you move it around to move the target data to the goal
x11-y22 = hole (xhole, yhole)
x29-y0 = target data (xmax, 0)
x0-y0 = target goal (0, 0)
x8-y14 - x29-y14 = wall (on the row of ywall starting with (xwall, ywall))

(11,22) -> (7,22): 4 (total 4)
(7,22) -> (7,0): 22 (total 26)
(7,0) -> (29,0): 22 (total 48)

[47]
0D
xx

[48]
xD0
xxx
data at 28,0 (when the hole is at (29,0))

[49]
xDx
xx0

[50]
xDx
x0x

[51]
xDx
0xx

[52]
0Dx
xxx

[53]
D0x
xxx
data at 27,0 (5 steps to move the data left by 1 position)

repeat 27 more times
188: data at 0,0
"""
