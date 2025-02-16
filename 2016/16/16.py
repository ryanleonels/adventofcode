#!/usr/bin/python3

fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
initial = fileData.strip()

def ab(a):
	n = len(a)
	result = a + '0'
	pos = n - 1
	while pos >= 0:
		ch = chr(97 - ord(a[pos]))
		result += ch
		pos -= 1
	return result

def checksum(a):
	n = len(a)
	if n % 2 == 1:
		return a
	b = ''
	pos = 0
	while pos < n:
		if a[pos] == a[pos+1]:
			b += '1'
		else:
			b += '0'
		pos += 2
	return checksum(b)

data = initial
diskSize = 272
while len(data) < diskSize:
	data = ab(data)
print(checksum(data[:diskSize]))
