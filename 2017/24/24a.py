#!/usr/local/bin/python3

fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
components = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(a, b) = tuple([int(x) for x in fileLine.split('/')])
	components.append((a, b))

maxStrs = {}

def maxStrength(curPort, curStr, compSoFar):
	#print(curPort, curStr, compSoFar)
	n = len(compSoFar)
	if n in maxStrs:
		maxStrs[n] = max(maxStrs[n], curStr)
	else:
		maxStrs[n] = curStr
	for component in components:
		if component[0] == curPort and component not in compSoFar:
			comp1 = compSoFar.copy()
			comp1.add(component)
			maxStrength(component[1], curStr + component[0] + component[1], comp1)
		else:
			if component[1] == curPort and component not in compSoFar:
				comp1 = compSoFar.copy()
				comp1.add(component)
				maxStrength(component[0], curStr + component[0] + component[1], comp1)
	return

maxStrength(0, 0, set())
#print(maxStrs)
maxLen = 0
for curLen in maxStrs:
	maxLen = max(curLen, maxLen)
print(maxStrs[maxLen])