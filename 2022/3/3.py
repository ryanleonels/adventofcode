#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
totalScore = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	n2 = n // 2
	for i in range(1, 27):
		if chr(i + 96) in fileLine[:n2] and chr(i + 96) in fileLine[n2:]:
			totalScore += i
		if chr(i + 64) in fileLine[:n2] and chr(i + 64) in fileLine[n2:]:
			totalScore += (i + 26)
print(totalScore)
