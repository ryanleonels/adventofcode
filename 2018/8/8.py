#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
data = [int(x) for x in fileData.strip().split(' ')]
n = len(data)
(pos, total) = (0, 0)

def addNode(depth):
	global data, pos, total
	nChild = data[pos]
	nMetadata = data[pos + 1]
	#print((' ' * (4 * depth)) + str((nChild, nMetadata)))
	pos += 2
	for i in range(0, nChild):
		addNode(depth + 1)
	total += sum(data[pos:(pos+nMetadata)])
	#print((' ' * (4 * depth)) + str(data[pos:(pos+nMetadata)]))
	pos += nMetadata

while pos < n:
	addNode(0)

print(total)