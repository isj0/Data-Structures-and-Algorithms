import double_ended_node


class DoublyLinkedList:

    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
    def append(self, value):
        new_node = double_ended_node.Node(value)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
    def pop_head(self):
        popped_node = self.first_node
        self.first_node = self.first_node.next_node
        self.first_node.previous_node = None
        return popped_node
    def reverse_print(self):
        current_node = self.last_node

        while current_node:
            print(current_node.data)
            current_node = current_node.previous_node
