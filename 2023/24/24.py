#!/usr/bin/python3

def intersect(first, second):
	minPos = 200000000000000
	maxPos = 400000000000000
	#minPos = 7
	#maxPos = 27
	posX1 = hailstones[first]["pos"][0]
	posY1 = hailstones[first]["pos"][1]
	vX1 = hailstones[first]["v"][0]
	vY1 = hailstones[first]["v"][1]
	posX2 = hailstones[second]["pos"][0]
	posY2 = hailstones[second]["pos"][1]
	vX2 = hailstones[second]["v"][0]
	vY2 = hailstones[second]["v"][1]
	# find general form
	# a1x + b1y + c1 = 0
	# (posX1, posY1) ~ (posX1 + vX1, posX1 + vY1)
	tempX1 = posX1
	tempX2 = posX1 + vX1
	tempY1 = posY1
	tempY2 = posY1 + vY1
	a1 = tempY2 - tempY1
	b1 = tempX1 - tempX2
	c1 = (tempY1 * (tempX2 - tempX1)) - ((tempY2 - tempY1) * tempX1)
	# a2x + b2y + c2 = 0
	tempX1 = posX2
	tempX2 = posX2 + vX2
	tempY1 = posY2
	tempY2 = posY2 + vY2
	a2 = tempY2 - tempY1
	b2 = tempX1 - tempX2
	c2 = (tempY1 * (tempX2 - tempX1)) - ((tempY2 - tempY1) * tempX1)
	# find point of intersection (x0, y0)
	bc = (b1 * c2) - (b2 * c1)
	ac = (c1 * a2) - (c2 * a1)
	ab = (a1 * b2) - (a2 * b1)
	if ab == 0: # never intersect
		#print(str(first)+" "+str(second)+": parallel paths (never intersect)")
		return False
	x0 = bc / ab
	y0 = ac / ab
	# check time of intersection
	if vX1 == 0: # check from y
		t1 = (y0 - posY1) / vY1
	else: # check from x
		t1 = (x0 - posX1) / vX1
	if vX2 == 0: # check from y
		t2 = (y0 - posY2) / vY2
	else: # check from x
		t2 = (x0 - posX2) / vX2
	# check if intersection happens between minPos and maxPos and in the future for both hailstones
	ok = True
	if x0 < minPos or x0 > maxPos or y0 < minPos or y0 > maxPos or t1 < 0 or t2 < 0:
		ok = False
	#print(str(first)+" "+str(second)+" x="+str(x0)+" y="+str(y0)+" t1="+str(t1)+" t2="+str(t2)+" ok="+str(ok))
	return ok

nIntersections = 0
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
for i in range(0, n):
	for j in range(i + 1, n):
		if intersect(i, j):
			nIntersections += 1
print(nIntersections)
