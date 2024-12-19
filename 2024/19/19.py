#!/usr/bin/python3

nDesigns = 0
maxPatternLength = 0
patterns = []
patternLine = True
possible = {}

def isPossible(design):
	global possible
	if design in possible:
		return possible[design]
	if len(design) <= 1:
		return False
	len1 = max(len(design) - maxPatternLength, 1)
	len2 = len(design)
	found = False
	for i in range(len1, len2):
		if isPossible(design[:i]) and (design[i:] in patterns):
			found = True
	possible[design] = found
	return found

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
			possible[pattern] = True
			if len(pattern) > maxPatternLength:
				maxPatternLength = len(pattern)
	else:
		if isPossible(fileLine):
			nDesigns += 1

print(nDesigns)