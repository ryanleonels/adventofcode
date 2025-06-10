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
arr = [0] * n
for i in range(0, n):
	cur = 0
	if nums[i] >= 1 and nums[i] <= 3:
		cur += 1
	if i >= 1:
		d = nums[i] - nums[i - 1]
		if d >= 1 and d <= 3:
			cur += arr[i - 1]
	if i >= 2:
		d = nums[i] - nums[i - 2]
		if d >= 1 and d <= 3:
			cur += arr[i - 2]
	if i >= 3:
		d = nums[i] - nums[i - 3]
		if d >= 1 and d <= 3:
			cur += arr[i - 3]
	arr[i] = cur
print(arr[n - 1])
