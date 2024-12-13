#!/usr/bin/python3

totalTokens = 0
(xa, ya, xb, yb, xp, yp) = (0, 0, 0, 0, 0, 0)
fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:10] == "Button A: ":
		xa = int(fileLine.split('X+')[1].split(',')[0])
		ya = int(fileLine.split('Y+')[1])
	if fileLine[:10] == "Button B: ":
		xb = int(fileLine.split('X+')[1].split(',')[0])
		yb = int(fileLine.split('Y+')[1])
	if fileLine[:7] == "Prize: ":
		xp = int(fileLine.split('X=')[1].split(',')[0])
		yp = int(fileLine.split('Y=')[1])
		minTokens = 999
		for i in range(0, 101):
			for j in range(0, 101):
				x = (i * xa) + (j * xb)
				y = (i * ya) + (j * yb)
				if x == xp and y == yp:
					tokens = (3 * i) + j
					if tokens < minTokens:
						minTokens = tokens
		if minTokens != 999:
			totalTokens += minTokens
print(totalTokens)