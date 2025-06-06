#!/usr/local/bin/python3

fileHandle = open("8.in", "r")
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
for i in range(0, n):
	if program[i][0] == 'jmp' or program[i][1] == 'nop':
		program1 = []
		for j in range(0, n):
			program1.append([program[j][0], program[j][1]])
		if program[i][0] == 'jmp':
			program1[i][0] = 'nop'
		if program[i][0] == 'nop':
			program1[i][0] = 'jmp'
		ptr = 0
		acc = 0
		#step = 0
		ran = set()
		while ptr < n:
			if ptr in ran:
				#print(i, "loop", acc, step)
				break
			ran.add(ptr)
			(ins, x) = (program1[ptr][0], int(program1[ptr][1]))
			match ins:
				case 'acc':
					acc += x
					ptr += 1
				case 'jmp':
					ptr += x
				case 'nop':
					ptr += 1
			#step += 1
		#print(i, acc)
		if ptr >= n:
			print(acc)
