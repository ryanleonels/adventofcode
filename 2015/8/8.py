#!/usr/bin/python3

total = 0
fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
strings = fileData.split('\n')
for string in strings:
	if string.strip() == '':
		continue
	n = len(string)
	n1 = 0
	pos = 1
	while pos < n - 1:
		if string[pos] == '\\':
			if string[pos+1] == 'x':
				pos += 4
			else:
				pos += 2
		else:
			pos += 1
		n1 += 1
	total += (n - n1)
print(total)