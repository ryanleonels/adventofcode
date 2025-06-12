#!/usr/local/bin/python3

import math

(lat1, long1, dir1) = (0, 0, 90)
fileHandle = open("12.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	action = fileLine[0]
	val = int(fileLine[1:])
	match action:
		case 'N':
			lat1 += val
		case 'S':
			lat1 -= val
		case 'E':
			long1 += val
		case 'W':
			long1 -= val
		case 'L':
			dir1 -= val
			if dir1 < 0:
				dir1 += 360
		case 'R':
			dir1 += val
			if dir1 >= 360:
				dir1 -= 360
		case 'F':
			lat1 += val * math.cos(dir1 * math.pi / 180)
			long1 += val * math.sin(dir1 * math.pi / 180)

print(abs(lat1) + abs(long1))
