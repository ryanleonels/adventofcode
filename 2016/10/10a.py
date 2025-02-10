#!/usr/local/bin/python3

bots = {}
outputs = {}
inits = []
gives = {}

fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')

for fileLine in fileLines:
	if fileLine.strip() == "":
		continue
	if fileLine[:5] == "value":
		(curval, curbot) = fileLine.split('value ')[1].split(' goes to bot ')
		inits.append((int(curval), int(curbot)))
	if fileLine[:3] == "bot":
		curbot = int(fileLine.split('bot ')[1].split(' gives low to ')[0])
		(lowtype, lownum) = fileLine.split(' gives low to ')[1].split(' and high to ')[0].split(' ')
		(hightype, highnum) = fileLine.split(' gives low to ')[1].split(' and high to ')[1].split(' ')
		if curbot in gives:
			print("duplicate " + str(curbot))
		gives[curbot] = (lowtype, int(lownum), hightype, int(highnum))

#print(inits)
#print(gives)

for (curval, curbot) in inits:
	if curbot not in bots:
		bots[curbot] = []
	bots[curbot].append(curval)
	bots[curbot].sort()

#print(bots)

n = 0
done = False
while not done:
	procs = []
	for bot in bots:
		if len(bots[bot]) == 2:
			procs.append(bot)
	#print(procs)
	for bot in procs:
		if len(bots[bot]) == 2:
			bots[bot].sort()
			(lowtype, lownum, hightype, highnum) = gives[bot]
			if lowtype == "bot":
				if lownum not in bots:
					bots[lownum] = []
				bots[lownum].append(bots[bot][0])
			if lowtype == "output":
				if lownum not in outputs:
					outputs[lownum] = []
				outputs[lownum].append(bots[bot][0])
			if hightype == "bot":
				if highnum not in bots:
					bots[highnum] = []
				bots[highnum].append(bots[bot][1])
			if hightype == "output":
				if highnum not in outputs:
					outputs[highnum] = []
				outputs[highnum].append(bots[bot][1])
			bots[bot] = []
	n += 1
	if len(procs) == 0:
		done = True

#print(bots)
#print(outputs)

print(outputs[0][0] * outputs[1][0] * outputs[2][0])