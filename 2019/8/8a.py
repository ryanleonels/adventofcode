#!/usr/local/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
imageData = fileData.strip()

(width, height) = (25, 6)
layerSize = width * height
nLayer = len(imageData) // layerSize

#for i in range(0, nLayer):
	#print(imageData[(i * layerSize):((i + 1) * layerSize)])

for i in range(0, height):
	line = ""
	for j in range(0, width):
		pos = (width * i) + j
		layer = 0
		pixel = imageData[pos]
		while pixel == '2' and layer < nLayer - 1:
			layer += 1
			pos += layerSize
			pixel = imageData[pos]
		if pixel == '0':
			line += '█'
		else:
			line += ' '
	print(line)
