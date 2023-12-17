#!/usr/bin/python3

valueSum = 0
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	l = 0
	while fileLine[l] < '1' or fileLine[l] > '9':
		l += 1
	r = n - 1
	while fileLine[r] < '1' or fileLine[r] > '9':
		r -= 1
	value = (int(fileLine[l]) * 10) + int(fileLine[r])
	valueSum += value
print(valueSum)
