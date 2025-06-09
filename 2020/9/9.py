#!/usr/bin/python3

nums = []
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	num = int(fileLine.strip())
	nums.append(num)

n = len(nums)
preambleSize = 25
for i in range(preambleSize, n):
	sum2 = False
	for j in range(i - preambleSize, i):
		for k in range(j, i):
			if nums[j] + nums[k] == nums[i]:
				sum2 = True
	if not sum2:
		print(nums[i])
		break
