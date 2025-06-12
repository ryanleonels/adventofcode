#!/usr/local/bin/python3

import math

(latS, longS, latW, longW) = (0, 0, 1, 10)
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
			latW += val
		case 'S':
			latW -= val
		case 'E':
			longW += val
		case 'W':
			longW -= val
		case 'L':
			radW = math.sqrt((latW * latW) + (longW * longW))
			dirW = math.atan2(longW, latW) * 180 / math.pi
			dirW -= val
			if dirW < 0:
				dirW += 360
			latW = radW * math.cos(dirW * math.pi / 180)
			longW = radW * math.sin(dirW * math.pi / 180)
		case 'R':
			radW = math.sqrt((latW * latW) + (longW * longW))
			dirW = math.atan2(longW, latW) * 180 / math.pi
			dirW += val
			if dirW >= 360:
				dirW -= 360
			latW = radW * math.cos(dirW * math.pi / 180)
			longW = radW * math.sin(dirW * math.pi / 180)
		case 'F':
			latS += val * latW
			longS += val * longW

print(abs(latS) + abs(longS))
