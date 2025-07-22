#!/usr/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(pos, depth) = (0, 0)
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	cmd = fileLine.split(' ')[0]
	n = int(fileLine.split(' ')[1])
	if cmd == "forward":
		pos += n
	if cmd == "down":
		depth += n
	if cmd == "up":
		depth -= n

print(pos * depth)
