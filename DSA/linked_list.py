# # Implementation of Linked list

import DSA.node as node

class LinkedList:

    def __init__(self, first_node = None):
        self.first_node = first_node

    # Linked List Reading

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
        
            if not current_node:
                return None
        
        return current_node.data
    
    # Linked List Searching
    
    def search(self, value):
        
        current_node = self.first_node
        current_index = 0

        while True:
            if current_node.data == value:
                return current_index
            
            current_node = current_node.next_node

            if not current_node:
                break

            current_index += 1

    # Linked List Insertion
    def insert(self, index, value):
        new_node = node.Node(value)

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

        
