#!/usr/bin/python3

import math

n = 0
found = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
sq = int(fileData.strip())

#square size n from centre: ((2n-1)^2, (2n+1)^2]
#start from (n, n) -> (n, -n) -> (-n, -n) -> (-n, n) -> (n, n)

def getCoord(n):
	n2 = math.isqrt(n)
	if n2 * n2 == n:
		n2 -= 1
	if n2 % 2 == 0:
		n2 -= 1
	size = (n2 + 1) // 2
	n1 = n - (n2 * n2)
	(x, y) = (0, 0)
	if n1 <= (size * 2):
		(x, y) = (size, size - n1)
	if n1 > (size * 2) and n1 <= (size * 4):
		(x, y) = (size - (n1 - (size * 2)), -size)
	if n1 > (size * 4) and n1 <= (size * 6):
		(x, y) = (-size, -size + (n1 - (size * 4)))
	if n1 >= (size * 6):
		(x, y) = (-size + (n1 - (size * 6)), size)
	return (x, y)

grid = {}
grid[(0, 0)] = 1
#print([1, (0, 0), 1])
i = 1
val = 1
while val <= sq:
	i += 1
	(x, y) = getCoord(i)
	val = 0
	if (x-1, y-1) in grid:
		val += grid[(x-1, y-1)]
	if (x-1, y) in grid:
		val += grid[(x-1, y)]
	if (x-1, y+1) in grid:
		val += grid[(x-1, y+1)]
	if (x, y-1) in grid:
		val += grid[(x, y-1)]
	if (x, y+1) in grid:
		val += grid[(x, y+1)]
	if (x+1, y-1) in grid:
		val += grid[(x+1, y-1)]
	if (x+1, y) in grid:
		val += grid[(x+1, y)]
	if (x+1, y+1) in grid:
		val += grid[(x+1, y+1)]
	grid[(x, y)] = val
	#print([i, (x, y), val])
print(val)