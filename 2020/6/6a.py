#!/usr/bin/python3

total = 0
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

qs = set()
first = True
for fileLine in fileLines:
	if fileLine.strip() == '': # check answers
		total += len(qs)
		qs = set()
		first = True
		continue
	answers = fileLine.strip()
	if first:
		for ch in answers:
			qs.add(ch)
		first = False
	else:
		ch1 = set()
		for ch in qs:
			if ch not in answers:
				ch1.add(ch)
		for ch in ch1:
			qs.remove(ch)
print(total)
