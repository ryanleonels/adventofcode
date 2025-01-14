#!/usr/bin/python3

from itertools import permutations

maxDist = 0
reindeerPoints = {}
reindeerDists = {}
fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for i in range(1, 2504):
	for fileLine in fileLines:
		if fileLine.strip() == '':
			continue
		words = fileLine.split(' ')
		name = words[0]
		if i == 1:
			reindeerPoints[name] = 0
			reindeerDists[name] = 0
		speed = int(words[3])
		tFly = int(words[6])
		tRest = int(words[13])
		tCycle = tFly + tRest
		distCycle = tFly * speed
		nCycle = i // tCycle
		curDist1 = distCycle * nCycle
		curTime = i % tCycle
		curDist = curDist1 + (min(curTime, tFly) * speed)
		reindeerDists[name] = curDist
	maxDist = 0
	for reindeer in reindeerDists:
		maxDist = max(reindeerDists[reindeer], maxDist)
	for reindeer in reindeerDists:
		if reindeerDists[reindeer] == maxDist:
			reindeerPoints[reindeer] += 1
maxPoints = 0
for reindeer in reindeerPoints:
	maxPoints = max(reindeerPoints[reindeer], maxPoints)
print(maxPoints)