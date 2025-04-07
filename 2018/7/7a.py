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
done = ""
(curTime, nextTime) = (0, 0)
curSteps = {}
while len(done) < n:
	# finish done steps
	curTime = nextTime
	stepsToDelete = []
	for step in curSteps:
		if curSteps[step] == curTime:
			done += step
			stepsToDelete.append(step)
			for req in dict(sorted(reqs.items())):
				if step in reqs[req]:
					reqs[req].remove(step)
	for step in stepsToDelete:
		del curSteps[step]
	# take ready steps (up to 5)
	for req in dict(sorted(reqs.items())):
		if len(curSteps) == 5:
			break
		if req not in done and req not in curSteps and len(reqs[req]) == 0:
			curSteps[req] = curTime + (ord(req) - 4)
	# record next step completion time
	if len(curSteps) > 0:
		nextTime = 999999999
		for step in curSteps:
			nextTime = min(nextTime, curSteps[step])
print(curTime)