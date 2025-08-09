#!/usr/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
knots = []
for i in range(0, 10):
	knots.append((0, 0))
tails = set()
tails.add(knots[9])
dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	dir1 = fileLine[0]
	nSteps = int(fileLine[2:])
	for i in range(0, nSteps):
		(xh, yh) = knots[0]
		xh += dirs[dir1][0]
		yh += dirs[dir1][1]
		knots[0] = (xh, yh)
		for j in range(1, 10):
			(xh, yh) = knots[j-1]
			(xt, yt) = knots[j]
			tailmove = (0, 0)
			if xh == xt + 2 and yh == yt:
				tailmove = (1, 0)
			if xh == xt - 2 and yh == yt:
				tailmove = (-1, 0)
			if xh == xt and yh == yt + 2:
				tailmove = (0, 1)
			if xh == xt and yh == yt - 2:
				tailmove = (0, -1)
			if xh > xt and yh > yt and (xh - xt > 1 or yh - yt > 1):
				tailmove = (1, 1)
			if xh > xt and yt > yh and (xh - xt > 1 or yt - yh > 1):
				tailmove = (1, -1)
			if xt > xh and yh > yt and (xt - xh > 1 or yh - yt > 1):
				tailmove = (-1, 1)
			if xt > xh and yt > yh and (xt - xh > 1 or yt - yh > 1):
				tailmove = (-1, -1)
			xt += tailmove[0]
			yt += tailmove[1]
			knots[j] = (xt, yt)
			if j == 9 and knots[j] not in tails:
				tails.add(knots[j])
				#print(knots[j])
print(len(tails))
