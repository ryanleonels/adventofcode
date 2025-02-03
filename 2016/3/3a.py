#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
n2 = 0
(col1, col2, col3) = ([], [], [])
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	sides1 = fileLine.split(' ')
	n1 = len(sides1)
	sides = []
	for i in range(0, n1):
		if sides1[i] != '':
			sides.append(int(sides1[i]))
	col1.append(sides[0])
	col2.append(sides[1])
	col3.append(sides[2])
	n2 += 1
for i in range(0, n2, 3):
	(a, b, c) = (col1[i], col1[i + 1], col1[i + 2])
	if a + b > c and a + c > b and b + c > a:
		n += 1
	(a, b, c) = (col2[i], col2[i + 1], col2[i + 2])
	if a + b > c and a + c > b and b + c > a:
		n += 1
	(a, b, c) = (col3[i], col3[i + 1], col3[i + 2])
	if a + b > c and a + c > b and b + c > a:
		n += 1
print(n)