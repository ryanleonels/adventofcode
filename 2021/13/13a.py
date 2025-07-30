#!/usr/bin/python3

fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
paper = set()
folds = []
foldPart = False
for fileLine in fileLines:
	if fileLine.strip() == '':
		foldPart = True
		continue
	if foldPart == False:
		(x, y) = [int(z) for z in fileLine.split(',')]
		paper.add((x, y))
	if foldPart == True:
		axis = fileLine.split("along ")[1].split('=')[0]
		n = int(fileLine.split("along ")[1].split('=')[1])
		folds.append((axis, n))

nFolds = len(folds)
for i in range(0, nFolds):
	(axis, n) = folds[i]
	paper1 = set()
	for (x, y) in paper:
		if axis == 'x' and x > n:
			x = n - (x - n)
		if axis == 'y' and y > n:
			y = n - (y - n)
		#print(x, y)
		paper1.add((x, y))
	paper = paper1
	#print(len(paper))

(xmin, xmax, ymin, ymax) = (9999, 0, 9999, 0)
for (x, y) in paper:
	xmin = min(xmin, x)
	xmax = max(xmax, x)
	ymin = min(ymin, y)
	ymax = max(ymax, y)

for y in range(ymin, ymax + 1):
	row = ""
	for x in range(xmin, xmax + 1):
		if (x, y) in paper:
			row += '█'
		else:
			row += ' '
	print(row)
