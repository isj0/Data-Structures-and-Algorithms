import node


class LinkedList:

    def __init__(self, first_node=None):
        self.first_node = first_node
    def read(self, index):
        current_node = self.first_node
        current_index = 0



        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:
                return None

        return current_node.data
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

        return None
    def append(self, value):
        new_node = node.Node(value)

        if not self.first_node:
            self.first_node = new_node
            return

        current_node = self.first_node

        while True:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                current_node.next_node = new_node
                break
    def recursive_append(self, value, current_node=None):
        new_node = node.Node(value)

        if not self.first_node:
            self.first_node = new_node
            return

        if not current_node:
            current_node = self.first_node

        if current_node.next_node:
            self.recursive_append(value, current_node.next_node)
        else:
            current_node.next_node = new_node
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
    def delete(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        node_after_deleted_node = current_node.next_node.next_node

        current_node.next_node = node_after_deleted_node
    def print_list(self):
        current_node = self.first_node

        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
    def last(self):
        current_node = self.first_node

        while current_node.next_node:
            current_node = current_node.next_node

        return current_node.data
    def recursive_last(self, current_node=None):
        if not current_node:
            current_node = self.first_node

        if current_node.next_node:
            return self.recursive_last(current_node.next_node)
        else:
            return current_node.data
    def reverse(self):
        previous_node = None
        current_node = self.first_node

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node

            previous_node = current_node
            current_node = next_node

        self.first_node = previous_node
