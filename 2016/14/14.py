#!/usr/bin/python3

import hashlib

hashes = {}
fileHandle = open("14.in", "r")
fileData = fileHandle.read()
fileHandle.close()
salt = fileData.strip()
n = 0
index = 0
while n < 64:
	if index in hashes:
		nHash = hashes[index]
	else:
		x = salt + str(index)
		nHash = hashlib.md5(x.encode("utf-8")).hexdigest()
		hashes[index] = nHash
	ch = ''
	for i in range(0, 30):
		if nHash[i] == nHash[i + 1] and nHash[i + 1] == nHash[i + 2]:
			ch = nHash[i]
			break
	if ch != '':
		found = False
		for i in range(index + 1, index + 1001):
			if i in hashes:
				nHash = hashes[i]
			else:
				x = salt + str(i)
				nHash = hashlib.md5(x.encode("utf-8")).hexdigest()
				hashes[i] = nHash
			if (ch * 5) in nHash:
				found = True
				break
		if found == True:
			n += 1
			if n == 64:
				print(index)
	index += 1
