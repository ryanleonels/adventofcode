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

grid1 = []
for i in range(1, 301):
	grid1.append([])
	for j in range(1, 301):
		if i == 1:
			if j == 1:
				grid1[i-1].append(grid[0][0])
			else:
				grid1[i-1].append(grid1[0][j-2] + grid[0][j-1])
		else:
			if j == 1:
				grid1[i-1].append(grid1[i-2][0] + grid[i-1][0])
			else:
				grid1[i-1].append(grid1[i-1][j-2] + grid1[i-2][j-1] - grid1[i-2][j-2] + grid[i-1][j-1])

"""
aab
aab
ccd

area of d = abcd - ab - ac + a"""

(x, y, size) = (0, 0, 0)
maxPower = 0
for k in range(1, 301):
	print("size="+str(k))
	for i in range(1, 302 - k):
		for j in range(1, 302 - k):
			power = grid1[i+k-2][j+k-2]
			if i > 1:
				power -= grid1[i-2][j+k-2]
			if j > 1:
				power -= grid1[i+k-2][j-2]
			if i > 1 and j > 1:
				power += grid1[i-2][j-2]
			if power > maxPower:
				maxPower = power
				(x, y, size) = (i, j, k)
print(x, y, size)
print(maxPower)
