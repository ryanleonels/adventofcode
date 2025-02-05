#!/usr/bin/python3

import hashlib

n = 0
found = 0
fileHandle = open("5.in", "r")
fileData = fileHandle.read()
fileHandle.close()
doorId = fileData.strip()
password = ""
chars = [' '] * 8
while found < 8:
	n += 1
	x = doorId + str(n)
	nHash = hashlib.md5(x.encode("utf-8")).hexdigest()
	if nHash[:5] == '00000':
		pos = nHash[5]
		ch = nHash[6]
		if pos < '8' and chars[int(pos)] == ' ':
			found += 1
			chars[int(pos)] = ch
			print(n)
			print(nHash)
password = ''.join(chars)
print(password)