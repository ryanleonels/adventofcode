#!/usr/local/bin/python3

import numpy

def solveRock():
	pos1 = hailstones[0]["pos"]
	v1 = hailstones[0]["v"]
	pos2 = hailstones[1]["pos"]
	v2 = hailstones[1]["v"]
	pos3 = hailstones[2]["pos"]
	v3 = hailstones[2]["v"]
	A = numpy.array([
	    [-(v1[1] - v2[1]), v1[0] - v2[0], 0, pos1[1] - pos2[1], -(pos1[0] - pos2[0]), 0],
	    [-(v1[1] - v3[1]), v1[0] - v3[0], 0, pos1[1] - pos3[1], -(pos1[0] - pos3[0]), 0],
	    [0, -(v1[2] - v2[2]), v1[1] - v2[1],  0, pos1[2] - pos2[2], -(pos1[1] - pos2[1])],
	    [0, -(v1[2] - v3[2]), v1[1] - v3[1],  0, pos1[2] - pos3[2], -(pos1[1] - pos3[1])],
	    [-(v1[2] - v2[2]), 0, v1[0] - v2[0],  pos1[2] - pos2[2], 0, -(pos1[0] - pos2[0])],
	    [-(v1[2] - v3[2]), 0, v1[0] - v3[0],  pos1[2] - pos3[2], 0, -(pos1[0] - pos3[0])]
    ])
	b = [
        (pos1[1] * v1[0] - pos2[1] * v2[0]) - (pos1[0] * v1[1] - pos2[0] * v2[1]),
        (pos1[1] * v1[0] - pos3[1] * v3[0]) - (pos1[0] * v1[1] - pos3[0] * v3[1]),
        (pos1[2] * v1[1] - pos2[2] * v2[1]) - (pos1[1] * v1[2] - pos2[1] * v2[2]),
        (pos1[2] * v1[1] - pos3[2] * v3[1]) - (pos1[1] * v1[2] - pos3[1] * v3[2]),
        (pos1[2] * v1[0] - pos2[2] * v2[0]) - (pos1[0] * v1[2] - pos2[0] * v2[2]),
        (pos1[2] * v1[0] - pos3[2] * v3[0]) - (pos1[0] * v1[2] - pos3[0] * v3[2])
    ]
	#print(A)
	#print(b)
	return numpy.linalg.solve(A, b)

hailstones = []
fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["19, 13, 30 @ -2,  1, -2","18, 19, 22 @ -1, -1, -2","20, 25, 34 @ -2, -2, -4","12, 31, 28 @ -1, -2, -1","20, 19, 15 @  1, -5, -3"]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	posX = int(fileLine.split(" @ ")[0].split(", ")[0])
	posY = int(fileLine.split(" @ ")[0].split(", ")[1])
	posZ = int(fileLine.split(" @ ")[0].split(", ")[2])
	vX = int(fileLine.split(" @ ")[1].split(", ")[0])
	vY = int(fileLine.split(" @ ")[1].split(", ")[1])
	vZ = int(fileLine.split(" @ ")[1].split(", ")[2])
	hailstone = {"pos": (posX, posY, posZ), "v": (vX, vY, vZ)}
	hailstones.append(hailstone)
n = len(hailstones)
#print(n)
#for i in range(0, n):
	#print(hailstones[i])
rock = solveRock()
#print(rock)
print(int(rock[0]+rock[1]+rock[2]+1e-14))
