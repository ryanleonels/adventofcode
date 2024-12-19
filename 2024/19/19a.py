#!/usr/bin/python3

total = 0
maxPatternLength = 0
patterns = []
patternLine = True
ways = {}

def numWays(design):
	global ways
	if design in ways:
		return ways[design]
	if len(design) == 0:
		return 1
	len1 = max(len(design) - maxPatternLength, 0)
	len2 = len(design)
	n = 0
	for i in range(len1, len2):
		if design[i:] in patterns:
			n += numWays(design[:i])
	ways[design] = n
	return n

fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		patternLine = False
		continue
	if patternLine == True:
		patterns = fileLine.split(', ')
		for pattern in patterns:
			if len(pattern) > maxPatternLength:
				maxPatternLength = len(pattern)
	else:
		nWays = numWays(fileLine)
		total += nWays

print(total)