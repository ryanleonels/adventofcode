#!/usr/local/bin/python3

reg = {'A': 0, 'B': 0, 'C': 0}
prog = []
fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine[:12] == "Register A: ":
		reg['A'] = int(fileLine[12:])
	if fileLine[:12] == "Register B: ":
		reg['B'] = int(fileLine[12:])
	if fileLine[:12] == "Register C: ":
		reg['C'] = int(fileLine[12:])
	if fileLine[:9] == "Program: ":
		prog = [int(x) for x in fileLine[9:].split(',')]

def runProgram():
	n = len(prog)
	ptr = 0
	out = []
	while ptr < n:
		opcode = prog[ptr]
		match opcode:
			case 0: #adv
				num = reg['A']
				den = 2 ** [0, 1, 2, 3, reg['A'], reg['B'], reg['C']][prog[ptr+1]]
				reg['A'] = num // den
				ptr += 2
			case 1: #bxl
				reg['B'] ^= prog[ptr+1]
				ptr += 2
			case 2: #bst
				val = [0, 1, 2, 3, reg['A'] % 8, reg['B'] % 8, reg['C'] % 8][prog[ptr+1]]
				reg['B'] = val
				ptr += 2
			case 3: #jnz
				if reg['A'] == 0:
					ptr += 2
				else:
					ptr = prog[ptr+1]
			case 4: #bxc
				val = reg['B'] ^ reg['C']
				reg['B'] = val
				ptr += 2
			case 5: #out
				val = [0, 1, 2, 3, reg['A'] % 8, reg['B'] % 8, reg['C'] % 8][prog[ptr+1]]
				out.append(val)
				ptr += 2
			case 6: #bdv
				num = reg['A']
				den = 2 ** [0, 1, 2, 3, reg['A'], reg['B'], reg['C']][prog[ptr+1]]
				reg['B'] = num // den
				ptr += 2
			case 7: #cdv
				num = reg['A']
				den = 2 ** [0, 1, 2, 3, reg['A'], reg['B'], reg['C']][prog[ptr+1]]
				reg['C'] = num // den
				ptr += 2
	return out

#reg = {'A': 2024, 'B': 0, 'C': 0}
#prog = [0,3,5,4,3,0]

(a, b, c) = (0, reg['B'], reg['C'])
n = len(prog)
i = n - 1
while True:
	j = 0
	while True:
		a += (8 ** i)
		j += 1
		while j == 8:
			i += 1
			j = (a // (8 ** i)) % 8
			if j == 0:
				j = 8
		reg = {'A': a, 'B': b, 'C': c}
		outp = runProgram()
		#print((i, j, a, outp, prog))
		if outp[i] == prog[i]:
			break
	i -= 1
	while i >= 0 and outp[i] == prog[i]:
		i -= 1
	if i < 0:
		break
print(a)

"""
Register A: 56256477
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,0,3,4,3,5,5,3,0

2 4 #bst 4: B = A % 8
1 1 #bxl 1: B = B ^ 1
7 5 #cdv 5: C = A / (2^B)
1 5 #bxl 5: B = B ^ B
0 3 #adv 3: A = A / 8
4 3 #bxc 3: B = B ^ C
5 5 #out 5: output B
3 0 #jnz 0: do while A != 0
"""