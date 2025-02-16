#!/usr/bin/python3

fileHandle = open("16.in", "r")
fileData = fileHandle.read()
fileHandle.close()
initial = fileData.strip()

def ab(a):
	n = len(a)
	result = a + '0'
	b = []
	pos = n - 1
	while pos >= 0:
		ch = chr(97 - ord(a[pos]))
		b.append(ch)
		pos -= 1
	result += (''.join(b))
	return result

def checksum(a):
	n = len(a)
	print(n)
	if n % 2 == 1:
		return a
	b = []
	pos = 0
	while pos < n:
		if a[pos] == a[pos+1]:
			b.append('1')
		else:
			b.append('0')
		pos += 2
	return checksum(''.join(b))

data = initial
diskSize = 35651584
while len(data) < diskSize:
	data = ab(data)
	print(len(data))
print(checksum(data[:diskSize]))
