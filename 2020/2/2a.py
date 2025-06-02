#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
valid = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(pos1, pos2) = [int(x) for x in fileLine.split(' ')[0].split('-')]
	ch = fileLine.split(' ')[1][0]
	password = fileLine.split(': ')[1]
	isValid = False
	if (password[pos1 - 1] == ch) or (password[pos2 - 1] == ch):
		isValid = True
	if (password[pos1 - 1] == ch) and (password[pos2 - 1] == ch):
		isValid = False
	if isValid:
		valid += 1
print(valid)
