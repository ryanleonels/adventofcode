#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	sides1 = fileLine.split(' ')
	n1 = len(sides1)
	sides = []
	for i in range(0, n1):
		if sides1[i] != '':
			sides.append(int(sides1[i]))
	(a, b, c) = sides
	if a + b > c and a + c > b and b + c > a:
		n += 1
print(n)