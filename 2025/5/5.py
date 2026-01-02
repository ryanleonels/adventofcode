#!/usr/bin/python3

n = 0
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
part = 0
(ranges, nRange) = ([], 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		part += 1
		continue
	if part == 0:
		ranges.append([int(x) for x in fileLine.split('-')])
		nRange += 1
	if part == 1:
		id1 = int(fileLine.strip())
		fresh = False
		for i in range(0, nRange):
			if id1 >= ranges[i][0] and id1 <= ranges[i][1]:
				fresh = True
				break
		if fresh:
			n += 1
print(n)
