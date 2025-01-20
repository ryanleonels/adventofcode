#!/usr/bin/python3

molecule = ""
molecules = set()
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
		n = len(replacements)
		n1 = len(molecule)
		for i in range(0, n):
			n2 = len(replacements[i][0])
			for j in range(0, n1):
				if j <= n1 - n2 and molecule[j:j+n2] == replacements[i][0]:
					molecule1 = molecule[0:j] + replacements[i][1] + molecule[j+n2:n1]
					molecules.add(molecule1)
print(len(molecules))
