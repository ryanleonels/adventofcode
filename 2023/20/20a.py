#!/usr/bin/python3

import math

low = 0
high = 0
modules = {}
pulses = {}
pulses1 = {}
fileHandle = open("20.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["broadcaster -> a, b, c","%a -> b","%b -> c","%c -> inv","&inv -> a"]
#fileLines = ["broadcaster -> a","%a -> inv, con","&inv -> b","%b -> con","&con -> output"]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	module = fileLine.split(" -> ")[0]
	destinations = fileLine.split(" -> ")[1].split(", ")
	modtype = ' '
	if module != "broadcaster":
		modtype = module[0]
		module = module[1:]
	modules[module] = {"modtype": modtype, "destinations": destinations, "on": False, "inputs": {}}
for module in modules:
	for destination in modules[module]["destinations"]:
		if destination in modules and modules[destination]["modtype"] == '&' and module not in modules[destination]["inputs"]:
			modules[destination]["inputs"][module] = False
#for module in modules:
	#print(str(module)+": " + str(modules[module]))
i = 0
rx = {}
rxDataComplete = False
rxModule = ""
for module in modules:
	if "rx" in modules[module]["destinations"]:
		rxModule = module
#print(rxModule)
#for i in range(0, 1000000):
while rxDataComplete == False:
	pulses = [("broadcaster", [], False)] #(destination, originList, isHigh)
	low += 1
	while len(pulses) > 0:
		pulses1 = []
		for pulse in pulses:
			originList = []
			for origin in pulse[1]:
				originList.append(origin)
			originList.append(pulse[0])
			if pulse[0] == "broadcaster":
				for destination in modules[pulse[0]]["destinations"]:
					pulses1.append((destination, originList, pulse[2]))
					if pulse[2] == True:
						high += 1
					else:
						low += 1
			if pulse[0] in modules and modules[pulse[0]]["modtype"] == '%': #flip-flop
				if pulse[2] == False:
					modules[pulse[0]]["on"] = not modules[pulse[0]]["on"]
					for destination in modules[pulse[0]]["destinations"]:
						pulses1.append((destination, originList, modules[pulse[0]]["on"]))
						if modules[pulse[0]]["on"] == True:
							high += 1
						else:
							low += 1
			if pulse[0] in modules and modules[pulse[0]]["modtype"] == '&': #conjunction
				modules[pulse[0]]["inputs"][pulse[1][-1]] = pulse[2]
				allHigh = True
				for input1 in modules[pulse[0]]["inputs"]:
					if modules[pulse[0]]["inputs"][input1] == False:
						allHigh = False
						break
				for destination in modules[pulse[0]]["destinations"]:
					if destination == "rx":
						allLow = True
						inputs = modules[pulse[0]]["inputs"]
						for input1 in inputs:
							if inputs[input1] == True:
								allLow = False
								if input1 not in rx:
									rx[input1] = [i]
								else:
									if i not in rx[input1]:
										rx[input1].append(i)
								#break
						#if allLow == False:
							#print(str(i) + " " + str(destination) + " " + str(inputs))
					pulses1.append((destination, originList, not allHigh))
					if allHigh == True:
						low += 1
					else:
						high += 1
		pulses = pulses1
	#print(str(low)+" "+str(high))
	#print(rx)
	i += 1
	if len(rx) == len(modules[rxModule]["inputs"]):
		rxDataComplete = True
		for input1 in modules[rxModule]["inputs"]:
			if len(rx[input1]) < 2:
				rxDataComplete = False
				break
#print(low * high)
#print(rx)
# quick method, may not always work (it worked just because each high pulse input occurs at button presses # (x-1), (2x-1), (3x-1), ... for this test case)
"""result = 1
for rx1 in rx:
	result = math.lcm(result, rx[rx1][1] - rx[rx1][0])"""
#print(result)
# a more rigorous approach that will work for all test cases
calc = []
for rx1 in rx:
	calc.append((rx[rx1][0], rx[rx1][1] - rx[rx1][0]))
#print(calc)
result1 = calc[0]
for i in range(1, len(calc)):
	x = result1[0]
	while x % calc[i][1] != calc[i][0]:
		x += result1[1]
	y = math.lcm(result1[1], calc[i][1])
	result1 = (x,y)
	#print(str(i)+": "+str(result1))
result = result1[0] + 1
print(result)
