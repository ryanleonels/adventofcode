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
	string1 = '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'
	n1 = len(string1)
	total += (n1 - n)
print(total)