#!/usr/bin/python3

containers = []
combinations = {} # combinations[n][r][k] = number of ways to store k litres using r of the first n containers
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
combinations[0][0] = {}
combinations[0][0][0] = 1
for i in range(0, n):
	combinations[i+1] = {}
	for j in range(0, i+2):
		combinations[i+1][j] = {}
	for j in range(0, i+1):
		for k in combinations[i][j]:
			if k not in combinations[i+1][j]:
				combinations[i+1][j][k] = 0
			combinations[i+1][j][k] += combinations[i][j][k]
			c = containers[i]
			if k+c not in combinations[i+1][j+1]:
				combinations[i+1][j+1][k+c] = 0
			combinations[i+1][j+1][k+c] += combinations[i][j][k]
for i in range(0, n):
	if 150 in combinations[n][i]:
		print(combinations[n][i][150])
		break
