#!/usr/bin/python3

fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
n = int(fileData.strip())

#print(n)
scores = [3, 7]
(elf1, elf2) = (0, 1)
#print(scores)
#print(elf1, elf2)
while len(scores) < n + 10:
	newScore = scores[elf1] + scores[elf2]
	if newScore >= 10:
		scores.append(newScore // 10)
		scores.append(newScore % 10)
	else:
		scores.append(newScore)
	elf1 = (elf1 + scores[elf1] + 1) % len(scores)
	elf2 = (elf2 + scores[elf2] + 1) % len(scores)
	#print(scores)
	#print(elf1, elf2)
result = ""
for i in range(n, n + 10):
	result += str(scores[i])
print(result)