#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	patterns = fileLine.split(' | ')[0].split(' ')
	values = fileLine.split(' | ')[1].split(' ')
	for value in values:
		if len(value) in [2, 3, 4, 7]:
			n += 1
print(n)
