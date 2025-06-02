#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
valid = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(min1, max1) = [int(x) for x in fileLine.split(' ')[0].split('-')]
	ch = fileLine.split(' ')[1][0]
	password = fileLine.split(': ')[1]
	len1 = len(password)
	n = 0
	for i in range(0, len1):
		if password[i] == ch:
			n += 1
	if n >= min1 and n <= max1:
		valid += 1
print(valid)
