#!/usr/bin/python3

fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
numbers = [int(x) for x in fileData.strip().split(',')]

n = len(numbers)
last = {}
for i in range(0, n):
	if numbers[i] in last:
		last[numbers[i]].append(i)
	else:
		last[numbers[i]] = [i]

while n < 30000000:
	prev1 = numbers[n - 1]
	if len(last[prev1]) > 1:
		next1 = (n - 1) - last[prev1][-2]
	else:
		next1 = 0
	if next1 in last:
		last[next1].append(n)
	else:
		last[next1] = [n]
	numbers.append(next1)
	n += 1
	if n % 1000000 == 0:
		print(str(n) + "/30000000")	

print(numbers[-1])
