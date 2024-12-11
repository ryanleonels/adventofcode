#!/usr/bin/python3

fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
numbers = [int(x) for x in fileData.split(' ')]
numbers1 = {}
for i in range(0, len(numbers)):
	if numbers[i] in numbers1:
		numbers1[numbers[i]] += 1
	else:
		numbers1[numbers[i]] = 1
for i in range(0, 75):
	numbers2 = {}
	for number in numbers1:
		n = numbers1[number]
		if number == 0:
			if 1 in numbers2:
				numbers2[1] += n
			else:
				numbers2[1] = n
		else:
			num = str(number)
			if len(num) % 2 == 0:
				n2 = len(num) // 2
				numleft = int(num[0:n2])
				numright = int(num[n2:])
				if numleft in numbers2:
					numbers2[numleft] += n
				else:
					numbers2[numleft] = n
				if numright in numbers2:
					numbers2[numright] += n
				else:
					numbers2[numright] = n
			else:
				number2 = number * 2024
				if number2 in numbers2:
					numbers2[number2] += n
				else:
					numbers2[number2] = n
	numbers1 = numbers2
n = 0
for number in numbers1:
	n += numbers1[number]
print(n)