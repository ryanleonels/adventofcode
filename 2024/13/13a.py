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
		xp += 10000000000000
		yp += 10000000000000
		b1 = (xp * ya) - (yp * xa)
		b2 = (xb * ya) - (xa * yb)
		if b2 != 0 and b1 % b2 == 0 and b1 // b2 >= 0:
			b = b1 // b2
			a1 = (xp - (xb * b))
			if a1 % xa == 0:
				a = a1 // xa
				x = (xa * a) + (xb * b) - xp
				y = (ya * a) + (yb * b) - yp
				totalTokens += ((a * 3) + b)
print(totalTokens)
