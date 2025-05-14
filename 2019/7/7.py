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

def runProgram(program, inputs):
	pos = 0
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
				input1 = inputStack.pop()
				program[a] = input1
				pos += 2
			case 4: # output
				a = program[pos+1]
				param1 = getParams([a], [mode1], program)
				output.append(param1)
				pos += 2
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
				break
				#pos += 1
	return output

maxSignal = 0
allPhases = permutations([0, 1, 2, 3, 4])
for phases in allPhases:
	programA = programData.copy()
	outputA = runProgram(programA, [phases[0], 0])
	programB = programData.copy()
	outputB = runProgram(programB, [phases[1], outputA[0]])
	programC = programData.copy()
	outputC = runProgram(programC, [phases[2], outputB[0]])
	programD = programData.copy()
	outputD = runProgram(programD, [phases[3], outputC[0]])
	programE = programData.copy()
	outputE = runProgram(programE, [phases[4], outputD[0]])
	#print(phases, outputE[0])
	maxSignal = max(outputE[0], maxSignal)

print(maxSignal)