#!/usr/bin/python3

def runWorkflow(workflowId, partId):
	#print((workflowId, partId))
	if workflowId == "A":
		return True
	if workflowId == 'R':
		return False
	rules = workflows[workflowId]
	part = parts[partId]
	for i in range(0, len(rules)):
		if ':' in rules[i]:
			rule = rules[i].split(':')[0]
			nextWorkflow = rules[i].split(':')[1]
			cat = rule[:2]
			req = int(rule[2:])
			if cat == "x>" and part['x'] > req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "x<" and part['x'] < req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "m>" and part['m'] > req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "m<" and part['m'] < req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "a>" and part['a'] > req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "a<" and part['a'] < req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "s>" and part['s'] > req:
				return runWorkflow(nextWorkflow, partId)
			if cat == "s<" and part['s'] < req:
				return runWorkflow(nextWorkflow, partId)
		else:
			return runWorkflow(rules[i], partId)
	print("Workflow error on " + str((workflowId, partId)))
	exit(1)

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
ratingSum = 0
for i in range(0, nParts):
	if runWorkflow("in", i) == True:
		ratingSum += (parts[i]['x'] + parts[i]['m'] + parts[i]['a'] + parts[i]['s'])
print(ratingSum)
