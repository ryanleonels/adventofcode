#!/usr/bin/python3

fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
offsets = []
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	offsets.append(int(fileLine.strip()))
n = len(offsets)
step = 0
ptr = 0
while ptr >= 0 and ptr < n:
	step += 1
	jmp = offsets[ptr]
	offsets[ptr] += 1
	ptr += jmp
print(step)