#!/usr/bin/python3

floor = 0
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
instruction = fileData.strip()
n = len(instruction)
for i in range(0, n):
	if instruction[i] == '(':
		floor += 1
	if instruction[i] == ')':
		floor -= 1
print(floor)