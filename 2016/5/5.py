#!/usr/bin/python3

import hashlib

n = 0
found = 0
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
doorId = fileData.strip()
password = ""
while found < 8:
	n += 1
	x = doorId + str(n)
	nHash = hashlib.md5(x.encode("utf-8")).hexdigest()
	if nHash[:5] == '00000':
		found += 1
		password += nHash[5]
		print(n)
print(password)