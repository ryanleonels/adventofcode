#!/usr/bin/python3

totalScore = 0
row = 0
col = 0
grid = []
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append([int(x) for x in list(fileLine)])
row = len(grid)
col = len(grid[0])
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] == 0:
			score = 0
			trailStack = [(i, j)]
			peaks = []
			while len(trailStack) > 0:
				cur = trailStack.pop()
				height = grid[cur[0]][cur[1]]
				if height == 9:
					peaks.append(cur)
					continue
				if cur[0] > 0 and grid[cur[0] - 1][cur[1]] == height + 1:
					trailStack.append((cur[0] - 1, cur[1]))
				if cur[0] < row - 1 and grid[cur[0] + 1][cur[1]] == height + 1:
					trailStack.append((cur[0] + 1, cur[1]))
				if cur[1] > 0 and grid[cur[0]][cur[1] - 1] == height + 1:
					trailStack.append((cur[0], cur[1] - 1))
				if cur[1] < col - 1 and grid[cur[0]][cur[1] + 1] == height + 1:
					trailStack.append((cur[0], cur[1] + 1))
			score = len(peaks)
			totalScore += score
print(totalScore)