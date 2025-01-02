#!/usr/bin/python3

total = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	dim = [int(x) for x in fileLine.split('x')]
	(l, w, h) = (dim[0], dim[1], dim[2])
	extra = min(l * w, w * h, h * l)
	cur = (2 * l * w) + (2 * w * h) + (2 * h * l) + extra
	total += cur
print(total)