#!/usr/local/bin/python3

total = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
program = [int(x) for x in fileData.strip().split(',')]
#n = len(program)
pos = 0
program[1] = 12
program[2] = 2
while True:
	op = program[pos]
	match op:
		case 1:
			(a, b, c) = program[pos+1:pos+4]
			program[c] = program[a] + program[b]
			pos += 4
		case 2:
			(a, b, c) = program[pos+1:pos+4]
			program[c] = program[a] * program[b]
			pos += 4
		case 99:
			break
			#pos += 1
#print(program)
print(program[0])