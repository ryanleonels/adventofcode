#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
bits = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	bits.append(fileLine.strip())

n = len(bits)
n1 = len(bits[0])
(gamma, epsilon) = (0, 0)
for i in range(0, n1):
	bit1 = 0
	for j in range(0, n):
		if bits[j][i] == '1':
			bit1 += 1
	if bit1 >= n / 2:
		curbit = 1
	else:
		curbit = 0
	gamma *= 2
	epsilon *= 2
	gamma += curbit
	epsilon += (1 - curbit)

print(gamma * epsilon)
