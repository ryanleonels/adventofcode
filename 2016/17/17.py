#!/usr/bin/python3

import hashlib

fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
passcode = fileData.strip()

startState = ("", 0, 0)
found = False
step = 0
curStep = [startState]
nextStep = []
while not found:
	step += 1
	for state in curStep:
		if state[1] == 3 and state[2] == 3:
			found = True
			print(state[0])
		else:
			hashkey = passcode + state[0]
			hashres = hashlib.md5(hashkey.encode("utf-8")).hexdigest()
			if state[1] > 0 and hashres[0] >= 'b':
				nextStep.append((state[0] + 'U', state[1] - 1, state[2]))
			if state[1] < 3 and hashres[1] >= 'b':
				nextStep.append((state[0] + 'D', state[1] + 1, state[2]))
			if state[2] > 0 and hashres[2] >= 'b':
				nextStep.append((state[0] + 'L', state[1], state[2] - 1))
			if state[2] < 3 and hashres[3] >= 'b':
				nextStep.append((state[0] + 'R', state[1], state[2] + 1))
	#print(step, len(nextStep))
	if len(nextStep) == 0:
		break
	if found == False:
		curStep = nextStep
		nextStep = []