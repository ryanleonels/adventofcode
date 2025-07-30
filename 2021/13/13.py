#!/usr/bin/python3

fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
dots = []
folds = []
foldPart = False
for fileLine in fileLines:
	if fileLine.strip() == '':
		foldPart = True
		continue
	if foldPart == False:
		(x, y) = [int(z) for z in fileLine.split(',')]
		dots.append((x, y))
	if foldPart == True:
		axis = fileLine.split("along ")[1].split('=')[0]
		n = int(fileLine.split("along ")[1].split('=')[1])
		folds.append((axis, n))

paper = set()
nDots = len(dots)
(axis, n) = folds[0]
for i in range(0, nDots):
	(x, y) = dots[i]
	if axis == 'x' and x > n:
		x = n - (x - n)
	if axis == 'y' and y > n:
		y = n - (y - n)
	dots[i] = (x, y)
	#print(x, y)
	paper.add((x, y))
print(len(paper))
