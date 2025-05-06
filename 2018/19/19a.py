#!/usr/local/bin/python3

fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

ip = 0
program = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	ins = fileLine.split(' ')
	if ins[0] == "#ip":
		ip = int(ins[1])
	else:
		(op, a, b, c) = (ins[0], int(ins[1]), int(ins[2]), int(ins[3]))
		program.append((op, a, b, c))

n = len(program)

#for i in range(0, n):
	#print(program[i])
#exit(0)

#n1 = 0
reg = [1, 0, 0, 0, 0, 0]
while reg[ip] >= 0 and reg[ip] < n:
	#if n1 % 1000000 == 0:
		#print(n1)
	(op, a, b, c) = program[reg[ip]]
	#print("ip=" + str(reg[ip]))
	#print(reg)
	#print(op, a, b, c)
	match op:
		case 'addr':
			reg[c] = reg[a] + reg[b]
		case 'addi':
			reg[c] = reg[a] + b
		case 'mulr':
			reg[c] = reg[a] * reg[b]
		case 'muli':
			reg[c] = reg[a] * b
		case 'banr':
			reg[c] = reg[a] & reg[b]
		case 'bani':
			reg[c] = reg[a] & b
		case 'borr':
			reg[c] = reg[a] | reg[b]
		case 'bori':
			reg[c] = reg[a] | b
		case 'setr':
			reg[c] = reg[a]
		case 'seti':
			reg[c] = a
		case 'gtir':
			if a > reg[b]:
				reg[c] = 1
			else:
				reg[c] = 0
		case 'gtri':
			if reg[a] > b:
				reg[c] = 1
			else:
				reg[c] = 0
		case 'gtrr':
			if reg[a] > reg[b]:
				reg[c] = 1
			else:
				reg[c] = 0
		case 'eqir':
			if a == reg[b]:
				reg[c] = 1
			else:
				reg[c] = 0
		case 'eqri':
			if reg[a] == b:
				reg[c] = 1
			else:
				reg[c] = 0
		case 'eqrr':
			if reg[a] == reg[b]:
				reg[c] = 1
			else:
				reg[c] = 0
	#print(reg)
	reg[ip] += 1
	#n1 += 1
	if reg[5] > 10000000:
		break
#print(n1)
#print(reg)
#print(reg[0])
# factorize reg[5], then sum all products
factors = []
n = reg[5]
if n % 2 == 0:
	factors.append(2)
	n //= 2
i = 3
while i * i <= n:
	if n % i == 0:
		factors.append(i)
		n //= i
	i += 2
factors.append(n)
result = 0
n1 = len(factors)
n2 = 2 ** n1
for i in range(0, n2):
	i1 = i
	cur = 1
	for j in range(0, n1):
		if i1 % 2 == 1:
			cur *= factors[j]
		i1 //= 2
	result += cur
print(result)