#!/usr/bin/python3

import math

(n, ids) = (0, [])
fileHandle = open("13.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if ',' in fileLine:
		ids = fileLine.split(',')
		n = len(ids)

(n1, mods) = (0, [])
for i in range(0, n):
	if ids[i] != 'x':
		#print("bus id " + ids[i] + " departs " + str(i) + " minutes after timestamp t")
		id1 = int(ids[i])
		mod1 = -i
		while mod1 < 0:
			mod1 += id1
		#print(mod1, id1)
		mods.append((mod1, id1))
n1 = len(mods)

t = 0
lcm1 = 1
for i in range(0, n1):
	#print("before: " + str((t, lcm1)))
	#print("current: " + str(mods[i]))
	prev = lcm1
	lcm1 = math.lcm(lcm1, mods[i][1])
	mult = lcm1 // prev
	while t % mods[i][1] != mods[i][0]:
		t += prev
	#print("after: " + str((t, lcm1)))
print(t)
