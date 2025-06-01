#!/usr/bin/python3

fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()

signal = [int(x) for x in list(fileData.strip())] * 10000
n = len(signal)
n2 = n // 2

offset = int(''.join([str(x) for x in signal[:7]]))
phases = 100
for t in range(0, phases):
	print("Computing phase " + str(t) + "...")
	signal1 = [0] * n
	result = 0
	for pos in range(n - 1, n2 - 1, -1): # only count second half as the input will be from the second half (first half is much harder to compute)
		result += signal[pos]
		signal1[pos] = result % 10
	for pos in range(n2, n):
		signal[pos] = signal1[pos]
print(''.join([str(x) for x in signal[offset:offset+8]]))
