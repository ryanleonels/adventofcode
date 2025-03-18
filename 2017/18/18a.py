#!/usr/local/bin/python3

fileHandle = open("18.in", "r")
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

registers0 = {}
for i in range(97, 123):
	registers0[chr(i)] = 0
registers0['p'] = 0
registers1 = {}
for i in range(97, 123):
	registers1[chr(i)] = 0
registers1['p'] = 1
(buffer0, buffer1) = ([], [])

(ptr0, ptr1) = (0, 0)
step = 0
(wait0, wait1) = (False, False)
sent = 0
while ptr0 < n and ptr1 < n:
	if wait0 == True and wait1 == True and len(buffer0) == 0 and len(buffer1) == 0:
		#print("deadlock")
		break #deadlock
	if wait0 == True and len(buffer1) > 0:
		wait0 = False
		registers0[x] = buffer1[0]
		buffer1 = buffer1[1:]
		ptr0 += 1
	if wait0 == False and ptr0 >= 0 and ptr0 < n:
		(ins, x) = (program[ptr0][0], program[ptr0][1])
		y = ""
		if len(program[ptr0]) > 2:
			y = program[ptr0][2]
		#print(ins, x, y)
		match ins:
			case 'snd':
				if x.isalpha():
					buffer0.append(registers0[x])
				else:
					buffer0.append(int(x))
				#print(0, buffer0[-1])
				ptr0 += 1
			case 'set':
				if y.isalpha():
					registers0[x] = registers0[y]
				else:
					registers0[x] = int(y)
				ptr0 += 1
			case 'add':
				if y.isalpha():
					registers0[x] += registers0[y]
				else:
					registers0[x] += int(y)
				ptr0 += 1
			case 'mul':
				if y.isalpha():
					registers0[x] *= registers0[y]
				else:
					registers0[x] *= int(y)
				ptr0 += 1
			case 'mod':
				if y.isalpha():
					registers0[x] %= registers0[y]
				else:
					registers0[x] %= int(y)
				ptr0 += 1
			case 'rcv':
				if len(buffer1) > 0:
					registers0[x] = buffer1[0]
					buffer1 = buffer1[1:]
					ptr0 += 1
				else:
					wait0 = True
			case 'jgz':
				if x.isalpha():
					x0 = registers0[x]
				else:
					x0 = int(x)
				if x0 > 0:
					if y.isalpha():
						ptr0 += registers0[y]
					else:
						ptr0 += int(y)
				else:
					ptr0 += 1
	if wait1 == True and len(buffer0) > 0:
		wait1 = False
		registers1[x] = buffer0[0]
		buffer0 = buffer0[1:]
		ptr1 += 1
	if wait1 == False and ptr1 >= 0 and ptr1 < n:
		(ins, x) = (program[ptr1][0], program[ptr1][1])
		y = ""
		if len(program[ptr1]) > 2:
			y = program[ptr1][2]
		#print(ins, x, y)
		match ins:
			case 'snd':
				if x.isalpha():
					buffer1.append(registers1[x])
				else:
					buffer1.append(int(x))
				#print(1, buffer1[-1])
				sent += 1
				ptr1 += 1
			case 'set':
				if y.isalpha():
					registers1[x] = registers1[y]
				else:
					registers1[x] = int(y)
				ptr1 += 1
			case 'add':
				if y.isalpha():
					registers1[x] += registers1[y]
				else:
					registers1[x] += int(y)
				ptr1 += 1
			case 'mul':
				if y.isalpha():
					registers1[x] *= registers1[y]
				else:
					registers1[x] *= int(y)
				ptr1 += 1
			case 'mod':
				if y.isalpha():
					registers1[x] %= registers1[y]
				else:
					registers1[x] %= int(y)
				ptr1 += 1
			case 'rcv':
				if len(buffer0) > 0:
					registers1[x] = buffer0[0]
					buffer0 = buffer0[1:]
					ptr1 += 1
				else:
					wait1 = True
			case 'jgz':
				if x.isalpha():
					x1 = registers1[x]
				else:
					x1 = int(x)
				if x1 > 0:
					if y.isalpha():
						ptr1 += registers1[y]
					else:
						ptr1 += int(y)
				else:
					ptr1 += 1
	step += 1
print(sent)