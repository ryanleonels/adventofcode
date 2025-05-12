#!/usr/bin/python3

import math

total = 0
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
field = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	field.append(list(fileLine))

(row, col) = (len(field), len(field[0]))
asteroids = set()
for i in range(0, row):
	#print(''.join(field[i]))
	for j in range(0, col):
		if field[i][j] == '#':
			asteroids.add((j, i))

#print(len(asteroids))
nmax = 0
best = (-1, -1)
bestDetectables = {}
for asteroid in asteroids:
	#print(asteroid)
	(x1, y1) = asteroid
	n = 0
	detectables = {}
	for asteroid2 in asteroids:
		(x2, y2) = asteroid2
		if x1 != x2 or y1 != y2:
			dx = x2 - x1
			dy = y2 - y1
			gcd = math.gcd(dx, dy)
			dx1 = dx // gcd
			dy1 = dy // gcd
			blocked = False
			for i in range(1, gcd):
				if (x1 + (dx1 * i), y1 + (dy1 * i)) in asteroids:
					blocked = True
					break
			if not blocked:
				n += 1
				dir1 = math.atan2(dx, -dy)
				if dir1 < 0:
					dir1 += (2 * math.pi)
				detectables[dir1] = asteroid2
	#print(n)
	if n > nmax:
		nmax = n
		best = asteroid
		bestDetectables = detectables
#print(best)
#print(nmax)
i = 0
for x in sorted(bestDetectables.keys()):
	i += 1
	#print(i, x, bestDetectables[x])
	if i == 200:
		asteroid = bestDetectables[x]
		print((asteroid[0] * 100) + asteroid[1])

#do additional rounds if needed, just in case
while i < 200:
	#destroy all asteroids so far
	for x in bestDetectables.keys():
		asteroids.remove(bestDetectables[x])
	(x1, y1) = best
	n = 0
	bestDetectables = {}
	for asteroid2 in asteroids:
		(x2, y2) = asteroid2
		if x1 != x2 or y1 != y2:
			dx = x2 - x1
			dy = y2 - y1
			gcd = math.gcd(dx, dy)
			dx1 = dx // gcd
			dy1 = dy // gcd
			blocked = False
			for i1 in range(1, gcd):
				if (x1 + (dx1 * i1), y1 + (dy1 * i1)) in asteroids:
					blocked = True
					break
			if not blocked:
				n += 1
				dir1 = math.atan2(dx, -dy)
				if dir1 < 0:
					dir1 += (2 * math.pi)
				bestDetectables[dir1] = asteroid2
	if len(bestDetectables) == 0: # no more asteroids to destroy (should not happen)
		break
	for x in sorted(bestDetectables.keys()):
		i += 1
		#print(i, x, bestDetectables[x])
		if i == 200:
			asteroid = bestDetectables[x]
			print((asteroid[0] * 100) + asteroid[1])
