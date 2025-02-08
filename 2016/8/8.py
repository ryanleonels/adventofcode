#!/usr/bin/python3

width = 50
height = 6
pixels = []
for i in range(0, height):
	pixels.append([])
	for j in range(0, width):
		pixels[i].append(False)
fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	if "rect" in fileLine:
		a = int(fileLine.split('x')[0].split(' ')[1])
		b = int(fileLine.split('x')[1])
		#print(['rect', a, b])
		for i in range(0, b):
			for j in range(0, a):
				pixels[i][j] = True
	if "rotate row y" in fileLine:
		a = int(fileLine.split(' by ')[0].split('=')[1])
		b = int(fileLine.split(' by ')[1])
		#print(['rotate row y', a, b])
		temprow = []
		for i in range(0, width):
			temprow.append(pixels[a][i])
		for i in range(0, width):
			pixels[a][(i+b)%width] = temprow[i]
	if "rotate column x" in fileLine:
		a = int(fileLine.split(' by ')[0].split('=')[1])
		b = int(fileLine.split(' by ')[1])
		#print(['rotate column x', a, b])
		tempcol = []
		for i in range(0, height):
			tempcol.append(pixels[i][a])
		for i in range(0, height):
			pixels[(i+b)%height][a] = tempcol[i]

for i in range(0, height):
	for j in range(0, width):
		if pixels[i][j] == True:
			n += 1
print(n)