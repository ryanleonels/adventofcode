#!/usr/bin/python3

total = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	dim = [int(x) for x in fileLine.split('x')]
	(l, w, h) = (dim[0], dim[1], dim[2])
	longest = max(l, w, h)
	wrap = (l + w + h - longest) * 2
	bow = l * w * h
	cur = wrap + bow
	total += cur
print(total)