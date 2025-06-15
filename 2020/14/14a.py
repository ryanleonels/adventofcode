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
		if mask[i] == '0':
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

def writeMem(addr, val):
	x1 = addr.find('X')
	if x1 == -1:
		pos = bit2val(addr)
		mem[pos] = val
	else:
		addr0 = addr.replace('X', '0', 1)
		writeMem(addr0, val)
		addr1 = addr.replace('X', '1', 1)
		writeMem(addr1, val)

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(var, val) = fileLine.split(" = ")
	if var == "mask":
		mask = val
	else:
		pos = int(var.split('[')[1].split(']')[0])
		addr1 = val2bit(pos)
		addr2 = applyMask(addr1, mask)
		val1 = int(val)
		writeMem(addr2, val1)

sum1 = 0
for pos in mem:
	sum1 += mem[pos]
	#print(pos, mem[pos])
print(sum1)
