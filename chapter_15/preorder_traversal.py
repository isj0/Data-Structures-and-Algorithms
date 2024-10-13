def traverse_and_print(node):
    if not node:
        return
    print(node.value)
    traverse_and_print(node.left_child)
    traverse_and_print(node.right_child)
