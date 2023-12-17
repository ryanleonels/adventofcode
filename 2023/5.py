#!/usr/bin/python3

# 0-7: seed, soil, fertilizer, water, light, temperature, humidity, location
minLocation = 2147483647
params = []
maps = []
for i in range(0,8):
	params.append([])
	maps.append([])
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
curMap = -1
titleRow = False
n = 0
for fileLine in fileLines:
	if len(fileLine) == 0:
		curMap += 1
		titleRow = True
		continue
	if titleRow == True:
		titleRow = False
		continue
	if curMap == -1:
		seeds = fileLine.split(' ')
		for i in range(1,len(seeds)):
			params[0].append(int(seeds[i]))
		n = len(params[0])
		continue
	paramData = fileLine.split(' ')
	maps[curMap].append((int(paramData[0]), int(paramData[1]), int(paramData[2])))
for i in range(0, 7):
	for j in range(0, n):
		processed = False
		for k in range(0, len(maps[i])):
			if params[i][j] >= maps[i][k][1] and params[i][j] < maps[i][k][1] + maps[i][k][2] and processed == False:
				processed = True
				params[i+1].append(maps[i][k][0] + (params[i][j] - maps[i][k][1]))
		if processed == False:
			params[i+1].append(params[i][j])
for i in range(0, n):
	if params[7][i] < minLocation:
		minLocation = params[7][i]
print(minLocation)
