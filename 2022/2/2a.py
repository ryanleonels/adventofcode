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
		if ch1 == 'A':
			curScore += 3
		if ch1 == 'B':
			curScore += 1
		if ch1 == 'C':
			curScore += 2
	if ch2 == 'Y':
		curScore += 3
		if ch1 == 'A':
			curScore += 1
		if ch1 == 'B':
			curScore += 2
		if ch1 == 'C':
			curScore += 3
	if ch2 == 'Z':
		curScore += 6
		if ch1 == 'A':
			curScore += 2
		if ch1 == 'B':
			curScore += 3
		if ch1 == 'C':
			curScore += 1
	totalScore += curScore
print(totalScore)
