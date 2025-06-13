#!/usr/bin/python3

(n, t, ids) = (0, 0, [])
fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if ',' in fileLine:
		ids = fileLine.split(',')
		n = len(ids)
	else:
		t = int(fileLine)

(minID, minTime) = (0, 999999999)
for i in range(0, n):
	if ids[i] != 'x':
		id1 = int(ids[i])
		curTime = id1 - (t % id1)
		if t % id1 == 0:
			curTime = 0 # just in case
		if curTime < minTime:
			(minID, minTime) = (id1, curTime)

print(minID * minTime)
