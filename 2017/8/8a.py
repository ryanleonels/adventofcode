#!/usr/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
registers = {}

maxval = 0
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	(reg1, ins, qty1, if1, reg2, cond, qty2) = fileLine.split(' ')
	(qty1, qty2) = (int(qty1), int(qty2))
	val1 = 0
	if reg1 in registers:
		val1 = registers[reg1]
	val2 = 0
	if reg2 in registers:
		val2 = registers[reg2]
	condition = False
	if cond == "==" and val2 == qty2:
		condition = True
	if cond == "!=" and val2 != qty2:
		condition = True
	if cond == ">" and val2 > qty2:
		condition = True
	if cond == ">=" and val2 >= qty2:
		condition = True
	if cond == "<" and val2 < qty2:
		condition = True
	if cond == "<=" and val2 <= qty2:
		condition = True
	if condition == True:
		if ins == "inc":
			val1 += qty1
		if ins == "dec":
			val1 -= qty1
		registers[reg1] = val1
		maxval = max(maxval, val1)

print(maxval)