#!/usr/bin/python3

molecule = ""
replacements = []
fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
replacementLine = True
for fileLine in fileLines:
	if fileLine.strip() == '':
		replacementLine = False
		continue
	if replacementLine == True:
		(before, after) = (fileLine.split(' => ')[0], fileLine.split(' => ')[1])
		replacements.append((before, after))
	if replacementLine == False:
		molecule = fileLine
		# forget the replacements, just count the patterns: Rn Y Ar always come in a set which acts like ( , ) here and assume all substitutions are optimal
		n = len(molecule)
		nElements = 0
		(nRn, nY, nAr) = (0, 0, 0)
		for i in range(0, n):
			if molecule[i] >= 'A' and molecule[i] <= 'Z':
				nElements += 1
			if i < n - 1 and molecule[i:i+2] == 'Rn':
				nRn += 1
			if molecule[i] == 'Y':
				nY += 1
			if i < n - 1 and molecule[i:i+2] == 'Ar':
				nAr += 1
		step = nElements - (nRn + nAr) - (nY * 2) - 1 # each Rn and Ar reduces number of steps by 1, each Y reduces number of steps by 2
print(step)
