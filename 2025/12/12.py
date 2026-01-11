#!/usr/bin/python3

shapes = {}
regions = []
fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
part = 1
shapeNum = -1
nRegions = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if ': ' in fileLine:
		part = 2
	if part == 1:
		if ':' in fileLine:
			shapeNum = int(fileLine.split(':')[0])
			shapes[shapeNum] = []
		else:
			shapes[shapeNum].append(list(fileLine.strip()))
	if part == 2:
		if ': ' in fileLine:
			regions.append((fileLine.split(': ')[0], [int(x) for x in fileLine.split(': ')[1].split(' ')]))
			nRegions += 1
areasMin = {}
areasMax = {}
for shape in shapes:
	#print(shape, shapes[shape])
	area = 0
	for i in range(0, len(shapes[shape])):
		for j in range(0, len(shapes[shape][i])):
			if shapes[shape][i][j] == '#':
				area += 1
	areasMin[shape] = area
	areasMax[shape] = len(shapes[shape]) * len(shapes[shape][0])
#print(areasMin)
#print(areasMax)
(lowerBound, upperBound) = (0, 0)
for region in regions:
	#print(region)
	(w, h) = [int(x) for x in region[0].split('x')]
	# calculate lower bound - will always be able to fit as total area occupied (including empty spaces) is <= area
	# calculate upper bound - assuming that all the shapes will be able to fit in if total size is <= area
	(areaMin, areaMax) = (0, 0)
	for i in range(0, len(region[1])):
		areaMin += region[1][i] * areasMin[i]
		areaMax += region[1][i] * areasMax[i]
	if areaMin <= w * h:
		upperBound += 1
	if areaMax <= w * h:
		lowerBound += 1
	#print(areaMin, areaMax, w * h)
print(f"Lower bound: {lowerBound}")
print(f"Upper bound: {upperBound}")
