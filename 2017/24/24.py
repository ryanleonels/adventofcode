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

def maxStrength(curPort, curStr, compSoFar):
	#print(curPort, curStr, compSoFar)
	maxStr = curStr
	for component in components:
		if component[0] == curPort and component not in compSoFar:
			comp1 = compSoFar.copy()
			comp1.add(component)
			str1 = maxStrength(component[1], curStr + component[0] + component[1], comp1)
			maxStr = max(str1, maxStr)
		else:
			if component[1] == curPort and component not in compSoFar:
				comp1 = compSoFar.copy()
				comp1.add(component)
				str1 = maxStrength(component[0], curStr + component[0] + component[1], comp1)
				maxStr = max(str1, maxStr)
	return maxStr

maxStr = maxStrength(0, 0, set())
print(maxStr)
