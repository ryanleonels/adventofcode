#!/usr/bin/python3

powerSum = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	curId = int(fileLine.split(':')[0].split("Game ")[1])
	shows = fileLine.split(': ')[1].split('; ')
	maxred = 0
	maxgreen = 0
	maxblue = 0
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
		if red > maxred:
			maxred = red
		if green > maxgreen:
			maxgreen = green
		if blue > maxblue:
			maxblue = blue
	power = maxred * maxgreen * maxblue
	powerSum += power
print(powerSum)
