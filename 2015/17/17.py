#!/usr/bin/python3

containers = []
combinations = {} # combinations[n][k] = number of ways to store k litres using the first n containers
fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	container = int(fileLine)
	containers.append(container)
n = len(containers)
combinations[0] = {}
combinations[0][0] = 1
for i in range(0, n):
	combinations[i+1] = {}
	for k in combinations[i]:
		if k not in combinations[i+1]:
			combinations[i+1][k] = 0
		combinations[i+1][k] += combinations[i][k]
		c = containers[i]
		if k+c not in combinations[i+1]:
			combinations[i+1][k+c] = 0
		combinations[i+1][k+c] += combinations[i][k]
print(combinations[n][150])
