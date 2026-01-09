#!/usr/local/bin/python3

from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

curPress = 0
totalPress = 0
config = ""
buttons = []
joltages = []
fileHandle = open("10.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	config = fileLine.split('[')[1].split(']')[0]
	buttons1 = fileLine.split('] (')[1].split(') {')[0].split(') (')
	buttons = []
	for button1 in buttons1:
		buttons.append([int(x) for x in button1.split(',')])
	joltages = [int(x) for x in fileLine.split('{')[1].split('}')[0].split(',')]
	n0 = len(joltages)
	n1 = len(buttons)
	#print(config, buttons, joltages)
	model = LpProblem(name="joltage-problem", sense=LpMinimize)
	variables = []
	if n1 >= 1: a = LpVariable(name="a", lowBound=0, cat="Integer")
	if n1 >= 2: b = LpVariable(name="b", lowBound=0, cat="Integer")
	if n1 >= 3: c = LpVariable(name="c", lowBound=0, cat="Integer")
	if n1 >= 4: d = LpVariable(name="d", lowBound=0, cat="Integer")
	if n1 >= 5: e = LpVariable(name="e", lowBound=0, cat="Integer")
	if n1 >= 6: f = LpVariable(name="f", lowBound=0, cat="Integer")
	if n1 >= 7: g = LpVariable(name="g", lowBound=0, cat="Integer")
	if n1 >= 8: h = LpVariable(name="h", lowBound=0, cat="Integer")
	if n1 >= 9: i = LpVariable(name="i", lowBound=0, cat="Integer")
	if n1 >= 10: j = LpVariable(name="j", lowBound=0, cat="Integer")
	if n1 >= 11: k = LpVariable(name="k", lowBound=0, cat="Integer")
	if n1 >= 12: l = LpVariable(name="l", lowBound=0, cat="Integer")
	if n1 >= 13: m = LpVariable(name="m", lowBound=0, cat="Integer")
	if n1 >= 14: n = LpVariable(name="n", lowBound=0, cat="Integer")
	if n1 >= 15: o = LpVariable(name="o", lowBound=0, cat="Integer")
	if n1 >= 16: p = LpVariable(name="p", lowBound=0, cat="Integer")
	if n1 >= 17: q = LpVariable(name="q", lowBound=0, cat="Integer")
	if n1 >= 18: r = LpVariable(name="r", lowBound=0, cat="Integer")
	if n1 >= 19: s = LpVariable(name="s", lowBound=0, cat="Integer")
	if n1 >= 20: t = LpVariable(name="t", lowBound=0, cat="Integer")
	if n1 >= 21: u = LpVariable(name="u", lowBound=0, cat="Integer")
	if n1 >= 22: v = LpVariable(name="v", lowBound=0, cat="Integer")
	if n1 >= 23: w = LpVariable(name="w", lowBound=0, cat="Integer")
	if n1 >= 24: x = LpVariable(name="x", lowBound=0, cat="Integer")
	if n1 >= 25: y = LpVariable(name="y", lowBound=0, cat="Integer")
	if n1 >= 26: z = LpVariable(name="z", lowBound=0, cat="Integer")
	for i1 in range(0, n0):
		constraintExpr = ""
		for j1 in range(0, n1):
			if i1 in buttons[j1]:
				if constraintExpr != "":
					constraintExpr += " + "
				constraintExpr += chr(j1+97)
		constraintExpr += (" == " + str(joltages[i1]))
		model += (eval(constraintExpr), f"constraint_{i1}")
	sumExpr = "["
	for i1 in range(0, n1):
		if i1 > 0:
			sumExpr += ", "
		sumExpr += chr(i1+97)
	sumExpr += "]"
	model += lpSum(eval(sumExpr))
	status = model.solve()
	curPress = 0
	if n1 >= 1: curPress += int(a.value())
	if n1 >= 2: curPress += int(b.value())
	if n1 >= 3: curPress += int(c.value())
	if n1 >= 4: curPress += int(d.value())
	if n1 >= 5: curPress += int(e.value())
	if n1 >= 6: curPress += int(f.value())
	if n1 >= 7: curPress += int(g.value())
	if n1 >= 8: curPress += int(h.value())
	if n1 >= 9: curPress += int(i.value())
	if n1 >= 10: curPress += int(j.value())
	if n1 >= 11: curPress += int(k.value())
	if n1 >= 12: curPress += int(l.value())
	if n1 >= 13: curPress += int(m.value())
	if n1 >= 14: curPress += int(n.value())
	if n1 >= 15: curPress += int(o.value())
	if n1 >= 16: curPress += int(p.value())
	if n1 >= 17: curPress += int(q.value())
	if n1 >= 18: curPress += int(r.value())
	if n1 >= 19: curPress += int(s.value())
	if n1 >= 20: curPress += int(t.value())
	if n1 >= 21: curPress += int(u.value())
	if n1 >= 22: curPress += int(v.value())
	if n1 >= 23: curPress += int(w.value())
	if n1 >= 24: curPress += int(x.value())
	if n1 >= 25: curPress += int(y.value())
	if n1 >= 26: curPress += int(z.value())
	totalPress += curPress
print(totalPress)
