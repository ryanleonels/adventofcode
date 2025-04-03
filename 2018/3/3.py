#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
fabric = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	id1 = int(fileLine.split('#')[1].split(' @ ')[0])
	x = int(fileLine.split(' @ ')[1].split(': ')[0].split(',')[0])
	y = int(fileLine.split(' @ ')[1].split(': ')[0].split(',')[1])
	w = int(fileLine.split(': ')[1].split('x')[0])
	h = int(fileLine.split(': ')[1].split('x')[1])
	for i in range(x, x + w):
		for j in range(y, y + h):
			if (i, j) in fabric:
				fabric[(i, j)].append(id1)
			else:
				fabric[(i, j)] = [id1]
n = 0
for sq in fabric:
	if len(fabric[sq]) > 1:
		n += 1
print(n)