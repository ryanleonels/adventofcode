#!/usr/bin/python3

n = 0
left = []
right = []
totalDist = 0
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n += 1
	nums = fileLine.split('   ')
	left.append(int(nums[0]))
	right.append(int(nums[1]))
left.sort()
right.sort()
for i in range(0, n):
	totalDist += abs(left[i] - right[i])
print(totalDist)
