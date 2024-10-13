def max(node):
    if node.right_child:
        return max(node.right_child)
    else:
        return node.value
