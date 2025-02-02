#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
instructions = fileData.split('\n')
(row, col) = (2, 0)
keys = {}
keys[(0, 2)] = '1'
keys[(1, 1)] = '2'
keys[(1, 2)] = '3'
keys[(1, 3)] = '4'
keys[(2, 0)] = '5'
keys[(2, 1)] = '6'
keys[(2, 2)] = '7'
keys[(2, 3)] = '8'
keys[(2, 4)] = '9'
keys[(3, 1)] = 'A'
keys[(3, 2)] = 'B'
keys[(3, 3)] = 'C'
keys[(4, 2)] = 'D'
code = ""
for instruction in instructions:
	if instruction.strip() == '':
		continue
	n = len(instruction)
	for i in range(0, n):
		if instruction[i] == 'U' and (row - 1, col) in keys:
			row -= 1
		if instruction[i] == 'D' and (row + 1, col) in keys:
			row += 1
		if instruction[i] == 'L' and (row, col - 1) in keys:
			col -= 1
		if instruction[i] == 'R' and (row, col + 1) in keys:
			col += 1
	button = keys[(row, col)]
	code += button
print(code)