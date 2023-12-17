#!/usr/bin/python3

idSum = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	curId = int(fileLine.split(':')[0].split("Game ")[1])
	possible = True
	shows = fileLine.split(': ')[1].split('; ')
	for show in shows:
		red = 0
		green = 0
		blue = 0
		cubes = show.split(', ')
		for cube in cubes:
			cube1 = cube.split(' ')
			num = int(cube1[0])
			color = cube1[1]
			if color == "red":
				red += num
			if color == "green":
				green += num
			if color == "blue":
				blue += num
		if red > 12 or green > 13 or blue > 14:
			possible = False
	if possible == True:
		idSum += curId
print(idSum)
