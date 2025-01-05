#!/usr/bin/python3

import hashlib

n = 0
found = False
fileHandle = open("4.in", "r")
fileData = fileHandle.read()
fileHandle.close()
secretKey = fileData.strip()
while found == False:
	n += 1
	x = secretKey + str(n)
	nHash = hashlib.md5(x.encode("utf-8")).hexdigest()
	if nHash[:5] == '00000':
		found = True
		print(n)
