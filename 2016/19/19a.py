#!/usr/bin/python3

fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
n = int(fileData.strip())

elf = []
for i in range(0, n):
	elf.append(i + 1)

while n > 1:
	#print(n)
	#print(elf)
	n1 = n
	n2 = n // 2
	elf1 = []
	pos = 0
	pos1 = n2
	stolen = []
	for i in range(0, n):
		stolen.append(False)
	while pos < n2 and pos1 < n:
		#print((pos, pos1))
		stolen[pos1] = True # pos steal from pos1
		pos += 1
		pos1 += ((n1 % 2) + 1)
		n1 -= 1
	#print(pos)
	#print(stolen)
	for i in range(pos, n):
		if stolen[i] == False:
			elf1.append(elf[i])
	for i in range(0, pos):
		if stolen[i] == False:
			elf1.append(elf[i])
	#print(elf1)
	elf = elf1
	n = len(elf)
	#break

print(elf[0])
