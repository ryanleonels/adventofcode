#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
blocks = [int(x) for x in fileData.split('\t')]
cycles = 0
n = len(blocks)
prevblocks = set()
while tuple(blocks) not in prevblocks:
	prevblocks.add(tuple(blocks))
	cycles += 1
	most = max(blocks)
	pos = blocks.index(most)
	most1 = most // n
	mostmod = most % n
	blocks[pos] = 0
	for i in range(1, n + 1):
		if i > mostmod:
			blocks[(pos + i) % n] += most1
		else:
			blocks[(pos + i) % n] += (most1 + 1)
	#print(blocks)
print(cycles)