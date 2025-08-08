#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
grid = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	row1 = [int(x) for x in list(fileLine.strip())]
	grid.append(row1)
row = len(grid)
col = len(grid[0])
maxScore = 0
for i in range(0, row):
	for j in range(0, col):
		score = 1
		#check up
		score1 = 0
		for k in range(i - 1, -1, -1):
			score1 += 1
			if grid[k][j] >= grid[i][j]:
				break
		score *= score1
		#check down
		score1 = 0
		for k in range(i + 1, row):
			score1 += 1
			if grid[k][j] >= grid[i][j]:
				break
		score *= score1
		#check left
		score1 = 0
		for k in range(j - 1, -1, -1):
			score1 += 1
			if grid[i][k] >= grid[i][j]:
				break
		score *= score1
		#check right
		score1 = 0
		for k in range(j + 1, col):
			score1 += 1
			if grid[i][k] >= grid[i][j]:
				break
		score *= score1
		if score > maxScore:
			maxScore = score
print(maxScore)
