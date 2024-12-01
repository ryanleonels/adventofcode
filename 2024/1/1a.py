#!/usr/bin/python3

n = 0
left = []
right = {}
similarity = 0
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
	if int(nums[1]) in right:
		right[int(nums[1])] += 1
	else:
		right[int(nums[1])] = 1
for i in range(0, n):
	mult = 0
	if left[i] in right:
		mult = right[left[i]]
	similarity += (left[i] * mult)
print(similarity)
