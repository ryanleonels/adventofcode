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

"""
observations: (special thanks to @sw_creeperking for providing a sample of correct graph to analyze from)
- XOR is only used on handling input/output (if intermediate nodes are using XOR where none of the input is x/y and the output is not z, it is probably wrong) 
- also each z should be using XOR (unless highest bit should use OR as it is carry bit-only)
- also the subchains from (x,y) to z for non-first/last digit is always XOR → (AND → OR) [n≥0 times] → XOR or AND → OR → (AND → OR) [n≥0 times] → XOR
- this means that AND must always be followed by OR (one exception exists for x00 AND y00)
- also XOR should never be followed by OR
"""

swapped = set()
for gate in gates:
	if gates[gate][1] == "XOR" and gate[0] != 'z' and gates[gate][0][0] != 'x' and gates[gate][0][0] != 'y' and gates[gate][1][0] != 'x' and gates[gate][1][0] != 'y':
		swapped.add(gate)
		print("XOR anti-pattern (not input/output): " + gate)
	if gate[0] == 'z' and gates[gate][1] != "XOR" and ('x' + gate[1:]) in wires:
		swapped.add(gate)
		print("non-final z anti-pattern (not XOR): " + gate)
	if gates[gate][1] == "AND" and gates[gate][0] != "x00" and gates[gate][2] != "x00":
		isAntiPattern = False
		for gate1 in gates:
			if (gates[gate1][0] == gate or gates[gate1][2] == gate) and gates[gate1][1] != "OR":
				isAntiPattern = True
				break
		if isAntiPattern == True:
			swapped.add(gate)
			print("non-initial AND anti-pattern (not followed by OR): " + gate)
	if gates[gate][1] == "XOR" and gate not in swapped:
		isAntiPattern = False
		for gate1 in gates:
			if (gates[gate1][0] == gate or gates[gate1][2] == gate) and gates[gate1][1] == "OR":
				isAntiPattern = True
				break
		if isAntiPattern == True:
			swapped.add(gate)
			print("XOR-OR anti-pattern: " + gate)
print(','.join(sorted(swapped)))
