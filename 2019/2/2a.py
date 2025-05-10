#!/usr/local/bin/python3

fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
prog = [int(x) for x in fileData.strip().split(',')]
for i in range(0, 100):
	for j in range(0, 100):
		program = prog.copy()		
		program[1] = i
		program[2] = j
		pos = 0
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
		if program[0] == 19690720:
			print(100 * i + j)