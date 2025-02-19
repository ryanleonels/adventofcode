#!/usr/bin/python3

fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
n = int(fileData.strip())

elf = []
for i in range(0, n):
	elf.append(i + 1)

while n > 1:
	elf1 = []
	if n % 2 == 1:
 		elf1.append(elf[n - 1])
	for i in range(0, (n // 2) * 2, 2):
		elf1.append(elf[i])
	elf = elf1
	n = len(elf)

print(elf[0])