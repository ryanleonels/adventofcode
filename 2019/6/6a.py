#!/usr/bin/python3

total = 0
fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
orbits = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(a, b) = fileLine.split(')')
	if a not in orbits:
		orbits[a] = ''
	if b in orbits:
		if orbits[b] != '':
			orbits[b] += ','
		orbits[b] += a
	if b not in orbits:
		orbits[b] = a

youOrbits = []
cur = 'YOU'
while orbits[cur] != '':
	youOrbits.append(orbits[cur])
	cur = orbits[cur]
#print(youOrbits)

sanOrbits = []
cur = 'SAN'
while orbits[cur] != '':
	sanOrbits.append(orbits[cur])
	cur = orbits[cur]
#print(sanOrbits)

for i in range(0, len(youOrbits)):
	if youOrbits[i] in sanOrbits:
		j = sanOrbits.index(youOrbits[i])
		print(i + j)
		break