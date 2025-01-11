#!/usr/bin/python3

def isValid(password):
	for i in range(0, 7):
		if password[i] in 'iol':
			return False
	straight = False
	for i in range(0, 6):
		if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i+1]) + 1:
			straight = True
			break
	if straight == False:
		return False
	overlap = 0
	start2 = 0
	for i in range(0, 7):
		if ord(password[i+1]) == ord(password[i]):
			overlap = 1
			start2 = i + 2
			break
	if overlap == 0 or start2 > 6:
		return False
	for i in range(start2, 7):
		if ord(password[i+1]) == ord(password[i]):
			overlap = 2
			break
	return overlap == 2

def incr(password):
	pos = 7
	done = False
	password1 = list(password)
	while not done:
		password1[pos] = chr(ord(password1[pos])+1)
		if password1[pos] in 'iol':
			password1[pos] = chr(ord(password1[pos])+1)
		if password1[pos] <= 'z' or pos == 0:
			done = True
			break
		password1[pos] = 'a'
		pos -= 1
	return ''.join(password1)

n = 0
fileHandle = open("11.in", "r")
fileData = fileHandle.read()
fileHandle.close()
password = fileData.strip()
while not isValid(password):
	password = incr(password)
password = incr(password)
while not isValid(password):
	password = incr(password)
print(password)