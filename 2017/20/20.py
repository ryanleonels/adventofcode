#!/usr/local/bin/python3

fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
minDist = 2 ** 1024
minParticle = -1
ticks = 1000
curParticle = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	p = tuple([int(x) for x in fileLine.split('p=<')[1].split('>')[0].split(',')])
	v = tuple([int(x) for x in fileLine.split('v=<')[1].split('>')[0].split(',')])
	a = tuple([int(x) for x in fileLine.split('a=<')[1].split('>')[0].split(',')])
	tick = 0
	while tick < ticks:
		v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
		p = (p[0] + v[0], p[1] + v[1], p[2] + v[2])
		tick += 1
	curDist = abs(p[0]) + abs(p[1]) + abs(p[2])
	if curDist < minDist:
		minDist = curDist
		minParticle = curParticle
		#print(minDist, minParticle)
	curParticle += 1
print(minParticle)