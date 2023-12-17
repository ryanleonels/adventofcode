#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
time = int(fileLines[0].split(':')[1].replace(' ', ''))
distance = int(fileLines[1].split(':')[1].replace(' ', ''))
n = 0
for j in range(0, time):
	dist = j * (time - j)
	if dist > distance:
		n += 1
print(n)
