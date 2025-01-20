#!/usr/bin/python3

import math

def getPresents(n):
	result = 0
	n2 = math.isqrt(n)
	for i in range(1, n2 + 1):
		if n % i == 0:
			result += (i * 10)
			i2 = n // i
			if i2 != i:
				result += (i2 * 10)
	return result

n = 0
fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
presents = int(fileData.strip())
maxPresents = 0
while True:
	n += 1
	curPresents = getPresents(n)
	maxPresents = max(curPresents, maxPresents)
	if n % 10000 == 0:
		print(str(n) + ", max presents so far = " + str(maxPresents))
	if getPresents(n) >= presents:
		break
print(n)
print(maxPresents)