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
		continue
ranges1 = sorted(ranges)
(allRanges, nAllRange) = ([], 0)
for i in range(0, nRange):
	if i == 0:
		allRanges.append(ranges1[i])
		nAllRange += 1
	else:
		if ranges1[i][0] <= allRanges[nAllRange - 1][1]:
			if ranges1[i][1] > allRanges[nAllRange - 1][1]:
				allRanges[nAllRange - 1][1] = ranges1[i][1]
		else:
			allRanges.append(ranges1[i])
			nAllRange += 1
for allRange in allRanges:
	n += (allRange[1] - allRange[0] + 1)
print(n)
