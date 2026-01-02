#!/usr/bin/python3

total = 0
fileHandle = open("2.in", "r")
fileData = fileHandle.read()
fileHandle.close()
idRanges = fileData.strip().split(',')
for idRange in idRanges:
	if idRange.strip() == '':
		continue
	(from1, to1) = idRange.split('-')
	(numFrom, numTo) = (int(from1), int(to1))
	invalids = set()
	for i in range(numFrom, numTo + 1):
		len1 = len(str(i))
		for j in range(1, len1):
			if len1 % j == 0:
				i1 = int(str(i)[:j] * (len1 // j))
				if i1 == i:
					invalids.add(i)
	for invalid in invalids:
		total += invalid
print(total)
