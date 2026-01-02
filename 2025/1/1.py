#!/usr/bin/python3

n = 0
dial = 50
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	rotDir = fileLine[0]
	rotQty = int(fileLine[1:])
	if rotDir == 'L':
		dial -= rotQty
	if rotDir == 'R':
		dial += rotQty
	dial %= 100
	if dial == 0:
		n += 1
print(n)
