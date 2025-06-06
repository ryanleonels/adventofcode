#!/usr/bin/python3

total = 0
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

answers = ""
for fileLine in fileLines:
	if fileLine.strip() == '': # check answers
		n = len(answers)
		qs = set()
		for i in range(0, n):
			qs.add(answers[i])
		total += len(qs)
		answers = ""
		continue
	answers += fileLine.strip()

print(total)
