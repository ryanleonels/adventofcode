#!/usr/bin/python3

boxes = []
lenses = {}

def getHash(label):
	val = 0
	n1 = len(label)
	for i in range(0, n1):
		val += ord(label[i])
		val *= 17
		val %= 256
	#print(val)
	return val

def runStep(step):
	focal = 0
	label = ""
	n = len(step)
	op = ""
	if step[n-1] == '-':
		label = step[:(n-1)]
		op = '-'
		if label in lenses:
			del lenses[label]
			box = getHash(label)
			for i in range(0, len(boxes[box])):
				if boxes[box][i][0] == label:
					boxes[box].pop(i)
					break
	else:
		label = step.split('=')[0]
		op = '='
		focal = int(step.split('=')[1])
		box = getHash(label)
		if label in lenses:
			for i in range(0, len(boxes[box])):
				if boxes[box][i][0] == label:
					boxes[box][i] = (label, focal)
		else:
			boxes[box].append((label, focal))
		lenses[label] = focal
	"""print("label = " + label)
	print("hash(label) = " + str(getHash(label)))
	print("op = " + op)
	if focal > 0:
		#print("focal = " + str(focal))"""
	"""print(step)
	print(boxes[:4])
	print(lenses)"""
	"""for i in range(0, 256):
		if len(boxes[i]) > 0:
			print("Box " + str(i) + ": " + str(boxes[i]))"""
	return

sumPower = 0
fileHandle = open("15.in", "r")
fileData = fileHandle.read()
fileHandle.close()
#fileData = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
steps = fileData.split('\n')[0].split(',')
n = len(steps)
#print(n)
#print(steps)
for i in range(0, 256):
	boxes.append([])
for step in steps:
	runStep(step)
for lens in lenses:
	boxPower = getHash(lens) + 1
	slotPower = 0
	for i in range(0, len(boxes[boxPower-1])):
		if boxes[boxPower-1][i][0] == lens:
			slotPower = i + 1
	focalPower = lenses[lens]
	power = boxPower * slotPower * focalPower
	#print(lens + ": " + str(boxPower) + " * " + str(slotPower) + " * " + str(focalPower) + " = " + str(power))
	sumPower += power
print(sumPower)
