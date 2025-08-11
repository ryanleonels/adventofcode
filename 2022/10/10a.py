#!/usr/local/bin/python3

fileHandle = open("10.in", "r")
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
x = 1
cycle = 0
crt = ""
while ptr < n:
	cmd = program[ptr]
	#print(cmd)
	if cmd[0] == "noop":
		cycle += 1
	if cmd[0] == "addx":
		cycle += 1
		pos = (cycle - 1) % 40
		if x == pos or x == pos + 1 or x == pos - 1:
			crt += '█'
		else:
			crt += ' '
		cycle += 1
	pos = (cycle - 1) % 40
	if x == pos or x == pos + 1 or x == pos - 1:
		crt += '█'
	else:
		crt += ' '
	if cmd[0] == "addx":
		x += int(cmd[1])
	ptr += 1
for i in range(0, 240, 40):
	print(crt[i:i+40])
