#!/usr/bin/python3

total = 0
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
orbits = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(a, b) = fileLine.split(')')
	if a not in orbits:
		orbits[a] = ''
	if b in orbits:
		if orbits[b] != '':
			orbits[b] += ','
		orbits[b] += a
	if b not in orbits:
		orbits[b] = a

nums = {}

def numOrbits(x):
	if x in nums:
		return nums[x]
	if orbits[x] == '':
		return 0
	n = 0
	for y in orbits[x].split(','):
		n += (numOrbits(y) + 1)
	nums[x] = n
	return n

n = 0
for x in orbits:
	n += numOrbits(x)
print(n)