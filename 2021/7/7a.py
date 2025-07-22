#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
crabs = [int(x) for x in fileData.strip().split(',')]
n = len(crabs)
#print(crabs)
(min1, max1) = (min(crabs), max(crabs))
maxDist = max1 - min1
minFuel = n * maxDist * (maxDist + 1) / 2
for i in range(min1, max1 + 1):
	fuel = 0
	for j in range(0, n):
		dist = abs(crabs[j] - i)
		fuel += (dist * (dist + 1) / 2)
	if fuel < minFuel:
		minFuel = int(fuel)
print(minFuel)
