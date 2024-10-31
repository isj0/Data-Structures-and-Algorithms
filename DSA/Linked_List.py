# Node class to creata a node for Linked List

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


# Implementation of Linked List

class LinkedList:

    # initialize linked list
    def __init__(self, first_node=None):
        self.first_node = first_node

    # Reading
    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:
                return None
            
            return current_node.data

    # Searching
    def search(self, value):
        current_node = self.first_node
        current_index = 0

        while True:
            if current_node == value:
                return current_index
            
            current_node = current_node.next_node

            if not current_node:
                break

            current_index += 1

        return None


    # Insertion
    def insert(self, index, value):
        new_node = Node.Node(value)

        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        
        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node

        current_node.next_node = new_node

    # Deletion
    


# node_1 = Node("Once")
# node_2 = Node("upon")
# node_3 = Node("a")
# node_4 = Node("time")

# node_1.next_node = node_2
# node_2.next_node = node_3
# node_3.next_node = node_4

list = LinkedList()
list.insert(2, "purple")

print(list)