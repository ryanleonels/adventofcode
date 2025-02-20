#!/usr/local/bin/python3

fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
blockedIntervals = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	blockedIntervals.append((int(fileLine.split('-')[0]),int(fileLine.split('-')[1])))

n = len(blockedIntervals)
maxValue = 4294967295
intervals = [(0, maxValue)]
for i in range(0, n):
	n1 = len(intervals)
	(blockedIntervalMin, blockedIntervalMax) = blockedIntervals[i]
	intervals1 = []
	for j in range(0, n1):
		(intervalMin, intervalMax) = intervals[j]
		if blockedIntervalMin <= intervalMax and blockedIntervalMax >= intervalMin:
			(blockedMin, blockedMax) = (max(blockedIntervalMin, intervalMin), min(blockedIntervalMax, intervalMax))
			if blockedMin > intervalMin:
				intervals1.append((intervalMin, blockedMin - 1))
			if blockedMax < intervalMax:
				intervals1.append((blockedMax + 1, intervalMax))
		else:
			intervals1.append((intervalMin, intervalMax))
	intervals = intervals1

ipAllowed = 0
n1 = len(intervals)
for i in range(0, n1):
	ipAllowed += (intervals[i][1] - intervals[i][0] + 1)
print(ipAllowed)