#!/usr/bin/python3

maxID = 0
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(rowmin, rowmax, rowsize) = (0, 127, 128)
	for i in range(0, 7):
		rowsize //= 2
		if fileLine[i] == 'F':
			rowmax -= rowsize
		if fileLine[i] == 'B':
			rowmin += rowsize
	row = rowmin
	(colmin, colmax, colsize) = (0, 7, 8)
	for i in range(7, 10):
		colsize //= 2
		if fileLine[i] == 'L':
			colmax -= colsize
		if fileLine[i] == 'R':
			colmin += colsize
	col = colmin
	seatID = (row * 8) + col
	#print(row, col, seatID)
	maxID = max(maxID, seatID)

print(maxID)
