#!/usr/bin/python3

def lookAndSay(x):
	result = ""
	n = len(x)
	curNum = 0
	curCnt = 0
	pos = 0
	while pos < n:
		if int(x[pos]) == curNum:
			curCnt += 1
		else:
			if curCnt > 0:
				result += str(curCnt)
				result += str(curNum)
			curNum = int(x[pos])
			curCnt = 1
		pos += 1
	if curCnt > 0:
		result += str(curCnt)
		result += str(curNum)
	return result

n = 0
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
seq = fileData.strip()
for i in range(1, 41):
	seq = lookAndSay(seq)
	#print(str(i) + " " + str(len(seq)))
print(len(seq))