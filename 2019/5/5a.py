#!/usr/local/bin/python3

fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
program = [int(x) for x in fileData.strip().split(',')]
pos = 0
inputStack = [5]
output = []

def getParams(params, modes):
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

while True:
	op = program[pos] % 100
	mode1 = (program[pos] // 100) % 10
	mode2 = (program[pos] // 1000) % 10
	mode3 = (program[pos] // 10000) % 10
	match op:
		case 1: # add
			(a, b, c) = program[pos+1:pos+4]
			(param1, param2) = getParams([a, b], [mode1, mode2])
			program[c] = param1 + param2
			pos += 4
		case 2: # multiply
			(a, b, c) = program[pos+1:pos+4]
			(param1, param2) = getParams([a, b], [mode1, mode2])
			program[c] = param1 * param2
			pos += 4
		case 3: # input
			a = program[pos+1]
			input1 = inputStack.pop()
			program[a] = input1
			pos += 2
		case 4: # output
			a = program[pos+1]
			param1 = getParams([a], [mode1])
			output.append(param1)
			pos += 2
		case 5: # jump-if-true
			(a, b) = program[pos+1:pos+3]
			(param1, param2) = getParams([a, b], [mode1, mode2])
			if param1 != 0:
				pos = param2
			else:
				pos += 3
		case 6: # jump-if-false
			(a, b) = program[pos+1:pos+3]
			(param1, param2) = getParams([a, b], [mode1, mode2])
			if param1 == 0:
				pos = param2
			else:
				pos += 3
		case 7: # less than
			(a, b, c) = program[pos+1:pos+4]
			(param1, param2) = getParams([a, b], [mode1, mode2])
			if param1 < param2:
				program[c] = 1
			else:
				program[c] = 0
			pos += 4
		case 8: # equals
			(a, b, c) = program[pos+1:pos+4]
			(param1, param2) = getParams([a, b], [mode1, mode2])
			if param1 == param2:
				program[c] = 1
			else:
				program[c] = 0
			pos += 4
		case 99: # halt
			break
			#pos += 1
#print(program)
#print(output)
if len(output) != 1:
	print("Error")
else:
	print(output[0])
