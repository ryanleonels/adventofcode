#!/usr/bin/python3

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
mem = {}
fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

def val2bit(val):
	bit = ""
	for i in range(0, 36):
		ch = str(val % 2)
		bit = ch + bit
		val //= 2
	return bit

def applyMask(bit1, mask):
	bit2 = ""
	for i in range(0, 36):
		if mask[i] == 'X':
			bit2 += bit1[i]
		else:
			bit2 += mask[i]
	return bit2

def bit2val(bit):
	val = 0
	for i in range(0, 36):
		val *= 2
		val += int(bit[i])
	return val

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(var, val) = fileLine.split(" = ")
	if var == "mask":
		mask = val
	else:
		pos = int(var.split('[')[1].split(']')[0])
		val1 = int(val)
		bit1 = val2bit(val1)
		bit2 = applyMask(bit1, mask)
		val2 = bit2val(bit2)
		mem[pos] = val2

sum1 = 0
for pos in mem:
	sum1 += mem[pos]
	#print(pos, mem[pos])
print(sum1)
