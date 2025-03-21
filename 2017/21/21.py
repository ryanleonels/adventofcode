#!/usr/local/bin/python3

fileHandle = open("21.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
rules = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(before, after) = fileLine.split(' => ')
	rules[before] = after
#print(rules)

def pack(x):
	if len(x) == 4:
		return x[0] + x[1] + '/' + x[2] + x[3]
	if len(x) == 9:
		return x[0] + x[1] + x[2] + '/' + x[3] + x[4] + x[5] + '/' + x[6] + x[7] + x[8]

"""for n in range(0, 16):
	x = bin(n)[2:]
	x = ('0' * (4 - len(x))) + x 
	x = x.replace('0', '.').replace('1', '#')
	(a, b, c, d) = list(x)
	x = x[0:2] + '/' + x[2:4]
	n1 = 0
	matches = []
	y = pack([a, b, c, d])
	y1 = y
	if y in rules: #original
		n1 += 1
		matches.append(y)
	y = pack([c, d, a, b])
	if y in rules and y not in matches and y1 not in matches: # flip row
		n1 += 1
		matches.append(y)
	y = pack([b, a, d, c])
	if y in rules and y not in matches and y1 not in matches: # flip column
		n1 += 1
		matches.append(y)
	y = pack([c, a, d, b])
	if y in rules and y not in matches and y1 not in matches: # rotate 90
		n1 += 1
		matches.append(y)
	y = pack([d, c, b, a])
	if y in rules and y not in matches and y1 not in matches: # rotate 180
		n1 += 1
		matches.append(y)
	y = pack([b, d, a, c])
	if y in rules and y not in matches and y1 not in matches: # rotate 270
		n1 += 1
		matches.append(y)
	print(x, n1, matches)

for n in range(0, 512):
	x = bin(n)[2:]
	x = ('0' * (9 - len(x))) + x 
	x = x.replace('0', '.').replace('1', '#')
	(a, b, c, d, e, f, g, h, i) = list(x)
	x = x[0:3] + '/' + x[3:6] + '/' + x[6:9]
	n1 = 0
	matches = []
	y = pack([a, b, c, d, e, f, g, h, i])
	y1 = y
	if y in rules: #original
		n1 += 1
		matches.append(y)
	y = pack([g, h, i, d, e, f, a, b, c])
	if y in rules and y not in matches and y1 not in matches: # flip row
		n1 += 1
		matches.append(y)
	y = pack([c, b, a, f, e, d, i, h, g])
	if y in rules and y not in matches and y1 not in matches: # flip column
		n1 += 1
		matches.append(y)
	y = pack([g, d, a, h, e, b, i, f, c])
	if y in rules and y not in matches and y1 not in matches: # rotate 90
		n1 += 1
		matches.append(y)
	y = pack([i, h, g, f, e, d, c, b, a])
	if y in rules and y not in matches and y1 not in matches: # rotate 180
		n1 += 1
		matches.append(y)
	y = pack([c, f, i, b, e, h, a, d, g])
	if y in rules and y not in matches and y1 not in matches: # rotate 270
		n1 += 1
		matches.append(y)
	y = pack([i, f, c, h, e, b, g, d, a])
	if y in rules and y not in matches and y1 not in matches: # rotate 90 + flip row
		n1 += 1
		matches.append(y)
	y = pack([a, d, g, b, e, h, c, f, i])
	if y in rules and y not in matches and y1 not in matches: # rotate 270 + flip row
		n1 += 1
		matches.append(y)
	print(x, n1, matches)
exit(0)"""

def findMatch(image):
	size = len(image)
	if size == 2:
		(a, b, c, d) = (image[0][0], image[0][1], image[1][0], image[1][1])
		y = pack([a, b, c, d])
		if y in rules: #original
			return y
		y = pack([c, d, a, b])
		if y in rules: # flip row
			return y
		y = pack([b, a, d, c])
		if y in rules: # flip column
			return y
		y = pack([c, a, d, b])
		if y in rules: # rotate 90
			return y
		y = pack([d, c, b, a])
		if y in rules: # rotate 180
			return y
		y = pack([b, d, a, c])
		if y in rules: # rotate 270
			return y
	if size == 3:
		(a, b, c, d, e, f, g, h, i) = (image[0][0], image[0][1], image[0][2], image[1][0], image[1][1], image[1][2], image[2][0], image[2][1], image[2][2])
		y = pack([a, b, c, d, e, f, g, h, i])
		if y in rules: # original
			return y
		y = pack([g, h, i, d, e, f, a, b, c])
		if y in rules: # flip row
			return y
		y = pack([c, b, a, f, e, d, i, h, g])
		if y in rules: # flip column
			return y
		y = pack([g, d, a, h, e, b, i, f, c])
		if y in rules: # rotate 90
			return y
		y = pack([i, h, g, f, e, d, c, b, a])
		if y in rules: # rotate 180
			return y
		y = pack([c, f, i, b, e, h, a, d, g])
		if y in rules: # rotate 270
			return y
		y = pack([i, f, c, h, e, b, g, d, a])
		if y in rules: # rotate 90 + flip row
			return y
		y = pack([a, d, g, b, e, h, c, f, i])
		if y in rules: # rotate 270 + flip row
			return y

def convert(image):
	match = findMatch(image)
	return rules[match].split('/')

def enhance(image):
	size = len(image)
	image1 = []
	if size % 2 == 0:
		size1 = size * 3 // 2
		for i in range(0, size1):
			image1.append('')
		for i in range(0, size, 2):
			for j in range(0, size, 2):
				image2 = [image[i][j:j+2], image[i+1][j:j+2]]
				image2a = convert(image2)
				for i1 in range(0, 3):
					image1[(i * 3 // 2) + i1] += image2a[i1]
	else:
		size1 = size * 4 // 3
		for i in range(0, size1):
			image1.append('')
		for i in range(0, size, 3):
			for j in range(0, size, 3):
				image2 = [image[i][j:j+3], image[i+1][j:j+3], image[i+2][j:j+3]]
				image2a = convert(image2)
				for i1 in range(0, 4):
					image1[(i * 4 // 3) + i1] += image2a[i1]
	return image1

image = [".#.", "..#", "###"]
for i in range(0, 5):
	image = enhance(image)

"""for i in range(0, len(image)):
	print(image[i])"""

pixels = 0
size = len(image)
for i in range(0, size):
	for j in range(0, size):
		if image[i][j] == '#':
			pixels += 1
print(pixels)