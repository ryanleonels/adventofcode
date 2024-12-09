#!/usr/bin/python3

disk = []
fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileId = 0
n = len(fileData)
for i in range(0, n, 2):
	lenFile = int(fileData[i])
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
left = 0
right = diskSize - 1
while left <= right:
	while left <= right and disk[left] != -1:
		left += 1
	while left <= right and disk[right] == -1:
		right -= 1
	if left <= right and disk[left] == -1 and disk[right] != -1:
		disk[left] = disk[right]
		disk[right] = -1
checksum = 0
for i in range(0, diskSize):
	if disk[i] != -1:
		checksum += (i * disk[i])
print(checksum)