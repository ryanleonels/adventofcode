#!/usr/bin/python3

partySize = 0
password = ""
conns = {}
fileHandle = open("23.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(c1, c2) = (fileLine.split('-')[0], fileLine.split('-')[1])
	if c1 not in conns:
		conns[c1] = set()
	conns[c1].add(c2)
	if c2 not in conns:
		conns[c2] = set()
	conns[c2].add(c1)

def checkParty(cList):
	global partySize, password
	nc = len(cList)
	n = 0
	for c in sorted(conns[cList[-1]]):
		if c > cList[-1]:
			connected = True
			for i in range(0, nc - 1):
				if c not in conns[cList[i]]:
					connected = False
					break
			if connected == True:
				n += 1
				cList1 = cList.copy()
				cList1.append(c)
				checkParty(cList1)
	if n == 0:
		curSize = nc
		if curSize > partySize:
			partySize = curSize
			password = ','.join(cList)

for c1 in sorted(conns):
	checkParty([c1])

print(password)