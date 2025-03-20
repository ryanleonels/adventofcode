#!/usr/local/bin/python3

fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
(p, v, a, destroyed) = ([], [], [], [])
n = 0
positions = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	pp = tuple([int(x) for x in fileLine.split('p=<')[1].split('>')[0].split(',')])
	vv = tuple([int(x) for x in fileLine.split('v=<')[1].split('>')[0].split(',')])
	aa = tuple([int(x) for x in fileLine.split('a=<')[1].split('>')[0].split(',')])
	p.append(pp)
	v.append(vv)
	a.append(aa)
	destroyed.append(False)
	n += 1
ticks = 1000
tick = 0
while tick < ticks:
	tick += 1
	positions = {}
	for i in range(0, n):
		if not destroyed[i]:
			v[i] = (v[i][0] + a[i][0], v[i][1] + a[i][1], v[i][2] + a[i][2])
			p[i] = (p[i][0] + v[i][0], p[i][1] + v[i][1], p[i][2] + v[i][2])
			if p[i] in positions:
				positions[p[i]].append(i)
			else:
				positions[p[i]] = [i]
	for position in positions:
		if len(positions[position]) > 1:
			for particle in positions[position]:
				destroyed[particle] = True
particlesLeft = 0
for i in range(0, n):
	if not destroyed[i]:
		particlesLeft += 1
print(particlesLeft)