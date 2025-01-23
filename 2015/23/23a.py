#!/usr/local/bin/python3

a = 1
b = 0
ptr = 0
program = []
fileHandle = open("23.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	instruction = fileLine.split(' ')[0]
	if instruction == "jmp":
		register = None
	else:
		register = fileLine.split(' ')[1][0]
	if instruction in ["jmp", "jie", "jio"]:
		offset = int(fileLine.split(' ')[-1])
	else:
		offset = None
	program.append((instruction, register, offset))
n = len(program)
while ptr < n:
	(instruction, register, offset) = program[ptr]
	match instruction:
		case "hlf":
			if register == "a":
				a //= 2
			if register == "b":
				b //= 2
			ptr += 1
		case "tpl":
			if register == "a":
				a *= 3
			if register == "b":
				b *= 3
			ptr += 1
		case "inc":
			if register == "a":
				a += 1
			if register == "b":
				b += 1
			ptr += 1
		case "jmp":
			ptr += offset
		case "jie":
			if register == "a":
				if a % 2 == 0:
					ptr += offset
				else:
					ptr += 1
			if register == "b":
				if b % 2 == 0:
					ptr += offset
				else:
					ptr += 1
		case "jio":
			if register == "a":
				if a == 1:
					ptr += offset
				else:
					ptr += 1
			if register == "b":
				if b == 1:
					ptr += offset
				else:
					ptr += 1
print(b)
