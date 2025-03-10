#!/usr/bin/python3

fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
lengths = [int(x) for x in fileData.split(',')]
n = len(lengths)

size = 256
list1 = list(range(0, size))
pos = 0

for i in range(0, n):
	(length, skip) = (lengths[i], i)
	(start, end) = (pos, pos + length)
	if end > size:
		(len1, len2) = (size - start, end - size)
		list2 = (list1[start:size] + list1[0:len2])[::-1]
		(list1[start:size], list1[0:len2]) = (list2[0:len1], list2[len1:length])
	else:
		list1[start:end] = list1[start:end][::-1]
	pos = (pos + length + skip) % size

print(list1[0] * list1[1])