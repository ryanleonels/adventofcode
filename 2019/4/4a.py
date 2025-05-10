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
		reallyHasDouble = False
		if i1[0] == i1[1] and i1[1] != i1[2]:
			reallyHasDouble = True
		if i1[-1] == i1[-2] and i1[-2] != i1[-3]:
			reallyHasDouble = True
		for j in range(1, len(i1) - 2):
			if i1[j] != i1[j - 1] and i1[j] == i1[j + 1] and i1[j] != i1[j + 2]:
				reallyHasDouble = True
		if reallyHasDouble:
			n += 1
	i += 1
print(n)
