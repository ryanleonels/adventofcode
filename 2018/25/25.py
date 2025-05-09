#!/usr/bin/python3

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

points = []
constellations = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y, z, t) = [int(x) for x in fileLine.split(',')]
	points.append((x, y, z, t))
	constellations.append(-1)

n = len(points)
cur = 0
n1 = 0
while n1 < n:
	i1 = 0
	while constellations[i1] != -1:
		i1 += 1
	constellations[i1] = cur
	n1 += 1
	done = False
	while not done:
		done = True
		for i in range(0, n):
			if constellations[i] == cur:
				for j in range(0, n):
					if i != j and constellations[j] == -1 and abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) + abs(points[i][2] - points[j][2]) + abs(points[i][3] - points[j][3]) <= 3:
						constellations[j] = constellations[i]
						done = False
						n1 += 1
	cur += 1
print(cur)
#print(constellations)