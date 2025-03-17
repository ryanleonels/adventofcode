#!/usr/bin/python3

fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = int(fileData.strip())

buffer = [0, 0]
pos = 0
curstep = 0
while curstep < 50000000:
	curstep += 1
	pos = (pos + steps) % curstep
	if pos == 0:
		buffer[1] = curstep
		#print(curstep)
	pos += 1
print(buffer[1])