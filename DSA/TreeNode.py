class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")

    root.add_child(laptop)

    return root

if __name__ == "__main__":
    build_product_tree()































# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left_child = left
#         self.right_child = right

#     # Searching

#     def search(search_value, node):
#         if not node or node.value == search_value:
#             return node
        
#         elif search_value < node.value:
#             return search(search_value, node.left_child)
        
#         else:
#             return search(search_value, node.right_child)

#     # Insertion
#     def insert(value, node):
#         if value < node.value:

#             if not node.left_child:
#                 node.left_child = TreeNode.TreeNode(value)
#             else:
#                 insert(value, node.left_child)

#         elif value > node.value:

#             if not node.right_child:
#                 node.right_child = TreeNode.TreeNode(value)
#             else:
#                 insert(value, node.right_child)


# node1 = TreeNode(25)
# node2 = TreeNode(75)
# root = TreeNode(50, node1, node2)


