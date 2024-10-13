import tree_node


def insert(value, node):
    if value < node.value:

        if not node.left_child:
            node.left_child = tree_node.TreeNode(value)
        else:
            insert(value, node.left_child)

    elif value > node.value:

        if not node.right_child:
            node.right_child = tree_node.TreeNode(value)
        else:
            insert(value, node.right_child)
