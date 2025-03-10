#!/usr/bin/python3

fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()

def knotHash(data):
	lengths = [ord(x) for x in data.strip()] + [17, 31, 73, 47, 23]
	n = len(lengths)

	size = 256
	list1 = list(range(0, size))
	(pos, skip) = (0, 0)

	for rnd in range(0, 64):
		for i in range(0, n):
			length = lengths[i]
			(start, end) = (pos, pos + length)
			if end > size:
				(len1, len2) = (size - start, end - size)
				list2 = (list1[start:size] + list1[0:len2])[::-1]
				(list1[start:size], list1[0:len2]) = (list2[0:len1], list2[len1:length])
			else:
				list1[start:end] = list1[start:end][::-1]
			pos = (pos + length + skip) % size
			skip += 1

	hash1 = []
	for i in range(0, 16):
		num = list1[16 * i]
		for j in range(1, 16):
			num ^= list1[(16 * i) + j]
		hash1.append(num)

	result = ""
	for i in range(0, 16):
		result += ("0123456789abcdef"[hash1[i] // 16] + "0123456789abcdef"[hash1[i] % 16])
	return result

print(knotHash(fileData))