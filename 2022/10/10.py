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
cycle = 1
signalsum = 0
while ptr < n:
	cmd = program[ptr]
	#print(cmd)
	if cmd[0] == "noop":
		cycle += 1
	if cmd[0] == "addx":
		cycle += 1
		if cycle in [20, 60, 100, 140, 180, 220]:
			signal = cycle * x
			#print(str(cycle) + " * " + str(x) + " = " + str(signal))
			signalsum += signal
		x += int(cmd[1])
		cycle += 1
	if cycle in [20, 60, 100, 140, 180, 220]:
		signal = cycle * x
		#print(str(cycle) + " * " + str(x) + " = " + str(signal))
		signalsum += signal
	ptr += 1
print(signalsum)
