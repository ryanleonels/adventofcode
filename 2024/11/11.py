#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
numbers = [int(x) for x in fileData.split(' ')]
for i in range(0, 25):
	n = len(numbers)
	numbers1 = []
	for j in range(0, n):
		if numbers[j] == 0:
			numbers1.append(1)
		else:
			num1 = str(numbers[j])
			if len(num1) % 2 == 0:
				n2 = len(num1) // 2
				numleft = int(num1[0:n2])
				numright = int(num1[n2:])
				numbers1.append(numleft)
				numbers1.append(numright)
			else:
				numbers1.append(numbers[j] * 2024)
	numbers = numbers1
print(len(numbers))