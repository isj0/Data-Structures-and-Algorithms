# Node class to create a node for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LList:
    def __init__(self):
        self.head : Node = None
