#!/usr/bin/python3

def compare(l, r):
	if type(l) is int and type(r) is int:
		if l < r:
			return 1
		if l > r:
			return -1
		if l == r:
			return 0
	if type(l) is list and type(r) is list:
		lr = min(len(l), len(r))
		for i in range(0, lr):
			c = compare(l[i], r[i])
			if c != 0:
				return c
		if len(l) < len(r):
			return 1
		if len(l) > len(r):
			return -1
		if len(l) == len(r):
			return 0
	if type(l) is int and type(r) is list:
		return compare([l], r)
	if type(l) is list and type(r) is int:
		return compare(l, [r])

fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0
for i in range(0, len(fileLines), 3):
	left = eval(fileLines[i])
	right = eval(fileLines[i + 1])
	#print(left)
	#print(right)
	rightOrder = compare(left, right)
	if rightOrder == 1:
		#print((i // 3) + 1)
		n += (i // 3) + 1
print(n)
