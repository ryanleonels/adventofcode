#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(n, n1) = (0, 0)
entries = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	cur = int(fileLine)
	entries.append(cur)
	n += 1

(cur, prev) = (entries[0] + entries[1] + entries[2], 0)
for i in range(3, n):
	prev = cur
	cur += (entries[i] - entries[i - 3])
	if cur > prev:
		n1 += 1

print(n1)
