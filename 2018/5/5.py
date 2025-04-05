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

polymer1 = react(polymer)
print(len(polymer1))
