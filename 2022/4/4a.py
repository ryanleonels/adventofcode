#!/usr/bin/python3

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	start1 = int(fileLine.split(',')[0].split('-')[0])
	end1 = int(fileLine.split(',')[0].split('-')[1])
	start2 = int(fileLine.split(',')[1].split('-')[0])
	end2 = int(fileLine.split(',')[1].split('-')[1])
	noOverlap = False
	# 1 < 2
	if start2 > end1:
		noOverlap = True
	# 1 > 2
	if start1 > end2:
		noOverlap = True
	if not noOverlap:
		n += 1
print(n)
