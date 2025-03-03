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
	n1 = len(sheet[i])
	for j in range(0, n1):
		for k in range(0, n1):
			if j != k and sheet[i][j] % sheet[i][k] == 0:
				checksum += (sheet[i][j] // sheet[i][k])
print(checksum)