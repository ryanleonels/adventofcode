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
				out.append(str(val))
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
	return ','.join(out)

print(runProgram())

"""
#Examples
reg['C'] = 9
prog = [2,6]
runProgram()
print(reg['B']) #1

reg['A'] = 10
prog = [5,0,5,1,5,4]
print(runProgram()) #0,1,2

reg['A'] = 2024
prog = [0,1,5,4,3,0]
print(runProgram()) #4,2,5,6,7,7,7,7,3,1,0
print(reg['A']) #0

reg['B'] = 29
prog = [1,7]
runProgram()
print(reg['B']) #26

reg['B'] = 2024
reg['C'] = 43690
prog = [4,0]
runProgram()
print(reg['B']) #44354

reg = {'A': 729, 'B': 0, 'C': 0}
prog = [0,1,5,4,3,0]
print(runProgram()) #4,6,3,5,6,3,5,2,1,0
"""