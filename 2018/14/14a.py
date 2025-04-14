#!/usr/bin/python3

fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
n = fileData.strip()
n1 = len(n)
#print(n)
scores = "37"
(elf1, elf2) = (0, 1)
#print(scores)
#print(elf1, elf2)
done = False

mil = 0
len1 = len(scores)
while not done:
	(score1, score2) = (int(scores[elf1]), int(scores[elf2]))
	newScore = score1 + score2
	check1 = False
	if newScore >= 10:
		check1 = True
		scores += str(newScore // 10)
		scores += str(newScore % 10)
	else:
		scores += str(newScore)
	len1 = len(scores)
	elf1 = (elf1 + score1 + 1) % len1
	elf2 = (elf2 + score2 + 1) % len1
	#print(scores)
	#print(elf1, elf2)
	if len1 >= (mil + 1) * 1000000:
		print(len1)
		mil += 1
	if len1 >= n1:
		if check1:
			result = scores[-(n1+1):]
			if result[:n1] == n:
				print(len1 - n1 - 1)
				done = True
		result = scores[-n1:]
		if result == n:
			print(len1 - n1)
			done = True
