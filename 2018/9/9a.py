#!/usr/bin/python3

fileHandle = open("9.in", "r")
fileData = fileHandle.read()
fileHandle.close()
(nPlayers, lastPoints) = (int(fileData.strip().split(' ')[0]), int(fileData.strip().split(' ')[-2]) * 100)
#print(nPlayers, lastPoints)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            if node != None:
            	nodes.append(str(node.data))
            else:
            	nodes.append('None')
        print(" -> ".join(nodes))

    def init(self, data):
    	a = Node(data)
    	a.next = a
    	a.previous = a
    	self.head = a

scores = [0] * nPlayers
circle = CircularLinkedList()
circle.init(0)
#circle.print_list()
curNode = circle.head

point = 1
while point <= lastPoints:
	if point % 100000 == 0:
		print(point)
	player = (point - 1) % nPlayers
	if point % 23 == 0:
		scores[player] += point
		for i in range(0, 7):
			curNode = curNode.prev
		scores[player] += curNode.data
		curNode.prev.next = curNode.next
		curNode.next.prev = curNode.prev
		curNode = curNode.next
	else:
		curNode = curNode.next
		newNode = Node(point)
		curNode.next.prev = newNode
		newNode.next = curNode.next
		curNode.next = newNode
		newNode.prev = curNode
		curNode = curNode.next
	#print(curNode.data)
	#circle.print_list()
	point += 1

print(scores)
print(max(scores))