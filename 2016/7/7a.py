#!/usr/bin/python3

message = ""
columns = []
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0

def is_aba(seq):
	if seq[1] != seq[0] and seq[2] == seq[0]:
		return True
	return False

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	sections = fileLine.split(']')
	normals = []
	hypernets = []
	abas = []
	for section in sections:
		section_normal = section.split('[')[0]
		normals.append(section_normal)
		"""if False:
			for i in range(0, n1 - 3):
				if is_abba(section_normal[i:i+4]):
					hasAbbaNormal = True"""
		if '[' in section:
			section_hypernet = section.split('[')[1]
			hypernets.append(section_hypernet)
			"""for i in range(0, n1 - 3):
				if is_abba(section_hypernet[i:i+4]):
					hasAbbaHypernet = True"""
	for normal in normals:
		n1 = len(normal)
		for i in range(0, n1 - 2):
			if is_aba(normal[i:i+3]):
				abas.append(normal[i:i+3])
	hasBab = False
	if len(abas) > 0:
		for hypernet in hypernets:
			n1 = len(hypernet)
			for i in range(0, n1 - 2):
				if is_aba(hypernet[i:i+3]):
					aba = hypernet[i+1] + hypernet[i] + hypernet[i+1]
					if aba in abas:
						hasBab = True
	if hasBab == True:
		n += 1
print(n)