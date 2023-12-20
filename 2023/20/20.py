#!/usr/bin/python3

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
for i in range(0, 1000):
	pulses = [("broadcaster", "button", False)] #(destination, origin, isHigh)
	low += 1
	while len(pulses) > 0:
		pulses1 = []
		for pulse in pulses:
			if pulse[0] == "broadcaster":
				for destination in modules[pulse[0]]["destinations"]:
					pulses1.append((destination, pulse[0], pulse[2]))
					if pulse[2] == True:
						high += 1
					else:
						low += 1
			if pulse[0] in modules and modules[pulse[0]]["modtype"] == '%': #flip-flop
				if pulse[2] == False:
					modules[pulse[0]]["on"] = not modules[pulse[0]]["on"]
					for destination in modules[pulse[0]]["destinations"]:
						pulses1.append((destination, pulse[0], modules[pulse[0]]["on"]))
						if modules[pulse[0]]["on"] == True:
							high += 1
						else:
							low += 1
			if pulse[0] in modules and modules[pulse[0]]["modtype"] == '&': #conjunction
				modules[pulse[0]]["inputs"][pulse[1]] = pulse[2]
				allHigh = True
				for input1 in modules[pulse[0]]["inputs"]:
					if modules[pulse[0]]["inputs"][input1] == False:
						allHigh = False
						break
				for destination in modules[pulse[0]]["destinations"]:
					pulses1.append((destination, pulse[0], not allHigh))
					if allHigh == True:
						low += 1
					else:
						high += 1
		pulses = pulses1
	#print(str(low)+" "+str(high))
print(low * high)
