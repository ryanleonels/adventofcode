#!/usr/bin/python3

total = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	(l, lPos) = (0, -1)
	for i in range(0, n - 1):
		if int(fileLine[i]) > l:
			(l, lPos) = (int(fileLine[i]), i)
		if l == 9:
			break
	r = 0
	for i in range(lPos + 1, n):
		if int(fileLine[i]) > r:
			r = int(fileLine[i])
		if r == 9:
			break
	joltage = (l * 10) + r
	total += joltage
print(total)
