#!/usr/bin/python3

nums = []
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	num = int(fileLine.strip())
	nums.append(num)

n = len(nums)
nums.sort()
(d1, d3) = (0, 0)
if nums[0] == 1:
	d1 += 1
if nums[0] == 3:
	d3 += 1
for i in range(1, n):
	d = nums[i] - nums[i - 1]
	if d == 1:
		d1 += 1
	if d == 3:
		d3 += 1
d3 += 1
print(d1 * d3)
