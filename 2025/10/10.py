#!/usr/bin/python3

curPress = 0
totalPress = 0
config = ""
buttons = []
joltages = []
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	config = fileLine.split('[')[1].split(']')[0]
	buttons1 = fileLine.split('] (')[1].split(') {')[0].split(') (')
	buttons = []
	for button1 in buttons1:
		buttons.append([int(x) for x in button1.split(',')])
	joltages = [int(x) for x in fileLine.split('{')[1].split('}')[0].split(',')]
	n = len(config)
	goal = 0
	i2 = 1
	for i in range(0, n):
		if config[i] == '#':
			goal += i2
		i2 *= 2
	#print(config, buttons, goal)
	presses = {}
	states = {}
	presses[0] = 0
	curPress = 0
	states[0] = [0]
	done = False
	while not done:
		if goal in states[curPress]:
			done = True
			totalPress += curPress
			break
		states[curPress + 1] = []
		for state in states[curPress]:
			for button in buttons:
				state1 = state
				for x in button:
					st = (state // (2 ** x)) % 2
					if st:
						state1 -= (2 ** x)
					else:
						state1 += (2 ** x)
				if state1 not in presses:
					presses[state1] = curPress + 1
					states[curPress + 1].append(state1)
		curPress += 1
		#print(states[curPress])
	#print(curPress)
print(totalPress)
