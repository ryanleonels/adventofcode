#!/usr/bin/python3

enabled = True
result = 0
fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	for i in range(0, n-4):
		if fileLine[i:i+4] == 'do()':
			enabled = True
		if i <= n-7 and fileLine[i:i+7] == "don't()":
			enabled = False
		if fileLine[i:i+4] == 'mul(' and enabled == True:
			mul1 = fileLine[i+4:].split(')')
			if len(mul1) == 1: # no )
				continue
			mul2 = mul1[0].split(',')
			if len(mul2) != 2:
				continue
			if mul2[0].isdigit() == False or mul2[1].isdigit() == False:
				continue
			if len(mul2[0]) < 1 or len(mul2[0]) > 3 or len(mul2[1]) < 1 or len(mul2[1]) > 3:
				continue
			result += (int(mul2[0]) * int(mul2[1]))
print(result)
