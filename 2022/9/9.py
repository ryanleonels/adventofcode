#!/usr/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
head = (0, 0)
tail = (0, 0)
tails = set()
tails.add(tail)
dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	dir1 = fileLine[0]
	nSteps = int(fileLine[2:])
	for i in range(0, nSteps):
		(xh, yh) = head
		(xt, yt) = tail
		xh += dirs[dir1][0]
		yh += dirs[dir1][1]
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
		head = (xh, yh)
		tail = (xt, yt)
		if tail not in tails:
			tails.add(tail)
			#print(tail)
print(len(tails))
