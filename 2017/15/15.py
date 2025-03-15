#!/usr/bin/python3

fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

(a, b) = (0, 0)
for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	if fileLine.split(' ')[1] == 'A':
		a = int(fileLine.split(' ')[-1])
	if fileLine.split(' ')[1] == 'B':
		b = int(fileLine.split(' ')[-1])

step = 0
count = 0
while step < 40000000:
	step += 1
	if step % 1000000 == 0:
		print(step)
	(a, b) = ((a * 16807) % 2147483647, (b * 48271) % 2147483647)
	if a % 65536 == b % 65536:
		count += 1
print(count)