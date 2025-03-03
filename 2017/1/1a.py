#!/usr/bin/python3

fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
digits = fileData.strip()
n = len(digits)
sumDigits = 0
for i in range(0, n):
	i1 = i + (n // 2)
	if i1 >= n:
		i1 -= n
	if digits[i] == digits[i1]:
		sumDigits += int(digits[i])
print(sumDigits)