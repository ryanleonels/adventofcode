#!/usr/local/bin/python3

wires = {}
circuit = []
fileHandle = open("7.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	tokens = fileLine.split(' ')
	out = tokens[-1]
	ins = ""
	arg1 = ""
	arg2 = ""
	if len(tokens) == 3:
		ins = "assign"
		arg1 = tokens[0]
	if len(tokens) == 4 and tokens[0] == "NOT":
		ins = "NOT"
		arg1 = tokens[1]
	if len(tokens) == 5:
		ins = tokens[1]
		arg1 = tokens[0]
		arg2 = tokens[2]
	circuit.append({'ins': ins, 'arg1': arg1, 'arg2': arg2, 'out': out, 'proc': False})
n = len(circuit)
nproc = 0
nprev = -1
while nproc < n and nproc > nprev:
	nprev = nproc
	for i in range(0, n):
		if circuit[i]['proc'] == False:
			arg1 = circuit[i]['arg1']
			arg2 = circuit[i]['arg2']
			out = circuit[i]['out']
			(x1, x2) = (-1, -1)
			if arg1.isdigit():
				x1 = int(arg1)
			else:
				if arg1 in wires:
					x1 = wires[arg1]
			if arg2.isdigit():
				x2 = int(arg2)
			else:
				if arg2 in wires:
					x2 = wires[arg2]
			match circuit[i]['ins']:
				case "assign":
					if x1 != -1:
						wires[out] = x1
						circuit[i]['proc'] = True
						nproc += 1
				case "NOT":
					if x1 != -1:
						wires[out] = 65535 - x1
						circuit[i]['proc'] = True
						nproc += 1
				case "AND":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 & x2
						circuit[i]['proc'] = True
						nproc += 1
				case "OR":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 | x2
						circuit[i]['proc'] = True
						nproc += 1
				case "LSHIFT":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 << x2
						circuit[i]['proc'] = True
						nproc += 1
				case "RSHIFT":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 >> x2
						circuit[i]['proc'] = True
						nproc += 1
a = wires['a']
wires = {}
for i in range(0, n):
	circuit[i]['proc'] = False
	if circuit[i]['ins'] == "assign" and circuit[i]['out'] == "b":
		circuit[i]['arg1'] = str(a)
nproc = 0
nprev = -1
while nproc < n and nproc > nprev:
	nprev = nproc
	for i in range(0, n):
		if circuit[i]['proc'] == False:
			arg1 = circuit[i]['arg1']
			arg2 = circuit[i]['arg2']
			out = circuit[i]['out']
			(x1, x2) = (-1, -1)
			if arg1.isdigit():
				x1 = int(arg1)
			else:
				if arg1 in wires:
					x1 = wires[arg1]
			if arg2.isdigit():
				x2 = int(arg2)
			else:
				if arg2 in wires:
					x2 = wires[arg2]
			match circuit[i]['ins']:
				case "assign":
					if x1 != -1:
						wires[out] = x1
						circuit[i]['proc'] = True
						nproc += 1
				case "NOT":
					if x1 != -1:
						wires[out] = 65535 - x1
						circuit[i]['proc'] = True
						nproc += 1
				case "AND":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 & x2
						circuit[i]['proc'] = True
						nproc += 1
				case "OR":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 | x2
						circuit[i]['proc'] = True
						nproc += 1
				case "LSHIFT":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 << x2
						circuit[i]['proc'] = True
						nproc += 1
				case "RSHIFT":
					if x1 != -1 and x2 != -1:
						wires[out] = x1 >> x2
						circuit[i]['proc'] = True
						nproc += 1
print(wires['a'])