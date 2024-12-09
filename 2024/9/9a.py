#!/usr/bin/python3

disk = []
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileId = 0
files = []
n = len(fileData)
for i in range(0, n, 2):
	lenFile = int(fileData[i])
	files.append((len(disk), lenFile))
	for j in range(0, lenFile):
		disk.append(fileId)
	if i < n - 2 or (i == n - 2 and fileData[i+1].strip() != ''):
		lenSpace = int(fileData[i+1])
	else:
		lenSpace = 0
	for j in range(0, lenSpace):
		disk.append(-1)
	fileId += 1
diskSize = len(disk)
left = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(files) - 1, 0, -1):
	(curpos, curlen) = (files[i][0], files[i][1])
	freepos = -1
	for j in range(left[curlen - 1], curpos - curlen + 1):
		free = True
		for k in range(0, curlen):
			if disk[j+k] != -1:
				free = False
				break
		if free == True:
			freepos = j
			break
	if freepos != -1:
		left[curlen - 1] = freepos
		for j in range(curlen, 9):
			if left[j] < freepos:
				left[j] = freepos
		for k in range(0, curlen):
			disk[freepos+k] = disk[curpos+k]
			disk[curpos+k] = -1
checksum = 0
for i in range(0, diskSize):
	if disk[i] != -1:
		checksum += (i * disk[i])
print(checksum)
