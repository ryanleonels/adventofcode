#!/usr/local/bin/python3

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
program = []

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	program.append(fileLine.split(' '))
n = len(program)
for i in range(0, n):
	print(i, program[i])

nPair = 5 # pairs of [0, 1] = 0, 1, 0, 1, 0, 1, 0, 1, 0, 1.... until it can be safely assume as infinite (here it is 5 as in problem description, minimum 4 / 6+ is safer but slower)

def run(init):
	ptr = 0
	(a, b, c, d) = (init, 0, 0, 0)
	signal = []
	step = 0
	while ptr < n:
		(ins, x) = (program[ptr][0], program[ptr][1])
		y = ""
		if len(program[ptr]) > 2:
			y = program[ptr][2]
		match ins:
			case 'cpy':
				x1 = eval(x)
				if y == 'a':
					a = x1
				if y == 'b':
					b = x1
				if y == 'c':
					c = x1
				if y == 'd':
					d = x1
				ptr += 1
			case 'inc':
				if x == 'a':
					a += 1
				if x == 'b':
					b += 1
				if x == 'c':
					c += 1
				if x == 'd':
					d += 1
				ptr += 1
			case 'dec':
				if x == 'a':
					a -= 1
				if x == 'b':
					b -= 1
				if x == 'c':
					c -= 1
				if x == 'd':
					d -= 1
				ptr += 1
			case 'jnz':
				x1 = eval(x)
				if x1 != 0:
					y1 = eval(y)
					ptr += y1
				else:
					ptr += 1
			case 'tgl':
				x1 = eval(x)
				ptr1 = ptr + x1
				if ptr1 >= 0 and ptr1 < n:
					if len(program[ptr1]) == 2:
						if program[ptr1][0] == 'inc':
							program[ptr1][0] = 'dec'
						else:
							program[ptr1][0] = 'inc'
					if len(program[ptr1]) == 3:
						if program[ptr1][0] == 'jnz':
							program[ptr1][0] = 'cpy'
						else:
							program[ptr1][0] = 'jnz'
				ptr += 1
			case 'out':
				x1 = eval(x)
				signal.append(x1)
				if len(signal) == 2 * nPair:
					print(init, signal)
					return signal
				ptr += 1
		step += 1
		#if step % 1000 == 0 or ptr >= n:
			#print("step=" + str(step) + " ptr=" + str(ptr) + " a=" + str(a) + " b=" + str(b) + " c=" + str(c) + " d=" + str(d))
	print(init, signal)
	return signal

i = 1
while True:
	clockSignal = run(i)
	i += 1
	if clockSignal == [0, 1] * nPair:
		break
