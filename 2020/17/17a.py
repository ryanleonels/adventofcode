#!/usr/bin/python3

grid2 = []
fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid2.append(list(fileLine.strip()))

row = len(grid2)
col = len(grid2[0])
#print(row, col)

cubes = {}
for i in range(0, row):
	#print(grid2[i])
	for j in range(0, col):
		if grid2[i][j] == '#':
			cubes[(i, j, 0, 0)] = True
		else:
			cubes[(i, j, 0, 0)] = False

xmin = 0
xmax = row - 1
ymin = 0
ymax = col - 1
zmin = 0
zmax = 0
wmin = 0
wmax = 0

n = 0
cubes1 = {}
for cycle in range(0, 6):
	for i in range(xmin - 1, xmax + 2):
		for j in range(ymin - 1, ymax + 2):
			for k in range(zmin - 1, zmax + 2):
				for l in range(wmin - 1, wmax + 2):
					adj = 0
					for i1 in range(-1, 2):
						if i + i1 >= xmin and i + i1 <= xmax:
							for j1 in range(-1, 2):
								if j + j1 >= ymin and j + j1 <= ymax:
									for k1 in range(-1, 2):
										if k + k1 >= zmin and k + k1 <= zmax:
											for l1 in range(-1, 2):
												if l + l1 >= wmin and l + l1 <= wmax and (i1, j1, k1, l1) != (0, 0, 0, 0):
													if cubes[(i + i1, j + j1, k + k1, l + l1)]:
														adj += 1
					if (i, j, k, l) in cubes and cubes[(i, j, k, l)]:
						if adj == 2 or adj == 3:
							cubes1[(i, j, k, l)] = True
						else:
							cubes1[(i, j, k, l)] = False
					else:
						if adj == 3:
							cubes1[(i, j, k, l)] = True
						else:
							cubes1[(i, j, k, l)] = False
	(xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax) = (xmin - 1, xmax + 1, ymin - 1, ymax + 1, zmin - 1, zmax + 1, wmin - 1, wmax + 1)
	n = 0
	cubes = {}
	for cube in cubes1:
		cubes[cube] = cubes1[cube]
		if cubes[cube]:
			n += 1
print(n)
