#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
totalScore = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(ch1, ch2) = (fileLine[0], fileLine[2])
	curScore = 0
	if ch2 == 'X':
		curScore += 1
		if ch1 == 'A':
			curScore += 3
		if ch1 == 'C':
			curScore += 6
	if ch2 == 'Y':
		curScore += 2
		if ch1 == 'A':
			curScore += 6
		if ch1 == 'B':
			curScore += 3
	if ch2 == 'Z':
		curScore += 3
		if ch1 == 'B':
			curScore += 6
		if ch1 == 'C':
			curScore += 3
	totalScore += curScore
print(totalScore)
