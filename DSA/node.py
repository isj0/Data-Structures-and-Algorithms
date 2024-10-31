# Node class to creata a node for Linked List

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


node_1 = Node("Once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
