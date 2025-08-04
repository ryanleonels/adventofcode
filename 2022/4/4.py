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
	fullyContained = False
	# 1 fully contains 2
	if start2 >= start1 and start2 <= end1 and end2 >= start1 and end2 <= end1:
		fullyContained = True
	# 2 fully contains 1
	if start1 >= start2 and start1 <= end2 and end1 >= start2 and end1 <= end2:
		fullyContained = True
	if fullyContained:
		n += 1
print(n)
