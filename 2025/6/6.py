#!/usr/bin/python3

grid = []
tokens = []
total = 0
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row = len(grid)
for i in range(0, row):
	len1 = len(grid[i])
	n1 = 0
	tokens1 = []
	space = True
	token = ""
	for j in range(0, len1):
		if grid[i][j] == ' ':
			if space == False:
				tokens1.append(token)
			space = True
		else:
			if space == True:
				token = grid[i][j]
			else:
				token += grid[i][j]
			space = False
			if j == len1 - 1:
				tokens1.append(token)
	tokens.append(tokens1)
col = len(tokens[0])
for i in range(0, col):
	result = 0
	if tokens[row - 1][i] == '+':
		for j in range(0, row - 1):
			result += int(tokens[j][i])
	if tokens[row - 1][i] == '*':
		result = 1
		for j in range(0, row - 1):
			result *= int(tokens[j][i])
	total += result
print(total)
