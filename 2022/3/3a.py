#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
rucksacks = []
totalScore = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	rucksacks.append(fileLine)
n = len(rucksacks)
for i in range(0, n, 3):
	badges = []
	for j in range(1, 27):
		if chr(j + 96) in rucksacks[i] and chr(j + 96) in rucksacks[i + 1] and chr(j + 96) in rucksacks[i + 2]:
			totalScore += j
		if chr(j + 64) in rucksacks[i] and chr(j + 64) in rucksacks[i + 1] and chr(j + 64) in rucksacks[i + 2]:
			totalScore += (j + 26)
print(totalScore)
