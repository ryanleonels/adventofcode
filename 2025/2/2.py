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
	(lenFrom, lenTo) = (len(from1), len(to1))
	if lenFrom % 2 == 0:
		(fromL, fromR) = (int(from1[:lenFrom//2]), int(from1[lenFrom//2:]))
	else:
		(fromL, fromR) = (10 ** (lenFrom // 2), 0)
	if lenTo % 2 == 0:
		(toL, toR) = (int(to1[:lenTo//2]), int(to1[lenTo//2:]))
	else:
		(toL, toR) = (10 ** (lenTo // 2), 0)
	if fromL == toL:
		if fromR <= fromL and toR >= toL:
			invalid = int(str(fromL) * 2)
			total += invalid
	else:
		if fromR <= fromL:
			invalid = int(str(fromL) * 2)
			total += invalid
		for i in range(fromL + 1, toL):
			invalid = int(str(i) * 2)
			total += invalid
		if toR >= toL:
			invalid = int(str(toL) * 2)
			total += invalid
print(total)
