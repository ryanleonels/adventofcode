#!/usr/local/bin/python3

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	row = int(fileLine.split("row ")[1].split(",")[0])
	col = int(fileLine.split("column ")[1].split(".")[0])
cycle = row + col - 1
pos = col
n = (cycle * (cycle - 1) // 2) + pos
code = 20151125
for i in range(1, n):
	code = (code * 252533) % 33554393
print(code)