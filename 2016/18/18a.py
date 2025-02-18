#!/usr/bin/python3

fileHandle = open("18.in", "r")
fileData = fileHandle.read()
fileHandle.close()
line1 = fileData.strip()
#print(line1)

def getSafeTiles(line):
	n = len(line)
	safeTiles = 0
	for i in range(0, n):
		if line[i] == '.':
			safeTiles += 1
	return safeTiles

def getNextLine(prevLine):
	n = len(prevLine)
	nextLine = ""
	for i in range(0, n):
		(left, right) = ('.', '.')
		if i > 0:
			left = prevLine[i - 1]
		center = prevLine[i]
		if i < n - 1:
			right = prevLine[i + 1]
		trap = False
		if left == '^' and center == '^' and right != '^':
			trap = True
		if left != '^' and center == '^' and right == '^':
			trap = True
		if left == '^' and center != '^' and right != '^':
			trap = True
		if left != '^' and center != '^' and right == '^':
			trap = True
		if trap == True:
			nextLine += '^'
		if trap == False:
			nextLine += '.'
	return nextLine

line = line1
safeTiles = getSafeTiles(line)
#print(line)
for i in range(1, 400000):
	if i % 10000 == 0:
		print(i)
	line = getNextLine(line)
	safeTiles += getSafeTiles(line)
	#print(line)
print(safeTiles)