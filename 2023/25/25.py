#!/usr/local/bin/python3

import networkx as nx

n1 = 0
n2 = 0
components = []
graph = {}
nxGraph = nx.Graph()

fileHandle = open("25.in", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
#fileLines = ["jqt: rhn xhk nvd","rsh: frs pzl lsr","xhk: hfx","cmg: qnr nvd lhk bvb","rhn: xhk bvb hfx","bvb: xhk hfx","pzl: lsr hfx nvd","qnr: nvd","ntq: jqt hfx bvb xhk","nvd: lhk","lsr: lhk","rzs: qnr cmg lsr rsh","frs: qnr lhk lsr"]
for fileLine in fileLines:
	if len(fileLine) == 0:
		continue
	component = fileLine.split(": ")[0]
	connections = fileLine.split(": ")[1].split(" ")
	components.append(component)
	if component not in graph:
		graph[component] = []
	for connection in connections:
		graph[component].append(connection)
		if connection not in graph:
			graph[connection] = []
			graph[connection].append(component)
		nxGraph.add_edge(component, connection, capacity=1.0)
n = len(graph)
"""print(n)
print(components)
for node in graph:
	print(str(node) + ": " + str(graph[node]))
print(nxGraph)
print(nxGraph.nodes)"""
#cutEdges = nx.algorithms.connectivity.minimum_edge_cut(nxGraph, components[0], components[-1])
#print("Cut edges: " + str(cutEdges))
cutWeight, partitions = nx.minimum_cut(nxGraph, components[0], components[-1])
n1 = len(partitions[0])
n2 = len(partitions[1])
print("Cut edges capacity " + str(cutWeight))
print("Size of 1st partition: " + str(n1))
print("Set of nodes in the 1st partition: " + str(partitions[0]))
print("Size of 2nd partition: " + str(n2))
print("Set of nodes in the 2nd partition: " + str(partitions[1]))
edgeCutList = [] # Computed by listing edges between the 2 partitions
for node1 in partitions[0]:
    for node2 in partitions[1]:
        if nxGraph.has_edge(node1,node2):
            edgeCutList.append((node1,node2))
print("Edges of the cut: " + str(edgeCutList))
print(n1 * n2)
