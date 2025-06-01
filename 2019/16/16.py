#!/usr/bin/python3

fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()

signal = [int(x) for x in list(fileData.strip())]
n = len(signal)
#print(''.join([str(x) for x in signal]))

phases = 100
for t in range(0, phases):
	signal1 = []
	for pos in range(0, n):
		result = 0
		for pos1 in range(0, n):
			pattern = [0, 1, 0, -1][((pos1 + 1) // (pos + 1)) % 4]
			result += (signal[pos1] * pattern)
		result = abs(result) % 10
		signal1.append(result)
	for pos in range(0, n):
		signal[pos] = signal1[pos]
	#print(''.join([str(x) for x in signal]))
print(''.join([str(x) for x in signal[:8]]))
