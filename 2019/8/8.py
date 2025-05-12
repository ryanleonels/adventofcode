#!/usr/local/bin/python3

fileHandle = open("8.in", "r")
fileData = fileHandle.read()
fileHandle.close()
imageData = fileData.strip()

(width, height) = (25, 6)
layerSize = width * height
nLayer = len(imageData) // layerSize

n12 = []
(min0, min0Layer) = (layerSize, -1)
for i in range(0, nLayer):
	(n0, n1, n2) = (0, 0, 0)
	for j in range(0, layerSize):
		if imageData[(i * layerSize) + j] == '0':
			n0 += 1
		if imageData[(i * layerSize) + j] == '1':
			n1 += 1
		if imageData[(i * layerSize) + j] == '2':
			n2 += 1
	if n0 < min0:
		(min0, min0Layer) = (n0, i)
	n12.append(n1 * n2)
print(n12[min0Layer])
