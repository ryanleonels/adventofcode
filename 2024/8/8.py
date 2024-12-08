#!/usr/bin/python3

result = 0
row = 0
col = 0
grid = []
antennas = {}
antinodes = []
fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))
row = len(grid)
col = len(grid[0])
for i in range(0, row):
	antinodes.append([])
	for j in range(0, col):
		antinodes[i].append(False)
		if grid[i][j] != '.':
			ch = grid[i][j]
			if ch in antennas:
				antennas[ch].append((i,j))
			else:
				antennas[ch] = [(i,j)]
for ch in antennas:
	n = len(antennas[ch])
	for i in range(0, n - 1):
		for j in range(i + 1, n):
			x1 = antennas[ch][i][0]
			y1 = antennas[ch][i][1]
			x2 = antennas[ch][j][0]
			y2 = antennas[ch][j][1]
			xa1 = x2 + (x2 - x1)
			ya1 = y2 + (y2 - y1)
			xa2 = x1 - (x2 - x1)
			ya2 = y1 - (y2 - y1)
			if xa1 >= 0 and xa1 < row and ya1 >= 0 and ya1 < col:
				antinodes[xa1][ya1] = True
			if xa2 >= 0 and xa2 < row and ya2 >= 0 and ya2 < col:
				antinodes[xa2][ya2] = True
for i in range(0, row):
	for j in range(0, col):
		if antinodes[i][j] == True:
			result += 1
print(result)