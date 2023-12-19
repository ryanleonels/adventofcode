#!/usr/bin/python3

def partOK(part):
	if part['x'][0] > part['x'][1]:
		return False
	if part['m'][0] > part['m'][1]:
		return False
	if part['a'][0] > part['a'][1]:
		return False
	if part['s'][0] > part['s'][1]:
		return False
	return True

def runWorkflows(workflowId, part):
	#print(str(workflowId) + " " + str(part))
	if workflowId == "A":
		return (part['x'][1]-part['x'][0]+1) * (part['m'][1]-part['m'][0]+1) * (part['a'][1]-part['a'][0]+1) * (part['s'][1]-part['s'][0]+1)
	if workflowId == "R":
		return 0
	result = 0
	rules = workflows[workflowId]
	curPart = {}
	for ch in part:
		curPart[ch] = part[ch]
	for i in range(0, len(rules)):
		if ':' in rules[i]:
			rule = rules[i].split(':')[0]
			nextWorkflow = rules[i].split(':')[1]
			cat = rule[:2]
			req = int(rule[2:])
			part1 = {}
			for ch in curPart:
				part1[ch] = curPart[ch]
			if cat == "x>":
				if (req + 1) > part1['x'][0]:
					part1['x'] = (req + 1, part1['x'][1])
				if req < curPart['x'][1]:
					curPart['x'] = (curPart['x'][0], req)
			if cat == "x<":
				if (req - 1) < part1['x'][1]:
					part1['x'] = (part1['x'][0], req - 1)
				if req > curPart['x'][0]:
					curPart['x'] = (req, curPart['x'][1])
			if cat == "m>":
				if (req + 1) > part1['m'][0]:
					part1['m'] = (req + 1, part1['m'][1])
				if req < curPart['m'][1]:
					curPart['m'] = (curPart['m'][0], req)
			if cat == "m<":
				if (req - 1) < part1['m'][1]:
					part1['m'] = (part1['m'][0], req - 1)
				if req > curPart['m'][0]:
					curPart['m'] = (req, curPart['m'][1])
			if cat == "a>":
				if (req + 1) > part1['a'][0]:
					part1['a'] = (req + 1, part1['a'][1])
				if req < curPart['a'][1]:
					curPart['a'] = (curPart['a'][0], req)
			if cat == "a<":
				if (req - 1) < part1['a'][1]:
					part1['a'] = (part1['a'][0], req - 1)
				if req > curPart['a'][0]:
					curPart['a'] = (req, curPart['a'][1])
			if cat == "s>":
				if (req + 1) > part1['s'][0]:
					part1['s'] = (req + 1, part1['s'][1])
				if req < curPart['s'][1]:
					curPart['s'] = (curPart['s'][0], req)
			if cat == "s<":
				if (req - 1) < part1['s'][1]:
					part1['s'] = (part1['s'][0], req - 1)
				if req > curPart['s'][0]:
					curPart['s'] = (req, curPart['s'][1])
			if partOK(part1) == True:
				result += runWorkflows(nextWorkflow, part1)
		else:
			if partOK(curPart) == True:
				result += runWorkflows(rules[i], curPart)
	return result

nWorkflows = 0
nParts = 0
workflows = {}
parts = []
fileHandle = open("19.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["px{a<2006:qkq,m>2090:A,rfg}","pv{a>1716:R,A}","lnx{m>1548:A,A}","rfg{s<537:gd,x>2440:R,A}","qs{s>3448:A,lnx}","qkq{x<1416:A,crn}","crn{x>2662:A,R}","in{s<1351:px,qqz}","qqz{s>2770:qs,m<1801:hdj,R}","gd{a>3333:R,R}","hdj{m>838:A,pv}","","{x=787,m=2655,a=1222,s=2876}","{x=1679,m=44,a=2067,s=496}","{x=2036,m=264,a=79,s=2244}","{x=2461,m=1339,a=466,s=291}","{x=2127,m=1623,a=2188,s=1013}",""]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	if fileLine[0] == '{':
		#parse parts
		part = {}
		part['x'] = int(fileLine.split("x=")[1].split(",")[0])
		part['m'] = int(fileLine.split("m=")[1].split(",")[0])
		part['a'] = int(fileLine.split("a=")[1].split(",")[0])
		part['s'] = int(fileLine.split("s=")[1].split("}")[0])
		parts.append(part)
		nParts += 1
	else:
		#parse workflows
		workflow = fileLine.split("{")[0]
		rules = fileLine.split("{")[1].split("}")[0].split(",")
		workflows[workflow] = rules
		nWorkflows += 1
#print(nWorkflows)
#print(workflows)
#print(nParts)
#print(parts)
#print(workflows['in'])
allParts = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
ratingSum = runWorkflows("in", allParts)
print(ratingSum)
