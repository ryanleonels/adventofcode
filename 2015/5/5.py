#!/usr/bin/python3

n = 0
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
strings = fileData.split('\n')
for string in strings:
	if string.strip() == '':
		continue
	nice = False
	n1 = len(string)
	vowels = 0
	for i in range(0, n1):
		if string[i] in ['a','e','i','o','u']:
			vowels += 1
	if vowels >= 3:
		nice = True
	if nice == True:
		n1 = len(string)
		repeat = False
		for i in range(1, n1):
			if string[i] == string[i-1]:
				repeat = True
				break
		if repeat == False:
			nice = False
	for naughty in ['ab','cd','pq','xy']:
		if naughty in string:
			nice = False
			break
	if nice == True:
		n += 1
print(n)