#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
dataStream = list(fileData.strip())
len1 = len(dataStream)
for i in range(4, len1 + 1):
	ch1 = dataStream[i - 1]
	ch2 = dataStream[i - 2]
	ch3 = dataStream[i - 3]
	ch4 = dataStream[i - 4]
	if ch1 != ch2 and ch1 != ch3 and ch1 != ch4 and ch2 != ch3 and ch2 != ch4 and ch3 != ch4:
		print(i)
		break
