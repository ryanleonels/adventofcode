#!/usr/local/bin/python3

fileHandle = open("17.in", "r")
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

# part 1: determine the map of the scaffolding

program = {}
for i in range(0, len(programData)):
	program[i] = programData[i]
outputs = runProgram(program)
#print(outputs['output'])
gridRaw = ''.join([chr(x) for x in outputs['output']])
print(gridRaw)

# part 2: trying to compute the full movement to traverse the scaffold (assuming it is all in a single long path)

grid = gridRaw.strip().split('\n')
(row, col) = (len(grid), len(grid[0]))
#print(row, col)
dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
dirL = {(-1, 0): (0, -1), (1, 0): (0, 1), (0, -1): (1, 0), (0, 1): (-1, 0)}
dirR = {(-1, 0): (0, 1), (1, 0): (0, -1), (0, -1): (-1, 0), (0, 1): (1, 0)}

for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] in '^v<>':
			pos1 = (i, j)
			dir1 = dirs[grid[i][j]]
			#print(pos1, dir1)

movements = ''
moveStack = []
n = 0
end = False
while not end:
	posNext = (pos1[0] + dir1[0], pos1[1] + dir1[1])
	if posNext[0] >= 0 and posNext[0] < row and posNext[1] >= 0 and posNext[1] < col and grid[posNext[0]][posNext[1]] == '#':
		n += 1
		pos1 = posNext
	else:
		if n > 0:
			moveStack.append(str(n))
		n = 0
		nextDir = ''
		posL = (pos1[0] + dirL[dir1][0], pos1[1] + dirL[dir1][1])
		if posL[0] >= 0 and posL[0] < row and posL[1] >= 0 and posL[1] < col and grid[posL[0]][posL[1]] == '#':
			nextDir = 'L'
			moveStack.append('L')
			dir1 = dirL[dir1]
		posR = (pos1[0] + dirR[dir1][0], pos1[1] + dirR[dir1][1])
		if nextDir == '' and posR[0] >= 0 and posR[0] < row and posR[1] >= 0 and posR[1] < col and grid[posR[0]][posR[1]] == '#':
			nextDir = 'R'
			moveStack.append('R')
			dir1 = dirR[dir1]
		if nextDir == '':
			end = True
		#print(posNext, posL, posR)

#print(moveStack)
#print(len(moveStack))
movements = ','.join(moveStack)
print(movements)

# part 3: splitting the movements into A, B, C (assumptions: it starts with A, finishes with C and A/B/C have even # of terms)
for a in range(2, 10, 2):
	functionA = ','.join(moveStack[:a])
	if len(functionA) <= 20:
		for c in range(2, 12, 2):
			functionC = ','.join(moveStack[-c:])
			if len(functionC) <= 20:
				movements1 = movements.replace(functionA, 'A').replace(functionC, 'C')
				movements1a = movements1.split(',A')[0]
				movements1c = movements1.split(',A')[0]
				if len(movements1a) < len(movements1c):
					functionB = movements1a[2:]
				else:
					functionB = movements1c[2:]
				if len(functionB) <= 20:
					mainRoutine = movements1.replace(functionB, 'B')
					if len(mainRoutine) <= 20:
						mainInput = mainRoutine + '\n' + functionA + '\n' + functionB + '\n' + functionC + '\n' + 'n' + '\n'
						print(mainInput)

# part 4: calculate the amount of space dust collected using the split movement inputs
program = {}
for i in range(0, len(programData)):
	program[i] = programData[i]
program[0] = 2
inputs = [ord(x) for x in mainInput]
outputs = runProgram(program, inputs)
print(outputs['output'][-1])
