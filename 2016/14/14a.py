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
		x = hashes[index]
	else:
		x = salt + str(index)
		for i in range(0, 2017):
			x = hashlib.md5(x.encode("utf-8")).hexdigest()
		hashes[index] = x
	ch = ''
	for i in range(0, 30):
		if x[i] == x[i + 1] and x[i + 1] == x[i + 2]:
			ch = x[i]
			break
	if ch != '':
		found = False
		for i in range(index + 1, index + 1001):
			if i in hashes:
				x = hashes[i]
			else:
				x = salt + str(i)
				for j in range(0, 2017):
					x = hashlib.md5(x.encode("utf-8")).hexdigest()
				hashes[i] = x
			if (ch * 5) in x:
				found = True
				break
		if found == True:
			n += 1
			if n == 64 or True:
				print(index)
	index += 1
