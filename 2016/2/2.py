#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
instructions = fileData.split('\n')
(row, col) = (1, 1)
code = ""
for instruction in instructions:
	if instruction.strip() == '':
		continue
	n = len(instruction)
	for i in range(0, n):
		if instruction[i] == 'U' and row > 0:
			row -= 1
		if instruction[i] == 'D' and row < 2:
			row += 1
		if instruction[i] == 'L' and col > 0:
			col -= 1
		if instruction[i] == 'R' and col < 2:
			col += 1
	button = (row * 3) + (col + 1)
	code += str(button)
print(code)