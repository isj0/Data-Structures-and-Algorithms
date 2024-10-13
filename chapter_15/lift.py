def lift(node, node_to_delete):

    if node.left_child:
        node.left_child = lift(node.left_child, node_to_delete)
        return node

    else:
        node_to_delete.value = node.value
        return node.right_child
