#!/usr/local/bin/python3

from itertools import permutations

fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
programData = [int(x) for x in fileData.strip().split(',')]

def getParams(params, modes, program):
	result = []
	for i in range(0, len(params)):
		match modes[i]:
			case 0:
				param = program[params[i]]
			case 1:
				param = params[i]
		result.append(param)
	if len(params) == 1:
		return result[0]
	return result

def runProgram(program, inputs, startingPos = 0, haltOnOutput = False):
	pos = startingPos
	inputStack = inputs[::-1]
	output = []
	while True:
		op = program[pos] % 100
		mode1 = (program[pos] // 100) % 10
		mode2 = (program[pos] // 1000) % 10
		mode3 = (program[pos] // 10000) % 10
		match op:
			case 1: # add
				(a, b, c) = program[pos+1:pos+4]
				(param1, param2) = getParams([a, b], [mode1, mode2], program)
				program[c] = param1 + param2
				pos += 4
			case 2: # multiply
				(a, b, c) = program[pos+1:pos+4]
				(param1, param2) = getParams([a, b], [mode1, mode2], program)
				program[c] = param1 * param2
				pos += 4
			case 3: # input
				a = program[pos+1]
				#if len(inputStack) > 0:
				input1 = inputStack.pop()
				program[a] = input1
				pos += 2
			case 4: # output
				a = program[pos+1]
				param1 = getParams([a], [mode1], program)
				output.append(param1)
				pos += 2
				if haltOnOutput:
					return {'finalHalt': False, 'lastPos': pos, 'output': output}
			case 5: # jump-if-true
				(a, b) = program[pos+1:pos+3]
				(param1, param2) = getParams([a, b], [mode1, mode2], program)
				if param1 != 0:
					pos = param2
				else:
					pos += 3
			case 6: # jump-if-false
				(a, b) = program[pos+1:pos+3]
				(param1, param2) = getParams([a, b], [mode1, mode2], program)
				if param1 == 0:
					pos = param2
				else:
					pos += 3
			case 7: # less than
				(a, b, c) = program[pos+1:pos+4]
				(param1, param2) = getParams([a, b], [mode1, mode2], program)
				if param1 < param2:
					program[c] = 1
				else:
					program[c] = 0
				pos += 4
			case 8: # equals
				(a, b, c) = program[pos+1:pos+4]
				(param1, param2) = getParams([a, b], [mode1, mode2], program)
				if param1 == param2:
					program[c] = 1
				else:
					program[c] = 0
				pos += 4
			case 99: # halt
				return {'finalHalt': True, 'lastPos': pos, 'output': output}
				#pos += 1
	#return output

maxSignal = 0
allPhases = permutations([5, 6, 7, 8, 9])
for phases in allPhases:
	programA = programData.copy()
	programB = programData.copy()
	programC = programData.copy()
	programD = programData.copy()
	programE = programData.copy()
	(firstrunA, firstrunB, firstrunC, firstrunD, firstrunE) = (True, True, True, True, True)
	(posA, posB, posC, posD, posE) = (0, 0, 0, 0, 0)
	lastOutput = 0
	while True:
		if firstrunA:
			inputA = [phases[0], 0]
		else:
			inputA = [outputE['output'][0]]
		outputA = runProgram(programA, inputA, posA, True)
		#print(outputA)
		firstrunA = False
		posA = outputA['lastPos']
		if outputA['finalHalt']:
			break
		if firstrunB:
			inputB = [phases[1], outputA['output'][0]]
		else:
			inputB = [outputA['output'][0]]
		outputB = runProgram(programB, inputB, posB, True)
		#print(outputB)
		firstrunB = False
		posB = outputB['lastPos']
		if outputB['finalHalt']:
			break
		if firstrunC:
			inputC = [phases[2], outputB['output'][0]]
		else:
			inputC = [outputB['output'][0]]
		outputC = runProgram(programC, inputC, posC, True)
		#print(outputC)
		firstrunC = False
		posC = outputC['lastPos']
		if outputC['finalHalt']:
			break
		if firstrunD:
			inputD = [phases[3], outputC['output'][0]]
		else:
			inputD = [outputC['output'][0]]
		outputD = runProgram(programD, inputD, posD, True)
		#print(outputD)
		firstrunD = False
		posD = outputD['lastPos']
		if outputD['finalHalt']:
			break
		if firstrunE:
			inputE = [phases[4], outputD['output'][0]]
		else:
			inputE = [outputD['output'][0]]
		outputE = runProgram(programE, inputE, posE, True)
		#print(outputE)
		firstrunE = False
		posE = outputE['lastPos']
		if len(outputE['output']) > 0:
			lastOutput = outputE['output'][0]
		if outputE['finalHalt']:
			break
	#print(phases, lastOutput)
	maxSignal = max(lastOutput, maxSignal)

print(maxSignal)