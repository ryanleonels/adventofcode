#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
gridSN = int(fileData.strip())

grid = []
for x in range(1, 301):
	grid.append([])
	for y in range(1, 301):
		rackID = x + 10
		power = rackID * y
		power += gridSN
		power *= rackID
		power = (power // 100) % 10
		power -= 5
		grid[x-1].append(power)

(x, y) = (0, 0)
maxPower = 0
for i in range(1, 299):
	for j in range(1, 299):
		power = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
		if power > maxPower:
			maxPower = power
			(x, y) = (i, j)
print(x, y)
print(maxPower)