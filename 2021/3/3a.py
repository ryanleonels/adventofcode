#!/usr/bin/python3

fileHandle = open("3.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
bits = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	bits.append(fileLine.strip())
n = len(bits)

set1 = set()
for i in range(0, n):
	set1.add(bits[i])
pos = 0

while len(set1) > 1:
	n1 = len(set1)
	set2 = set()
	n2 = 0
	for num in set1:
		if num[pos] == '1':
			n2 += 1
	if n2 >= n1 / 2:
		curbit = 1
	else:
		curbit = 0
	for num in set1:
		if int(num[pos]) == curbit:
			set2.add(num)
	pos += 1
	set1 = set2

for num in set1:
	n1 = len(num)
	oxygen = 0
	for i in range(0, n1):
		oxygen *= 2
		oxygen += int(num[i])

set1 = set()
for i in range(0, n):
	set1.add(bits[i])
pos = 0

while len(set1) > 1:
	n1 = len(set1)
	set2 = set()
	n2 = 0
	for num in set1:
		if num[pos] == '0':
			n2 += 1
	if n2 <= n1 / 2:
		curbit = 0
	else:
		curbit = 1
	for num in set1:
		if int(num[pos]) == curbit:
			set2.add(num)
	pos += 1
	set1 = set2

for num in set1:
	n1 = len(num)
	co2 = 0
	for i in range(0, n1):
		co2 *= 2
		co2 += int(num[i])

print(oxygen * co2)
