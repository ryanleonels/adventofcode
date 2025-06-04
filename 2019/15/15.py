#!/usr/local/bin/python3

fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
programData = [int(x) for x in fileData.strip().split(',')]
screen = {}
ball = (-1, -1)
paddle = (-1, -1)

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
				# custom logic start (halt if all inputs are done)
				if len(inputStack) == 0:
					return {'finalHalt': False, 'lastPos': pos, 'output': output}
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

def runCommands(commands):
	program = {}
	for i in range(0, len(programData)):
		program[i] = programData[i]
	inputs = [int(x) for x in commands]
	outputs = runProgram(program, inputs)
	return outputs['output']

area = {}
area[(0, 0)] = {'type': 1, 'dist': 0, 'path': []}  # types: 0 = wall, 1 = empty space, 2 = oxygen system; dist: distance from origin, path: shortest path to reach current point
curDist = 0
curNodes = [(0, 0)]
nextNodes = []
oxygenFound = False
oxygenPos = (-999, -999)

while not oxygenFound:
	for node in curNodes:
		curPath = area[node]['path']
		(lat1, long1) = node
		# try north
		if (lat1 + 1, long1) not in area:
			output = runCommands(curPath + [1])
			curType = output[-1]
			area[(lat1 + 1, long1)] = {'type': curType, 'dist': curDist + 1, 'path': curPath + [1]}
			if curType == 1:
				nextNodes.append((lat1 + 1, long1))
			if curType == 2:
				oxygenFound = True
				oxygenPos = (lat1 + 1, long1)
				print("oxygen found at " + str(oxygenPos))
		# try south
		if (lat1 - 1, long1) not in area:
			output = runCommands(curPath + [2])
			curType = output[-1]
			area[(lat1 - 1, long1)] = {'type': curType, 'dist': curDist + 1, 'path': curPath + [2]}
			if curType == 1:
				nextNodes.append((lat1 - 1, long1))
			if curType == 2:
				oxygenFound = True
				oxygenPos = (lat1 - 1, long1)
				print("oxygen found at " + str(oxygenPos))
		# try west
		if (lat1, long1 - 1) not in area:
			output = runCommands(curPath + [3])
			curType = output[-1]
			area[(lat1, long1 - 1)] = {'type': curType, 'dist': curDist + 1, 'path': curPath + [3]}
			if curType == 1:
				nextNodes.append((lat1, long1 - 1))
			if curType == 2:
				oxygenFound = True
				oxygenPos = (lat1, long1 - 1)
				print("oxygen found at " + str(oxygenPos))
		# try east
		if (lat1, long1 + 1) not in area:
			output = runCommands(curPath + [4])
			curType = output[-1]
			area[(lat1, long1 + 1)] = {'type': curType, 'dist': curDist + 1, 'path': curPath + [4]}
			if curType == 1:
				nextNodes.append((lat1, long1 + 1))
			if curType == 2:
				oxygenFound = True
				oxygenPos = (lat1, long1 + 1)
				print("oxygen found at " + str(oxygenPos))
	curDist += 1
	curNodes = []
	print("dist=" + str(curDist) + " nodes=" + str(len(nextNodes)))
	for node in nextNodes:
		curNodes.append(node)
		#print(node, area[node])
	nextNodes = []

print(curDist)
