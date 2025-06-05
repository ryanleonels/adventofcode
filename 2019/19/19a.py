#!/usr/local/bin/python3

fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
programData = [int(x) for x in fileData.strip().split(',')]

def readParams(program, pos, n):
	params = []
	for i in range(1, n + 1):
		if pos + i >= 0 and (pos + i) not in program:
			params.append(0)
		else:
			params.append(program[pos + i])
	if len(params) == 1:
		return params[0]
	return params

def getParams(params, modes, program, relBase):
	result = []
	for i in range(0, len(params)):
		match modes[i]:
			case 0:
				if params[i] >= 0 and params[i] not in program:
					param = 0
				else:
					param = program[params[i]]
			case 1:
				param = params[i]
			case 2:
				if params[i] + relBase >= 0 and (params[i] + relBase) not in program:
					param = 0
				else:
					param = program[params[i] + relBase]
		result.append(param)
	if len(params) == 1:
		return result[0]
	return result

def runProgram(program, inputs = [], startingPos = 0, haltOnOutput = False, startingRelBase = 0):
	global panel, x, y, dirx, diry
	(pos, relBase) = (startingPos, startingRelBase)
	inputStack = inputs[::-1]
	output = []
	while True:
		if pos > 0 and pos not in program:
			cmd = 0
		else:
			cmd = program[pos]
		op = cmd % 100
		mode1 = (cmd // 100) % 10
		mode2 = (cmd // 1000) % 10
		mode3 = (cmd // 10000) % 10
		match op:
			case 1: # add
				(a, b, c) = readParams(program, pos, 3)
				(param1, param2) = getParams([a, b], [mode1, mode2], program, relBase)
				c1 = c
				if mode3 == 2:
					c1 += relBase
				program[c1] = param1 + param2
				pos += 4
			case 2: # multiply
				(a, b, c) = readParams(program, pos, 3)
				(param1, param2) = getParams([a, b], [mode1, mode2], program, relBase)
				c1 = c
				if mode3 == 2:
					c1 += relBase
				program[c1] = param1 * param2
				pos += 4
			case 3: # input
				a = readParams(program, pos, 1)
				if len(inputStack) > 0:
					input1 = inputStack.pop()
				else:
					return {'finalHalt': False, 'lastPos': pos, 'output': output}
				# custom logic start (none currently)
				# custom logic end
				a1 = a
				if mode1 == 2:
					a1 += relBase
				program[a1] = input1
				pos += 2
			case 4: # output
				a = readParams(program, pos, 1)
				param1 = getParams([a], [mode1], program, relBase)
				output.append(param1)
				# custom logic start (none currently)
				# custom logic end
				pos += 2
				if haltOnOutput:
					return {'finalHalt': False, 'lastPos': pos, 'output': output}
			case 5: # jump-if-true
				(a, b) = readParams(program, pos, 2)
				(param1, param2) = getParams([a, b], [mode1, mode2], program, relBase)
				if param1 != 0:
					pos = param2
				else:
					pos += 3
			case 6: # jump-if-false
				(a, b) = readParams(program, pos, 2)
				(param1, param2) = getParams([a, b], [mode1, mode2], program, relBase)
				if param1 == 0:
					pos = param2
				else:
					pos += 3
			case 7: # less than
				(a, b, c) = readParams(program, pos, 3)
				(param1, param2) = getParams([a, b], [mode1, mode2], program, relBase)
				c1 = c
				if mode3 == 2:
					c1 += relBase
				if param1 < param2:
					program[c1] = 1
				else:
					program[c1] = 0
				pos += 4
			case 8: # equals
				(a, b, c) = readParams(program, pos, 3)
				(param1, param2) = getParams([a, b], [mode1, mode2], program, relBase)
				c1 = c
				if mode3 == 2:
					c1 += relBase
				if param1 == param2:
					program[c1] = 1
				else:
					program[c1] = 0
				pos += 4
			case 9: # adjust relative base
				a = readParams(program, pos, 1)
				param1 = getParams([a], [mode1], program, relBase)
				relBase += param1
				pos += 2
			case 99: # halt
				return {'finalHalt': True, 'lastPos': pos, 'output': output}
				#pos += 1
	#return output

def inTractorBeam(x, y):
	program = {}
	for i in range(0, len(programData)):
		program[i] = programData[i]
	inputs = [x, y]
	outputs = runProgram(program, inputs)
	return outputs['output'][0]

# calculate first 50x50
n = 50
grid = []
for x in range(0, n):
	grid.append([])
	for y in range(0, n):
		grid[x].append(inTractorBeam(x, y))
	print(''.join([str(x) for x in grid[x]]))

windows = {}
# keep computing the window of y affected by tractor beam in each x until it is found, starting from the first 50
for x in range(0, n):
	minY = 0
	while minY < n and grid[x][minY] == 0:
		minY += 1
	if minY == n:
		windows[x] = (-1, -1)
	else:
		maxY = minY
		while maxY < n - 1 and grid[x][maxY + 1] == 1:
			maxY += 1
		windows[x] = (minY, maxY)
	print(x, windows[x])

# assumptions: the 100x100 square starts at x > 50, the tractor beam window keep increasing in both y and size as x increases
x = n
n2 = 100
squareFound = False
while not squareFound:
	minY = windows[x - 1][0]
	while inTractorBeam(x, minY) == 0:
		minY += 1
	maxY = windows[x - 1][1]
	while inTractorBeam(x, maxY + 1) == 1:
		maxY += 1
	windows[x] = (minY, maxY)
	print(x, windows[x])
	if x >= n2 - 1 and windows[x - (n2 - 1)][1] >= windows[x][0] + (n2 - 1):
		squareFound = True
		x1 = x - (n2 - 1)
		y1 = windows[x][0]
		print((x1 * 10000) + y1)
	else:
		x += 1
