#!/usr/bin/python3

total = 0
conns = {}
fileHandle = open("23.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(c1, c2) = (fileLine.split('-')[0], fileLine.split('-')[1])
	if c1 not in conns:
		conns[c1] = set()
	conns[c1].add(c2)
	if c2 not in conns:
		conns[c2] = set()
	conns[c2].add(c1)

for c1 in sorted(conns):
	for c2 in sorted(conns[c1]):
		if c2 > c1:
			for c3 in sorted(conns[c2]):
				if c3 > c2 and c3 in conns[c1]:
					if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
						total += 1

print(total)