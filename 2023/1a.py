#!/usr/bin/python3

def getValue(line,pos):
	if line[pos] >= '1' and line[pos] <= '9':
		return int(line[pos])
	digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for i in range(0, len(digits)):
		if pos <= (len(line) - len(digits[i])) and line[pos:pos+len(digits[i])] == digits[i]:
			return i + 1
	return 0

valueSum = 0
fileHandle = open("1.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	l = 0
	while getValue(fileLine, l) == 0:
		l += 1
	r = n - 1
	while getValue(fileLine, r) == 0:
		r -= 1
	value = (getValue(fileLine, l) * 10) + getValue(fileLine, r)
	valueSum += value
print(valueSum)
