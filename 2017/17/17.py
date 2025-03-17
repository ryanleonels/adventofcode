#!/usr/bin/python3

fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = int(fileData.strip())

buffer = [0]
pos = 0
for curstep in range(1, 2018):
	n = len(buffer)
	pos = (pos + steps) % n
	buffer.insert(pos + 1, curstep)
	pos += 1
print(buffer[pos+1])