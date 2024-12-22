#!/usr/bin/python3

def mix(x, y):
	return x ^ y

def prune(x):
	return x % 16777216

def encrypt(x):
	x1 = prune(mix(x, x * 64))
	x2 = prune(mix(x1, x1 // 32))
	x3 = prune(mix(x2, x2 * 2048))
	return x3

total = 0
#fileHandle = open("temp.in", "r")
fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	secret = int(fileLine)
	for i in range(0, 2000):
		secret = encrypt(secret)
	total += secret
	#print(secret)
print(total)
