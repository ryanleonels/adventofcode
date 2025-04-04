#!/usr/bin/python3

fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
entries = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	entries.append(fileLine)
entries.sort()
guards = {}
guardMins = {}
(curGuard, curSleep) = (0, 0)
(sleeping, sleepStart) = (False, 0)
(maxGuard, maxSleep) = (0, 0)
for entry in entries:
	m = int(entry.split(' ')[1].split(':')[1][:-1])
	if entry[-12:] == "begins shift":
		curGuard = int(entry.split('#')[1].split(' ')[0])
		curSleep = 0
	if entry[-12:] == "falls asleep":
		sleeping = True
		sleepStart = m
	if entry[-8:] == "wakes up":
		sleeping = False
		curTime = m
		sleepTime = curTime - sleepStart
		if curGuard not in guards:
			guards[curGuard] = 0
			guardMins[curGuard] = {}
		for i in range(sleepStart, curTime):
			if i in guardMins[curGuard]:
				guardMins[curGuard][i] += 1
			else:
				guardMins[curGuard][i] = 1
			if guardMins[curGuard][i] > guards[curGuard]:
				guards[curGuard] = guardMins[curGuard][i]
		if guards[curGuard] > maxSleep:
			(maxGuard, maxSleep) = (curGuard, guards[curGuard])
#print(maxGuard)
#print(guardMins[maxGuard])
maxMin = 0
maxSleep1 = 0
for min1 in guardMins[maxGuard]:
	if guardMins[maxGuard][min1] > maxSleep1:
		(maxMin, maxSleep1) = (min1, guardMins[maxGuard][min1])
#print(maxMin)
print(maxGuard * maxMin)