#!/usr/bin/python3

sum1 = 0
fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

publicKeys = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	publicKeys.append(int(fileLine))
#publicKeys = [5764801, 17807724]
#print(publicKeys)

loopSizes = []
for i in range(0, len(publicKeys)):
	n = 0
	key = 1
	while key != publicKeys[i]:
		key = (key * 7) % 20201227
		n += 1
	loopSizes.append(n)
#print(loopSizes)

(publicKey, loopSize) = (1, 0)
if loopSizes[0] < loopSizes[1]:
	(publicKey, loopSize) = (publicKeys[1], loopSizes[0])
else:
	(publicKey, loopSize) = (publicKeys[0], loopSizes[1])
i = 0
key = 1
while i < loopSize:
	key = (key * publicKey) % 20201227
	i += 1
print(key)
