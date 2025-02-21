#!/usr/local/bin/python3

def movePos(s, x, y):
	if x < y:
		return s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
	if x == y:
		return s
	if x > y:
		return s[:y] + s[x] + s[y:x] + s[x+1:]

def reversePos(s, x, y):
	return s[:x] + s[x:y+1][::-1] + s[y+1:]

def rotateLeft(s, x):
	return s[x:] + s[:x]

def rotateRight(s, x):
	return rotateLeft(s, len(s) - x)

def rotatePos(s, x):
	x1 = s.index(x)
	if x1 >= 4:
		x1 += 1
	x1 = (x1 + 1) % len(s)
	return rotateRight(s, x1)

def swapPos(s, x, y):
	s1 = list(s)
	(s1[x], s1[y]) = (s[y], s[x])
	return ''.join(s1)

def swapLetter(s, x, y):
	(x1, y1) = (s.index(x), s.index(y))
	return swapPos(s, x1, y1)

fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
password = "fbgdceah"

def unmovePos(s, x, y):
	return movePos(s, y, x)

def unreversePos(s, x, y):
	return reversePos(s, x, y)

def unrotateLeft(s, x):
	return rotateRight(s, x)

def unrotateRight(s, x):
	return rotateLeft(s, x)

def unrotatePos(s, x):
	for i in range(0, len(s)):
		s1 = unrotateRight(s, i)
		if rotatePos(s1, x) == s:
			return s1

def unswapPos(s, x, y):
	return swapPos(s, x, y)

def unswapLetter(s, x, y):
	return swapLetter(s, x, y)

n = len(fileLines)
for i in range(n - 1, -1, -1):
	fileLine = fileLines[i]
	if fileLine.strip() == '':
		continue
	#print(password)
	ops = fileLine.split(' ')
	#print(ops)
	if ops[0] == "move":
		x = int(ops[2])
		y = int(ops[5])
		password = unmovePos(password, x, y)
	if ops[0] == "reverse":
		x = int(ops[2])
		y = int(ops[4])
		password = unreversePos(password, x, y)
		pass
	if ops[0] == "rotate":
		if ops[1] == "based":
			x = ops[6]
			password = unrotatePos(password, x)
		if ops[1] == "left":
			x = int(ops[2])
			password = unrotateLeft(password, x)
		if ops[1] == "right":
			x = int(ops[2])
			password = unrotateRight(password, x)
	if ops[0] == "swap":
		if ops[1] == "letter":
			x = ops[2]
			y = ops[5]
			password = unswapLetter(password, x, y)
		if ops[1] == "position":
			x = int(ops[2])
			y = int(ops[5])
			password = unswapPos(password, x, y)
print(password)