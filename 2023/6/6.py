#!/usr/bin/python3

fileHandle = open("6.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
times1 = fileLines[0].split(':')[1].split(' ')
distances1 = fileLines[1].split(':')[1].split(' ')
times = []
distances = []
for time in times1:
	if time != '':
		times.append(int(time))
for distance in distances1:
	if distance != '':
		distances.append(int(distance))
prod = 1
for i in range(0, len(times)):
	n = 0
	for j in range(0, times[i]):
		dist = j * (times[i] - j)
		if dist > distances[i]:
			n += 1
	prod *= n
print(prod)
