#!/usr/bin/python3

result = 0
value = 0
numbers = []
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	value = int(fileLine.split(': ')[0])
	numbers = [int(x) for x in fileLine.split(': ')[1].split(' ')]
	n = len(numbers)
	n2 = 2 ** (n - 1)
	found = False
	for i in range(0, n2):
		n1 = i
		result1 = numbers[0]
		for j in range(1, n):
			if n1 % 2 == 0:
				result1 += numbers[j]
			else:
				result1 *= numbers[j]
			n1 //= 2
		if result1 == value:
			found = True
			break
	if found == True:
		result += value
print(result)