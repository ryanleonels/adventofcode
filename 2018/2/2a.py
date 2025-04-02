#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
ids = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	ids.append(fileLine)
n = len(ids)
for i in range(0, n - 1):
	for j in range(i + 1, n):
		n1 = len(ids[i])
		diff = 0
		commons = ""
		for k in range(0, n1):
			if ids[i][k] == ids[j][k]:
				commons += ids[i][k]
			else:
				diff += 1
		if diff == 1:
			print(commons)