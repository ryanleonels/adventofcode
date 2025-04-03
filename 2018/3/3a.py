#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
fabric = {}
overlaps = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	id1 = int(fileLine.split('#')[1].split(' @ ')[0])
	x = int(fileLine.split(' @ ')[1].split(': ')[0].split(',')[0])
	y = int(fileLine.split(' @ ')[1].split(': ')[0].split(',')[1])
	w = int(fileLine.split(': ')[1].split('x')[0])
	h = int(fileLine.split(': ')[1].split('x')[1])
	overlaps[id1] = False
	for i in range(x, x + w):
		for j in range(y, y + h):
			if (i, j) in fabric:
				fabric[(i, j)].append(id1)
				overlaps[id1] = True
			else:
				fabric[(i, j)] = [id1]
for sq in fabric:
	if len(fabric[sq]) > 1:
		for id2 in fabric[sq]:
			overlaps[id2] = True
for id3 in overlaps:
	if overlaps[id3] == False:
		print(id3)