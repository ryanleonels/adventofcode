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
password = "abcdefgh"

#password = "abcde"
#fileLines = ['swap position 4 with position 0', 'swap letter d with letter b', 'reverse positions 0 through 4', 'rotate left 1 step', 'move position 1 to position 4', 'move position 3 to position 0', 'rotate based on position of letter b', 'rotate based on position of letter d']

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	#print(password)
	ops = fileLine.split(' ')
	#print(ops)
	if ops[0] == "move":
		x = int(ops[2])
		y = int(ops[5])
		password = movePos(password, x, y)
	if ops[0] == "reverse":
		x = int(ops[2])
		y = int(ops[4])
		password = reversePos(password, x, y)
		pass
	if ops[0] == "rotate":
		if ops[1] == "based":
			x = ops[6]
			password = rotatePos(password, x)
		if ops[1] == "left":
			x = int(ops[2])
			password = rotateLeft(password, x)
		if ops[1] == "right":
			x = int(ops[2])
			password = rotateRight(password, x)
	if ops[0] == "swap":
		if ops[1] == "letter":
			x = ops[2]
			y = ops[5]
			password = swapLetter(password, x, y)
		if ops[1] == "position":
			x = int(ops[2])
			y = int(ops[5])
			password = swapPos(password, x, y)
print(password)