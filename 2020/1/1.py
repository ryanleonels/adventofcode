#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
entries = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	entries.append(int(fileLine))

n = len(entries)
for i in range(0, n - 1):
	for j in range(i + 1, n):
		if entries[i] + entries[j] == 2020:
			print(entries[i] * entries[j])
