#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
sheet = []
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	row = [int(x) for x in fileLine.split('\t')]
	sheet.append(row)
n = len(sheet)
checksum = 0
for i in range(0, n):
	maxval = max(sheet[i])
	minval = min(sheet[i])
	checksum += (maxval - minval)
print(checksum)