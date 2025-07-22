#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(n, cur, prev) = (0, 0, 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	prev = cur
	cur = int(fileLine)
	if cur > prev and prev != 0:
		n += 1

print(n)
