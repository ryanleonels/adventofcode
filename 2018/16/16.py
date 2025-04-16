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

n = 0
for i in range(0, nSample):
	nOpcode = 0
	(before, ins, after) = (sampleBefore[i], sampleIns[i], sampleAfter[i])
	addr = before.copy()
	addr[ins[3]] = addr[ins[1]] + addr[ins[2]]
	if addr == after:
		nOpcode += 1
	addi = before.copy()
	addi[ins[3]] = addi[ins[1]] + ins[2]
	if addi == after:
		nOpcode += 1
	mulr = before.copy()
	mulr[ins[3]] = mulr[ins[1]] * mulr[ins[2]]
	if mulr == after:
		nOpcode += 1
	muli = before.copy()
	muli[ins[3]] = muli[ins[1]] * ins[2]
	if muli == after:
		nOpcode += 1
	banr = before.copy()
	banr[ins[3]] = banr[ins[1]] & banr[ins[2]]
	if banr == after:
		nOpcode += 1
	bani = before.copy()
	bani[ins[3]] = bani[ins[1]] & ins[2]
	if bani == after:
		nOpcode += 1
	borr = before.copy()
	borr[ins[3]] = borr[ins[1]] | borr[ins[2]]
	if borr == after:
		nOpcode += 1
	bori = before.copy()
	bori[ins[3]] = bori[ins[1]] | ins[2]
	if bori == after:
		nOpcode += 1
	setr = before.copy()
	setr[ins[3]] = setr[ins[1]]
	if setr == after:
		nOpcode += 1
	seti = before.copy()
	seti[ins[3]] = ins[1]
	if seti == after:
		nOpcode += 1
	gtir = before.copy()
	if ins[1] > gtir[ins[2]]:
		gtir[ins[3]] = 1
	else:
		gtir[ins[3]] = 0
	if gtir == after:
		nOpcode += 1
	gtri = before.copy()
	if gtri[ins[1]] > ins[2]:
		gtri[ins[3]] = 1
	else:
		gtri[ins[3]] = 0
	if gtri == after:
		nOpcode += 1
	gtrr = before.copy()
	if gtrr[ins[1]] > gtrr[ins[2]]:
		gtrr[ins[3]] = 1
	else:
		gtrr[ins[3]] = 0
	if gtrr == after:
		nOpcode += 1
	eqir = before.copy()
	if ins[1] == eqir[ins[2]]:
		eqir[ins[3]] = 1
	else:
		eqir[ins[3]] = 0
	if eqir == after:
		nOpcode += 1
	eqri = before.copy()
	if eqri[ins[1]] == ins[2]:
		eqri[ins[3]] = 1
	else:
		eqri[ins[3]] = 0
	if eqri == after:
		nOpcode += 1
	eqrr = before.copy()
	if eqrr[ins[1]] == eqrr[ins[2]]:
		eqrr[ins[3]] = 1
	else:
		eqrr[ins[3]] = 0
	if eqrr == after:
		nOpcode += 1
	if nOpcode >= 3:
		n += 1
print(n)