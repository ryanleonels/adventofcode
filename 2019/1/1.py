#!/usr/bin/python3

total = 0
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	m = int(fileLine)
	f = (m // 3) - 2
	total += f
print(total)
