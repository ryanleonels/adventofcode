#!/usr/local/bin/python3

fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
program = [int(x) for x in fileData.strip().split(',')]
pos = 0
inputStack = [1]
output = []
while True:
	op = program[pos] % 100
	mode1 = (program[pos] // 100) % 10
	mode2 = (program[pos] // 1000) % 10
	mode3 = (program[pos] // 10000) % 10
	match op:
		case 1: # add
			(a, b, c) = program[pos+1:pos+4]
			result = 0
			match mode1:
				case 0:
					result += program[a]
				case 1:
					result += a
			match mode2:
				case 0:
					result += program[b]
				case 1:
					result += b
			program[c] = result
			pos += 4
		case 2: # multiply
			(a, b, c) = program[pos+1:pos+4]
			result = 1
			match mode1:
				case 0:
					result *= program[a]
				case 1:
					result *= a
			match mode2:
				case 0:
					result *= program[b]
				case 1:
					result *= b
			program[c] = result
			pos += 4
		case 3: # input
			a = program[pos+1]
			input1 = inputStack.pop()
			program[a] = input1
			pos += 2
		case 4: # output
			a = program[pos+1]
			match mode1:
				case 0:
					result = program[a]
				case 1:
					result = a
			output.append(result)
			pos += 2
		case 99: # halt
			break
			#pos += 1
#print(program)
#print(output)
if output[:-1] != [0] * (len(output) - 1):
	print("Error")
else:
	print(output[-1])
