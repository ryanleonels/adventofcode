#!/usr/bin/python3

timelines = 1
timelineCache = {}
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
row = len(fileLines) - 1
col = len(fileLines[0])

def countTimelines(r, c):
	if r == row - 1:
		return 1
	if (r, c) in timelineCache:
		return timelineCache[(r, c)]
	if fileLines[r + 1][c] == '^':
		result = countTimelines(r + 1, c - 1) + countTimelines(r + 1, c + 1)
		timelineCache[(r, c)] = result
		return result
	result = countTimelines(r + 1, c)
	timelineCache[(r, c)] = result
	return result

s = fileLines[0].find('S')
if s != -1:
	timelines = countTimelines(0, s)
print(timelines)
