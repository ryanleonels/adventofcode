#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
data = [int(x) for x in fileData.strip().split(' ')]
n = len(data)
pos = 0

def addNode(depth):
	global data, pos
	nChild = data[pos]
	nMetadata = data[pos + 1]
	#print((' ' * (4 * depth)) + str((nChild, nMetadata)))
	pos += 2
	if nChild == 0:
		total = sum(data[pos:(pos+nMetadata)])
		pos += nMetadata
		return total
	values = []
	for i in range(0, nChild):
		value = addNode(depth + 1)
		values.append(value)
	total = 0
	for i in range(0, nMetadata):
		entry = data[pos + i]
		if entry >= 1 and entry <= nChild:
			total += values[entry - 1]
	pos += nMetadata
	return total

print(addNode(0))
