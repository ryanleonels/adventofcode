#!/usr/bin/python3

message = ""
columns = []
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if n == 0:
		n = len(fileLine)
		for i in range(0, n):
			columns.append({})
	for i in range(0, n):
		ch = fileLine[i]
		if ch in columns[i]:
			columns[i][ch] += 1
		else:
			columns[i][ch] = 1
for i in range(0, n):
	ch1 = ''
	minN = len(fileLines)
	for ch in columns[i]:
		curN = columns[i][ch]
		if curN < minN:
			minN = curN
			ch1 = ch
	message += ch1
print(message)