#!/usr/bin/python3

# 0-7: seed, soil, fertilizer, water, light, temperature, humidity, location
minLocation = 2147483647
seeds = []
maps = []
for i in range(0,7):
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
		seedLine = fileLine.split(' ')
		for i in range(1,len(seedLine), 2):
			seeds.append((int(seedLine[i]), int(seedLine[i+1])))
		n = len(seeds)
		continue
	paramData = fileLine.split(' ')
	maps[curMap].append((int(paramData[0]), int(paramData[1]), int(paramData[2])))
start = 0
end = 0
minloc = 0
for i in range(0, n):
	print("Processing range " + str(seeds[i]) + "...")
	for j in range(0, seeds[i][1], 1000):
		param = seeds[i][0] + j
		for i1 in range(0, 7):
			processed = False
			for j1 in range(0, len(maps[i1])):
				if processed == False and param >= maps[i1][j1][1] and param < maps[i1][j1][1] + maps[i1][j1][2]:
					processed = True
					param = maps[i1][j1][0] + (param - maps[i1][j1][1])
		if param < minLocation:
			start = seeds[i][0]
			end = seeds[i][0] + seeds[i][1]
			minloc = seeds[i][0] + j
			minLocation = param
			print(str(seeds[i][0] + j) + "th seed processed, location = " + str(param))
start1 = minloc - 1000
if start1 < start:
	start1 = start
end1 = minloc + 1000
if end1 > end:
	end1 = end
for i in range(start1, end1):
	param = i
	for i1 in range(0, 7):
		processed = False
		for j1 in range(0, len(maps[i1])):
			if processed == False and param >= maps[i1][j1][1] and param < maps[i1][j1][1] + maps[i1][j1][2]:
				processed = True
				param = maps[i1][j1][0] + (param - maps[i1][j1][1])
	if param < minLocation:
		minLocation = param
		print(str(i) + "th seed processed, location = " + str(param))
print(minLocation)
