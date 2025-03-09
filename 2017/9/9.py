#!/usr/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileStream = fileData.strip()

def getScore(stream):
	n = len(stream)
	pos = 0
	level = 0
	score = 0
	inGarbage = False
	isCanceled = False
	while pos < n:
		if isCanceled == True:
			isCanceled = False
		else:
			ch = stream[pos]
			if inGarbage == True:
				if ch == '!':
					isCanceled = True
				if ch == '>':
					inGarbage = False
			else:
				if ch == '<':
					inGarbage = True
				if ch == '{':
					level += 1
				if ch == '}':
					score += level
					level -= 1
				if ch == ',':
					pass
		pos += 1
	return score

print(getScore(fileStream))