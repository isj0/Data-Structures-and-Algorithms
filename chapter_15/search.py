def search(search_value, node):
    if not node or node.value == search_value:
        return node

    elif search_value < node.value:
        return search(search_value, node.left_child)

    else:
        return search(search_value, node.right_child)
