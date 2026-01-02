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
len1 = len(grid[0])
nProblems = 0
problems = []
problem = []
for i in range(0, len1):
	if grid[row - 1][i] != ' ':
		if i > 0:
			problems.append(problem)
		problem = [grid[row - 1][i]]
	number = ''
	for j in range(0, row - 1):
		if grid[j][i] != ' ':
			number += grid[j][i]
	if number != '':
		problem.append(int(number))
	if i == len1 - 1:
		problems.append(problem)
for problem in problems:
	result = 0
	len2 = len(problem)
	if problem[0] == '+':
		for i in range(1, len2):
			result += problem[i]
	if problem[0] == '*':
		result = 1
		for i in range(1, len2):
			result *= problem[i]
	total += result
print(total)
