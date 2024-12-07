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
	n3 = 3 ** (n - 1)
	found = False
	for i in range(0, n3):
		n1 = i
		result1 = numbers[0]
		for j in range(1, n):
			if n1 % 3 == 0:
				result1 += numbers[j]
			if n1 % 3 == 1:
				result1 *= numbers[j]
			if n1 % 3 == 2:
				result1 = int(str(result1)+str(numbers[j]))
			n1 //= 3
		if result1 == value:
			found = True
			break
	if found == True:
		result += value
	print([value, numbers, found])
print(result)