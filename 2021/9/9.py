#!/usr/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
heightMap = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	heightMap.append(fileLine)
row = len(heightMap)
col = len(heightMap[0])
riskLevel = 0
for i in range(0, row):
	for j in range(0, col):
		lowPoint = True
		if i > 0 and heightMap[i - 1][j] <= heightMap[i][j]:
			lowPoint = False
		if i < row - 1 and heightMap[i + 1][j] <= heightMap[i][j]:
			lowPoint = False
		if j > 0 and heightMap[i][j - 1] <= heightMap[i][j]:
			lowPoint = False
		if j < col - 1 and heightMap[i][j + 1] <= heightMap[i][j]:
			lowPoint = False
		if lowPoint == True:
			riskLevel += (int(heightMap[i][j]) + 1)
print(riskLevel)
