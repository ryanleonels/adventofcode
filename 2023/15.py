#!/usr/bin/python3

def getHash(step):
	val = 0
	n1 = len(step)
	for i in range(0, n1):
		val += ord(step[i])
		val *= 17
		val %= 256
	#print(val)
	return val

sumHash = 0
fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
#fileData = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
steps = fileData.split('\n')[0].split(',')
n = len(steps)
#print(n)
#print(steps)
for step in steps:
	sumHash += getHash(step)
print(sumHash)
