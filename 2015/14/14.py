#!/usr/bin/python3

from itertools import permutations

maxDist = 0
fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	words = fileLine.split(' ')
	name = words[0]
	speed = int(words[3])
	tFly = int(words[6])
	tRest = int(words[13])
	tCycle = tFly + tRest
	distCycle = tFly * speed
	nCycle = 2503 // tCycle
	curDist1 = distCycle * nCycle
	curTime = 2503 % tCycle
	curDist = curDist1 + (min(curTime, tFly) * speed)
	maxDist = max(maxDist, curDist)
print(maxDist)