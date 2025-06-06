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
ptr = 0
acc = 0
#step = 0
ran = set()
while ptr < n:
	if ptr in ran:
		#print(step)
		break
	ran.add(ptr)
	(ins, x) = (program[ptr][0], int(program[ptr][1]))
	match ins:
		case 'acc':
			acc += x
			ptr += 1
		case 'jmp':
			ptr += x
		case 'nop':
			ptr += 1
	#step += 1
print(acc)
