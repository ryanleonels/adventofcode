#!/usr/bin/python3

fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
polymer = fileData.strip()

def react(units):
	n = len(units)
	res = ""
	for i in range(0, n):
		res += units[i]
		if len(res) >= 2 and abs(ord(res[-1]) - ord(res[-2])) == 32:
			res = res[:-2]
	return res

def removeUnit(units, ch):
	n = len(units)
	res = ""
	for i in range(0, n):
		if ord(units[i]) != ch and ord(units[i]) != (ch + 32):
			res += units[i]
	return res

minLength = len(polymer)
for i in range(65, 91):
	polymer1 = removeUnit(polymer, i)
	polymer2 = react(polymer1)
	#print(chr(i), len(polymer1), len(polymer2))
	minLength = min(minLength, len(polymer2))
print(minLength)