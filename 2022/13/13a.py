#!/usr/bin/python3

import functools

def compare(l, r):
	if type(l) is int and type(r) is int:
		if l < r:
			return -1
		if l > r:
			return 1
		if l == r:
			return 0
	if type(l) is list and type(r) is list:
		lr = min(len(l), len(r))
		for i in range(0, lr):
			c = compare(l[i], r[i])
			if c != 0:
				return c
		if len(l) < len(r):
			return -1
		if len(l) > len(r):
			return 1
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
packets = []
for i in range(0, len(fileLines), 3):
	left = eval(fileLines[i])
	right = eval(fileLines[i + 1])
	packets.append(left)
	packets.append(right)
packets.append([[2]])
packets.append([[6]])

sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
(l, r) = (0, 0)
for i in range(0, len(packets)):
	#print(sorted_packets[i])
	if sorted_packets[i] == [[2]]:
		l = i + 1
	if sorted_packets[i] == [[6]]:
		r = i + 1
#print(l, r)
print(l * r)
