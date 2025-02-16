#!/usr/local/bin/python3

fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
discs = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	numpos = int(fileLine.split(' has ')[1].split(' positions')[0])
	startpos = int(fileLine.split(' at position ')[1].split('.')[0])
	discs.append((numpos, startpos))
n = len(discs)
#print(n)
#print(discs)
mods = []
for i in range(0, n):
	(numpos, startpos) = discs[i]
	pos0 = (startpos + (i + 1)) % numpos
	goalmod = (numpos - pos0) % numpos
	#print(str(goalmod) + " mod " + str(numpos))
	mods.append((goalmod, numpos))
t = 0
done = False
while not done:
	done = True
	for i in range(0, n):
		if t % mods[i][1] != mods[i][0]:
			done = False
			break
	if done:
		print(t)
	else:
		t += 1