#!/usr/bin/python3

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
(a, b) = [int(x) for x in fileData.split('-')]
n = 0
i = a
while i <= b:
	i1 = str(i)
	hasDouble = False
	neverDecrease = True
	for j in range(1, len(i1)):
		if i1[j] == i1[j - 1]:
			hasDouble = True
		if i1[j] < i1[j - 1]:
			neverDecrease = False
	if hasDouble and neverDecrease:
		n += 1
	i += 1
print(n)
