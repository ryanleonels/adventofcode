#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
dataStream = fileData.strip()
len1 = len(dataStream)
for i in range(14, len1 + 1):
	set1 = set(dataStream[i-14:i])
	if len(set1) == 14:
		print(i)
		break
