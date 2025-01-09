#!/usr/bin/python3

from itertools import permutations

minDist = 999999999
distances = {}
cities = []
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	from1 = fileLine.split(' to ')[0]
	to1 = fileLine.split(' to ')[1].split(' = ')[0]
	dist = int(fileLine.split(' = ')[1])
	if from1 not in cities:
		cities.append(from1)
		distances[from1] = {}
		distances[from1][from1] = 0
	if to1 not in cities:
		cities.append(to1)
		distances[to1] = {}
		distances[to1][to1] = 0
	distances[from1][to1] = dist
	distances[to1][from1] = dist
n = len(cities)
orders = list(permutations(cities))
for order in orders:
	curDist = 0
	for i in range(0, n - 1):
		curDist += distances[order[i]][order[i+1]]
	if curDist < minDist:
		minDist = curDist
print(minDist)