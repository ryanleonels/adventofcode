#!/usr/bin/python3

message = ""
columns = []
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = 0

def is_abba(seq):
	if seq[1] != seq[0] and seq[2] == seq[1] and seq[3] == seq[0]:
		return True
	return False

for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	sections = fileLine.split(']')
	hasAbbaNormal = False
	hasAbbaHypernet = False
	for section in sections:
		if hasAbbaNormal == False:
			section_normal = section.split('[')[0]
			n1 = len(section_normal)
			for i in range(0, n1 - 3):
				if is_abba(section_normal[i:i+4]):
					hasAbbaNormal = True
		if '[' in section and hasAbbaHypernet == False:
			section_hypernet = section.split('[')[1]
			n1 = len(section_hypernet)
			for i in range(0, n1 - 3):
				if is_abba(section_hypernet[i:i+4]):
					hasAbbaHypernet = True
	if hasAbbaNormal == True and hasAbbaHypernet == False:
		n += 1
print(n)