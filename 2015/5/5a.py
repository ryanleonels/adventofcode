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
	rule1 = False
	for i in range(0, n1-3):
		for j in range(i+2, n1-1):
			if string[i:i+2] == string[j:j+2]:
				rule1 = True
				break
	rule2 = False
	for i in range(0, n1-2):
		if string[i] == string[i+2]:
			rule2 = True
			break
	if rule1 == True and rule2 == True:
		nice = True
	if nice == True:
		n += 1
print(n)