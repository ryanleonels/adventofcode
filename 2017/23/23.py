#!/usr/local/bin/python3

fileHandle = open("23.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
program = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	program.append(fileLine.split(' '))
n = len(program)
#for i in range(0, n):
	#print(i, program[i])

registers = {}
for i in range(97, 105):
	registers[chr(i)] = 0

ptr = 0
step = 0
nMul = 0
while ptr < n:
	(ins, x) = (program[ptr][0], program[ptr][1])
	y = ""
	if len(program[ptr]) > 2:
		y = program[ptr][2]
	#print(ins, x, y)
	match ins:
		case 'set':
			if y.isalpha():
				registers[x] = registers[y]
			else:
				registers[x] = int(y)
			ptr += 1
		case 'sub':
			if y.isalpha():
				registers[x] -= registers[y]
			else:
				registers[x] -= int(y)
			ptr += 1
		case 'mul':
			if y.isalpha():
				registers[x] *= registers[y]
			else:
				registers[x] *= int(y)
			ptr += 1
			nMul += 1
		case 'jnz':
			if x.isalpha():
				x1 = registers[x]
			else:
				x1 = int(x)
			if x1 != 0:
				if y.isalpha():
					ptr += registers[y]
				else:
					ptr += int(y)
			else:
				ptr += 1
	step += 1
	#if step % 1000 == 0 or ptr >= n:
		#print(step, registers)

print(nMul)