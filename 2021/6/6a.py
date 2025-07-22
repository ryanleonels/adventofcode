#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fish = [int(x) for x in fileData.strip().split(',')]
n = len(fish)
fishes = {}
for i in range(0, 9):
	fishes[i] = 0
for i in range(0, n):
	fishes[fish[i]] += 1
#print(fishes)
for t in range(1, 257):
	fish0 = fishes[0]
	for i in range(0, 8):
		fishes[i] = fishes[i + 1]
	fishes[6] += fish0
	fishes[8] = fish0
	n = 0
	for i in range(0, 9):
		n += fishes[i]
	#print(t, n)
print(n)
