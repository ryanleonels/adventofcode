#!/usr/bin/python3

def fuel(n):
	return max((n // 3) - 2, 0)

total = 0
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	m = int(fileLine)
	f = fuel(m)
	f1 = f
	while fuel(f1) > 0:
		f += fuel(f1)
		f1 = fuel(f1)
	total += f
print(total)
