#!/usr/bin/python3

import math

fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
pos = []
vel = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	x = int(fileLine.split("x=")[1].split(",")[0])
	y = int(fileLine.split("y=")[1].split(",")[0])
	z = int(fileLine.split("z=")[1].split(">")[0])
	pos.append([x, y, z])
	vel.append([0, 0, 0])
	n += 1

#pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
#pos = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
pos0 = []
for i in range(0, n):
	(x, y, z) = pos[i]
	pos0.append([x, y, z])

t = 0
"""print(t)
for i in range(0, n):
	print(pos[i], vel[i])"""

cycles = [0, 0, 0]
while 0 in cycles:
	for i in range(0, n - 1):
		for j in range(i + 1, n):
			for k in range(0, 3):
				if pos[i][k] > pos[j][k]:
					vel[i][k] -= 1
					vel[j][k] += 1
				if pos[i][k] < pos[j][k]:
					vel[i][k] += 1
					vel[j][k] -= 1
	for i in range(0, n):
		for k in range(0, 3):
			pos[i][k] += vel[i][k]
	t += 1
	for i in range(0, 3):
		if cycles[i] == 0:
			cycle = True
			for j in range(0, n):
				if pos[j][i] != pos0[j][i] or vel[j][i] != 0:
					cycle = False
					break
			if cycle:
				cycles[i] = t

#print(cycles)
print(math.lcm(cycles[0], cycles[1], cycles[2]))
