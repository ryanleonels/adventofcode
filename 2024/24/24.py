#!/usr/local/bin/python3

wires = {}
gates = {}
gateInput = False
fileHandle = open("24.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		gateInput = True
		continue
	if gateInput == True:
		gates[fileLine.split(' -> ')[1]] = fileLine.split(' -> ')[0].split(' ')
	else:
		wires[fileLine.split(': ')[0]] = int(fileLine.split(': ')[1])

n = 1
while n > 0:
	n = 0
	for gate in gates:
		(wire1, op, wire2) = gates[gate]
		if gate not in wires and wire1 in wires and wire2 in wires:
			n += 1
			match op:
				case "AND":
					wires[gate] = wires[wire1] & wires[wire2]
				case "OR":
					wires[gate] = wires[wire1] | wires[wire2]
				case "XOR":
					wires[gate] = wires[wire1] ^ wires[wire2]

output = 0
for gate in sorted(gates):
	if gate in wires and gate[0] == 'z':
		num = int(gate[1:])
		output += (wires[gate] * (2 ** num))
print(output)