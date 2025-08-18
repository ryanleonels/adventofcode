#!/usr/bin/python3

digits = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
digits1 = '012=-'

def snafu2dec(s):
	n = len(s)
	d = 0
	for i in range(0, n):
		d *= 5
		d += digits[s[i]]
	return d

def dec2snafu(d):
	if d <= 2:
		return digits1[d]
	d1 = (d + 2) // 5
	d0 = d - (d1 * 5)
	return dec2snafu(d1) + digits1[d0]

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
total = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	num = snafu2dec(fileLine.strip())
	total += num
print(dec2snafu(total))
