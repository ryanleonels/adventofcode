#!/usr/bin/python3

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
reqs = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(step1, step2) = (fileLine.split(' ')[1], fileLine.split(' ')[7])
	if step2 not in reqs:
		reqs[step2] = set()
	reqs[step2].add(step1)
	if step1 not in reqs:
		reqs[step1] = set()
n = len(reqs)
order = ""
for i in range(0, n):
	step = ' '
	for req in dict(sorted(reqs.items())):
		if req not in order and len(reqs[req]) == 0:
			step = req
			break
	order += step
	for req in dict(sorted(reqs.items())):
		if step in reqs[req]:
			reqs[req].remove(step)
print(order)