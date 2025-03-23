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
registers['a'] = 1

ptr = 0
step = 0
"""while ptr < n:
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
	if step % 1000000 == 0 or ptr >= n:
		print(step, registers)

print(registers['h'])"""

#the code is inefficient (the 2 inner for loops are needed to calculate % as the processor does not have that instruction)
#instead of executing the O(n^2) code, calculate it using O(n) equivalent with % instead as below
(a, b, c, d, e, f, g, h) = (1, 0, 0, 0, 0, 0, 0, 0)
b = int(program[0][2])
c = b
if a != 0:
	b = (b * 100) + 100000
	c = b + 17000
while True:
	(f, d, e) = (1, 2, 2)
	while d * d <= b:
		if b % d == 0:
			f = 0
			break
		d += 1
	if f == 0:
		h += 1
	g = b - c
	if g == 0:
		break
	b += 17
print(h)