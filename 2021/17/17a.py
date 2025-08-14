#!/usr/bin/python3

fileHandle = open("17.in", "r")
fileData = fileHandle.read()
fileHandle.close()
(xmin, xmax) = [int(x) for x in fileData.strip().split('x=')[1].split(',')[0].split('..')]
(ymin, ymax) = [int(y) for y in fileData.strip().split('y=')[1].split('..')]
#print(xmin, xmax, ymin, ymax)

# for initial velocity (x, y) assuming positive x
# pos_x after time t = (x * (x + 1) / 2) - ((x - t) * (x - t + 1) / 2) for t <= x, (x * (x + 1) / 2) for t > x (for negative x, opposite side for t <= |x|)
# pos_y after time t = (y * t) - (t * (t - 1) / 2)
# v_x after time t = x - t for t <= x, 0 for t > x (for negative x, x + t for t <= |x| and 0 for t > |x|)
# v_y after time t = y - t
# max height: 0 if y <= 0, y * (y + 1) / 2 if y > 0

def pos_x(v, t):
	if t > v:
		return (v * (v + 1) / 2)
	return (v * (v + 1) / 2) - ((v - t) * (v - t + 1) / 2)

def pos_y(v, t):
	return (v * t) - (t * (t - 1) / 2)

def max_height(y):
	if y <= 0:
		return 0
	return int(y * (y + 1) / 2)

# assuming positive x ranges, calculate possible vx ranges and times when they are in target area
xtimes = {}
vxmin = 1
while vxmin * (vxmin + 1) / 2 < xmin:
	vxmin += 1
for vx in range(vxmin, xmax + 1):
	t = 0
	while pos_x(vx, t) < xmin:
		t += 1
	if pos_x(vx, t) > xmax:
		continue
	tmin = t
	tmax = t
	while pos_x(vx, t) <= xmax:
		t += 1
		if pos_x(vx, t) <= xmax:
			tmax += 1
		if t == vx:
			tmax = 999999999 # x will always stay within target area
			break
	xtimes[vx] = (tmin, tmax)
	#print(vx, tmin, tmax)

# assuming negative y ranges, calculate possible vy ranges and times when they are in target area
ytimes = {}
tmaxall = 0
for vy in range(ymin, -ymin): # < ymin or >= -ymin = immediate overshoot
	t = 0
	while pos_y(vy, t) > ymax:
		t += 1
	if pos_y(vy, t) < ymin:
		continue
	tmin = t
	tmax = t
	while pos_y(vy, t) >= ymin:
		t += 1
		if pos_y(vy, t) >= ymin:
			tmax += 1
	tmaxall = max(tmaxall, tmax)
	ytimes[vy] = (tmin, tmax)
	#print(vy, tmin, tmax)

# check all pairs if they intersect with each other
n = 0
for vx in xtimes:
	(txmin, txmax) = xtimes[vx]
	for vy in ytimes:
		(tymin, tymax) = ytimes[vy]
		if txmin <= tymax and tymin <= txmax:
			n += 1
			#print(vx, vy)
print(n)
