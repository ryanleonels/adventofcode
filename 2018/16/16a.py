#!/usr/bin/python3

fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

inSample = False
(nSample, nProgram) = (0, 0)
(sampleBefore, sampleIns, sampleAfter, program) = ([], [], [], [])
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if fileLine[:6] == "Before":
		inSample = True
		before = [int(x) for x in fileLine.split("Before: [")[1].split("]")[0].split(", ")]
		sampleBefore.append(before)
	if fileLine[:5] == "After":
		inSample = False
		after = [int(x) for x in fileLine.split("After:  [")[1].split("]")[0].split(", ")]
		sampleAfter.append(after)
	if fileLine[0].isdigit():
		ins = [int(x) for x in fileLine.split(" ")]
		if inSample:
			sampleIns.append(ins)
		else:
			program.append(ins)

nSample = len(sampleIns)
nProgram = len(program)

"""print(nSample)
for i in range(0, nSample):
	print(sampleBefore[i], sampleIns[i], sampleAfter[i])
print(nProgram)
for i in range(0, nProgram):
	print(program[i])"""

opcodes = {}
for opcode in ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']:
	opcodes[opcode] = set(range(0, 16))

for i in range(0, nSample):
	(before, ins, after) = (sampleBefore[i], sampleIns[i], sampleAfter[i])
	if ins[0] in opcodes['addr']:
		addr = before.copy()
		addr[ins[3]] = addr[ins[1]] + addr[ins[2]]
		if addr != after:
			opcodes['addr'].remove(ins[0])
	if ins[0] in opcodes['addi']:
		addi = before.copy()
		addi[ins[3]] = addi[ins[1]] + ins[2]
		if addi != after:
			opcodes['addi'].remove(ins[0])
	if ins[0] in opcodes['mulr']:
		mulr = before.copy()
		mulr[ins[3]] = mulr[ins[1]] * mulr[ins[2]]
		if mulr != after:
			opcodes['mulr'].remove(ins[0])
	if ins[0] in opcodes['muli']:
		muli = before.copy()
		muli[ins[3]] = muli[ins[1]] * ins[2]
		if muli != after:
			opcodes['muli'].remove(ins[0])
	if ins[0] in opcodes['banr']:
		banr = before.copy()
		banr[ins[3]] = banr[ins[1]] & banr[ins[2]]
		if banr != after:
			opcodes['banr'].remove(ins[0])
	if ins[0] in opcodes['bani']:
		bani = before.copy()
		bani[ins[3]] = bani[ins[1]] & ins[2]
		if bani != after:
			opcodes['bani'].remove(ins[0])
	if ins[0] in opcodes['borr']:
		borr = before.copy()
		borr[ins[3]] = borr[ins[1]] | borr[ins[2]]
		if borr != after:
			opcodes['borr'].remove(ins[0])
	if ins[0] in opcodes['bori']:
		bori = before.copy()
		bori[ins[3]] = bori[ins[1]] | ins[2]
		if bori != after:
			opcodes['bori'].remove(ins[0])
	if ins[0] in opcodes['setr']:
		setr = before.copy()
		setr[ins[3]] = setr[ins[1]]
		if setr != after:
			opcodes['setr'].remove(ins[0])
	if ins[0] in opcodes['seti']:
		seti = before.copy()
		seti[ins[3]] = ins[1]
		if seti != after:
			opcodes['seti'].remove(ins[0])
	if ins[0] in opcodes['gtir']:
		gtir = before.copy()
		if ins[1] > gtir[ins[2]]:
			gtir[ins[3]] = 1
		else:
			gtir[ins[3]] = 0
		if gtir != after:
			opcodes['gtir'].remove(ins[0])
	if ins[0] in opcodes['gtri']:
		gtri = before.copy()
		if gtri[ins[1]] > ins[2]:
			gtri[ins[3]] = 1
		else:
			gtri[ins[3]] = 0
		if gtri != after:
			opcodes['gtri'].remove(ins[0])
	if ins[0] in opcodes['gtrr']:
		gtrr = before.copy()
		if gtrr[ins[1]] > gtrr[ins[2]]:
			gtrr[ins[3]] = 1
		else:
			gtrr[ins[3]] = 0
		if gtrr != after:
			opcodes['gtrr'].remove(ins[0])
	if ins[0] in opcodes['eqir']:
		eqir = before.copy()
		if ins[1] == eqir[ins[2]]:
			eqir[ins[3]] = 1
		else:
			eqir[ins[3]] = 0
		if eqir != after:
			opcodes['eqir'].remove(ins[0])
	if ins[0] in opcodes['eqri']:
		eqri = before.copy()
		if eqri[ins[1]] == ins[2]:
			eqri[ins[3]] = 1
		else:
			eqri[ins[3]] = 0
		if eqri != after:
			opcodes['eqri'].remove(ins[0])
	if ins[0] in opcodes['eqrr']:
		eqrr = before.copy()
		if eqrr[ins[1]] == eqrr[ins[2]]:
			eqrr[ins[3]] = 1
		else:
			eqrr[ins[3]] = 0
		if eqrr != after:
			opcodes['eqrr'].remove(ins[0])

n = 0
insOpcode = [''] * 16
while n < 16:
	toRemove = set()
	for opcode in opcodes:
		#print(opcode, opcodes[opcode])
		if len(opcodes[opcode]) == 1:
			for i in opcodes[opcode]:
				n += 1
				insOpcode[i] = opcode
				toRemove.add(i)
	for i in toRemove:
		for opcode in opcodes:
			if i in opcodes[opcode]:
				opcodes[opcode].remove(i)
	#print(insOpcode)
print(insOpcode)

reg = [0, 0, 0, 0]
for i in range(0, nProgram):
	(ins, a, b, c) = program[i]
	opcode = insOpcode[ins]
	if opcode == 'addr':
		reg[c] = reg[a] + reg[b]
	if opcode == 'addi':
		reg[c] = reg[a] + b
	if opcode == 'mulr':
		reg[c] = reg[a] * reg[b]
	if opcode == 'muli':
		reg[c] = reg[a] * b
	if opcode == 'banr':
		reg[c] = reg[a] & reg[b]
	if opcode == 'bani':
		reg[c] = reg[a] & b
	if opcode == 'borr':
		reg[c] = reg[a] | reg[b]
	if opcode == 'bori':
		reg[c] = reg[a] | b
	if opcode == 'setr':
		reg[c] = reg[a]
	if opcode == 'seti':
		reg[c] = a
	if opcode == 'gtir':
		if a > reg[b]:
			reg[c] = 1
		else:
			reg[c] = 0
	if opcode == 'gtri':
		if reg[a] > b:
			reg[c] = 1
		else:
			reg[c] = 0
	if opcode == 'gtrr':
		if reg[a] > reg[b]:
			reg[c] = 1
		else:
			reg[c] = 0
	if opcode == 'eqir':
		if a == reg[b]:
			reg[c] = 1
		else:
			reg[c] = 0
	if opcode == 'eqri':
		if reg[a] == b:
			reg[c] = 1
		else:
			reg[c] = 0
	if opcode == 'eqrr':
		if reg[a] == reg[b]:
			reg[c] = 1
		else:
			reg[c] = 0
print(reg)
print(reg[0])