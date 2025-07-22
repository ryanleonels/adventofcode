#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
crabs = [int(x) for x in fileData.strip().split(',')]
n = len(crabs)
#print(crabs)
(min1, max1) = (min(crabs), max(crabs))
minFuel = n * (max1 - min1)
for i in range(min1, max1 + 1):
	fuel = 0
	for j in range(0, n):
		fuel += abs(crabs[j] - i)
	if fuel < minFuel:
		minFuel = fuel
print(minFuel)
