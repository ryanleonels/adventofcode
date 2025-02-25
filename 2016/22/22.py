#!/usr/local/bin/python3

fileHandle = open("22.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nodes = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:10] == "/dev/grid/":
		name = fileLine[10:22].strip()
		size = int(fileLine[23:27].strip())
		used = int(fileLine[29:33].strip())
		avail = int(fileLine[35:40].strip())
		use = int(fileLine[42:46].strip())
		nodes.append((name, size, used, avail, use))
n = len(nodes)
pairs = 0
for i in range(0, n):
	for j in range(0, n):
		if i != j and nodes[i][2] > 0 and nodes[i][2] <= nodes[j][3]:
			pairs += 1
print(pairs)